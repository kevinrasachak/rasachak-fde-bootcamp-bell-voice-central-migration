def lookup_customer_account_wrapper(telephone_number: str) -> dict:
    '''Webhook Wrapper for customer-identification#search-by-tn. Parses response and sets state directly.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            api_response = {'users': [{'billing_accounts': [{'billing_account_number': '123456789', 'services': [{'service_type': 'mobility', 'is_prepaid': False}]}]}]}
        else:
            payload = {'telephone_number': telephone_number}
            api_response = tools.search_by_tn_search_by_tn(payload).json()

        users = api_response.get('users', [])
        if not users:
            set_variable('identification_status', 'Fail')
            set_variable('line_type', 'New')
            set_variable('customer_type', 'New')
            print('Business logic success')
            return {'status': 'not_found'}

        first_user = users[0]
        billing_accounts = first_user.get('billing_accounts', [])
        if not billing_accounts:
            set_variable('identification_status', 'Fail')
            set_variable('line_type', 'Existing')
            set_variable('customer_type', 'Existing')
            print('Business logic success')
            return {'status': 'no_billing_accounts'}

        n_billing_accounts = len(billing_accounts)
        service_types = []
        is_prepaid = False

        for account in billing_accounts:
            for service in account.get('services', []):
                service_type = service.get('service_type')
                if service_type:
                    service_types.append(service_type)
                if service.get('is_prepaid'):
                    is_prepaid = True

        unique_service_types = list(set(service_types))

        if n_billing_accounts == 1 and not is_prepaid:
            set_variable('identification_status', 'Pass')
            set_variable('line_type', 'Existing')
            set_variable('customer_type', 'Existing')
        elif n_billing_accounts > 1:
            set_variable('identification_status', 'Pass')
            set_variable('line_type', 'Existing')
            set_variable('customer_type', 'Existing')
            set_variable('multiban_sales_lob', unique_service_types)
        else:
            set_variable('identification_status', 'Fail')
            set_variable('line_type', 'Existing')
            set_variable('customer_type', 'Existing')

        print('Business logic success')
        return {'status': 'success', 'n_billing_accounts': n_billing_accounts, 'is_prepaid': is_prepaid}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the user that we are experiencing technical issues and proceed to ask for their phone number or route to sales.'}
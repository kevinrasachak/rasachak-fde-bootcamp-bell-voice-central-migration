def search_by_tn_wrapper(telephone_number: str) -> dict:
    '''Webhook Wrapper for the customer-identification search-by-tn API.'''
    try:
        mock_mode = get_variable('mock_mode')
        sanitized_tn = telephone_number.strip().replace('-', '').replace(' ', '')
        if mock_mode:
            set_variable('webhook_success', True)
            mock_data = {
                'users': [{'billing_accounts': [{'services': [
                    {'technology_type': 'DTH', 'service_id': 'SAT123', 'service_address': {'stateOrProvince': 'ON'}},
                    {'technology_type': 'IPTV', 'service_id': 'FIBE456', 'service_address': {'stateOrProvince': 'ON'}}
                ]}]}]
            }
            return {'status': 'success', 'data': mock_data}

        payload = {'telephone_number': sanitized_tn}
        api_response = tools.search_by_tn_search_by_tn(payload).json()
        set_variable('webhook_success', True)
        print('Business logic success')
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        set_variable('webhook_success', False)
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
def fetch_billing_profile(ban_type: str, ban_sub_type: str) -> dict:
    '''Evaluates ban_type and ban_sub_type to call the appropriate NM1 profile webhook (customer or ban). Updates session variables and handles mock mode.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('oneBillIndicator', 'M')
            set_variable('accountType', 'I')
            set_variable('accountSubType', 'R')
            set_variable('pastDueAmount', 0.0)
            set_variable('accountBalance', 50.0)
            print('Business logic success - Mocked')
            return {'status': 'success', 'returnCode': 1}

        sanitized_type = str(ban_type).strip().upper()
        sanitized_sub_type = str(ban_sub_type).strip().upper()
        payload = {'banType': sanitized_type, 'banSubType': sanitized_sub_type}

        call_customer_profile = False
        if sanitized_type == 'I' and sanitized_sub_type in ['B', 'N', '5']:
            call_customer_profile = True
        elif sanitized_type == 'C' and sanitized_sub_type in ['V', 'T', 'P']:
            call_customer_profile = True

        if call_customer_profile:
            api_response = tools.nm1_get_customer_profile(payload).json()
            set_variable('oneBillIndicator', api_response.get('oneBill', ''))
            set_variable('accountType', api_response.get('banType', ''))
            set_variable('accountSubType', api_response.get('banSubType', ''))
            set_variable('pastDueAmount', api_response.get('pastDueAmount', 0.0))
            set_variable('accountBalance', api_response.get('arBalance', 0.0))
            returnCode = api_response.get('returnCode', -1)
        else:
            api_response = tools.nm1_get_ban_profile(payload).json()
            set_variable('oneBillIndicator', api_response.get('oneBillIndicator', ''))
            set_variable('accountType', api_response.get('accountType', ''))
            set_variable('accountSubType', api_response.get('accountSubType', ''))
            set_variable('pastDueAmount', api_response.get('pastDueAmount', 0.0))
            set_variable('accountBalance', api_response.get('accountBalance', 0.0))
            returnCode = api_response.get('returnCode', -1)

        print('Business logic success')
        return {'status': 'success', 'returnCode': returnCode}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties retrieving their profile and offer to transfer them to a representative.'}
def tool_get_customer_profile(billing_account: str = '') -> dict:
    '''Webhook Wrapper Tool. Implements calls to NM1 BAN and Customer Profile logic.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'onebillindicator': 'Y', 'errorCode': '0', 'banType': 'I', 'banSubType': 'B'}
        sanitized_account = billing_account.strip()
        payload = {'billing_account': sanitized_account}
        api_response = tools.nm1_get_ban_profile(payload).json()
        api_response_cust = tools.nm1_get_customer_profile(payload).json()
        print('Business logic success')
        return {
            'onebillindicator': api_response.get('oneBillIndicator', 'N'),
            'errorCode': api_response.get('returnCode', '0'),
            'banType': api_response.get('accountType', ''),
            'banSubType': api_response.get('accountSubType', '')
        }
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the system is experiencing an issue and prompt them if they would like an SMS with instructions to proceed.'}
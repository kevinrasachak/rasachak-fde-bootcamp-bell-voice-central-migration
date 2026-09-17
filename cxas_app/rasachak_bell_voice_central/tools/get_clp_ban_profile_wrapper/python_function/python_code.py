def get_clp_ban_profile_wrapper(ban_number: str = "") -> dict:
    '''Webhook Wrapper. Retrieves the user's updated BAN profile limits.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'status': 'success', 'curSpendingLimitBal': 500.0, 'aul_threshold': 400.0, 'sus_threshold': 600.0, 'pastDueAmount': 0.0}

        payload = {'ban_number': ban_number}
        api_response = tools.nm1_get_ban_profile(payload).json()
        print('Business logic success')
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties retrieving account details and proceed with default routing.'}
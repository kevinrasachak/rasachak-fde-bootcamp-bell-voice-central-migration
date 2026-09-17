def get_clp_details_wrapper() -> dict:
    '''Retrieves Credit Limit Program (CLP) details for the user.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')

        if mock_mode:
            print('Mock mode enabled for get_clp_details')
            return {'webhook_success': True, 'spending_limit': 0}

        payload = {}
        api_response = tools.get_clp_details_get_clp_details(payload).json()
        print('Business logic success')

        return {
            'webhook_success': api_response.get('webhook_success', True),
            'spending_limit': api_response.get('spendingLimit', 0)
        }
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Silently transition logic to bell_Feedback as CLP details could not be reliably retrieved.'}
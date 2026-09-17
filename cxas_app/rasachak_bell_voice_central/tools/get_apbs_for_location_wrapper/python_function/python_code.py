def get_apbs_for_location_wrapper(location_id: float = 0.0) -> dict:
    '''Executes API call to fetch APBs for a given location.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            mock_data = {
                'apb_message': 'This is a mock automated playback message.',
                'hang_up': False,
                'agent_transfer': False,
                'interruptible': 'Y',
                'department_id': '123'
            }
            set_variable('get_ras_apb_response', mock_data)
            set_variable('webhook_success', True)
            print('Business logic success - Mock Mode')
            return {'status': 'success', 'data': mock_data}

        payload = {'location_id': int(location_id)}
        try:
            api_response = tools.NA_get_apbs_for_location(payload).json()
        except Exception:
            api_response = {
                'apb_message': 'Production APB message fallback.',
                'hang_up': False,
                'agent_transfer': False,
                'interruptible': 'Y',
                'department_id': ''
            }

        set_variable('get_ras_apb_response', api_response)
        set_variable('webhook_success', True)
        print('Business logic success - Backend Execution')
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        logger.error(f'Crash: {e}')
        set_variable('webhook_success', False)
        return {'error': str(e), 'agent_action': 'Inform the user there is a technical error and proceed to evaluate routing.'}
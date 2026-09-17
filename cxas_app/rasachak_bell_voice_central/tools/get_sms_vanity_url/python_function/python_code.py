def get_sms_vanity_url(route: str = "") -> dict:
    '''Fetches an SDL mapping URL for fallback links via SMS.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'url': 'https://mock.bell.ca/support'}

        payload = {'route': route}
        res = tools.intent_sdl_mapping_intent_sdl_mapping(payload).json()
        print('Business logic success')
        return {'url': res.get('url', 'https://bell.ca/support')}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the customer that the link cannot be sent right now and offer to wait while they find their information.'}
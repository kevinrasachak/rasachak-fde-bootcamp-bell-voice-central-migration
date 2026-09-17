def get_vanity_url_mapping(intent_name: str = "", brand: str = "", language: str = "") -> dict:
    '''Retrieves a self-serve vanity URL based on intent.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'status': 'success', 'vanity_url': 'bell.ca/support'}
        payload = {'intent_name': intent_name, 'brand': brand, 'language': language}
        api_response = tools.intent_sdl_mapping_intent_sdl_mapping(payload).json()
        print('Business logic success - get_vanity_url_mapping')
        return {'status': 'success', 'vanity_url': api_response.get('url', 'bell.ca/support')}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Read the fallback message including bell.ca/support.'}
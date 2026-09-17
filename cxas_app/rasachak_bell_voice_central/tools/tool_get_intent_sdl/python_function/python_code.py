def tool_get_intent_sdl(intent_route: str = '', language: str = 'en') -> dict:
    '''Invokes intent-sdl-mapping using intent route and language to fetch a vanity URL.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'vanity_url': 'bell.ca/support'}
        sanitized_route = intent_route.strip()
        sanitized_lang = language.strip().lower()
        payload = {'intent_route': sanitized_route, 'language': sanitized_lang}
        api_response = tools.intent_sdl_mapping_get(payload).json()
        print('Business logic success')
        return {'vanity_url': api_response.get('url', 'bell.ca/support')}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the system is experiencing an issue and prompt them if they would like an SMS with instructions to proceed.'}
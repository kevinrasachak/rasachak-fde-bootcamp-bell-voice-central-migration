def get_sdl_vanity_url_wrapper(intent_route: str = '') -> dict:
    '''Webhook Wrapper tool to fetch the vanity URL based on intent routing.'''
    import json
    try:
        intent_clean = intent_route.strip()
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('vanity_url', 'bell.ca/mybell')
            return {'status': 'success', 'vanity_url': 'bell.ca/mybell'}

        payload = {'intent': intent_clean, 'tag': 'default'}
        api_response = tools.intent_sdl_mapping_intent_sdl_mapping(payload).json()
        vanity_url = api_response.get('url', 'bell.ca/mybell')
        set_variable('vanity_url', vanity_url)
        print('Business logic success')
        return {'status': 'success', 'vanity_url': vanity_url}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the customer they can review their account details in the MyBell app without providing a specific URL.'}
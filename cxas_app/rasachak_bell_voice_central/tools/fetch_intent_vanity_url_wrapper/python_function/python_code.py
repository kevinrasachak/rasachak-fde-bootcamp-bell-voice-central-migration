def fetch_intent_vanity_url_wrapper(intent_route: str = "", brand: str = "", language: str = "") -> dict:
    '''Webhook Wrapper Tool for intent vanity URL retrieval.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {"url": "bell.ca/mock-support"}

        payload = {
            "intent_route": intent_route.strip(),
            "brand": brand.strip(),
            "language": language.strip()
        }
        response = tools.intent_sdl_mapping_get(payload).json()
        print("Business logic success - URL fetched")
        return {"url": response.get("url", "bell.ca/support")}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the user that we are experiencing technical difficulties and offer bell.ca/support as a fallback URL."}
def get_intent_sdl_mapping(route: str = "") -> dict:
    '''Fetches fallback URL for failures from intent-sdl-mapping API.'''
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            print("Business logic success: Mock SDL mapped")
            return {"status": "success", "url": "https://bell.ca/support"}

        payload = {"route": route}
        result = tools.intent_sdl_mapping_intent_sdl_mapping(payload).json()

        print("Business logic success: Webhook mapped")
        return {"status": "success", "data": result}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer alternative ways to resolve their issue."}
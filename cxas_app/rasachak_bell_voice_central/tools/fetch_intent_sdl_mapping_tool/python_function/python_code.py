def fetch_intent_sdl_mapping_tool(intent_name: str = "", brand: str = "", language: str = "") -> dict:
    '''Webhook Wrapper: Fetches the vanity URL for self-serve fallback based on intent and brand.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {"vanity_url": "bell.ca/mock-support", "webhook_success": True}
        payload = {"intent": intent_name, "brand": brand, "language": language}
        res = tools.intent_sdl_mapping_default(payload).json()
        print("Business logic success")
        return {"vanity_url": res.get("url", "bell.ca/support"), "webhook_success": True}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "webhook_success": False, "agent_action": "Transition to bell_Feedback explaining self-serve at bell.ca/support."}
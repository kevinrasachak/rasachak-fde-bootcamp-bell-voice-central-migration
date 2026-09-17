def fetch_customized_sdl_url(brand: str, language: str, route: str) -> dict:
    '''Webhook Wrapper & State Manipulator. Replaces intent-sdl-mapping webhook.'''
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            url = "bell.ca/support" if "en" in language.lower() else "bell.ca/soutien"
            set_variable("faq_link", url)
            set_variable("webhook_success", True)
            print("Business logic success (mock)")
            return {"status": "success", "url": url}

        payload = {"brand": brand, "language": language, "intent": route}
        api_response = tools.intent_sdl_mapping_post(payload).json()

        url = api_response.get("url")
        if url:
            set_variable("faq_link", url)
            set_variable("webhook_success", True)
            print("Business logic success")
            return {"status": "success", "url": url}
        else:
            set_variable("webhook_success", False)
            print("No URL found in response")
            return {"status": "success", "message": "No URL found"}

    except Exception as e:
        logger.error(f"Crash: {e}")
        set_variable("webhook_success", False)
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties."}
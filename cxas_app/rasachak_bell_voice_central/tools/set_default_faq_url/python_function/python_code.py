def set_default_faq_url(default_url: str) -> dict:
    '''State Manipulator. Assigns fallback URL to faq_link.'''
    try:
        sanitized_url = default_url.strip()
        set_variable("faq_link", sanitized_url)
        print("Business logic success")
        return {"status": "success", "faq_link": sanitized_url}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Proceed with conversational flow."}
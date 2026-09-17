def prepare_sms_content_tool(language: str = "") -> dict:
    '''State/Variable Manipulator: Sets sms_type and sms_content localized messages for pre-auth setup.'''
    try:
        lang_clean = language.lower().strip() if language else "en"
        if "fr" in lang_clean:
            content = "Vous pouvez visiter https://m.bell.ca/chatpreauthorizedbankf pour configurer les paiements préautorisés dans l'appli MonBell. ( bell.ca/apropos )"
        else:
            content = "You can visit https://m.bell.ca/chatmanagepaymente to set up pre-authorized payments in the MyBell app. ( bell.ca/about-us )"
        set_variable("sms_type", "Public")
        set_variable("sms_content", content)
        print("Business logic success")
        return {"sms_type": "Public", "sms_content": content, "status": "success"}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely apologize and route the user to bell_Feedback."}
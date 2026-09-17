def set_sms_payload() -> dict:
    '''State/Variable Manipulator. Evaluates language session variable and sets SMS payload.'''
    try:
        lang = get_variable("language") or "en"
        lang = str(lang).lower().strip()
        set_variable("sms_type", "Public")

        if "fr" in lang:
            content = "Mess. de Bell: Vous pouvez visiter https://m.bell.ca/ecgererpaiement pour effectuer un paiement dans l'application MonBell. ( bell.ca/apropos )"
        else:
            content = "Bell msg: You can visit https://m.bell.ca/ecmanagepayment to make a payment in the MyBell app. ( bell.ca/about-us )"

        set_variable("sms_content", content)
        print("SMS payload set successfully.")
        return {"status": "success", "sms_content": content}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Proceed with fallback SMS text."}
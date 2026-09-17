def format_sms_content_tool(language: str = "", route: str = "") -> dict:
    '''Evaluates context to format SMS content and update global variables securely.'''
    try:
        sanitized_lang = language.lower().strip()
        sanitized_route = route.lower().strip().replace(' ', '_')

        sms_content = ""
        hardstop = False

        print("Evaluating language and route for SMS content formatting")
        if sanitized_lang == "en":
            if sanitized_route in ["payment_update_autopay", "payment_setup_autopay"]:
                sms_content = "You can visit https://m.bell.ca/chatpreauthorizedbanke to complete setting up Pre Authorized payment in MyBell. (bell.ca/about-us )"
            elif sanitized_route == "payment_make_payment":
                sms_content = "Bell msg: You can visit https://m.bell.ca/ecmanagepayment to make a payment in the MyBell app. ( bell.ca/about-us )"
            else:
                hardstop = True
        elif sanitized_lang == "fr-ca":
            if sanitized_route in ["payment_update_autopay", "payment_setup_autopay"]:
                sms_content = "Vous pouvez visiter le https://m.bell.ca/chatpreauthorizedbankf pour terminer la configuration du prélèvement automatique dans MonBell. ( bell.ca/apropos )"
            elif sanitized_route == "payment_make_payment":
                sms_content = "Mess. de Bell: Vous pouvez visiter https://m.bell.ca/ecgererpaiement pour effectuer un paiement dans l'application MonBell. ( bell.ca/apropos )"
            else:
                hardstop = True
        else:
            hardstop = True

        if hardstop:
            print("No match found, setting hardstop flag")
            set_variable("hardstop", True)
            return {"status": "success", "hardstop_triggered": True, "agent_action": "Transition to the bell_aqd exit route."}
        else:
            print("Match found, setting sms_type and sms_content")
            set_variable("sms_type", "Public")
            set_variable("sms_content", sms_content)
            return {"status": "success", "sms_formatted": True, "agent_action": "Route the user to the SMS Trigger flow."}

    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "A technical error occurred while preparing the text message. Politely apologize and offer standard fallback support."}
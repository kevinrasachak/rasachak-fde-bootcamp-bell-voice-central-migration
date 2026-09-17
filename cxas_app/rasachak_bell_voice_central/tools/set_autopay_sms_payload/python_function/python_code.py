def set_autopay_sms_payload(language: str = "en", is_accepted: bool = False, is_different_number: bool = False, is_maintenance_path: bool = False) -> dict:
    '''Evaluates user confirmation and sets sms-related session variables.'''
    try:
        lang = str(language).lower().strip()

        if is_maintenance_path:
            set_variable("preauth_exit_3", True)

        if is_accepted or is_different_number:
            set_variable("sms_type", "Public")
            if "fr" in lang:
                set_variable("sms_content", "Vous pouvez visiter https://m.bell.ca/chatmanagepaymentf pour annuler les paiements préautorisés dans l'appli MonBell. ( bell.ca/apropos )")
            else:
                set_variable("sms_content", "You can visit https://m.bell.ca/chatmanagepaymente to cancel pre-authorized payments in the MyBell app. ( bell.ca/about-us )")

        if is_different_number:
            set_variable("different_number", True)

        if not is_accepted and not is_different_number:
            set_variable("sms_send_status", "Declined")

        print("Business logic success. SMS payload variables set.")
        return {"status": "success"}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
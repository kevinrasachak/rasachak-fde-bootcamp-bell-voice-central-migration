def check_home_phone_status(contact_number: str) -> dict:
    '''Webhook Wrapper. Checks if the collected number is a home phone within the BAN.'''
    try:
        mock_mode = get_variable("mock_mode")
        sanitized_number = str(contact_number).strip() if contact_number else ""

        if mock_mode:
            print("Mock mode enabled, returning dummy data")
            is_home_phone = False
            set_variable("is_home_phone", is_home_phone)
            return {"status": "success", "is_home_phone": is_home_phone}

        payload = {"contact_number": sanitized_number}
        api_response = tools.cpm_profile_info_hp_in_ban(payload).json()
        print("Business logic success")

        is_home_phone = api_response.get("is_home_phone", False)
        set_variable("is_home_phone", is_home_phone)

        return {"status": "success", "is_home_phone": is_home_phone}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
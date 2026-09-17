def check_number_in_account(phone_number: str = "") -> dict:
    '''State/Variable Manipulator: Checks if the phone_number exists in customer_id_search_response.'''
    import json
    try:
        raw_response = get_variable("customer_id_search_response")
        is_in_account = False

        if isinstance(raw_response, str):
            try:
                raw_response = json.loads(raw_response)
            except:
                raw_response = []

        if not isinstance(raw_response, list):
            raw_response = [raw_response] if raw_response else []

        sanitized_phone = str(phone_number).strip().replace(" ", "").replace("-", "")

        for item in raw_response:
            if isinstance(item, dict):
                users = item.get("users", [])
                for user in users:
                    if isinstance(user, dict):
                        contact = user.get("contact_number")
                        if contact:
                            sanitized_contact = str(contact).strip().replace(" ", "").replace("-", "")
                            if sanitized_contact == sanitized_phone:
                                is_in_account = True
                                break
            if is_in_account:
                break

        set_variable("is_in_account", is_in_account)
        print(f"Business logic success. is_in_account: {is_in_account}")
        return {"status": "success", "is_in_account": is_in_account}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Assume the number is not in the account and continue with normal verification."}
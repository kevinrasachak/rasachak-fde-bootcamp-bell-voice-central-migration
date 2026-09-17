def submit_cc_payment_details(card_number: str = "", expiry_month: str = "", expiry_year: str = "", cvv_number: str = "") -> dict:
    '''Submits CC details to pre-auth-payment API.'''
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            set_variable("cc_details_valid", True)
            set_variable("cc_error_code_id", "000")
            print("Business logic success: Mock CC submitted")
            return {"status": "success", "cc_details_valid": True}

        payload = {
            "card_number": card_number,
            "expiry_month": expiry_month,
            "expiry_year": expiry_year,
            "cvv_number": cvv_number
        }

        result = tools.pre_auth_payment_cc_payment_details(payload).json()

        is_valid = result.get("isValid", False)
        error_code = result.get("errorCodeID", "")
        set_variable("cc_details_valid", is_valid)
        set_variable("cc_error_code_id", error_code)

        print("Business logic success: Webhook submitted")
        return {"status": "success", "data": result}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties processing the payment and offer an alternative method."}
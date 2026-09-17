def check_existing_payment_method(menu_type: str = "", brand: str = "") -> dict:
    '''Webhook Wrapper. Calls the pre-auth-payment service to fetch existing payment methods.'''
    import json
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            set_variable("webhook_success", True)
            return {"result": {"webhook_success": True, "paymentMethod": "None"}}

        payload = {"menu_type": menu_type, "brand": brand}
        api_response = tools.pre_auth_payment_get_existing(payload).json()
        print("Business logic success - check_existing_payment_method")

        payment_method = api_response.get("paymentMethod", "None")
        set_variable("webhook_success", True)

        return {"result": {"webhook_success": True, "paymentMethod": payment_method}}
    except Exception as e:
        logger.error(f"Crash: {e}")
        set_variable("webhook_success", False)
        return {"error": str(e), "agent_action": "Apologize to the user and state you are having trouble confirming payment methods. Offer to send a text to their device to pay via the MyBell app."}
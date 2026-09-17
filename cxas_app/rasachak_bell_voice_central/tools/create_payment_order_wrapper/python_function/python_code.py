def create_payment_order_wrapper() -> dict:
    '''Webhook Wrapper for generating a one-time payment order.'''
    import json
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            print("Mock mode enabled for create-order.")
            set_variable("transaction_id", "mock_order_12345")
            set_variable("webhook_success", True)
            return {"status": "success", "transaction_id": "mock_order_12345"}

        payload = {}
        api_response = tools.one_time_payment_create_order(payload).json()
        print("Business logic success")

        order_form_id = api_response.get("OrderFormId", "unknown")
        if order_form_id != "unknown":
            set_variable("transaction_id", order_form_id)
            set_variable("webhook_success", True)
            return {"status": "success"}
        else:
            set_variable("webhook_success", False)
            return {"status": "failure", "error": "OrderFormId not found"}
    except Exception as e:
        logger.error(f"Crash: {e}")
        set_variable("webhook_success", False)
        return {"error": str(e), "agent_action": "Politely inform the customer that the payment system is down and offer to send an SMS link to pay via the MyBell app, or fallback to the SDL mapping."}
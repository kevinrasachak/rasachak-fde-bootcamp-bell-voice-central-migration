def create_payment_order(billing_account: str = "") -> dict:
    '''Initiates a payment notification order.'''
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            return {"result": {"status": "success", "transaction_id": "TXN123456789", "current_balance": 150.0, "due_date": "2023-12-01"}}

        payload = {"billing_account": billing_account}
        api_response = tools.payment_notification_create_order(payload).json()

        print("Business logic success")
        return {"result": api_response}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the user that the system is unable to process the request at this time and offer an alternative (WEBHOOK_FAILURE_FALLBACK)."}
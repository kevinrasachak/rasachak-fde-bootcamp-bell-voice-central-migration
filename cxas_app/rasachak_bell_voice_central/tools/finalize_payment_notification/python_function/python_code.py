def finalize_payment_notification(transaction_id: str = "", amount_paid: float = 0.0, payment_method: str = "", billing_account: str = "") -> dict:
    '''Updates the order with the user's payment amount/method, submits the order, and fetches the updated past_due_amount.'''
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            return {"result": {"status": "success", "confirmation_number": "CONF999888777", "past_due_amount": 0.0, "amountPaid": amount_paid}}

        sanitized_pmt = payment_method.lower().strip().replace(" ", "")
        payload = {"transaction_id": transaction_id, "amount_paid": amount_paid, "payment_method": sanitized_pmt, "billing_account": billing_account}
        api_response = tools.payment_notification_submit_sequence(payload).json()

        print("Business logic success")
        return {"result": api_response}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the user that the system is unable to process the request at this time and offer an alternative (WEBHOOK_FAILURE_FALLBACK)."}
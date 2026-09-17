def submit_payment_arrangement_order(billing_account: str, amount: float, payment_type: str) -> dict:
    '''Webhook Wrapper to submit the payment arrangement order.'''
    import json
    import uuid
    try:
        mock_mode = get_variable('mock_mode')
        sanitized_type = str(payment_type).strip().title()

        if mock_mode:
            print("Business logic success - Mocked submit order")
            return {"confirmationNumber": f"CONF-{uuid.uuid4().hex[:8].upper()}", "webhook_success": True}

        payload = {"billing_account": billing_account, "amount": amount, "payment_type": sanitized_type}
        api_response = tools.UNKNOWN_CUSTOM_API_submit_payment_arrangement_order(payload).json()
        print("Business logic success")
        return {"confirmationNumber": api_response.get("confirmationNumber", ""), "webhook_success": api_response.get("webhook_success", True)}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "webhook_success": False, "agent_action": "Transition to HANDLE_SYSTEM_FAILURE. Inform the user that system maintenance prevents setting up the arrangement, and ask if they want a text message to set it up in MyBell."}
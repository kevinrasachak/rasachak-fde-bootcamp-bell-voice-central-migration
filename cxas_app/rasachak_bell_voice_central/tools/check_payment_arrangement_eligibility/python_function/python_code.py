def check_payment_arrangement_eligibility(billing_account: str = "", menu_type: str = "", brand: str = "") -> dict:
    '''Webhook Wrapper. Calls the payment-arrangement service to check user eligibility criteria.'''
    import json
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            set_variable("webhook_success", True)
            set_variable("eligibilityCriteria", True)
            set_variable("installmentDetails", [])
            set_variable("installmentCheck", 0)
            return {"result": {"status": "success", "eligibilityCriteria": True}}

        payload = {"billing_account": billing_account, "menu_type": menu_type, "brand": brand}
        api_response = tools.payment_arrangement_get_eligibility_criteria(payload).json()
        print("Business logic success - check_payment_arrangement_eligibility")

        show_payment = api_response.get("showPaymentArrangementLink", False)
        installment_details = api_response.get("installmentDetails", [])

        set_variable("webhook_success", True)
        set_variable("eligibilityCriteria", show_payment)
        set_variable("installmentDetails", installment_details)
        set_variable("installmentCheck", len(installment_details))

        return {"result": {"status": "success", "eligibilityCriteria": show_payment, "installmentCheck": len(installment_details)}}
    except Exception as e:
        logger.error(f"Crash: {e}")
        set_variable("webhook_success", False)
        return {"error": str(e), "agent_action": "Apologize to the user and state you are having trouble confirming payment methods. Offer to send a text to their device to pay via the MyBell app."}
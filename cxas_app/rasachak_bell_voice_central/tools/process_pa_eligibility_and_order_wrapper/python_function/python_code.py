def process_pa_eligibility_and_order_wrapper(billing_account_number: float = 0.0, brand: str = "") -> dict:
    '''Webhook Wrapper bundling a sequential chain: 1) get-delinquency-details, 2) get-eligibility-criteria, 3) create-order.'''
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            return {"is_delinquent": True, "is_eligible": True, "order_created": True, "installment_count": 2, "error_reason": ""}

        payload = {
            "billing_account_number": billing_account_number,
            "brand": brand
        }
        result = tools.payment_arrangement_orchestration_chain_post_payment_arrangement_orchestration_chain(payload).json()
        print("Business logic success")
        return result
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user that the automated check cannot proceed and offer to send an SMS link to set up Payment Arrangement in MyBell."}
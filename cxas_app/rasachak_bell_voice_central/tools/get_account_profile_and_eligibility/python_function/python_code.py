def get_account_profile_and_eligibility(billing_account: str = "", clid: int = 0, CIRN: int = 0) -> dict:
    '''Fetches ban profile, customer profile, NPA-NXX lookup, and PA eligibility sequentially to establish account status and eligibility.'''
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            return {"result": {"status": "success", "auth_status": "Pass", "identification_status": "Pass", "showPaymentArrangementLink": True, "past_due_amount": 100.0, "oneBillIndicator": "N"}}

        payload = {"billing_account": billing_account, "clid": clid, "CIRN": CIRN}
        api_response = tools.Multiple_profile_lookups_get(payload).json()

        print("Business logic success")
        return {"result": api_response}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the user that the system is unable to process the request at this time and offer an alternative (WEBHOOK_FAILURE_FALLBACK)."}
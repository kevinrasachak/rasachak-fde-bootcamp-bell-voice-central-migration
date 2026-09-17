def get_ban_profile(billing_account: str) -> dict:
    '''Webhook Wrapper for fetching customer ban profile.'''
    import json
    from datetime import datetime, timedelta
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print("Business logic success - Mocked get_ban_profile")
            return {"pastDueAmount": 50.00, "currentBalance": 150.00, "calculated_payment_date": (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")}

        payload = {"billing_account": billing_account}
        api_response = tools.UNKNOWN_CUSTOM_API_get_ban_profile(payload).json()
        print("Business logic success")
        return {"pastDueAmount": api_response.get("pastDueAmount", 0.0), "currentBalance": api_response.get("currentBalance", 0.0), "calculated_payment_date": api_response.get("calculated_payment_date", "")}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Transition to HANDLE_SYSTEM_FAILURE. Inform the user that system maintenance prevents setting up the arrangement, and ask if they want a text message to set it up in MyBell."}
def get_account_profile_wrapper(billing_account_number: float = 0.0, profile_type_preference: str = "") -> dict:
    '''Webhook Wrapper for fetching ban-profile or customer-profile.'''
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            return {"accountType": "I", "accountSubType": "R", "oneBillIndicator": "N", "pastDueAmount": 100.0, "accountBalance": 100.0}

        payload = {
            "billing_account_number": billing_account_number,
            "profile_type_preference": profile_type_preference
        }
        result = tools.nm1_get_profiles_post_nm1_get_profiles(payload).json()
        print("Business logic success")
        return result
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user that the automated check cannot proceed and offer to send an SMS link to set up Payment Arrangement in MyBell."}
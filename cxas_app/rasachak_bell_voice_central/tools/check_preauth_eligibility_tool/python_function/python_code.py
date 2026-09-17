def check_preauth_eligibility_tool(billing_account: str = "") -> dict:
    '''Webhook Wrapper: Calls get-existing, then sequentially calls pa-eligibility if applicable. Returns payment_method_check and eligInd.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {"payment_method_check": "Regular", "eligInd": "Y", "webhook_success": True}
        payload = {"billing_account": billing_account}
        existing_res = tools.pre_auth_payment_get_existing(payload).json()
        pm_check = existing_res.get("paymentMethod", "Regular")
        if pm_check in ["PreAuthBank", "PreAuthCreditCard"]:
            print("Business logic success - Existing preauth found")
            return {"payment_method_check": pm_check, "eligInd": "N", "webhook_success": True}
        elig_res = tools.nm1_get_pa_eligibility(payload).json()
        elig_info = elig_res.get("paymentEligInfo", {}).get("eligibilityCheckInfo", {}).get("eligibilityInfo", [])
        elig_ind = "N"
        if isinstance(elig_info, list) and len(elig_info) > 1:
            elig_ind = elig_info[1].get("eligInd", "N")
        elif isinstance(elig_info, list) and len(elig_info) > 0:
            elig_ind = elig_info[0].get("eligInd", "N")
        print("Business logic success")
        return {"payment_method_check": pm_check, "eligInd": elig_ind, "webhook_success": True}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "webhook_success": False, "agent_action": "Inform the user that the request could not be completed and transition to <handle_flow_failure>."}
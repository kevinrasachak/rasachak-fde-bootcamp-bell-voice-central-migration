def fetch_billing_profile_tool(billing_account: str = "", banType: str = "", banSubType: str = "") -> dict:
    '''Webhook Wrapper: Evaluates banType and banSubType to conditionally call either customer-profile or ban-profile.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {"onebillindicator": "N", "errorCode": "1", "Bantype": banType or "I", "Bansubtype": banSubType or "R", "webhook_success": True}
        payload = {"billing_account": billing_account}
        is_cust = False
        bt = banType.upper()
        bst = banSubType.upper()
        if (bt == "I" and bst in ["B", "N", "5"]) or (bt == "C" and bst in ["V", "T", "P"]):
            is_cust = True
        if is_cust:
            res = tools.nm1_get_customer_profile(payload).json()
            data = {"onebillindicator": res.get("oneBill", ""), "errorCode": res.get("returnCode", ""), "Bantype": res.get("banType", ""), "Bansubtype": res.get("banSubType", ""), "webhook_success": True}
        else:
            res = tools.nm1_get_ban_profile(payload).json()
            data = {"onebillindicator": res.get("oneBillIndicator", ""), "errorCode": res.get("returnCode", ""), "Bantype": res.get("accountType", ""), "Bansubtype": res.get("accountSubType", ""), "webhook_success": True}
        print("Business logic success")
        return data
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "webhook_success": False, "agent_action": "Inform the user that the request could not be completed and transition to <handle_flow_failure>."}
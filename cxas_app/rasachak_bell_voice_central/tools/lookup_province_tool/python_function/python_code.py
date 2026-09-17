def lookup_province_tool(phone_number: str = "") -> dict:
    '''Webhook Wrapper: Extracts NPA and NXX components from a phone number, calls lookup API, and returns Province.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {"Province": "ON", "webhook_success": True}
        sanitized = phone_number.strip().replace(" ", "").replace("-", "").replace("+", "")
        npa = sanitized[-10:-7] if len(sanitized) >= 10 else "000"
        nxx = sanitized[-7:-4] if len(sanitized) >= 10 else "000"
        payload = {"npa": npa, "nxx": nxx}
        res = tools.npa_nxx_lookup_lookup(payload).json()
        print("Business logic success")
        return {"Province": res.get("province", ""), "webhook_success": True}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "webhook_success": False, "agent_action": "Inform the user that the request could not be completed and transition to <handle_flow_failure>."}
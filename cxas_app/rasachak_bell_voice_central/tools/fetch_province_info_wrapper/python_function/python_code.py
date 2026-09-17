def fetch_province_info_wrapper(cirn: int = 0, clid: int = 0) -> dict:
    '''Webhook Wrapper Tool to determine province based on NPA/NXX natively checking mock_mode.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {"province": "ON"}

        temp_num = str(cirn) if cirn and str(cirn) != "0" else str(clid)
        temp_num = "".join(filter(str.isdigit, temp_num))

        if len(temp_num) < 6:
            print("Business logic success - Invalid phone length, skipping province lookup")
            return {"province": "UNKNOWN"}

        npa = temp_num[:3]
        nxx = temp_num[3:6]
        payload = {"npa": npa, "nxx": nxx}

        response = tools.npa_nxx_lookup_get(payload).json()
        print("Business logic success - Province fetched")
        return {"province": response.get("province", "")}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Proceed to SMS confirmation smoothly, bypassing the province check due to technical errors."}
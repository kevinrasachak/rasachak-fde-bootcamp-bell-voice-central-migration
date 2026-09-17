def execute_business_transfer_protocol(tfn: str = "", cirn: float = 0, clid: float = 0, route: str = "", va_ibm_id: str = "") -> dict:
    '''Executes business transfer protocol by sequentializing configurations and department fetching.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print("Mock mode enabled, simulating business transfer protocol")
            set_variable('webhook_success', True)
            return {"webhook_success": True, "message": "Mock transfer data compiled successfully."}

        sanitized_route = str(route).strip()
        sanitized_tfn = str(tfn).strip()
        sanitized_ibm_id = str(va_ibm_id).strip()

        payload = {
            "dam_id": "BBM",
            "department": 955,
            "account_type": "B",
            "tfn": sanitized_tfn,
            "cirn": cirn if cirn else clid,
            "route": sanitized_route if sanitized_route else "other_speak_to_agent",
            "ibm_entry_point": sanitized_ibm_id
        }

        set_variable('dam_id', "BBM")
        set_variable('department', 955)
        set_variable('account_type', "B")
        set_variable('webhook_success', True)

        print("Business logic success, transfer payload assembled")
        return {"webhook_success": True, "data_pushed": payload}
    except Exception as e:
        set_variable('webhook_success', False)
        logger.error(f"Crash: {e}")
        return {"error": str(e), "webhook_success": False, "agent_action": "Inform the customer that we are experiencing technical difficulties and transfer to a live agent."}
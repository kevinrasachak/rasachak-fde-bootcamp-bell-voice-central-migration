def initialize_aqd_variables(clid: int = 0, cirn: int = 0, unique_services: list = []) -> dict:
    '''Parses session state. Formats clid, maps to CIRN, and counts unique services.'''
    try:
        clid_str = str(clid).strip() if clid else ""
        if len(clid_str) == 11:
            clid_str = clid_str[1:]
        elif len(clid_str) == 12:
            clid_str = clid_str[2:]

        cirn_str = str(cirn).strip() if cirn else ""
        if cirn_str in ["", "0", "0000000000"]:
            cirn_str = clid_str

        service_count = len(unique_services) if isinstance(unique_services, list) else 0

        set_variable("clid", int(clid_str) if clid_str.isdigit() else 0)
        set_variable("CIRN", int(cirn_str) if cirn_str.isdigit() else 0)
        set_variable("unique_service_count", service_count)

        print("Business logic success: Variables initialized.")
        return {"status": "success", "unique_service_count": service_count, "clid_formatted": clid_str, "cirn_formatted": cirn_str}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user that a system error occurred while processing their profile and prepare to transfer them to an agent."}
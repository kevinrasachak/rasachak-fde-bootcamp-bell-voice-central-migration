def get_agent_queue_details(lob: str = "", route: str = "", special_queue: str = "", cirn: int = 0) -> dict:
    '''Fetches target department_id and menu_id for agent routing based on evaluated flags.'''
    import json
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            print("Executing mock queue details fetch")
            return {"status": "success", "menu_id": "DEFAULT_MENU", "department_id": 2005}

        payload = {
            "lob": str(lob).strip().lower().replace(' ', '_'),
            "route": str(route).strip(),
            "special_queue": str(special_queue).strip(),
            "cirn": cirn
        }
        api_response = tools.AQD_get_agent_queue_details(payload).json()
        print("Business logic success: Queue details fetched.")
        return {"status": "success", "data": api_response}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user that the system is unable to route the call due to technical issues, and proceed to end the session."}
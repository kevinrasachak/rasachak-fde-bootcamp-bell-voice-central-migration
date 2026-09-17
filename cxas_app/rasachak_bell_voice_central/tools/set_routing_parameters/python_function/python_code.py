def set_routing_parameters(apb_location_id: int = 0, special_queue: str = "", event_type: str = "", hardstop: bool = False, page_id: str = "", flow_id: str = "", page_name: str = "") -> dict:
    '''Updates session variables to route the user to the correct downstream agent based on matched conditions.'''
    try:
        print("Executing set_routing_parameters")
        if apb_location_id != 0:
            set_variable("apb_location_id", apb_location_id)
        if special_queue != "":
            set_variable("special_queue", special_queue)
        if event_type != "":
            set_variable("event_type", event_type)
        if hardstop:
            set_variable("hardstop", hardstop)
        if page_id != "":
            set_variable("page_id", page_id)
        if flow_id != "":
            set_variable("flow_id", flow_id)
        if page_name != "":
            set_variable("page_name", page_name)
        print("Business logic success: Routing parameters set successfully")
        return {"status": "success", "message": "Variables updated successfully."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
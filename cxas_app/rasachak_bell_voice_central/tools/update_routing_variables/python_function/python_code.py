def update_routing_variables(identification_status: str = "", customer_type: str = "", route: str = "", hardstop: bool = False, page_name: str = "", page_id: str = "", flow_id: str = "") -> dict:
    '''State Manipulator to update routing variables before transitions.'''
    if get_variable("mock_mode"):
        return {
            "status": "success",
            "agent_action": "Variables successfully updated. Immediately execute the appropriate transition based on instructions.",
            "mocked_state": {
                "identification_status": identification_status if identification_status else "Pass",
                "customer_type": customer_type if customer_type else "consumer",
                "route": route if route else "M2 AuthenticationAndIdentity",
                "hardstop": hardstop,
                "page_name": page_name if page_name else "mock_page_name",
                "page_id": page_id if page_id else "mock_page_id",
                "flow_id": flow_id if flow_id else "mock_flow_id"
            }
        }
    else:
        try:
            if identification_status:
                set_variable('identification_status', identification_status)
            if customer_type:
                set_variable('customer_type', customer_type)
            if route:
                set_variable('route', route)
            set_variable('hardstop', hardstop)
            if page_name:
                set_variable('page_name', page_name)
            if page_id:
                set_variable('page_id', page_id)
            if flow_id:
                set_variable('flow_id', flow_id)
            print("Business logic success")
            return {"status": "success", "agent_action": "Variables successfully updated. Immediately execute the appropriate transition based on instructions."}
        except Exception as e:
            logger.error(f"Crash: {e}")
            return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
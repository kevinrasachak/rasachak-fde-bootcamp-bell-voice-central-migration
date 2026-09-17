def update_state_variables(route: str = "", event_type: str = "") -> dict:
    """State Manipulator. Sets routing and event tracking parameters (route, event_type) required by the conversational state machine before a transition."""
    try:
        if route:
            safe_route = str(route).strip()
            set_variable('route', safe_route)
            print(f"Updated route to: {safe_route}")

        if event_type:
            safe_event = str(event_type).strip()
            set_variable('event_type', safe_event)
            print(f"Updated event_type to: {safe_event}")

        print("Business logic success")
        return {"status": "success", "route_set": route, "event_type_set": event_type}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
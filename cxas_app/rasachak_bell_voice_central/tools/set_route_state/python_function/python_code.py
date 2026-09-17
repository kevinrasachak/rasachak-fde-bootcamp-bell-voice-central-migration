def set_route_state(route_value: str) -> dict:
    '''State Manipulator. Sets the 'route' variable in the session state to the provided value.'''
    try:
        sanitized_val = str(route_value).strip()
        set_variable('route', sanitized_val)
        print(f"Successfully set route to {sanitized_val}")
        return {"status": "success", "route": sanitized_val}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
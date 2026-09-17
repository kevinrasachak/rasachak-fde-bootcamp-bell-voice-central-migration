def update_session_route(new_route_value: str) -> dict:
    '''State Manipulator. Generative LLMs cannot reliably set or update session variables via plain text. This tool explicitly mutates the session state by updating the `route` variable to the provided string value.'''
    try:
        sanitized_route = str(new_route_value).strip()
        set_variable('route', sanitized_route)
        print(f"Business logic success: Route updated to {sanitized_route}")
        return {"status": "success", "message": f"Route successfully updated to {sanitized_route}"}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
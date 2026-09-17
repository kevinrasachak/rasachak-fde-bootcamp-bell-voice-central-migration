def set_routing_variables(special_queue_value: str = "") -> dict:
    '''State Manipulator. Updates the 'special_queue' variable in the session state.'''
    try:
        sanitized_val = special_queue_value.strip()
        set_variable('special_queue', sanitized_val)
        print("Business logic success")
        return {"status": "success", "message": f"special_queue set to {sanitized_val}"}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and gracefully end the session."}
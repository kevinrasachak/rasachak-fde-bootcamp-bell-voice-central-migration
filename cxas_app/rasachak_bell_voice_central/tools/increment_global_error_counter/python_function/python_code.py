def increment_global_error_counter() -> dict:
    '''State/Variable Manipulator. Retrieves the session variable 'global_error_counter', adds 1, saves it back, and returns the new value.'''
    try:
        current_val = get_variable("global_error_counter")
        if current_val is None or current_val == "":
            current_val = 0
        new_val = int(current_val) + 1
        set_variable("global_error_counter", new_val)
        print(f"Incremented global_error_counter to {new_val}")
        return {"status": "success", "global_error_counter": new_val}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Explain the technical error to the user and offer to transfer them to a representative."}
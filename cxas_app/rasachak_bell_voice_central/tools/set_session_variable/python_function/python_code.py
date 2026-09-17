def set_session_variable(variable_name: str = "", variable_value: str = "") -> dict:
    '''State Manipulator. Generative LLMs cannot reliably set session variables via plain text. This tool explicitly updates a given session variable to a specified string value (e.g., setting 'route' to 'sales_order_device').'''
    try:
        sanitized_name = variable_name.strip()
        sanitized_value = variable_value.strip()
        if not sanitized_name:
            return {"error": "variable_name is required", "agent_action": "Log internal error"}
        set_variable(sanitized_name, sanitized_value)
        print(f"Business logic success: Variable {sanitized_name} set to {sanitized_value}")
        return {"status": "success", "message": f"Successfully set {sanitized_name}."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
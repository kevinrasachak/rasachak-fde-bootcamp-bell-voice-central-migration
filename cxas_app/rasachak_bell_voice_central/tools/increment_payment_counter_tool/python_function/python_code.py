def increment_payment_counter_tool() -> dict:
    '''State/Variable Manipulator: Increments the incorrect_payment_method_counter session variable and resets payment_method.'''
    try:
        current_count = int(get_variable("incorrect_payment_method_counter") or 0)
        new_count = current_count + 1
        set_variable("incorrect_payment_method_counter", new_count)
        set_variable("payment_method", None)
        print(f"Business logic success: Counter incremented to {new_count}")
        return {"incorrect_payment_method_counter": new_count, "status": "success"}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that the payment method is unaccepted and guide them to <handle_flow_failure>."}
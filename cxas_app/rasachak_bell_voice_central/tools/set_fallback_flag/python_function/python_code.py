def set_fallback_flag(fallback_flag_value: bool = True) -> dict:
    '''State Manipulator. Updates the conversation state by setting the fallback_3_triggered session variable to True.'''
    if get_variable("mock_mode"):
        return {"status": "success", "fallback_3_triggered": fallback_flag_value}

    import logging
    logger = logging.getLogger(__name__)
    try:
        set_variable('fallback_3_triggered', fallback_flag_value)
        print("Business logic success: fallback_3_triggered set.")
        return {"status": "success", "fallback_3_triggered": fallback_flag_value}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
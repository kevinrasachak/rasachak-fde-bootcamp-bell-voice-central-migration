def reset_session_counters() -> dict:
    '''State Manipulator. Sets sms_counter, loud_counter, more_time_counter, mistake_counter, phn_invalid_counter, fallback_counter, and repeat_counter to 0 in the session state.'''
    try:
        set_variable('sms_counter', 0)
        set_variable('loud_counter', 0)
        set_variable('more_time_counter', 0)
        set_variable('mistake_counter', 0)
        set_variable('phn_invalid_counter', 0)
        set_variable('fallback_counter', 0)
        set_variable('repeat_counter', 0)
        set_variable('SMS_Counter', 0)
        set_variable('Loud_Counter', 0)
        set_variable('More_Time_Counter', 0)
        set_variable('Mistake_Counter', 0)
        set_variable('PHN_Invalid_Counter', 0)
        print("Session counters successfully reset to 0.")
        return {"status": "success", "message": "All session counters have been initialized to 0."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Silently note the technical error and proceed to the SMS Trigger flow."}
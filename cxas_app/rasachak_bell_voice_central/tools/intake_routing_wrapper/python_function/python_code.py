def intake_routing_wrapper(intake_tfn: str = "") -> dict:
    '''Webhook Wrapper tool for TFN routing lookup.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print("Mock mode enabled, returning dummy intake routing.")
            return {
                "success": True,
                "caller_channel": "Voice",
                "va_entry_flow": "bell_aqd",
                "va_ibm_id": "ibm-12345"
            }

        sanitized_tfn = intake_tfn.replace('-', '').replace(' ', '').strip()
        payload = {"intake_tfn": sanitized_tfn}

        api_response = tools.intake_routing_post_intake_routing(payload).json()
        print("Business logic success")

        return {
            "success": True,
            "caller_channel": api_response.get("va_caller_channel", ""),
            "va_entry_flow": api_response.get("va_entry_flow", ""),
            "va_ibm_id": api_response.get("va_ibm_id", "")
        }
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {
            "error": str(e),
            "agent_action": "Inform the user that the TFN routing lookup failed and ask them to try entering the TFN again."
        }
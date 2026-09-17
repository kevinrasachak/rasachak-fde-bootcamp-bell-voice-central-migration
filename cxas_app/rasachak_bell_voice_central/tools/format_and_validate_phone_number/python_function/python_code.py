def format_and_validate_phone_number(raw_phone_number: str = "") -> dict:
    '''State/Variable Manipulator: Sanitizes and validates a 10-digit phone number.'''
    try:
        import re
        sanitized = re.sub(r"\D", "", str(raw_phone_number))
        if len(sanitized) == 10:
            set_variable("clid", int(sanitized))
            print("Business logic success - 10-digit phone number validated")
            return {"status": "valid", "formatted_number": sanitized}
        elif len(sanitized) == 11 and sanitized.startswith("1"):
            sanitized_10 = sanitized[1:]
            set_variable("clid", int(sanitized_10))
            print("Business logic success - 11-digit phone number validated and trimmed")
            return {"status": "valid", "formatted_number": sanitized_10}
        else:
            print("Business logic check - Invalid length")
            return {"status": "invalid", "message": "Phone number must be exactly 10 digits."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Ask the user to repeat their phone number."}
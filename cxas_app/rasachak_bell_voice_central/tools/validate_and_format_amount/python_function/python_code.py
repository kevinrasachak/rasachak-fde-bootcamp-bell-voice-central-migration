def validate_and_format_amount(raw_amount: str) -> dict:
    '''State Manipulator. Parses input, checks if >= 1 and <= 10000, formats to 2 decimal places. Returns is_valid, formatted_amount, and error_reason.'''
    import re
    try:
        sanitized_arg = str(raw_amount).strip().replace('$', '').replace(',', '').replace(' ', '')
        val = float(sanitized_arg)
        if 1.0 <= val <= 10000.0:
            set_variable('bad_amount', 0)
            print("Business logic success - amount valid")
            return {"is_valid": True, "formatted_amount": round(val, 2), "error_reason": ""}
        else:
            bad_amt = get_variable('bad_amount')
            bad_amt_val = int(bad_amt) if bad_amt is not None else 0
            set_variable('bad_amount', bad_amt_val + 1)
            print("Business logic success - amount invalid range")
            return {"is_valid": False, "formatted_amount": 0.0, "error_reason": "Amount must be between $1 and $10,000."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        bad_amt = get_variable('bad_amount')
        bad_amt_val = int(bad_amt) if bad_amt is not None else 0
        set_variable('bad_amount', bad_amt_val + 1)
        return {"error": "Could not parse amount", "agent_action": "Inform the user that the amount was not understood and ask them to repeat."}
def validate_payment_amount(spoken_amount: str) -> dict:
    '''State/Variable Manipulator. Validates the user's spoken amount, converts to NUMBER, checks limits.'''
    try:
        sanitized = str(spoken_amount).replace("$", "").replace(",", "").strip()
        import re
        match = re.search(r"[0-9.]+", sanitized)
        if not match:
            raise ValueError("No numeric value found.")

        amount = float(match.group())
        if 1 <= amount <= 10000:
            set_variable("clp_bad_amount", 0)
            set_variable("clp_amount_paid", amount)
            print("Amount validated successfully.")
            return {"status": "valid", "amount": amount}
        else:
            bad_amount = get_variable("clp_bad_amount") or 0
            bad_amount += 1
            set_variable("clp_bad_amount", bad_amount)
            breached = bool(bad_amount >= 3)
            print(f"Amount invalid. Bad amount count: {bad_amount}")
            return {"status": "invalid", "breached_limit": breached, "agent_action": "Inform the user that payments must be between $1 and $10,000."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        bad_amount = get_variable("clp_bad_amount") or 0
        bad_amount += 1
        set_variable("clp_bad_amount", bad_amount)
        return {"error": "Invalid format", "breached_limit": bool(bad_amount >= 3), "agent_action": "Inform the user that payments must be between $1 and $10,000."}
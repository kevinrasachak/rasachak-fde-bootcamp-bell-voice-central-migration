def evaluate_consolidated_customer_logic(account_type: str = "", account_sub_type: str = "", one_bill_indicator: str = "") -> dict:
    '''State Manipulator. Evaluates if the customer is a supported consolidated customer based on account parameters.'''
    try:
        print("Executing evaluate_consolidated_customer_logic")
        sanitized_type = account_type.strip().upper()
        sanitized_sub = account_sub_type.strip().upper()
        sanitized_one_bill = one_bill_indicator.strip().upper()

        is_supported = False
        if (sanitized_type == "I" and sanitized_sub in ["R", "P", "N", "B", "5", "E"]):
            is_supported = True
        elif (sanitized_type == "C" and sanitized_sub in ["P", "V", "T"]):
            is_supported = True
        elif (sanitized_one_bill in ["M", "Y"]):
            is_supported = True

        print(f"Logic result: {is_supported}")
        return {"is_supported_consolidated_customer": is_supported}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user that the automated check cannot proceed and offer to send an SMS link to set up Payment Arrangement in MyBell."}
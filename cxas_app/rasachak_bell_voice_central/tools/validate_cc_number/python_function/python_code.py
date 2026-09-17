def validate_cc_number(raw_cc_input: str = "") -> dict:
    '''Validates the raw CC number string, determines card brand, and saves to session variables.'''
    try:
        import re
        sanitized_cc = re.sub(r'\D', '', str(raw_cc_input))
        if not sanitized_cc:
            return {"error": "No valid digits found in input", "is_valid": False}

        card_brand = "UNKNOWN"
        cc_type = "UNKNOWN"
        is_valid = False

        if sanitized_cc.startswith('34') or sanitized_cc.startswith('37'):
            card_brand = "AMEX"
            cc_type = "AX"
            if len(sanitized_cc) == 15:
                is_valid = True
        elif sanitized_cc.startswith('4'):
            card_brand = "VISA"
            cc_type = "VI"
            if len(sanitized_cc) == 16:
                is_valid = True
        elif sanitized_cc.startswith('5'):
            card_brand = "MC"
            cc_type = "MC"
            if len(sanitized_cc) == 16:
                is_valid = True
        else:
            if len(sanitized_cc) in [15, 16]:
                card_brand = "UNKNOWN"
                is_valid = True

        set_variable("card_number", sanitized_cc)
        set_variable("card_brand", card_brand)
        set_variable("cc_type", cc_type)

        print("Business logic success: CC validated")
        return {"status": "success", "is_valid": is_valid, "card_brand": card_brand}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user that there was a technical error processing the card and ask them to try again."}
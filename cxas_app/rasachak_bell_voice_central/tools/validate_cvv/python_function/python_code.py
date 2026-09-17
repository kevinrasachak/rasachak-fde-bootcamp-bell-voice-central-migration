def validate_cvv(raw_cvv_input: str = "", card_brand: str = "") -> dict:
    '''Validates CVV length based on card brand.'''
    try:
        import re
        sanitized_cvv = re.sub(r'\D', '', str(raw_cvv_input))
        brand = str(card_brand).upper()

        is_valid = False
        if brand in ['AMEX', 'AX']:
            if len(sanitized_cvv) == 4:
                is_valid = True
        else:
            if len(sanitized_cvv) == 3:
                is_valid = True

        if is_valid:
            set_variable("cvv_number", sanitized_cvv)

        print("Business logic success: CVV validated")
        return {"status": "success", "is_valid": is_valid}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user of a validation system error and ask them to retry."}
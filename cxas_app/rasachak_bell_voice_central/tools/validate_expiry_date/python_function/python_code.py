def validate_expiry_date(raw_expiry_input: str = "") -> dict:
    '''Validates expiry date is future and correctly formatted MMYY/MMYYYY.'''
    try:
        import re
        from datetime import datetime
        sanitized_expiry = re.sub(r'\D', '', str(raw_expiry_input))

        if len(sanitized_expiry) == 4:
            month = sanitized_expiry[:2]
            year = sanitized_expiry[2:]
        elif len(sanitized_expiry) == 6:
            month = sanitized_expiry[:2]
            year = sanitized_expiry[4:]
        else:
            return {"error": "Invalid format", "is_valid": False}

        month_int = int(month)
        year_int = int("20" + year if len(year) == 2 else year)

        if not (1 <= month_int <= 12):
            return {"error": "Invalid month", "is_valid": False}

        now = datetime.now()
        current_year = now.year
        current_month = now.month

        is_valid = False
        if year_int > current_year or (year_int == current_year and month_int >= current_month):
            is_valid = True
            set_variable("expiry_month", month)
            set_variable("expiry_year", year[-2:])
            set_variable("expiry_date", month + year[-2:])

        print("Business logic success: Expiry validated")
        return {"status": "success", "is_valid": is_valid, "expiry_month": month, "expiry_year": year[-2:]}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user that there was a technical error and ask them to retry entering the expiry date."}
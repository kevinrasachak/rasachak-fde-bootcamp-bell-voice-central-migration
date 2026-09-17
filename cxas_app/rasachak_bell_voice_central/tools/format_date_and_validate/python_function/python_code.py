def format_date_and_validate(spoken_day: str, wfas_availability_response: dict) -> dict:
    '''Validates spoken day against available dates.'''
    try:
        sanitized_day = spoken_day.lower().strip().replace(' ', '_')
        available_dates = wfas_availability_response.get("available_dates", [])

        date_within_range = False
        if available_dates:
            date_within_range = any(sanitized_day in str(d).lower() for d in available_dates)

        result = {
            "full_date": spoken_day,
            "day_of_week": "Unknown",
            "date_within_range": date_within_range
        }
        print("Business logic success")
        return result
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely ask the user to repeat or rephrase the day they would prefer."}
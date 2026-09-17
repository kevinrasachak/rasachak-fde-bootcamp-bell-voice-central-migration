def extract_time_slot_object(time_input: str, slot_details: dict) -> dict:
    '''Parses selected time string against the interval array.'''
    try:
        sanitized_input = time_input.lower().strip().replace(' ', '')
        intervals = slot_details.get("intervals", [])

        selected_start_time = ""
        selected_end_time = ""
        selected_interval_name = ""

        for interval in intervals:
            name = interval.get("interval_name", "").lower()
            if name and name in sanitized_input:
                selected_start_time = interval.get("start_time", "")
                selected_end_time = interval.get("end_time", "")
                selected_interval_name = interval.get("interval_name", "")
                break

        result = {
            "selected_start_time": selected_start_time,
            "selected_end_time": selected_end_time,
            "selected_interval_name": selected_interval_name
        }
        print("Business logic success")
        return result
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely ask the user to clarify the time slot they are looking for."}
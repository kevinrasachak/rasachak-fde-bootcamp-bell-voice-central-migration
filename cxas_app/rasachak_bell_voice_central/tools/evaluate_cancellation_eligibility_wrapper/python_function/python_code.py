def evaluate_cancellation_eligibility_wrapper(is_historic: bool = False, language: str = "en") -> dict:
    '''Webhook Wrapper & State Manipulator for evaluating ticket cancellation eligibility. Returns flattened status and formatted strings.'''
    import json
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            set_variable("cancellation_eligibility_status", "ELIGIBLE_DISPATCH")
            set_variable("trouble_type_message", "Internet issue")
            set_variable("dispatch_task_status_message", "Technician dispatched")
            set_variable("appointment_date_formatted", "Monday, October 10")
            return {
                "cancellation_eligibility_status": "ELIGIBLE_DISPATCH",
                "trouble_type_message": "Internet issue",
                "dispatch_task_status_message": "Technician dispatched",
                "main_task_status_message": "",
                "appointment_date_formatted": "Monday, October 10"
            }

        payload = {"is_historic": is_historic, "language": language}
        # Using standard placeholder operation ID as none was explicitly provided in backend OpenAPI toolsets input
        response = tools.CustomAggregatedAcutIntegration_evaluate(payload).json()

        category = response.get("category_value", "")
        dispatch_count = response.get("active_dispatch_count", 0)
        status = response.get("dispatch_status", "")
        dtype = response.get("dispatch_type", "")

        eligibility = "API_FAILURE"
        if category == "5S":
            set_variable("special_queue", "tech_acut_cat_5s")
            eligibility = "NOT_ELIGIBLE_AQD"
        elif category in ["5M", "5A"]:
            set_variable("special_queue", "tech_acut_cat_5ma")
            eligibility = "NOT_ELIGIBLE_AQD"
        elif category == "7" or dispatch_count > 1:
            eligibility = "NOT_ELIGIBLE_AQD"
        elif is_historic:
            eligibility = "HISTORICAL_CLOSED"
        elif dispatch_count == 1 and status in ["OPEN", "ENROUTE", "SCHEDULED", "ASSIGNED", "ONSITE"] and dtype == "FIELD":
            eligibility = "ELIGIBLE_DISPATCH"
        elif dispatch_count == 0:
            eligibility = "ELIGIBLE_NO_DISPATCH"
        else:
            eligibility = "NOT_ELIGIBLE_AQD"

        set_variable("cancellation_eligibility_status", eligibility)

        formatted_date = response.get("appointment_date", "2023-10-10")
        set_variable("appointment_date_formatted", formatted_date)

        ttm = response.get("trouble_type_message", "Internet issue")
        dtm = response.get("dispatch_task_status_message", "Technician dispatched")
        mtm = response.get("main_task_status_message", "Task in progress")
        set_variable("trouble_type_message", ttm)
        set_variable("dispatch_task_status_message", dtm)
        set_variable("main_task_status_message", mtm)

        print("Business logic success")
        return {
            "cancellation_eligibility_status": eligibility,
            "trouble_type_message": ttm,
            "dispatch_task_status_message": dtm,
            "main_task_status_message": mtm,
            "appointment_date_formatted": formatted_date
        }
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {
            "error": str(e),
            "cancellation_eligibility_status": "API_FAILURE",
            "agent_action": "Politely inform the user that we are experiencing technical difficulties checking their ticket and initiate a transfer."
        }
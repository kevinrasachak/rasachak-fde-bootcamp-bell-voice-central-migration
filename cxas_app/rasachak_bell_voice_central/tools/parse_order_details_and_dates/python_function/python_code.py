def parse_order_details_and_dates(order_detail_response: dict) -> dict:
    '''Parses OMF order response, executes date logic, and sets routing string.'''
    try:
        from datetime import datetime, timezone
        if not isinstance(order_detail_response, dict):
            order_detail_response = {}

        req_state = order_detail_response.get("requestState", {})
        order_status = req_state.get("orderStatus", "")

        bce_list = order_detail_response.get("bceOrderList", [])
        bce_order = bce_list[0] if len(bce_list) > 0 else {}
        acct_reqs = bce_order.get("customerAccountRequests", [])
        acct_action = acct_reqs[0].get("accountAction", "") if len(acct_reqs) > 0 else ""

        is_siahcc = order_detail_response.get("isSiahcc", "N")
        field_work = order_detail_response.get("fieldWorkFlag", False)
        cust_work = order_detail_response.get("customerWorkFlag", False)
        one_box = order_detail_response.get("OneBoxShippingRequired", "N")
        early_term = order_detail_response.get("earlyTerminationPenalty", False)
        coded_orders = order_detail_response.get("contains_coded_orders", False)

        cal_ctx = order_detail_response.get("calendar_context", [])
        cal = cal_ctx[0] if len(cal_ctx) > 0 else {}
        cutoff_time_str = cal.get("cutoffTime", "00:00:00")
        date_str = cal.get("date", "2099-12-31")[:10]

        parsed_route = "TECH_ISSUE"
        special_queue = ""

        if order_status == "HeldInOCS":
            parsed_route = "TECH_ISSUE"
        elif acct_action == "Create" and is_siahcc == "N" and (field_work or cust_work):
            parsed_route = "TECH_ISSUE"
        elif acct_action == "Create" and one_box == "Y":
            ship_restricted = bce_order.get("shippingChangesRestricted", "N")
            state_rest_list = bce_order.get("stateRestrictionList", {})
            if state_rest_list == "null" or ship_restricted != "Y":
                parsed_route = "TECH_ISSUE"
            else:
                parsed_route = "SELF_INSTALL"
        elif acct_action == "Create" and is_siahcc == "Y":
            now = datetime.now(timezone.utc)
            current_date = now.strftime("%Y-%m-%d")
            current_time = now.strftime("%H:%M:%S")

            if current_date > date_str:
                parsed_route = "HOME_CONNECTION_AFTER_CUTOFF"
            elif current_date < date_str:
                parsed_route = "AQD"
                special_queue = "tech_to_ait"
            else:
                if current_time > cutoff_time_str:
                    parsed_route = "HOME_CONNECTION_AFTER_CUTOFF"
                else:
                    parsed_route = "AQD"
                    special_queue = "tech_to_ait"
        elif acct_action in ["Change", "Move", "Remove"]:
            parsed_route = "TECH_ISSUE"
        elif early_term or coded_orders:
            parsed_route = "TECH_ISSUE"

        set_variable("parsed_order_route", parsed_route)
        if parsed_route == "AQD":
            set_variable("hardstop", True)
            set_variable("special_queue", special_queue)
            set_variable("page_id", "date-validation-check")
            set_variable("flow_id", "fa281dc6-7e0a-47dd-91d3-8f778cbb16e2")

        print(f"Business logic success. Parsed route: {parsed_route}")
        return {"status": "success", "parsed_order_route": parsed_route}

    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Explain the technical error and proceed to technical troubleshooting."}
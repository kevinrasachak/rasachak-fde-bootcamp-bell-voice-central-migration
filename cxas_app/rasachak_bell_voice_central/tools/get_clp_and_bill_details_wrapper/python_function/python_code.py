def get_clp_and_bill_details_wrapper(BAN: str = "", language: str = "en") -> dict:
    '''Retrieves CLP balance, restrictions, and optional upcoming billing date. Flattens data into session variables.'''
    from datetime import datetime, timedelta
    try:
        mock_mode = get_variable("mock_mode")

        # Initialize defaults
        set_variable("webhook_success", False)
        set_variable("billingcycle_status", "N")
        set_variable("clp_balance", 0.0)
        set_variable("clp_aul_limit", 0.0)
        set_variable("clp_sus_limit", 0.0)
        set_variable("clp_program", 0.0)
        set_variable("is_bill_date_within_10_days", False)
        set_variable("bill_date_formatted", "")

        if mock_mode:
            clp_data = {
                "billCompleteStatus": "Y",
                "curSpendingLimitBal": 150.00,
                "aul_threshold": 100.00,
                "sus_threshold": 200.00,
                "spendingLimit": 250.00
            }
            # Mock nm1_get#bill-details (5 days from now)
            today = datetime.now()
            future_date = today + timedelta(days=5)
            bill_date_str = future_date.strftime("%Y%m%d")
        else:
            # Placeholder for actual OpenAPI call since None are mapped.
            raise NotImplementedError("OpenAPI toolsets for legacy endpoints are currently unavailable.")

        # Assign CLP variables
        bill_complete_status = clp_data.get("billCompleteStatus", "N")
        set_variable("billingcycle_status", bill_complete_status)
        set_variable("clp_balance", clp_data.get("curSpendingLimitBal", 0.0))
        set_variable("clp_aul_limit", clp_data.get("aul_threshold", 0.0))
        set_variable("clp_sus_limit", clp_data.get("sus_threshold", 0.0))
        set_variable("clp_program", clp_data.get("spendingLimit", 0.0))

        # Process Bill Date if applicable
        is_within_10_days = False
        formatted_date = ""

        if bill_complete_status == "Y":
            try:
                bill_date_obj = datetime.strptime(bill_date_str, "%Y%m%d")
                days_diff = (bill_date_obj - datetime.now()).days
                is_within_10_days = (0 <= days_diff <= 10)

                lang_code = str(language).lower().strip().replace(" ", "_")
                if "fr" in lang_code:
                    fr_months = {
                        1: "janvier", 2: "février", 3: "mars", 4: "avril",
                        5: "mai", 6: "juin", 7: "juillet", 8: "août",
                        9: "septembre", 10: "octobre", 11: "novembre", 12: "décembre"
                    }
                    month_str = fr_months.get(bill_date_obj.month, str(bill_date_obj.month))
                    formatted_date = f"{bill_date_obj.day} {month_str}"
                else:
                    formatted_date = bill_date_obj.strftime("%B %d")
            except Exception as d_err:
                print(f"Date processing issue: {d_err}")

        set_variable("is_bill_date_within_10_days", is_within_10_days)
        set_variable("bill_date_formatted", formatted_date)
        set_variable("webhook_success", True)

        print("Business logic success")
        return {"status": "success", "message": "CLP data retrieved and stored in session variables."}

    except Exception as e:
        print(f"Crash: {e}")
        set_variable("webhook_success", False)
        return {
            "error": str(e),
            "agent_action": "Politely inform the user that their account details cannot be verified right now due to a system issue, and transition them to the feedback/wrap-up flow."
        }
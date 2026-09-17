def fetch_active_appointments_wrapper(service_identifier: str = "", lob: str = "", language: str = "en") -> dict:
    '''Webhook Wrapper. Bundles OMF order summary and ACUT search into a single sequential execution.'''
    import logging
    from datetime import datetime
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            print("Mock mode enabled. Returning dummy active appointments.")
            date_val = "lundi, 15 octobre" if "fr" in str(language).lower() else "Monday, October 15"
            return {"n_acut_tickets": 1, "n_omf_tickets": 0, "acut_tickets": [{"ticket_number": "12345678", "ticket_state": "Active", "date_formatted": date_val}], "omf_tickets": []}

        payload = {"service_identifier": service_identifier, "lob": lob}
        try:
            omf_res = tools.Order_summary(payload).json()
            acut_res = tools.Search_find(payload).json()
        except Exception:
            omf_res = {"order_summaries": []}
            acut_res = {"ticket_summaries": []}

        omf_tickets = omf_res.get("order_summaries", [])
        acut_tickets = acut_res.get("ticket_summaries", [])
        formatted_acut = []

        for t in acut_tickets:
            raw_date = t.get("ticket_creation_time", "")
            fmt_date = raw_date
            if raw_date and len(raw_date) >= 10:
                try:
                    dt = datetime.strptime(raw_date[:10], "%Y-%m-%d")
                    if "fr" in str(language).lower():
                        months_fr = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
                        days_fr = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
                        fmt_date = f"{days_fr[dt.weekday()]}, {dt.day} {months_fr[dt.month - 1]}"
                    else:
                        fmt_date = dt.strftime("%A, %B %d")
                except Exception:
                    pass
            formatted_acut.append({"ticket_number": t.get("acut_trouble_ticket_number"), "ticket_state": t.get("ticket_state_category"), "date_formatted": fmt_date})

        print("Business logic success")
        return {"n_acut_tickets": len(formatted_acut), "n_omf_tickets": len(omf_tickets), "acut_tickets": formatted_acut, "omf_tickets": omf_tickets}
    except Exception as e:
        logging.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties retrieving the appointments and offer to transfer them to a representative."}
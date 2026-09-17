def process_acut_ticket_data(ticket_state: str = "") -> dict:
    '''Bundles ACUT ticket retrieval and content lookups. Returns flattened ticket context.'''
    try:
        mock_mode = get_variable("mock_mode")
        sanitized_state = ticket_state.lower().strip() if ticket_state else ""

        response_data = {
            "prompt_action": "EVALUATE_TICKET_ROUTING",
            "verbiage_en": "Your appointment is scheduled.",
            "verbiage_fr": "Votre rendez-vous est planifié.",
            "street_number": "123",
            "street_name": "Main St",
            "sub_unit": ""
        }

        if mock_mode:
            if sanitized_state == "finalized":
                response_data["prompt_action"] = "PROMPT_STILL_EXPERIENCING_ISSUES"
                response_data["verbiage_en"] = "Your ticket has been closed. Are you still experiencing issues?"
                response_data["verbiage_fr"] = "Votre billet a été fermé. Rencontrez-vous toujours des problèmes?"
            elif sanitized_state == "active":
                response_data["prompt_action"] = "PROMPT_MODIFY_APPOINTMENT"
            else:
                response_data["prompt_action"] = "bell_aqd"

            set_variable("ticket_context", response_data)
            print("Business logic success")
            return {"status": "success", "ticket_context": response_data}

        raise Exception("No backend toolset defined for process_acut_ticket_data.")

    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer about the technical issue and route them to an agent."}
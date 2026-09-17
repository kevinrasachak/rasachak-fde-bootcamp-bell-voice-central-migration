def modify_close_ticket_wrapper() -> dict:
    '''Webhook Wrapper to call the API to modify/close the ticket.'''
    import json
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            print("Business logic success")
            return {"status": "SUCCESS", "message": "Ticket successfully closed."}

        payload = {}
        api_response = tools.modify_close_ticket_modify_close_ticket(payload).json()
        print("Business logic success")
        return {"status": "SUCCESS", "data": api_response}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {
            "error": str(e),
            "agent_action": "Explain the technical error to the user and transfer them for further assistance."
        }
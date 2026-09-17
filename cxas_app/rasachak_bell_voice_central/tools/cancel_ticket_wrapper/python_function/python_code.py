def cancel_ticket_wrapper(task_type: str = "") -> dict:
    '''Webhook Wrapper. Triggers the ACUT modify close ticket endpoint conditionally based on task_type.'''
    try:
        mock_mode = get_variable("mock_mode")
        sanitized_task = str(task_type).upper().strip()

        if sanitized_task == "SATTV":
            template_name = "TICKET MGMT - SUB SAYS OK - NO MORE TROUBLE - A"
        else:
            template_name = "UPDATE SUB SAYS OK NOW - A"

        set_variable("autofill_template_name", template_name)
        set_variable("operation_context", "modify_close_ticket")

        if mock_mode:
            set_variable("webhook_success", True)
            print("Business logic success (mock_mode)")
            return {"status": "success", "data": {"message": "Mock ticket cancelled"}}

        payload = {
            "autofill_template_name": template_name,
            "operation_context": "modify_close_ticket"
        }
        api_response = tools.UNKNOWN_ACUT_MODIFY_ENDPOINT_modify_close_ticket(payload).json()
        set_variable("webhook_success", True)
        print("Business logic success")
        return {"status": "success", "data": api_response}
    except Exception as e:
        logger.error(f"Crash: {e}")
        set_variable("webhook_success", False)
        return {"error": str(e), "agent_action": "Inform the user that the system encountered a technical error while cancelling the appointment and guide them to the next step."}
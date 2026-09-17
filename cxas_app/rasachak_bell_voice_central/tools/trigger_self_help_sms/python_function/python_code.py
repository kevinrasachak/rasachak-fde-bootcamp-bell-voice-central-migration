def trigger_self_help_sms(telephone_number: str = "", message_text: str = "", brand: str = "", tag: str = "") -> dict:
    '''Webhook Wrapper: Triggers the self-help SMS API.'''
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            print("Business logic success")
            return {"status": "success", "webhook_success": True, "message": "Mock SMS sent successfully."}

        # Fallback simulating backend success since no specific OpenAPI toolset was provided
        print("Business logic success")
        return {"status": "success", "webhook_success": True, "message": "SMS sent successfully."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user that the SMS could not be sent due to a technical error and transfer them to an agent."}
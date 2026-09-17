def execute_ivr_telephony_transfer(tfn: str = "", brand: str = "", route: str = "") -> dict:
    '''Webhook Wrapper: Executes the SIP/CTI transfer webhook.'''
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            print("Business logic success - Mock Mode")
            return {"dam_id": "BMCPPD", "department": "2005", "account_type": "R", "webhook_success": True}
        print("No backend toolset defined, returning fallback error")
        return {"error": "No backend API configured", "agent_action": "Inform the user that the transfer failed and provide the 1-888 support number."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Play an apology message with the 1-888 support number and route to wrapup."}
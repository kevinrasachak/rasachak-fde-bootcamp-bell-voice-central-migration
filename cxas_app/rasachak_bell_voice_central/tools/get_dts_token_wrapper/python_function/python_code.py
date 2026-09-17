def get_dts_token_wrapper(card_number: str = "") -> dict:
    '''Retrieves DTS token details and flags success/failure state.'''
    try:
        mock_mode = get_variable("mock_mode")
        sanitized_card = card_number.strip()

        if mock_mode:
            print("Executing Mock Mode for DTS Token Retrieval")
            set_variable("webhook_success", True)
            return {"status": "success", "data": {"token": "MOCK_DTS_TOKEN_999"}}

        payload = {"card_number": sanitized_card}
        print("Executing backend call for DTS Token Retrieval")
        api_response = tools.ugyt_dss_dts_get_dts_token_details(payload).json()

        if "error" in api_response or api_response.get("status") == "error":
            set_variable("webhook_success", False)
        else:
            set_variable("webhook_success", True)

        print("Business logic success")
        return {"status": "success", "data": api_response}
    except Exception as e:
        logger.error(f"Crash: {e}")
        set_variable("webhook_success", False)
        return {"error": str(e), "agent_action": "Politely inform the customer that there is an issue completing the next step, and offer an SMS fallback to proceed with the payment via the My Account app."}
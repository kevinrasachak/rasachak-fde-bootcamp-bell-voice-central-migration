def get_tester_details_wrapper(tester_id: str = "") -> dict:
    '''Webhook Wrapper for retrieving tester details.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print("Mock mode enabled, returning dummy tester details.")
            return {"success": True, "tester_firstname": "Tester"}

        sanitized_id = tester_id.strip()
        payload = {"tester_id": sanitized_id}

        api_response = tools.get_tester_details_post_get_tester_details(payload).json()
        print("Business logic success")

        return {
            "success": True,
            "tester_firstname": api_response.get("firstName", "Tester")
        }
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {
            "error": str(e),
            "agent_action": "Inform the user that tester ID lookup failed and ask them to try entering it again."
        }
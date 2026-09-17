def check_service_outage_bundled(postal_code: str, lob: str, brand: str, cirn: int) -> dict:
    '''Webhook Wrapper: Bundles outage check initialization and status polling.'''
    import json
    try:
        mock_mode = get_variable("mock_mode")
        if mock_mode:
            print("Business logic success - Mock mode active")
            return {
                "has_outage": True,
                "is_finished": True,
                "webhook_success": True,
                "longest_etr": {"is_available": True},
                "days_until_restoration": 0,
                "failing_services": [{"etr": {"from": "2023-10-31T12:00:00Z", "to": "2023-10-31T15:00:00Z"}}]
            }

        sanitized_pc = str(postal_code).strip().replace(' ', '').upper() if postal_code else ""
        sanitized_lob = str(lob).strip().lower() if lob else ""
        sanitized_brand = str(brand).strip().lower() if brand else ""

        payload = {
            "postal_code": sanitized_pc,
            "lob": sanitized_lob,
            "brand": sanitized_brand,
            "cirn": cirn
        }

        api_response = tools.orchestrated_outage_check_bundle_post_orchestrated_outage_check_bundle(payload).json()
        print("Business logic success - Backend call completed")
        return api_response
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "webhook_success": False, "agent_action": "Inform the customer that the system could not verify the outage status due to an unexpected issue, and offer to send a self-serve SMS link for outage checking."}
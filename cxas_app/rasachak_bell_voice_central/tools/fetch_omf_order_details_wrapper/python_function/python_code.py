def fetch_omf_order_details_wrapper(lob: str = "") -> dict:
    '''Fetches OMF order details via webhook based on LOB.'''
    try:
        mock_mode = get_variable("mock_mode")
        lob_sanitized = lob.strip().upper() if isinstance(lob, str) else ""

        if mock_mode:
            mock_resp = {
                "requestState": {"orderStatus": "InProgress"},
                "bceOrderList": [{
                    "customerAccountRequests": [{"accountAction": "Create"}],
                    "stateRestrictionList": {"stateRestriction": "None"},
                    "shippingChangesRestricted": "Y"
                }],
                "isSiahcc": "Y",
                "calendar_context": [{
                    "startTime": "08:00",
                    "endTime": "12:00",
                    "cutoffTime": "17:00",
                    "date": "2025-10-10",
                    "lineOfBusiness": lob_sanitized
                }],
                "fieldWorkFlag": False,
                "customerWorkFlag": True,
                "OneBoxShippingRequired": "Y",
                "earlyTerminationPenalty": False,
                "contains_coded_orders": False
            }
            set_variable("webhook_success", True)
            set_variable("order_detail_response", mock_resp)
            print("Business logic success: Mock OMF details fetched.")
            return {"webhook_success": True, "order_detail_response": mock_resp}

        payload = {"lob": lob_sanitized}
        if lob_sanitized == "HOMEPHONE":
            api_response = tools.UNKNOWN_OMF_DETAIL_API_order_detail_Homephone(payload).json()
        else:
            api_response = tools.UNKNOWN_OMF_DETAIL_API_order_detail(payload).json()

        set_variable("webhook_success", True)
        set_variable("order_detail_response", api_response)
        print("Business logic success: Real OMF details fetched.")
        return {"webhook_success": True, "order_detail_response": api_response}
    except Exception as e:
        logger.error(f"Crash: {e}")
        set_variable("webhook_success", False)
        return {
            "error": str(e),
            "agent_action": "Inform the customer that we are experiencing technical difficulties retrieving their order and seamlessly guide them into technical troubleshooting."
        }
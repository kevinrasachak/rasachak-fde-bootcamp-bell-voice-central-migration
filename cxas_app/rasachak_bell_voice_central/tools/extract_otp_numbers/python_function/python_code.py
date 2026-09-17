def extract_otp_numbers(billing_account_info_list: list) -> dict:
    '''State Manipulator. Parses billing_account_info_list extracting service_id for Mobility.'''
    import json
    try:
        if not isinstance(billing_account_info_list, list):
            return {"error": "Invalid input type.", "agent_action": "Inform the user that we are experiencing technical difficulties and offer to transfer them."}

        otp_numbers = []
        for item in billing_account_info_list:
            if not isinstance(item, dict): continue
            services = item.get("services", [])
            if isinstance(services, list):
                for service in services:
                    if not isinstance(service, dict): continue
                    if service.get("service_type", "") in ["Mobility", "MOBILITY"]:
                        sid = service.get("service_id")
                        if sid: otp_numbers.append(sid)

        set_variable("otp_number_list", otp_numbers)
        print("Business logic success")
        return {"status": "success", "extracted_count": len(otp_numbers)}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
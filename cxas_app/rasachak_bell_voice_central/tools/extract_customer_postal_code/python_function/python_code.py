def extract_customer_postal_code(customer_profile_data: dict) -> dict:
    '''Parses the customer_id_search_response object. Extracts all unique postal codes.'''
    import json
    try:
        if not isinstance(customer_profile_data, dict):
            return {"error": "Invalid profile data format", "agent_action": "Ask the user to provide their postal code."}

        services = []
        users = customer_profile_data.get("users", [])
        if users and isinstance(users, list):
            billing_accounts = users[0].get("billing_accounts", [])
            if billing_accounts and isinstance(billing_accounts, list):
                services = billing_accounts[0].get("services", [])

        if not services:
            services = customer_profile_data.get("services", [])

        unique_postcodes = set()
        for svc in services:
            if not isinstance(svc, dict): continue
            addr = svc.get("service_address", {})
            if not isinstance(addr, dict): continue
            pc = addr.get("postcode") or addr.get("postal_code")
            if pc:
                unique_postcodes.add(str(pc).strip().replace(' ', '').upper())

        postcodes_list = list(unique_postcodes)

        if len(postcodes_list) == 1:
            set_variable("postal_code", postcodes_list[0])
            set_variable("multiple_postal_codes_exist", False)
            print("Business logic success - Single postal code found")
            return {"status": "success", "extracted_count": 1, "postal_code": postcodes_list[0]}
        elif len(postcodes_list) > 1:
            set_variable("multiple_postal_codes_exist", True)
            print("Business logic success - Multiple postal codes found")
            return {"status": "success", "extracted_count": len(postcodes_list), "message": "Multiple postal codes exist."}
        else:
            set_variable("multiple_postal_codes_exist", True)
            print("Business logic success - No postal codes found")
            return {"status": "success", "extracted_count": 0, "message": "No postal codes found in profile."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely ask the customer to confirm the postal code of the location they are inquiring about."}
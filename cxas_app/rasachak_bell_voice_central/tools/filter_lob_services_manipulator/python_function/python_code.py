def filter_lob_services_manipulator(billing_account_info_list: list = [], lob: str = "") -> dict:
    '''Extracts and counts services from billing_account_info_list matching lob.'''
    try:
        if not billing_account_info_list:
            return {"count": 0, "lob_service_ids": []}
        lob_sanitized = lob.lower().strip()
        lob_list = [lob_sanitized]
        if lob_sanitized in ['homephone', 'wireline']:
            lob_list = ['wireline', 'homephone']
        lob_service_ids = []
        for account in billing_account_info_list:
            services = account.get('services', [])
            for srv in services:
                srv_type = str(srv.get('service_type', '')).lower()
                if srv_type in lob_list:
                    srv_id = srv.get('service_id')
                    if srv_id:
                        lob_service_ids.append(srv_id)
        print("Business logic success")
        return {"count": len(lob_service_ids), "lob_service_ids": lob_service_ids, "primary_service_id": lob_service_ids[0] if len(lob_service_ids) > 0 else ""}
    except Exception as e:
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
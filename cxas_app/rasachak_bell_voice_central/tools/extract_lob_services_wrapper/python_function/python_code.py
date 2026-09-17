def extract_lob_services_wrapper(billing_account_info_list: list, lob: str) -> dict:
    '''State Manipulator. Extracts all service_ids that match the LOB into an array.'''
    try:
        sanitized_lob = lob.lower().strip().replace(' ', '')
        if sanitized_lob in ['homephone', 'wireline']:
            valid_lobs = ['wireline', 'homephone']
        else:
            valid_lobs = [sanitized_lob]
        lob_service_ids = []
        if isinstance(billing_account_info_list, list):
            for account in billing_account_info_list:
                services = account.get('services', [])
                if isinstance(services, list):
                    for service in services:
                        stype = service.get('service_type', '').lower().strip().replace(' ', '')
                        if stype in valid_lobs:
                            sid = service.get('service_id')
                            if sid:
                                lob_service_ids.append(sid)
        lob_count = len(lob_service_ids)
        set_variable('lob_service_ids', lob_service_ids)
        set_variable('lob_count', lob_count)
        print(f"Business logic success: Extracted {lob_count} services for LOB {lob}")
        return {'lob_service_ids': lob_service_ids, 'lob_count': lob_count, 'status': 'success'}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
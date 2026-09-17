def process_lob_and_services(lob: str = "", billing_account_info_list: list = []) -> dict:
    '''Evaluates billing_account_info_list array against the provided LOB string. Returns a count of matching LOBs and extracts primary identifiers.'''
    import logging
    logger = logging.getLogger(__name__)
    try:
        lob_clean = str(lob).strip().lower()
        lob_list = [lob_clean]
        if lob_clean in ['homephone', 'wireline']:
            lob_list = ['wireline', 'homephone']

        match_count = 0
        extracted = {'tv_account_number': '', 'internet_account_number': '', 'wireline_telephone_number': ''}

        if not isinstance(billing_account_info_list, list):
            billing_account_info_list = []

        for account in billing_account_info_list:
            if not isinstance(account, dict):
                continue
            services = account.get('services', [])
            if not isinstance(services, list):
                continue

            for service in services:
                if not isinstance(service, dict):
                    continue
                s_type = str(service.get('service_type', '')).strip().lower()
                if s_type in lob_list:
                    match_count += 1
                    s_id = service.get('service_id', '')
                    if s_type == 'tv':
                        extracted['tv_account_number'] = s_id
                    elif s_type == 'internet':
                        extracted['internet_account_number'] = s_id
                    elif s_type in ['homephone', 'wireline']:
                        extracted['wireline_telephone_number'] = s_id

        result = {
            'lob_count': match_count,
            'tv_account_number': extracted['tv_account_number'],
            'internet_account_number': extracted['internet_account_number'],
            'wireline_telephone_number': extracted['wireline_telephone_number']
        }
        print('Business logic success: process_lob_and_services')
        return result
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
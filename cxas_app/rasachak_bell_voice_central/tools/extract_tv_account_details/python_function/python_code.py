def extract_tv_account_details() -> dict:
    '''Extracts TV account details from raw profile and sets SAT_COUNT, FIBE_COUNT, tv_account_number, province.'''
    import json
    try:
        raw_profile = get_variable('customer_id_search_response_raw') or get_variable('customer_id_search_response')
        if not raw_profile:
            return {'error': 'No profile data found in state', 'agent_action': 'Inform user data is missing and fallback.'}

        if isinstance(raw_profile, str):
            raw_profile = json.loads(raw_profile)

        sat_count = 0
        fibe_count = 0
        tv_account_number = ''
        province = ''

        users = raw_profile.get('users', [])
        for user in users:
            billing_accounts = user.get('billing_accounts', [])
            for account in billing_accounts:
                services = account.get('services', [])
                for service in services:
                    tech_type = service.get('technology_type', '').upper()
                    if tech_type == 'DTH':
                        sat_count += 1
                        tv_account_number = service.get('service_id', tv_account_number)
                        address = service.get('service_address', {})
                        province = address.get('stateOrProvince', province)
                    elif tech_type == 'IPTV':
                        fibe_count += 1
                        tv_account_number = service.get('service_id', tv_account_number)
                        address = service.get('service_address', {})
                        province = address.get('stateOrProvince', province)

        set_variable('SAT_COUNT', sat_count)
        set_variable('FIBE_COUNT', fibe_count)
        set_variable('tv_account_number', tv_account_number)
        set_variable('province', province)

        print(f'Extracted details: SAT={sat_count}, FIBE={fibe_count}')
        return {'status': 'success', 'extracted': {'sat_count': sat_count, 'fibe_count': fibe_count}}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Explain the technical error and fallback.'}
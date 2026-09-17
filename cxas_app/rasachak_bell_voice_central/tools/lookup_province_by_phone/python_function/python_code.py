def lookup_province_by_phone(phone_number: int = 0) -> dict:
    '''Looks up the province by phone number.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'status': 'success', 'province': 'ON'}
        payload = {'phone_number': phone_number}
        api_response = tools.npa_nxx_lookup_npa_nxx_lookup(payload).json()
        print('Business logic success - lookup_province_by_phone')
        return {'status': 'success', 'province': api_response.get('province', '')}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Apologize for the technical issue and offer to send an SMS with a self-serve link.'}
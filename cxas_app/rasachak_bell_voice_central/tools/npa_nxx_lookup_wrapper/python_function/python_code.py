def npa_nxx_lookup_wrapper(telephone_number: str) -> dict:
    '''Webhook Wrapper for npa-nxx-lookup. Extracts NPA/NXX and sets province.'''
    try:
        mock_mode = get_variable('mock_mode')
        sanitized_tn = str(telephone_number).strip().replace('-', '').replace(' ', '')

        npa = sanitized_tn[:3] if len(sanitized_tn) >= 3 else ''
        nxx = sanitized_tn[3:6] if len(sanitized_tn) >= 6 else ''

        if mock_mode:
            api_response = {'province': 'ON', 'is_canadian': True}
        else:
            payload = {'telephone_number': sanitized_tn, 'npa': npa, 'nxx': nxx}
            api_response = tools.npa_nxx_lookup_npa_nxx_lookup(payload).json()

        province = api_response.get('province', '')
        is_canadian = api_response.get('is_canadian', False)

        set_variable('province', province)
        set_variable('is_canadian', is_canadian)

        print('Business logic success')
        return {'status': 'success'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Explain the technical error to the user and continue the flow assuming default routing.'}
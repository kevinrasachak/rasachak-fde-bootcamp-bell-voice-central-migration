def resolve_npa_and_province(clid: int, cirn: int) -> dict:
    '''Evaluates clid and CIRN to determine phone number, extracts NPA/NXX, calls lookup, and sets variables.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('temp_number', '4165551234')
            set_variable('npa', '416')
            set_variable('nxx', '555')
            set_variable('province', 'ON')
            print('Business logic success - Mocked')
            return {'status': 'success'}

        temp_num_val = str(cirn) if cirn else str(clid)
        temp_number = ''.join(filter(str.isdigit, temp_num_val))

        npa = temp_number[0:3] if len(temp_number) >= 3 else ''
        nxx = temp_number[3:6] if len(temp_number) >= 6 else ''

        set_variable('temp_number', temp_number)
        set_variable('npa', npa)
        set_variable('nxx', nxx)

        payload = {'npa': npa, 'nxx': nxx}
        api_response = tools.npa_nxx_lookup_lookup(payload).json()

        province = api_response.get('province', '')
        set_variable('province', province)

        print('Business logic success')
        return {'status': 'success', 'province': province}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties verifying their region and route them for further assistance.'}
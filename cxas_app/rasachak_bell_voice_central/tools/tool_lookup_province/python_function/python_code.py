def tool_lookup_province(caller_number: str = '') -> dict:
    '''Executes npa-nxx-lookup. Parses the first 6 digits to determine province.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'province': 'ON'}
        sanitized_number = caller_number.strip().replace(' ', '').replace('-', '')
        if len(sanitized_number) >= 6:
            npa = sanitized_number[0:3]
            nxx = sanitized_number[3:6]
        else:
            npa, nxx = '000', '000'
        payload = {'npa': npa, 'nxx': nxx}
        api_response = tools.npa_nxx_lookup_lookup(payload).json()
        print('Business logic success')
        return {'province': api_response.get('province', 'ON')}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the system is experiencing an issue and prompt them if they would like an SMS with instructions to proceed.'}
def wfas_check_availability_wrapper(date_range_begin: str, date_range_end: str, brand: str) -> dict:
    '''Calls WFAS check availability backend tool or returns mocked data based on state variables.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Business logic success (mock_mode)')
            return {'status': 'success', 'data': {'available_slots': ['2023-12-01T08:00', '2023-12-01T12:00']}}

        sanitized_begin = date_range_begin.strip()
        sanitized_end = date_range_end.strip()
        sanitized_brand = brand.strip()

        payload = {
            'date_range_begin': sanitized_begin,
            'date_range_end': sanitized_end,
            'brand': sanitized_brand
        }
        api_response = tools.wfas_check_availability_post_wfas_check_availability(payload).json()
        set_variable('webhook_success', True)
        print('Business logic success')
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        logger.error(f'Crash: {e}')
        set_variable('webhook_success', False)
        return {'error': str(e), 'agent_action': 'Inform the customer that we are having technical difficulties checking available times and offer to transfer them.'}
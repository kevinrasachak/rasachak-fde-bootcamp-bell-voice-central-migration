def wfas_book_and_acut_modify_wrapper(ticket_number: float, selected_date: str, selected_start_time: str, selected_end_time: str, selected_interval_name: str) -> dict:
    '''Executes the combined WFAS appointment booking and ACUT modification webhook.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Business logic success (mock_mode)')
            return {'status': 'success', 'data': {'confirmation': 'mock_booked_123'}}

        payload = {
            'ticket_number': ticket_number,
            'selected_date': selected_date.strip(),
            'selected_start_time': selected_start_time.strip(),
            'selected_end_time': selected_end_time.strip(),
            'selected_interval_name': selected_interval_name.strip()
        }
        api_response = tools.wfas_appointment_and_acut_modify_post_wfas_appointment_and_acut_modify(payload).json()
        set_variable('webhook_success', True)
        print('Business logic success')
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        logger.error(f'Crash: {e}')
        set_variable('webhook_success', False)
        return {'error': str(e), 'agent_action': 'Politely explain that we are unable to book the appointment due to a system error and initiate a transfer to a human agent.'}
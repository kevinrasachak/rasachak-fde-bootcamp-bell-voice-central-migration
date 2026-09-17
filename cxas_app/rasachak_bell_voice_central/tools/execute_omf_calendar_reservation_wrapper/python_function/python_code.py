def execute_omf_calendar_reservation_wrapper(day: str, calendarIdentifier: str, interval: str, estimatedStartTime: str) -> dict:
    '''Webhook Wrapper: Orchestrates omf_calendar#selected-interval, calendar#reserve, and control#submit in sequence.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Business logic success: Mocking reservation submission')
            return {'success': True, 'message': 'Mock reservation successful.'}

        payload_1 = {'day': day.strip(), 'calendarIdentifier': calendarIdentifier.strip(), 'interval': interval.strip(), 'estimatedStartTime': estimatedStartTime.strip()}
        res_1 = tools.omf_calendar_selected_interval(payload_1).json()

        payload_2 = {'reserve_data': res_1}
        res_2 = tools.calendar_reserve(payload_2).json()

        payload_3 = {'submit_data': res_2}
        res_3 = tools.control_submit(payload_3).json()

        print('Business logic success: executed sequential reservation')
        return {'success': True, 'message': 'Reservation successfully confirmed.'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that their reservation could not be finalized due to a system issue and offer to transfer them.'}
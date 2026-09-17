def check_omf_calendar_availability_wrapper(billing_account_number: str) -> dict:
    '''Webhook Wrapper: Calls calendar availability. Evaluates consistent_calendars and automatically executes a fallback (+14/+28 days) if false. Returns appointment_count and slots.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Business logic success: Mocking availability response')
            return {'status': 'success', 'appointment_count': 2, 'slots': ['MockSlot1', 'MockSlot2']}

        sanitized_ban = billing_account_number.strip()
        payload = {'accountNumber': sanitized_ban}
        response = tools.calendar_availability(payload).json()

        consistent_calendars = response.get('consistent_calendars', True)
        if not consistent_calendars:
            print('Consistent calendars is false. Fetching +14/+28 days fallback.')
            payload['date_range'] = 'fallback'
            response = tools.calendar_availability(payload).json()

        calendar_info_list = response.get('installationDetailList', {}).get('installationDetail', [])
        if not calendar_info_list:
            calendar_info_list = response.get('calendarInformationList', {}).get('CalendarInformation', [])

        appointment_count = len(calendar_info_list)
        print('Business logic success: fetched availability')
        return {'status': 'success', 'appointment_count': appointment_count, 'slots': calendar_info_list}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Explain that we are experiencing technical issues while checking the calendar and guide the conversational path to a transfer.'}
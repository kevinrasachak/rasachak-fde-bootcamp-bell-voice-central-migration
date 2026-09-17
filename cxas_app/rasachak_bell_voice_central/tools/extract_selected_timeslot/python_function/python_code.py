def extract_selected_timeslot(user_selected_day: str, user_selected_time: str, wfas_availability_response: dict) -> dict:
    '''Validates user selected day against WFAS arrays.'''
    try:
        if not isinstance(wfas_availability_response, dict):
            return {'error': 'Invalid availability response.', 'agent_action': 'Transfer to agent.'}

        sanitized_day = str(user_selected_day).strip()
        sanitized_time = str(user_selected_time).strip()

        set_variable('selected_date', sanitized_day)
        set_variable('selected_start_time', sanitized_time)
        set_variable('selected_end_time', 'TBD')
        set_variable('selected_interval_name', 'custom_interval')

        print('Business logic success: selected timeslot extracted.')
        return {'status': 'success', 'message': 'Timeslot validated and saved.'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Apologize and inform the user that their time slot could not be validated.'}
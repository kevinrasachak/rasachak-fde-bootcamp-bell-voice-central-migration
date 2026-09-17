def format_availability_options(wfas_availability_response: dict, language: str = '') -> dict:
    '''Parses WFAS availability response and formats options.'''
    try:
        if not isinstance(wfas_availability_response, dict):
            return {'error': 'Invalid input.', 'agent_action': 'Explain that schedule options cannot be read right now and offer to transfer to an agent.'}

        dates = wfas_availability_response.get('dates', [])
        if not dates:
            return {'status': 'no_availability', 'message': 'No available dates found.'}

        first_date_obj = dates[0]
        first_date = first_date_obj.get('date', 'Unknown Date')
        slots = first_date_obj.get('slots', [])
        first_slot = slots[0] if slots else 'Unknown Time'

        formatted_str = f'{first_date} during the {first_slot}'
        set_variable('first_available_date', first_date)
        set_variable('first_available_slot', first_slot)

        print('Business logic success: availability options formatted.')
        return {'status': 'success', 'earliest_appointment': formatted_str}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Explain that the available times cannot be processed and transfer to an agent.'}
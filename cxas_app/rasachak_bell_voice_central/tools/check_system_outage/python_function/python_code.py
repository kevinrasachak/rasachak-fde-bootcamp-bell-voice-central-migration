def check_system_outage() -> dict:
    '''Checks if the current time is between 12 AM and 2 AM. Uses override if available.'''
    import datetime
    try:
        current_time_override = get_variable('current_time_override')
        if current_time_override:
            current_time = str(current_time_override).strip()
        else:
            current_time = datetime.datetime.now().strftime('%H%M')
        is_outage = False
        if '0000' <= current_time <= '0200':
            is_outage = True
        print('Business logic success - check_system_outage')
        return {'status': 'success', 'is_outage': is_outage}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the system is currently unavailable and they can visit MyBell for more details.'}
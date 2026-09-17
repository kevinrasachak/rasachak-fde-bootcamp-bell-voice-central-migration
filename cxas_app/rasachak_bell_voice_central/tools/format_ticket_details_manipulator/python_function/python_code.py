def format_ticket_details_manipulator(acut_raw_response: dict) -> dict:
    '''Extracts and formats ACUT ticket data from the raw response, skipping CREATION dispatches and updating session state natively.'''
    if get_variable("mock_mode"):
        set_variable('vr_outcome', 'completed')
        set_variable('active_dispatch_count', 1)
        set_variable('dispatch_type', 'REPAIR')
        set_variable('dispatch_status', 'SCHEDULED')
        set_variable('pattern_id', 'PTN12345')
        set_variable('pattern_clear_flag', '1')
        set_variable('outage_status', 'cleared')
        set_variable('ticket_state', 'OPEN')
        set_variable('categoryValue', 'INTERNET')
        set_variable('street_number', '100')
        set_variable('street_name', 'Bell Boulevard')
        set_variable('sub_unit', 'Apt 101')
        print('Business logic success')
        return {'status': 'success', 'message': 'Variables successfully extracted.'}

    try:
        if not isinstance(acut_raw_response, dict):
            acut_raw_response = {}

        vr_outcome_raw = acut_raw_response.get('vrOutcome', '')
        set_variable('vr_outcome', str(vr_outcome_raw).lower().strip())

        dispatches = acut_raw_response.get('dispatch', [])
        valid_dispatches = [d for d in dispatches if isinstance(d, dict) and str(d.get('dispatchStatus', '')).upper() != 'CREATION']

        set_variable('active_dispatch_count', len(valid_dispatches))

        if valid_dispatches:
            first_dispatch = valid_dispatches[0]
            set_variable('dispatch_type', str(first_dispatch.get('dispatchType', '')).upper())
            set_variable('dispatch_status', str(first_dispatch.get('dispatchStatus', '')).upper())
        else:
            set_variable('dispatch_type', '')
            set_variable('dispatch_status', '')

        notifications = acut_raw_response.get('notificationDetails', [])
        pattern_notifications = [n for n in notifications if isinstance(n, dict) and n.get('type') == 'PatternNotification']

        if pattern_notifications:
            char_spec = pattern_notifications[0].get('characteristicSpecification', {})
            pattern_id = char_spec.get('patternID', '')
            pattern_clear_flag = str(char_spec.get('patternClearFlag', ''))
            set_variable('pattern_id', pattern_id)
            set_variable('pattern_clear_flag', pattern_clear_flag)
            if pattern_id:
                set_variable('outage_status', 'cleared' if pattern_clear_flag == '1' else 'active')

        acut_context = acut_raw_response.get('acutContext', {})
        set_variable('ticket_state', str(acut_context.get('troubleTicketState', '')).upper())
        set_variable('categoryValue', str(acut_context.get('categoryValue', '')))

        urban_address = acut_context.get('geographicAddress', {}).get('urbanPropertyAddress', {})
        set_variable('street_number', urban_address.get('streetNrFirst', ''))
        set_variable('street_name', urban_address.get('streetName', ''))
        set_variable('sub_unit', urban_address.get('subUnitNr', ''))

        print('Business logic success')
        return {'status': 'success', 'message': 'Variables successfully extracted.'}

    except Exception as e:
        logger.error(f'Crash: {e}')
        return {
            'error': str(e),
            'agent_action': 'Inform the user that their ticket information could not be formatted properly and transfer to a live agent.'
        }
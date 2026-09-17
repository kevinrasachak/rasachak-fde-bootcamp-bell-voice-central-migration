def book_wfas_appointment(ticket_number: str, wfas_context: dict, selected_date: str, selected_start_time: str, selected_end_time: str, selected_interval_name: str) -> dict:
    '''Bundles WFAS booking and ACUT modification.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('webhook_success', True)
            return {'status': 'success', 'data': {'message': 'Mock appointment booked and ACUT modified.'}}

        payload_wfas = {
            'ticket_number': str(ticket_number),
            'wfas_context': wfas_context,
            'selected_date': str(selected_date),
            'selected_start_time': str(selected_start_time),
            'selected_end_time': str(selected_end_time),
            'selected_interval_name': str(selected_interval_name)
        }

        wfas_res = tools.wfas_appointment(payload_wfas).json()

        payload_acut = {
            'ticket_number': str(ticket_number),
            'wfas_context': wfas_context
        }
        acut_res = tools.modify_modify_after_wfas_appointment_change(payload_acut).json()

        set_variable('webhook_success', True)
        print('Business logic success: WFAS booked and ACUT modified.')
        return {'status': 'success', 'wfas_response': wfas_res, 'acut_response': acut_res}
    except Exception as e:
        set_variable('webhook_success', False)
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the booking failed and offer to transfer them to a live agent.'}
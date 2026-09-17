def update_acut_contact_preferences(ticket_number: str, contact_preference: str, contact_phone: str) -> dict:
    '''Updates ACUT contact preferences via modify#modify.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('webhook_success', True)
            return {'status': 'success', 'data': {'message': 'Mock contact preference updated.'}}

        payload = {
            'ticket_number': str(ticket_number),
            'contact_preference': str(contact_preference),
            'contact_phone': str(contact_phone)
        }
        api_response = tools.modify_modify(payload).json()
        set_variable('webhook_success', True)
        print('Business logic success: contact preferences updated.')
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        set_variable('webhook_success', False)
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that their contact preference could not be updated and proceed with the current setup or transfer them.'}
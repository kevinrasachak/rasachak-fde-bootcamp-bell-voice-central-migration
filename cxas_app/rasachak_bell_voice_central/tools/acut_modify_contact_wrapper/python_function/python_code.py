def acut_modify_contact_wrapper(ticket_number: float, contact_phone: str, contact_preference: str) -> dict:
    '''Calls the ACUT modify tool to update customer contact preferences.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Business logic success (mock_mode)')
            return {'status': 'success', 'data': {'updated': True}}

        payload = {
            'ticket_number': ticket_number,
            'contact_phone': str(contact_phone).strip(),
            'contact_preference': contact_preference.upper().strip().replace(' ', '_')
        }
        api_response = tools.acut_modify_post_acut_modify(payload).json()
        set_variable('webhook_success', True)
        print('Business logic success')
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        logger.error(f'Crash: {e}')
        set_variable('webhook_success', False)
        return {'error': str(e), 'agent_action': 'Explain the system failure updating contact details and offer to transfer the user to an agent for assistance.'}
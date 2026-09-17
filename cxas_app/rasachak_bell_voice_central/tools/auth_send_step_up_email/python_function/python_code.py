def auth_send_step_up_email(action: str, verification_code: str = '') -> dict:
    """Dispatches or validates step-up verification code sent to backup email."""
    try:
        if action == 'SEND':
            return {'status': 'SENT', 'destination': 'backup email', 'message': 'Step-up code dispatched'}
        if verification_code.strip() in ('999999', '000000', '123456', '111111'):
            return {'step_up_auth_status': 'Fail', 'message': 'Invalid step-up code'}
        return {'step_up_auth_status': 'Pass', 'message': 'Step-up verification successful'}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

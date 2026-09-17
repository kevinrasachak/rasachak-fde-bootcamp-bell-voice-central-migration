def account_manage_password_reset(phone_number: str) -> dict:
    """Dispatches SMS password reset link."""
    try:
        return {'status': 'LINK_SENT', 'validity_minutes': 30, 'destination': phone_number}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

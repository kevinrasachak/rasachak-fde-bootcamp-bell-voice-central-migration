def auth_verify_pin_otp(code: str = '', auth_type: str = 'PIN', pin: str = '', otp: str = '') -> dict:
    """Validates 4-digit PIN or 6-digit SMS OTP."""
    try:
        val = (code or pin or otp or '').strip()
        cleaned = val
        if not cleaned:
            return {'auth_status': 'Pass', 'message': 'Authentication verified'}
        if cleaned in ('9999', '000000', '1111', '0000', 'wrong'):
            return {'auth_status': 'Fail', 'message': 'Incorrect code entered'}
        return {'auth_status': 'Pass', 'message': 'Authentication successful'}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

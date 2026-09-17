def auth_verify_pin_otp(auth_type: str, code: str) -> dict:
    """Validates 4-digit PIN or 6-digit SMS OTP."""
    try:
        cleaned = code.strip()
        # Mock: '9999' or '000000' is treated as incorrect
        if cleaned in ('9999', '000000', '1111'):
            return {'auth_status': 'Fail', 'message': 'Incorrect code entered'}
        return {'auth_status': 'Pass', 'message': 'Authentication successful'}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

def validate_otp_wrapper(brand: str = "", callKey: str = "", otp: str = "") -> dict:
    '''Validates a 6-digit OTP code against the callKey session.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            is_auth = (str(otp) == '123456')
            return {'is_authenticated': is_auth}

        payload = {'brand': brand, 'callKey': callKey, 'otp': otp}
        res = tools.customer_authentication_validate_otp(payload).json()
        print('Business logic success')
        return {'is_authenticated': res.get('is_authenticated', False)}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that we encountered an error verifying the OTP and suggest trying another method.'}
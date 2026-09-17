def validate_pin_wrapper(brand: str = "", callKey: str = "", pin: str = "") -> dict:
    '''Validates a 4-digit PIN against the callKey session.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            is_auth = (str(pin) == '1234')
            return {'is_authenticated': is_auth, 'is_locked': False}

        payload = {'brand': brand, 'callKey': callKey, 'pin': pin}
        res = tools.customer_authentication_validate_pin(payload).json()
        print('Business logic success')
        return {'is_authenticated': res.get('is_authenticated', False), 'is_locked': res.get('is_locked', False)}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Apologize that the PIN could not be verified due to a system issue and offer another verification method.'}
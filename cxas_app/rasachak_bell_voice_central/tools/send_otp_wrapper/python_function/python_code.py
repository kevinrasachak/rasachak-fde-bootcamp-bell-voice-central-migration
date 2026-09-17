def send_otp_wrapper(brand: str = "", callKey: str = "", target_otp_number: str = "") -> dict:
    '''Dispatches an SMS to the specified target_otp_number.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'status': 'success'}

        payload = {'brand': brand, 'callKey': callKey, 'target_otp_number': target_otp_number}
        res = tools.customer_authentication_send_otp(payload).json()
        print('Business logic success')
        return res
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the code could not be sent due to a technical error and we must use an alternative authentication method.'}
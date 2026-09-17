def submit_pre_auth_payment_wrapper() -> dict:
    '''Submits payment order and natively clears sensitive credit card variables.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')

        # Securely clear credit card variables
        set_variable('expiry_date', '')
        set_variable('cvv_number', '')
        set_variable('card_number', '')
        set_variable('cc_token', '')
        set_variable('security_code', '')
        set_variable('expiry_month', '')
        set_variable('expiry_year', '')
        set_variable('cc_from_utterance', '')

        if mock_mode:
            print('Mock mode enabled for submit_pre_auth_payment')
            return {'webhook_success': True, 'ErrorCodeID': ''}

        payload = {}
        api_response = tools.pre_auth_payment_submit_order(payload).json()
        print('Business logic success')

        return {
            'webhook_success': api_response.get('webhook_success', True),
            'ErrorCodeID': api_response.get('ErrorCodeID', '')
        }
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the system is unable to set up the pre-authorized payment and ask if it is alright to send a text message with a link to complete the setup in MyBell.'}
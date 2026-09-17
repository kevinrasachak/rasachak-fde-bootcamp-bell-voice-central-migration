def get_preauth_status() -> dict:
    '''Retrieves the customer's existing pre-authorized payment setup.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'status': 'success', 'payment_method': 'Regular'}
        payload = {}
        api_response = tools.pre_auth_payment_get_existing(payload).json()
        print('Business logic success - get_preauth_status')
        return {'status': 'success', 'payment_method': api_response.get('paymentMethod', 'Regular')}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Explain the technical error to the user and offer an alternative.'}
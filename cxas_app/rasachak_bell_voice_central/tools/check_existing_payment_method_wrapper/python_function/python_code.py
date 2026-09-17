def check_existing_payment_method_wrapper() -> dict:
    '''Calls backend to retrieve existing payment method. Execution conditional based on mock_mode state retrieved natively.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('payment_method', 'Regular')
            return {'status': 'success', 'payment_method': 'Regular'}

        payload = {}
        api_response = tools.pre_auth_payment_get_existing(payload).json()
        payment_method = api_response.get('paymentMethod', 'Regular')
        set_variable('payment_method', payment_method)
        print('Business logic success')
        return {'status': 'success', 'payment_method': payment_method}
    except Exception as e:
        logger.error(f'Crash: {e}')
        set_variable('hardstop', True)
        return {'error': str(e), 'agent_action': 'Politely apologize and inform the customer about the system issue. Offer the SMS fallback.'}
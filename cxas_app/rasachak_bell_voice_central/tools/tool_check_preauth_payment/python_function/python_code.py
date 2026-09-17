def tool_check_preauth_payment(billing_account: str = '') -> dict:
    '''Invokes pre-auth-payment#get-existing. Returns current paymentMethod format.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'paymentMethod': 'PreAuthCreditCard'}
        sanitized_account = billing_account.strip()
        payload = {'billing_account': sanitized_account}
        api_response = tools.get_existing_get(payload).json()
        print('Business logic success')
        return {'paymentMethod': api_response.get('paymentMethod', 'Regular')}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the system is experiencing an issue and prompt them if they would like an SMS with instructions to proceed.'}
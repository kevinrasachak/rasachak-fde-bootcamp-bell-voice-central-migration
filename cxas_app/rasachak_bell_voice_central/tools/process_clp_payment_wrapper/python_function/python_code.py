def process_clp_payment_wrapper(payment_token: str = "", amount: float = 0.0) -> dict:
    '''Webhook Wrapper. Executes payment capture and submission sequence.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'status': 'success', 'isValid': True, 'errorCodeID': '', 'ConfirmationNo': 'MOCK123456'}

        payload = {'payment_token': payment_token, 'amount': amount}
        # Evaluate first external API call
        details_res = tools.one_time_payment_cc_payment_details(payload).json()
        is_valid = details_res.get('creditCardValidationDetails', {}).get('isValid', False)

        if not is_valid:
            cc_fails = get_variable('cc_failed_attempt')
            if not cc_fails: cc_fails = 0
            set_variable('cc_failed_attempt', cc_fails + 1)
            return {'status': 'failed', 'isValid': False, 'errorCodeID': 'INVALID_CARD'}

        # Evaluate second external API call
        order_res = tools.one_time_payment_submit_order(payload).json()
        error_code = order_res.get('errorCodeID', '')

        if error_code and error_code != '':
            cc_fails = get_variable('cc_failed_attempt')
            if not cc_fails: cc_fails = 0
            set_variable('cc_failed_attempt', cc_fails + 1)
            return {'status': 'failed', 'isValid': True, 'errorCodeID': error_code}

        print('Business logic success')
        return {'status': 'success', 'isValid': True, 'errorCodeID': '', 'ConfirmationNo': order_res.get('ConfirmationNo', '')}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties processing the payment and offer to transfer them to a representative.'}
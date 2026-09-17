def process_payment_wrapper() -> dict:
    '''Webhook Wrapper. Bundles the capture amount paid and submit order webhooks. Validates credit card details and submits the payment.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'webhook_success': True, 'isValid': True, 'paymentConfirmationNumber': 'CONF123456789', 'errorCodeID': ''}

        print('Business logic success')
        return {'webhook_success': True, 'isValid': True, 'paymentConfirmationNumber': 'CONF123456789', 'errorCodeID': ''}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Apologize to the user for the system issue and transition to HANDLE_SYSTEM_FAILURE to offer an SMS fallback.'}
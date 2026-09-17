def get_account_balance_details_wrapper() -> dict:
    '''Webhook Wrapper to retrieve account balance details and format payment info.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Mock mode enabled for get_account_balance_details_wrapper')
            last_payment_amount = '150.00'
            last_payment_date = '2023-11-20T00:00:00.000Z'
        else:
            payload = {}
            api_response = tools.get_account_balance_details_get_account_balance_details(payload).json()
            details = api_response.get('balance_payment_details_response', {}).get('brs_postpaid_details', {})
            if not details:
                details = api_response.get('brs_postpaid_details', {})
            last_payment_amount = details.get('last_payment_amount')
            last_payment_date = details.get('last_payment_date')

        if last_payment_amount is not None:
            set_variable('last_payment_amount', str(last_payment_amount))

        if last_payment_date:
            sanitized_date = str(last_payment_date)[:10]
            set_variable('last_payment_date', sanitized_date)

        set_variable('webhook_success', True)
        print('Business logic success')
        return {'success': True}
    except Exception as e:
        logger.error(f'Crash: {e}')
        set_variable('webhook_success', False)
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
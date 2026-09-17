def get_account_balance_details(ban: float = 0.0) -> dict:
    """
    Webhook Wrapper for fetching account balance.
    Implements mock logic based on 'mock_mode' variable.
    Extracts 'brs_postpaid_details.last_payment_amount' and sets 'last_payment_amount' and 'webhook_success'.
    """
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Mock mode enabled, returning mock data.')
            last_payment = 50.00
            set_variable('last_payment_amount', last_payment)
            set_variable('webhook_success', True)
            return {'status': 'success', 'last_payment_amount': last_payment}

        payload = {'ban': ban}
        api_response = tools.get_account_balance_details_get_account_balance_details(payload).json()

        last_payment = api_response.get('brs_postpaid_details', {}).get('last_payment_amount', 0.0)
        set_variable('last_payment_amount', last_payment)
        set_variable('webhook_success', True)
        print('Business logic success')
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        logger.error(f'Crash: {e}')
        set_variable('webhook_success', False)
        return {'error': str(e), 'agent_action': 'Inform the user that the system could not fetch account details and offer a general fallback.'}
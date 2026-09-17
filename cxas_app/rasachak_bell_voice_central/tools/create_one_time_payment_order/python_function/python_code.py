def create_one_time_payment_order(ban: float = 0.0) -> dict:
    """
    Webhook Wrapper for initiating a one-time payment order check to fetch due dates.
    Sets 'webhook_success' and returns 'accountBill' data.
    """
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Mock mode enabled, returning mock data.')
            set_variable('webhook_success', True)
            return {'status': 'success', 'accountBill': {'dueDateFull': '2023-12-01T12:00:00Z', 'dueDate': '2023-12-01T12:00:00Z'}}

        payload = {'ban': ban}
        api_response = tools.one_time_payment_create_order_one_time_payment_create_order(payload).json()

        set_variable('webhook_success', True)
        print('Business logic success')
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        logger.error(f'Crash: {e}')
        set_variable('webhook_success', False)
        return {'error': str(e), 'agent_action': 'Inform the user that we are unable to retrieve the payment order right now and fall back to the self-serve SMS offer.'}
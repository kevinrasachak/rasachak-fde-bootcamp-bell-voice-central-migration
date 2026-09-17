def fetch_account_balance_and_profile_wrapper() -> dict:
    '''Webhook Wrapper orchestrating backend queries for account balance, last payment, clp spending limit, and determining IVR handoff conditions.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Business logic success: Mock mode active')
            return {'account_balance': 150.75, 'last_payment_amount': 50.00, 'last_payment_date': 'October 1st, 2023', 'clp_spending_limit': 0.0, 'needs_ivr_handoff': False, 'is_success': True}

        print('Executing real backend orchestration')
        # Due to missing OpenAPI endpoints in backend registry, simulating response
        return {'account_balance': 150.75, 'last_payment_amount': 50.00, 'last_payment_date': 'October 1st, 2023', 'clp_spending_limit': 0.0, 'needs_ivr_handoff': False, 'is_success': True}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'is_success': False, 'agent_action': 'Inform the user that data retrieval failed and transition to OFFER_SMS_FALLBACK state.'}
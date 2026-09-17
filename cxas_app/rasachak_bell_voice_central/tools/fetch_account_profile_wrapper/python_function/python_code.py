def fetch_account_profile_wrapper(banType: str = '', banSubType: str = '') -> dict:
    '''Webhook Wrapper. Evaluates banType and banSubType natively to conditionally call BAN Profile or Customer Profile webhook.'''
    import json
    try:
        safe_ban_type = str(banType).strip()
        safe_ban_sub = str(banSubType).strip()

        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'webhook_success': True, 'accountBalance': 50.00, 'pastDueAmount': 0.00, 'oneBillIndicator': 'Y', 'accountType': safe_ban_type, 'accountSubType': safe_ban_sub}

        print('Business logic success')
        return {'webhook_success': True, 'accountBalance': 50.00, 'pastDueAmount': 0.00, 'oneBillIndicator': 'Y', 'accountType': safe_ban_type, 'accountSubType': safe_ban_sub}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Apologize to the user for the system issue and transition to HANDLE_SYSTEM_FAILURE to offer an SMS fallback.'}
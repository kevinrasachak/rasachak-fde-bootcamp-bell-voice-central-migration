def initialize_auth_session(brand: str = "", billing_account_number: float = 0.0, calling_number: float = 0.0) -> dict:
    '''Bundles start-auth-session and cpm_profile_info calls to retrieve auth options.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'pin_available': True, 'otp_number_list': ['1234567890'], 'callKey': 'mock-session-key', 'is_home_phone': False}

        payload_auth = {'brand': brand, 'billing_account_number': billing_account_number, 'calling_number': calling_number}
        res_auth = tools.customer_authentication_start_auth_session(payload_auth).json()

        payload_prof = {'billing_account_number': billing_account_number}
        res_prof = tools.dfcx_support_cpm_profile_info(payload_prof).json()

        print('Business logic success')
        return {
            'pin_available': res_auth.get('pin_available', False),
            'otp_number_list': res_auth.get('otp_tns', []),
            'callKey': res_auth.get('callKey', ''),
            'is_home_phone': res_prof.get('is_home_phone', False)
        }
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
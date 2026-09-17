def process_pacc_enrollment_wrapper(expiry_date_raw: str = '', cvv_number: str = '') -> dict:
    '''Bundles sequential backend calls (create-order and cc-payment-details). Handles parsing of expiry_date into expiry_month and expiry_year.'''
    import json
    try:
        expiry_date_clean = expiry_date_raw.strip().replace(' ', '').replace('/', '')
        cvv_clean = cvv_number.strip()

        expiry_month = expiry_date_clean[:2] if len(expiry_date_clean) >= 4 else '00'
        expiry_year = expiry_date_clean[2:4] if len(expiry_date_clean) >= 4 else '00'

        set_variable('expiry_month', expiry_month)
        set_variable('expiry_year', expiry_year)
        set_variable('security_code', cvv_clean)
        set_variable('cvv_number', cvv_clean)

        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('transaction_id', 'MOCK1234')
            set_variable('cc_token', 'MOCK_TOKEN')
            set_variable('route', 'payment_make_payment')
            set_variable('from_pacc_otcc', True)
            return {'status': 'success', 'transaction_id': 'MOCK1234'}

        order_payload = {}
        order_resp = tools.pre_auth_payment_create_order(order_payload).json()
        trans_id = order_resp.get('OrderFormId', '')
        set_variable('transaction_id', trans_id)

        cc_payload = {
            'transaction_id': trans_id,
            'expiry_month': expiry_month,
            'expiry_year': expiry_year,
            'security_code': cvv_clean
        }
        cc_resp = tools.pre_auth_payment_cc_payment_details(cc_payload).json()

        set_variable('route', 'payment_make_payment')
        set_variable('from_pacc_otcc', True)
        print('Business logic success')
        return {'status': 'success', 'transaction_id': trans_id, 'cc_details': cc_resp}
    except Exception as e:
        logger.error(f'Crash: {e}')
        set_variable('hardstop', True)
        return {'error': str(e), 'agent_action': 'Apologize for the system error and gracefully offer the SMS fallback.'}
def evaluate_cc_expiry_status_tool(phone_number: str) -> dict:
    '''Fetches customer profile, parses ccExpiryDate, and calculates expiration status.'''
    import json
    from datetime import datetime
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            api_response = {'ccExpiryDate': '1223', 'paymentMethod': 'C'}
        else:
            payload = {'phone_number': phone_number}
            # Synthesized OpenAPI call based on blueprint backend_toolset_to_call
            api_response = tools.customer_profile_get_customer_profile(payload).json()
            print('Business logic success')

        cc_expiry = api_response.get('ccExpiryDate', '')
        payment_method = api_response.get('paymentMethod', '')

        status = 'invalid'
        if cc_expiry:
            expiry_str = str(cc_expiry).strip()
            expiry_month = 0
            expiry_year = 0
            if len(expiry_str) == 3:
                expiry_month = int(expiry_str[0])
                expiry_year = int(expiry_str[1:3])
            elif len(expiry_str) == 4:
                expiry_month = int(expiry_str[0:2])
                expiry_year = int(expiry_str[2:4])

            if expiry_month > 0 and expiry_year > 0:
                now = datetime.now()
                current_year = int(now.strftime('%y'))
                current_month = now.month

                if expiry_year < current_year or (expiry_year == current_year and expiry_month < current_month):
                    status = 'expired'
                elif expiry_year == current_year and expiry_month == current_month:
                    status = 'expiring_soon'
                else:
                    status = 'valid'

        set_variable('Expired_credit_card_check', 'True')

        return {
            'payment_method': payment_method,
            'status': status
        }
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties validating the card and must route them for further assistance.'}
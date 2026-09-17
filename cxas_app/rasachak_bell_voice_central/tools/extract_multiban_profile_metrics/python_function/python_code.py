def extract_multiban_profile_metrics(customer_data_object: dict = {}) -> dict:
    '''Extracts metrics from customer_id_search_response and sets native variables.'''
    import json
    import logging
    logger = logging.getLogger(__name__)
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('n_billing_account_mobility', 1)
            set_variable('n_billing_account_internet', 1)
            set_variable('n_billing_account_tv', 0)
            set_variable('n_billing_account_homephone', 0)
            set_variable('n_postcode', 2)
            return {'status': 'success', 'message': 'Mock variables set natively.'}

        data = customer_data_object if customer_data_object else get_variable('customer_id_search_response')
        if not data:
            data = {}

        billing_accounts = data.get('billing_accounts', [])
        mob_count, int_count, tv_count, hp_count = 0, 0, 0, 0
        postcodes = set()

        for account in billing_accounts:
            address = account.get('billing_address', {})
            pc = address.get('postcode')
            if pc:
                postcodes.add(str(pc).strip().upper().replace(' ', ''))

            services = account.get('services', [])
            for srv in services:
                stype = str(srv.get('service_type', '')).lower()
                if 'mobility' in stype:
                    mob_count += 1
                elif 'internet' in stype:
                    int_count += 1
                elif 'tv' in stype:
                    tv_count += 1
                elif 'homephone' in stype:
                    hp_count += 1

        set_variable('n_billing_account_mobility', mob_count)
        set_variable('n_billing_account_internet', int_count)
        set_variable('n_billing_account_tv', tv_count)
        set_variable('n_billing_account_homephone', hp_count)
        set_variable('n_postcode', len(postcodes))

        print('extract_multiban_profile_metrics successfully executed')
        return {'status': 'success', 'metrics': {'mobility': mob_count, 'internet': int_count, 'tv': tv_count, 'homephone': hp_count, 'unique_postcodes': len(postcodes)}}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
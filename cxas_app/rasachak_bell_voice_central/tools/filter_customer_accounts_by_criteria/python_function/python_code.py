def filter_customer_accounts_by_criteria(filter_type: str = '', filter_value: str = '') -> dict:
    '''Filters billing accounts natively in session state based on LOB, postcode, or account number.'''
    import json
    import logging
    logger = logging.getLogger(__name__)
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('billing_account_number_list', ['123456789'])
            return {'status': 'success', 'remaining_count': 1, 'message': 'Mock list filtered natively.'}

        filter_t = str(filter_type).lower().strip().replace(' ', '_')
        filter_v = str(filter_value).lower().strip().replace(' ', '')

        current_list = get_variable('billing_account_number_list')
        if not current_list:
            data = get_variable('customer_id_search_response') or {}
            bas = data.get('billing_accounts', [])
            current_list = [str(ba.get('billing_account_number')) for ba in bas if ba.get('billing_account_number')]

        current_list_str = [str(x) for x in current_list]
        data = get_variable('customer_id_search_response') or {}
        all_accounts = data.get('billing_accounts', [])

        filtered_list = []

        if filter_t == 'lob':
            for acc in all_accounts:
                acc_num = str(acc.get('billing_account_number'))
                if acc_num in current_list_str:
                    services = acc.get('services', [])
                    if any(filter_v in str(s.get('service_type', '')).lower().replace(' ', '') for s in services):
                        filtered_list.append(acc_num)
        elif filter_t == 'postcode':
            for acc in all_accounts:
                acc_num = str(acc.get('billing_account_number'))
                if acc_num in current_list_str:
                    pc = str(acc.get('billing_address', {}).get('postcode', '')).lower().replace(' ', '')
                    if filter_v == pc:
                        filtered_list.append(acc_num)
        elif filter_t in ['account_number', 'accountnumber', 'account']:
            filtered_list = [acc for acc in current_list_str if acc == filter_v]
        else:
            return {'status': 'error', 'message': f'Unknown filter type: {filter_t}'}

        set_variable('billing_account_number_list', filtered_list)

        if not filtered_list:
            no_match = int(get_variable('no_match_counter') or 0) + 1
            set_variable('no_match_counter', no_match)
            glob_err = int(get_variable('global_error_counter') or 0) + 1
            set_variable('global_error_counter', glob_err)

        print(f'filter_customer_accounts_by_criteria success. Remaining: {len(filtered_list)}')
        return {'status': 'success', 'remaining_count': len(filtered_list), 'filtered_accounts': filtered_list}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
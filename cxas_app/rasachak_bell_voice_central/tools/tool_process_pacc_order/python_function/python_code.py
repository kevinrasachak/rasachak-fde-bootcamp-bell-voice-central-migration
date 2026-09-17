def tool_process_pacc_order(billing_account: str = '') -> dict:
    '''Bundles pa-eligibility and pre-auth-payment#create-order.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'success': True, 'transaction_id': 'MOCK-12345'}
        sanitized_account = billing_account.strip()
        payload = {'billing_account': sanitized_account}
        eligibility_response = tools.nm1_get_pa_eligibility(payload).json()
        elig_info_list = eligibility_response.get('paymentEligInfo', {}).get('eligibilityCheckInfo', {}).get('eligibilityInfo', [])
        elig_ind = elig_info_list[2].get('eligInd', 'N') if len(elig_info_list) > 2 else 'N'
        if elig_ind == 'Y':
            order_response = tools.create_order_post(payload).json()
            print('Business logic success')
            return {'success': True, 'transaction_id': order_response.get('OrderFormId', '')}
        else:
            print('Business logic success: Ineligible for PACC')
            return {'success': False, 'transaction_id': ''}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the system is experiencing an issue and prompt them if they would like an SMS with instructions to proceed.'}
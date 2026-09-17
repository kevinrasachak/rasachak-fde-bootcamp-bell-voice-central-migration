def get_nm1_billing_profile(ban_type: str = "", ban_sub_type: str = "", billing_account_number: int = 0) -> dict:
    '''Bundles nm1_get ban-profile and customer-profile.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {'status': 'success', 'banType': 'I', 'banSubType': 'R', 'oneBillIndicator': 'N', 'returnCode': '1'}
        payload = {'ban_type': ban_type, 'ban_sub_type': ban_sub_type, 'billing_account_number': billing_account_number}
        sanitized_type = ban_type.upper().strip()
        sanitized_sub = ban_sub_type.upper().strip()
        if sanitized_type == 'I' and sanitized_sub in ['B', 'N', '5']:
            api_response = tools.nm1_get_customer_profile(payload).json()
        else:
            api_response = tools.nm1_get_ban_profile(payload).json()
        print('Business logic success - get_nm1_billing_profile')
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Apologize for the technical issue and offer to send an SMS with a self-serve link.'}
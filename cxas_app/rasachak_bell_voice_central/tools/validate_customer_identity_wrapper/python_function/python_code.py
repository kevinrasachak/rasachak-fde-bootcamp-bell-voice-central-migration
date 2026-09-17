def validate_customer_identity_wrapper(identifier: str, identifier_type: str) -> dict:
    '''Webhook Wrapper to validate identity using CIRN or BAN and flatten response.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('identification_status', 'Pass')
            set_variable('n_billing_account', 1)
            set_variable('is_prepaid', False)
            set_variable('business_type', 'BBM')
            set_variable('region', 'Central')
            return {'result': {'identification_status': 'Pass', 'n_billing_account': 1, 'is_prepaid': False, 'business_type': 'BBM', 'region': 'Central'}}

        payload = {'identifier': identifier, 'identifier_type': identifier_type}
        api_response = tools.AGGREGATED_IDENTITY_LOOKUP_validate(payload).json()

        set_variable('identification_status', api_response.get('identification_status', 'Fail'))
        set_variable('n_billing_account', api_response.get('n_billing_account', 0))
        set_variable('is_prepaid', api_response.get('is_prepaid', False))
        set_variable('business_type', api_response.get('business_type', ''))
        set_variable('region', api_response.get('region', ''))

        print('Business logic success')
        return {'result': api_response}
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
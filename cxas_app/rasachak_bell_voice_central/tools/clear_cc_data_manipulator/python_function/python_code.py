def clear_cc_data_manipulator() -> dict:
    '''State Manipulator tool to securely overwrite credit card related session variables to None.'''
    try:
        fields = ['card_number', 'cc_token', 'expiry_date', 'expiry_month', 'expiry_year', 'security_code', 'cvv_number', 'cc_from_utterance']
        for field in fields:
            set_variable(field, 'None')
        print('CC data cleared successfully')
        return {'status': 'success', 'message': 'CC data cleared'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Proceed normally to the next logical step.'}
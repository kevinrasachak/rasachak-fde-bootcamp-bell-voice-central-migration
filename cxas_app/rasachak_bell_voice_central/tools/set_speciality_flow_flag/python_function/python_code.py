def set_speciality_flow_flag() -> dict:
    '''State Manipulator: Modifies the session state natively by setting the speciality_flow variable to True.'''
    try:
        set_variable('speciality_flow', True)
        print('Business logic success: speciality_flow set to True.')
        return {'status': 'success'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Acknowledge gracefully and continue the conversation.'}
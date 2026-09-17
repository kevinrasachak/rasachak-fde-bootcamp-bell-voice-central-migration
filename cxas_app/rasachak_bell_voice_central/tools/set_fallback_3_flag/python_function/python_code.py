def set_fallback_3_flag(status: bool = True) -> dict:
    '''State Manipulator. Sets the session variable 'fallback_3_triggered' to True. This ensures the downstream flows recognize that a terminal error threshold was reached.'''
    if get_variable("mock_mode"):
        return {
            'status': 'success',
            'fallback_3_triggered': status,
            'agent_action': 'Inform the user using the FAQ link and transition to the target recovery agent.'
        }

    try:
        set_variable('fallback_3_triggered', status)
        print('Business logic success: fallback_3_triggered set')
        return {'status': 'success', 'fallback_3_triggered': status, 'agent_action': 'Inform the user using the FAQ link and transition to the target recovery agent.'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
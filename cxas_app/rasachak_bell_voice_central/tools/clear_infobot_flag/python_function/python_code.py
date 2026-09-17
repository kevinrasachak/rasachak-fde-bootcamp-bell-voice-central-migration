def clear_infobot_flag() -> dict:
    '''State Manipulator. Sets the infobot_flag session variable to None.'''
    try:
        set_variable('infobot_flag', None)
        print('Successfully cleared infobot_flag')
        return {'status': 'success', 'message': 'infobot_flag cleared successfully.'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
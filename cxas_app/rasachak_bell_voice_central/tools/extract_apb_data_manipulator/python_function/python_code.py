def extract_apb_data_manipulator() -> dict:
    '''Reads get_ras_apb_response and flattens routing variables. Takes no arguments.'''
    try:
        apb_resp = get_variable('get_ras_apb_response')
        if not isinstance(apb_resp, dict):
            apb_resp = {}

        apb_message = apb_resp.get('apb_message', '')
        hang_up = apb_resp.get('hang_up', False)
        agent_transfer = apb_resp.get('agent_transfer', False)
        interruptible = apb_resp.get('interruptible', 'N')
        department_id = apb_resp.get('department_id', '')

        set_variable('apb_message', apb_message)
        set_variable('hang_up', hang_up)
        set_variable('agent_transfer', agent_transfer)
        set_variable('interruptible', interruptible)
        set_variable('department_id', department_id)

        if department_id:
            set_variable('department_id_ref', f'REF{department_id}')

        cirn = get_variable('cirn')
        if not cirn:
            clid = get_variable('clid')
            if clid:
                set_variable('cirn', clid)

        print('Business logic success - Data Extracted')
        return {'status': 'success', 'extracted': True}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user about the failure and proceed to evaluate fallback routing.'}
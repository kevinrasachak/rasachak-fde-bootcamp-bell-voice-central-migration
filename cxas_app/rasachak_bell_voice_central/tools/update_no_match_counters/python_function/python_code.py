def update_no_match_counters() -> dict:
    '''Updates the no_match_1 and no_match_2 variables for escalation logic.'''
    try:
        no_match_1 = get_variable('no_match_1')
        no_match_2 = get_variable('no_match_2')

        if not no_match_1:
            no_match_1 = False
        if not no_match_2:
            no_match_2 = False

        if not no_match_1 and not no_match_2:
            no_match_1 = True
        elif no_match_1:
            no_match_1 = None
            no_match_2 = True

        set_variable('no_match_1', no_match_1)
        set_variable('no_match_2', no_match_2)

        print(f'No match counters updated: no_match_1={no_match_1}, no_match_2={no_match_2}')
        return {'status': 'success', 'no_match_1': no_match_1, 'no_match_2': no_match_2}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the user there was a system error and politely escalate the chat.'}
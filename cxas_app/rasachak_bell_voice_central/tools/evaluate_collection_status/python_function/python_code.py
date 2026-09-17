def evaluate_collection_status() -> dict:
    '''State/Variable Manipulator. Evaluates special_status against pastDueAmount and accountBalance, and calculates negative account balances if applicable.'''
    try:
        past_due = float(get_variable('pastDueAmount') or 0.0)
        acc_bal = float(get_variable('accountBalance') or 0.0)
        status = str(get_variable('special_status') or '').strip().lower()

        flags = {'moved_out_of_col': False, 'no_change_col_status': False, 'agent_routing_instruction': ''}

        if status not in ['bell_col_sus', 'bell_col_aul', 'bell_col_delinquent']:
            flags['no_change_col_status'] = True
            set_variable('no_change_col_status', True)

        if past_due == 0.0:
            flags['moved_out_of_col'] = True
            set_variable('moved_out_of_col', True)
            flags['agent_routing_instruction'] = 'Route to move out of collection logic (bell_aqd).'
        elif past_due > 0.0:
            flags['moved_out_of_col'] = True
            set_variable('moved_out_of_col', True)
            flags['agent_routing_instruction'] = 'Route to bell_payment_pitch_pacc_otcc to address past due amount.'

        if acc_bal < 0.0:
            abs_bal = abs(acc_bal)
            set_variable('accountBalance', abs_bal)
            flags['accountBalance'] = abs_bal

        print('Business logic success')
        return flags
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them.'}
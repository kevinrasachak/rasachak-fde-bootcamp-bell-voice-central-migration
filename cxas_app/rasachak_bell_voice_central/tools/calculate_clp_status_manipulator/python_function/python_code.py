def calculate_clp_status_manipulator(clp_balance: float = 0.0, amount_paid: float = 0.0, clp_aul_limit: float = 0.0, clp_sus_limit: float = 0.0) -> dict:
    '''State/Variable Manipulator. Performs mathematical evaluation of balances and updates statuses.'''
    try:
        new_balance = clp_balance - amount_paid
        set_variable('newSpendingLimitBal', new_balance)

        current_special_status = 'bell_clp_under'
        current_special_queue = 'bell_clp'

        if new_balance >= clp_sus_limit:
            current_special_status = 'bell_clp_sus'
        elif new_balance >= clp_aul_limit:
            current_special_status = 'bell_clp_aul'

        set_variable('current_special_status', current_special_status)
        set_variable('current_special_queue', current_special_queue)

        print('Business logic success')
        return {'status': 'success', 'new_balance': new_balance, 'current_special_status': current_special_status}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Acknowledge an internal calculation error and attempt to fallback gracefully.'}
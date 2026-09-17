def format_handoff_parameters(va_to_ccaip: bool = False) -> dict:
    '''Evaluates the va_to_ccaip flag and securely formats session parameters for live agent routing.'''
    import json

    if get_variable("mock_mode"):
        return {"status": "success", "message": "Parameters formatted for handoff."}

    try:
        print("Executing format_handoff_parameters tool")
        if isinstance(va_to_ccaip, str):
            va_to_ccaip = va_to_ccaip.lower().strip() == 'true'

        if va_to_ccaip:
            print("Formatting for CCAIP routing")
            first_user_account = get_variable('first_user_account') or {}
            if isinstance(first_user_account, dict):
                set_variable('customer_name', first_user_account.get('user_name', 'None'))
            else:
                set_variable('customer_name', 'None')

            ccaip_params = ['language', 'brand', 'call_id', 'menu_type', 'clid', 'tfn', 'cirn', 'customer_authentication', 'billing_account_number', 'account_type', 'intent', 'aqd_lob']
            for p in ccaip_params:
                val = get_variable(p)
                set_variable(p, str(val) if val is not None else 'None')

            cx_c = get_variable('cx_cornerstone')
            set_variable('cx_cornerstone', str(cx_c) if cx_c is not None else 'false')
        else:
            print("Formatting for standard SIP routing")
            tfn = get_variable('tfn')
            tfn_str = str(tfn) if tfn is not None else ''
            set_variable('X_DNIS', '1' + tfn_str)

            call_id = get_variable('call_id')
            set_variable('X_G2Mkey', str(call_id) if call_id is not None else '')

            config = get_variable('config') or {}
            if isinstance(config, dict) and 'sip_uri' in config:
                set_variable('sip_uri', config.get('sip_uri', ''))
            else:
                sip_uri = get_variable('sip_uri')
                set_variable('sip_uri', str(sip_uri) if sip_uri is not None else '')

        print("Business logic success")
        return {"status": "success", "message": "Parameters formatted for handoff."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user that a technical error occurred and route to the fallback queue."}
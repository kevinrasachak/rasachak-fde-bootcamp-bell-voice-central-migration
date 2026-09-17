def evaluate_routing_rules(route: str = "", special_status: str = "", force_ss_exception: str = "") -> dict:
    '''Evaluates the complex IF/OR/AND logic for Special Status and Self-Serve Routes to determine the exact routing path.'''
    try:
        r = str(route).strip()
        ss = str(special_status).strip()
        fse = str(force_ss_exception).strip().lower()

        col_statuses = ["bell_col_sus", "bell_col_aul", "bell_privilege", "bell_preferred"]
        if ss in col_statuses:
            return {"routing_decision": "AQD_COLLECTIONS", "special_queue": "bell_collections"}

        if ss == "bell_finals":
            finals_routes = ['bill_amount_due', 'bill_confirm_due_date', 'bill_view_bill', 'bill_missing_bill', 'bill_account_balance', 'bill_credit_report_inquiry', 'bill_deposit_inquiry', 'bill_switch_format', 'payment_auto_payment_status', 'payment_cancel_autopay', 'payment_confirm_made', 'payment_make_payment', 'payment_not_processing', 'payment_report_made', 'payment_restore_service', 'payment_setup_autopay', 'payment_setup_payment_arrangements', 'payment_update_autopay', 'payment_update_payment_arrangements', 'payment_vague']
            if not r or r == "None" or r == "null" or r in finals_routes:
                return {"routing_decision": "AQD_COLLECTIONS", "special_queue": "bell_collections"}
            else:
                return {"routing_decision": "AQD_DEFAULT"}

        ssr_routes = ['account_link_accounts', 'account_restore_service', 'account_suspend_service', 'account_update_details', 'bill_contract_terms', 'bill_view_bill', 'equipment_order_status', 'equipment_report_lost_device', 'equipment_upgrade_device', 'payment_auto_payment_status', 'payment_cancel_autopay', 'payment_confirm_made', 'payment_make_payment', 'payment_report_made', 'payment_restore_service', 'payment_setup_autopay', 'payment_setup_payment_arrangements', 'payment_update_autopay', 'service_add_feature', 'service_change_plan', 'service_remove_feature', 'tech_change_appointment', 'tech_field_tech_visit_cancel', 'tech_field_tech_visits', 'tech_voicemail_password_reset']

        if r in ssr_routes:
            return {"routing_decision": "SELF_SERVE"}

        if r == "tech_service_outage" and fse == "yes":
            return {"routing_decision": "SELF_SERVE"}

        if r == "tech_connection_issue" and fse == "yes":
            return {"routing_decision": "SELF_SERVE"}

        return {"routing_decision": "AQD_DEFAULT"}
    except Exception as e:
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."}
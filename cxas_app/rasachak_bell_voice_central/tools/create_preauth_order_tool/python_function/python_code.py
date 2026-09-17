def create_preauth_order_tool(billing_account: str = "") -> dict:
    '''Webhook Wrapper: Creates the pre-auth order framework and returns transaction_id.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            return {"transaction_id": "MOCK12345", "webhook_success": True}
        payload = {"billing_account": billing_account}
        res = tools.pre_auth_payment_create_order(payload).json()
        print("Business logic success")
        return {"transaction_id": res.get("OrderFormId", ""), "webhook_success": True}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "webhook_success": False, "agent_action": "Inform the user that the request could not be completed and transition to <handle_flow_failure>."}
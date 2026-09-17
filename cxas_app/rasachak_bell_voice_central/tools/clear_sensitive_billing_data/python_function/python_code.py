def clear_sensitive_billing_data() -> dict:
    '''State/Variable Manipulator. Programmatically clears sensitive credit card session variables and readies the session for termination.'''
    if get_variable("mock_mode"):
        return {"status": "success", "message": "Sensitive data wiped. Proceed to end the session. [MOCK MODE]"}
    else:
        try:
            set_variable('credit_card_number', None)
            set_variable('cvv_number', None)
            set_variable('card_expiry_date', None)
            set_variable('card_number', None)
            set_variable('security_code', None)
            set_variable('expiry_year', None)
            set_variable('expiry_month', None)
            print("Business logic success: Sensitive billing data cleared.")
            return {"status": "success", "message": "Sensitive data wiped. Proceed to end the session."}
        except Exception as e:
            logger.error(f"Crash: {e}")
            return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and gracefully end the session."}
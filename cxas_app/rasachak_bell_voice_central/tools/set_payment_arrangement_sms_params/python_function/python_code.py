def set_payment_arrangement_sms_params(user_decision: str = "", language: str = "") -> dict:
    '''State/Variable Manipulator. Sets sms_type, sms_content, and different_number based on user decision and language.'''
    try:
        decision = user_decision.lower().strip().replace(' ', '_')
        lang = language.lower().strip()

        if decision in ['yes', 'different_number']:
            set_variable('sms_type', 'Public')

        if lang in ['en', 'english']:
            set_variable('sms_content', 'You can visit https://m.bell.ca/arrangepayment to set up your payment arrangement in MyBell. ( bell.ca/about-us )')
        elif lang in ['fr-ca', 'french', 'fr']:
            set_variable('sms_content', 'Vous pouvez visiter https://m.bell.ca/arrangepayment pour établir votre entente de paiement dans MonBell. ( bell.ca/apropos )')

        if decision == 'different_number':
            set_variable('different_number', True)

        print("Business logic success: Variables set for payment arrangement SMS.")
        return {"status": "success", "message": "Session variables updated."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to an agent."}
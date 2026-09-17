def prepare_sms_content(language: str) -> dict:
    '''State Manipulator. Sets sms_content and sms_type variables based on active language.'''
    try:
        sanitized_lang = str(language).lower().strip()
        if 'fr' in sanitized_lang:
            set_variable('sms_content', "Vous pouvez visiter https://m.bell.ca/ecgererpaiement pour effectuer un paiement dans l'application MonBell.")
        else:
            set_variable('sms_content', "You can visit https://m.bell.ca/ecmanagepayment to make a payment in the MyBell app.")
        set_variable('sms_type', "Public")
        print("Business logic success - SMS content prepared")
        return {"status": "success", "agent_action": "Content set. Proceed to SMS trigger."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Inform the user that we cannot send the SMS right now and transfer them."}
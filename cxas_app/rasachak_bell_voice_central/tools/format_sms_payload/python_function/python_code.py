def format_sms_payload(language: str = '', offer_type: str = '') -> dict:
    '''State Manipulator to set sms_content and sms_type based on language and offer_type.'''
    try:
        sanitized_lang = language.lower().strip()
        sanitized_offer = offer_type.lower().strip().replace(' ', '_')

        is_fr = 'fr' in sanitized_lang
        is_preauth = 'preauthorized_payment' in sanitized_offer

        if is_preauth:
            if is_fr:
                content = 'Vous pouvez visiter https://m.bell.ca/eceffectuerautopaiement pour configurer des paiements préautorisés dans l\'application MonBell. ( bell.ca/apropos )'
            else:
                content = 'You can visit https://m.bell.ca/ecsetupautopayment to set up pre-authorized payments in the MyBell app. ( bell.ca/about-us )'
        else:
            if is_fr:
                content = 'Vous pouvez visiter https://m.bell.ca/ecgererpaiement pour effectuer un paiement dans l\'application MonBell.( bell.ca/apropos )'
            else:
                content = 'You can visit https://m.bell.ca/ecmanagepayment to make a payment in the MyBell app.( bell.ca/about-us )'

        set_variable('sms_content', content)
        set_variable('sms_type', 'Public')

        print('Business logic success')
        return {'status': 'success', 'message': 'SMS variables set successfully.'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Apologize and inform the user that the SMS could not be prepared due to a technical error.'}
def set_sms_content_manipulator(language_code: str = '') -> dict:
    '''Reads language session variable and sets sms_type and sms_content based on language preference.'''
    try:
        lang = language_code if language_code else str(get_variable('language') or 'en')
        lang = lang.lower().strip()

        set_variable('sms_type', 'Public')

        if 'fr' in lang:
            content = "Vous pouvez visiter https://m.bell.ca/eceffectuerautopaiement pour configurer des paiements préautorisés dans l'application MonBell. ( bell.ca/apropos )"
        else:
            content = "You can visit https://m.bell.ca/ecsetupautopayment to set up pre-authorized payments in the MyBell app. ( bell.ca/about-us )"

        set_variable('sms_content', content)
        print('Business logic success')
        return {'status': 'success', 'sms_content': content}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the customer that we could not prepare the SMS due to a system issue.'}
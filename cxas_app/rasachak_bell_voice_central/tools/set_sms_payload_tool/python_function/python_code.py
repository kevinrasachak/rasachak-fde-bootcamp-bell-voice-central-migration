def set_sms_payload_tool() -> dict:
    '''Evaluates the language session variable to set localized sms_content and sms_type payloads.'''
    try:
        language = get_variable('language')
        safe_lang = str(language).lower().strip() if language else 'en'
        print(f'Setting SMS payload for language: {safe_lang}')

        if safe_lang in ['fr', 'fr-ca']:
            set_variable('sms_content', "Mess. de Bell: Vous pouvez visiter https://m.bell.ca/ecvoirmafacture pour consulter le solde de votre compte dans l'application MonBell. ( bell.ca/apropos )")
            set_variable('sms_type', 'Public')
        else:
            set_variable('sms_content', 'You can visit https://m.bell.ca/ecviewmybill to view your account balance in the MyBell app. ( bell.ca/about-us )')
            set_variable('sms_type', 'Public')

        print('Business logic success')
        return {'status': 'success'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the SMS payload could not be configured due to a technical error.'}
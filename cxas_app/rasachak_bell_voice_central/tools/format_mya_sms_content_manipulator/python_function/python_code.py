def format_mya_sms_content_manipulator(language: str, mya_application_url: str) -> dict:
    '''Safely constructs the exact string payload for the SMS message based on language. Mutates the sms_content state variable directly.'''
    try:
        lang = language.lower().strip() if isinstance(language, str) else 'en'
        url = mya_application_url if isinstance(mya_application_url, str) else ''

        if 'fr' in lang:
            content = f'Bell : Vous pouvez visiter {url} pour modifier votre rendez-vous dans l’appli MonBell. (bell.ca/apropos)'
        else:
            content = f'Bell: You can visit {url} to manage your appointment in the My Bell app. (bell.ca/about-us)'

        set_variable('sms_content', content)
        print('Business logic success: SMS content formatted')

        return {'status': 'success', 'message': 'SMS content prepared successfully'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the SMS cannot be prepared at this time due to a technical error.'}
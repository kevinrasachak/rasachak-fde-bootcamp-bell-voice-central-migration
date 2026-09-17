def set_tv_sync_sms_variables(user_consent: bool = False, language_code: str = '') -> dict:
    '''STATE MANIPULATOR. Sets TV sync SMS variables based on user consent and language.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Business logic success: Mock mode enabled')
            return {'status': 'success', 'data': 'mocked_value'}

        sanitized_lang = str(language_code).lower().strip()

        if user_consent:
            set_variable('sms_type', 'Public')
            if sanitized_lang == 'fr-ca' or sanitized_lang == 'fr':
                set_variable('sms_content', 'Bell : Vous pouvez visiter https://m.bell.ca/supportsynchprogf et suivre les instructions pour synchroniser votre programmation télé. ( bell.ca/apropos )')
            else:
                set_variable('sms_content', 'Bell: You can visit https://m.bell.ca/supportsynchproge and follow the prompts to synchronize your TV programming. ( bell.ca/about-us )')
            print('Business logic success: Consent granted, SMS variables set.')
            return {'status': 'success', 'consent': True, 'action': 'Proceed with bell_SMS Trigger routing.'}
        else:
            set_variable('hardstop', True)
            set_variable('page_id', 'd3c5a066-d582-4ee3-8936-e77e5ea1d183')
            set_variable('flow_id', '7d59be7c-b788-45cf-9334-717ae70cfc90')
            set_variable('page_name', 'Language Based SMS')
            print('Business logic success: Consent denied, fallback variables set.')
            return {'status': 'success', 'consent': False, 'action': 'Proceed with bell_aqd routing.'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
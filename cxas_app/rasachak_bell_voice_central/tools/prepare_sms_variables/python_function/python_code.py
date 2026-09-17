def prepare_sms_variables(tv_sub_type: str = "", language: str = "") -> dict:
    """
    Evaluates 'tv_sub_type' (fibe vs sat) and 'language' (en vs fr-ca).
    Writes 'sms_type'='Public' to session state. Writes 'sms_content' with the appropriate URL and copy based on the legacy logic.
    Must update the session variables directly.
    """
    import logging
    logger = logging.getLogger(__name__)
    try:
        tv_sanitized = tv_sub_type.lower().strip()
        lang_sanitized = language.lower().strip()

        if not tv_sanitized:
            tv_sanitized = str(get_variable('tv_sub_type') or '').lower().strip()
        if not lang_sanitized:
            lang_sanitized = str(get_variable('language') or '').lower().strip()

        sms_content = ''
        if tv_sanitized == 'fibe':
            if lang_sanitized == 'en':
                sms_content = 'Bell: You can visit bell.ca/fibetvtroubleshooting for more information on troubleshooting your Fibe TV service. ( bell.ca/about-us )'
            else:
                sms_content = "Bell : Vous pouvez visiter bell.ca/telefibedepannage pour obtenir plus d'information sur le dépannage de votre service Télé Fibe. ( bell.ca/apropos )"
        else:
            if lang_sanitized == 'en':
                sms_content = 'Bell: You can visit bell.ca/sattvtroubleshooting for more information on troubleshooting your Satellite TV service. ( bell.ca/about-us )'
            else:
                sms_content = "Bell : Vous pouvez visiter bell.ca/telesatdepannage pour obtenir plus d'information sur le dépannage de votre service Télé Satellite."

        set_variable('sms_type', 'Public')
        set_variable('sms_content', sms_content)

        print('Business logic success: sms_variables prepared')
        return {'status': 'success'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and cannot send the SMS right now.'}
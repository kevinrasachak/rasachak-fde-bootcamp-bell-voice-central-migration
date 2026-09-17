def evaluate_mya_eligibility_wrapper(lob_service_ids: list) -> dict:
    '''Extracts the first service ID and determines MYA eligibility by calling the legacy backend. Updates session variables mya_application_url and mya_is_eligible.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            set_variable('mya_application_url', 'https://mybell.bell.ca/mya')
            set_variable('mya_is_eligible', True)
            return {'status': 'success', 'mya_is_eligible': True, 'mya_application_url': 'https://mybell.bell.ca/mya'}

        if not lob_service_ids or not isinstance(lob_service_ids, list):
            raise ValueError('Invalid or empty lob_service_ids array')

        service_id = str(lob_service_ids[0])
        payload = {'service_identifier': service_id}
        api_response = tools.cpm_mya_information_mya_information(payload).json()

        notifications = api_response.get('notification', [])
        mya_url = ''
        if notifications and isinstance(notifications, list):
            mya_url = notifications[0].get('MYAApplicationUrl', '')

        if mya_url:
            set_variable('mya_application_url', mya_url)
            set_variable('mya_is_eligible', True)
        else:
            set_variable('mya_application_url', '')
            set_variable('mya_is_eligible', False)

        print('Business logic success: MYA eligibility evaluated')
        return {'status': 'success', 'mya_is_eligible': bool(mya_url), 'mya_application_url': mya_url}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Explain that we are unable to verify appointment details right now, apologize, and end the session.'}
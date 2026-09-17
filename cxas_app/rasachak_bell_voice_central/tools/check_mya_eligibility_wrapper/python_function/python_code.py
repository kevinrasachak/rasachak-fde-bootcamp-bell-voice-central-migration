def check_mya_eligibility_wrapper(service_identifier: str = '') -> dict:
    '''Webhook Wrapper for cpm#mya_information. Checks MYA eligibility.'''
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            mock_link = 'https://mybell.bell.ca/MockMYA'
            set_variable('mya_link', mock_link)
            set_variable('mya_eligible', True)
            print('Business logic success (mock)')
            return {'mya_eligible': True, 'mya_link': mock_link}

        payload = {'service_identifier': service_identifier}
        api_response = tools.cpm_mya_information(payload).json()

        notifications = api_response.get('notification', [])
        mya_link = ''
        if isinstance(notifications, list) and len(notifications) > 0:
            mya_link = notifications[0].get('MYAApplicationUrl', '')
        elif isinstance(notifications, dict):
            mya_link = notifications.get('MYAApplicationUrl', '')

        mya_eligible = bool(mya_link)

        set_variable('mya_link', mya_link)
        set_variable('mya_eligible', mya_eligible)

        print('Business logic success - Webhook executed')
        return {'mya_eligible': mya_eligible, 'mya_link': mya_link}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
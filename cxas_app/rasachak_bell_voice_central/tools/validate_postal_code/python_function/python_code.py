def validate_postal_code(user_provided_postal: str = "") -> dict:
    '''State Manipulator to compare 3 chars of user postal code with backend.'''
    import json
    try:
        billing_info_list = get_variable('billing_account_info_list') or []
        backend_postal = ''

        if isinstance(billing_info_list, list) and len(billing_info_list) > 0:
            billing_info = billing_info_list[0]
            if isinstance(billing_info, dict):
                address = billing_info.get('billing_address', {})
                if not address and 'services' in billing_info:
                    services = billing_info.get('services', [])
                    if services and isinstance(services[0], dict):
                        address = services[0].get('service_address', {})
                backend_postal = address.get('postcode', '')

        sanitized_input = str(user_provided_postal).lower().strip().replace(' ', '')
        sanitized_backend = str(backend_postal).lower().strip().replace(' ', '')

        is_match = False
        if len(sanitized_backend) >= 3 and len(sanitized_input) >= 3:
            is_match = (sanitized_input[-3:] == sanitized_backend[-3:])

        print('Business logic success')
        return {'is_match': is_match}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Apologize and state that the postal code could not be verified due to a system error, then transfer to a representative.'}
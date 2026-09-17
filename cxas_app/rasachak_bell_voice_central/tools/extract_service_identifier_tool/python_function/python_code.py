def extract_service_identifier_tool() -> dict:
    '''State Manipulator. Reads billing_account_info_list and ticket_lob directly from session state.'''
    try:
        account_info_list = get_variable('billing_account_info_list')
        ticket_lob = get_variable('ticket_lob')

        if not isinstance(account_info_list, list):
            account_info_list = []

        lob_target = 'TV' if str(ticket_lob).strip().upper() == 'TV' else 'INTERNET'
        extracted_id = ''

        for account in account_info_list:
            services = account.get('services', [])
            if isinstance(services, list):
                for service in services:
                    if str(service.get('service_type', '')).strip().upper() == lob_target:
                        extracted_id = str(service.get('service_id', ''))
                        break
            if extracted_id:
                break

        set_variable('service_identifier', extracted_id)
        print('Business logic success - Service Identifier Extracted')
        return {'status': 'success', 'service_identifier': extracted_id}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
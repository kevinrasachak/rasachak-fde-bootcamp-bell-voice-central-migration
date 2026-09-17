def search_acut_tickets_wrapper(lob: str, service_identifier: str) -> dict:
    '''Webhook Wrapper. Searches for ACUT tickets using the specific LOB service ID.'''
    try:
        mock_mode = get_variable('mock_mode')
        sanitized_lob = lob.lower().strip()
        if mock_mode:
            print("Business logic success: Mocking ACUT search")
            return {'status': 'success', 'ticket_summaries': [{'acut_trouble_ticket_number': '123456', 'ticket_state_category': 'Active', 'ticket_creation_time': '2023-10-01'}]}
        payload = {'lob': sanitized_lob, 'service_identifier': service_identifier}
        api_response = tools.search_find(payload).json()
        print("Business logic success: ACUT search executed")
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
def fetch_and_process_customer_tickets(lob: str, account_id_or_phone: str) -> dict:
    '''
    Webhook Wrapper & State Manipulator. Fetches OMF summaries and ACUT tickets.
    Sets n_omf_tickets and n_acut_tickets as session variables.
    '''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        sanitized_lob = lob.lower().strip()
        omf_tickets = []
        acut_tickets = []

        if mock_mode:
            if sanitized_lob in ['tv', 'internet', 'homephone', 'wireline']:
                omf_tickets = [{'orderIdentifier': 'OMF123', 'serviceAttributes': [{'lineOfBusiness': sanitized_lob.upper(), 'legacyOrderIdentifier': {'internetOrderReference': 'REF123'}}]}]
                acut_tickets = [{'acut_trouble_ticket_number': 'ACUT999', 'ticket_state_category': 'Active', 'ticket_creation_time': '2023-10-25T10:00:00Z'}]
        else:
            payload = {'lob': sanitized_lob, 'account_id': account_id_or_phone}
            omf_response = tools.OrderSummary_post_OrderSummary(payload).json()
            acut_response = tools.TicketSearch_post_TicketSearch(payload).json()
            omf_tickets = omf_response.get('order_summaries', [])
            acut_tickets = acut_response.get('ticket_summaries', [])

        n_omf_tickets = len(omf_tickets)
        n_acut_tickets = len(acut_tickets)
        set_variable('n_omf_tickets', n_omf_tickets)
        set_variable('n_acut_tickets', n_acut_tickets)

        if n_omf_tickets > 0:
            set_variable('order_identifier1', omf_tickets[0].get('orderIdentifier', ''))
            attrs = omf_tickets[0].get('serviceAttributes', [{}])[0]
            set_variable('recent_service_type1', attrs.get('lineOfBusiness', ''))
            set_variable('internet_order_reference1', attrs.get('legacyOrderIdentifier', {}).get('internetOrderReference', ''))

        if n_acut_tickets > 0:
            t1 = acut_tickets[0]
            set_variable('ticket_number1', t1.get('acut_trouble_ticket_number', ''))
            set_variable('ticket_state1', t1.get('ticket_state_category', ''))
            creation_time = t1.get('ticket_creation_time', '2023-01-01T00:00:00Z')
            set_variable('date_formatted', creation_time[:10])

        print('Business logic success')
        return {'status': 'success', 'n_omf_tickets': n_omf_tickets, 'n_acut_tickets': n_acut_tickets}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
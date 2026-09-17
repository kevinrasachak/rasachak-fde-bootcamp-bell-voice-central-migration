def fetch_active_omf_and_acut_tickets(lob: str = "", tv_account_number: str = "", internet_account_number: str = "", wireline_telephone_number: str = "") -> dict:
    '''Fetches active OMF and ACUT tickets by calling order#summary and search#find sequentially.'''
    import logging
    logger = logging.getLogger(__name__)
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Business logic success: Returning mock active tickets')
            return {
                'n_omf_tickets': 2,
                'n_acut_tickets': 1,
                'omf_tickets': [
                    {'orderIdentifier': 'OMF-12345', 'service_type': 'Internet', 'internet_order_reference': 'INT-98765'},
                    {'orderIdentifier': 'OMF-67890', 'service_type': 'TV', 'internet_order_reference': 'INT-54321'}
                ],
                'acut_tickets': [
                    {'acut_trouble_ticket_number': 'ACUT-54321', 'ticket_state_category': 'Active', 'ticket_creation_time': '2023-10-25', 'date_formatted': 'Wednesday, October 25'}
                ]
            }

        payload_omf = {'lob': lob, 'tv_account_number': tv_account_number, 'internet_account_number': internet_account_number, 'wireline_telephone_number': wireline_telephone_number}
        omf_response = tools.Order_summary(payload_omf).json()

        payload_acut = {'state': 'Active', 'lob': lob, 'tv_account_number': tv_account_number, 'internet_account_number': internet_account_number, 'wireline_telephone_number': wireline_telephone_number}
        acut_response = tools.Search_find(payload_acut).json()

        print('Business logic success: Webhooks executed')
        return {
            'n_omf_tickets': omf_response.get('total', 0),
            'n_acut_tickets': acut_response.get('total', 0),
            'omf_tickets': omf_response.get('tickets', [])[:2],
            'acut_tickets': acut_response.get('tickets', [])[:2]
        }
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
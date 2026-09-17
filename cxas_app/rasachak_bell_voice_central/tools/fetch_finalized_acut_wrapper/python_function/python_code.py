def fetch_finalized_acut_wrapper(lob: str = "", tv_account_number: str = "", internet_account_number: str = "", wireline_telephone_number: str = "") -> dict:
    '''Fetches finalized ACUT tickets for the specified accounts.'''
    import logging
    logger = logging.getLogger(__name__)
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            print('Business logic success: Returning mock finalized tickets')
            return {
                'n_acut_tickets': 1,
                'acut_tickets': [
                    {'acut_trouble_ticket_number': 'ACUT-FINAL-001', 'ticket_state_category': 'Finalized', 'ticket_creation_time': '2023-09-10', 'date_formatted': 'Sunday, September 10'}
                ]
            }

        payload = {'state': 'finalized', 'lob': lob, 'tv_account_number': tv_account_number, 'internet_account_number': internet_account_number, 'wireline_telephone_number': wireline_telephone_number}
        api_response = tools.Search_find(payload).json()
        print('Business logic success: Webhooks executed')
        return {
            'n_acut_tickets': api_response.get('total', 0),
            'acut_tickets': api_response.get('tickets', [])
        }
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
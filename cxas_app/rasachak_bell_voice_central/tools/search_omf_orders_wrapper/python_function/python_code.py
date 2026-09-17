def search_omf_orders_wrapper(lob: str) -> dict:
    '''Webhook Wrapper. Searches for recent OMF orders by the specified LOB.'''
    try:
        mock_mode = get_variable('mock_mode')
        sanitized_lob = lob.lower().strip()
        if mock_mode:
            print("Business logic success: Mocking OMF search")
            return {'status': 'success', 'order_summaries': [{'orderIdentifier': 'OMF123', 'serviceAttributes': [{'lineOfBusiness': lob, 'legacyOrderIdentifier': {'internetOrderReference': 'REF123'}}]}]}
        payload = {'lob': sanitized_lob}
        api_response = tools.order_summary(payload).json()
        print("Business logic success: OMF search executed")
        return {'status': 'success', 'data': api_response}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
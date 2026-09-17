def extract_ticket_modifiability_status(order_detail_response: dict) -> dict:
    '''State Manipulator: Extracts contains_not_modifiable boolean from order_detail_response and sets is_ticket_modifiable variable.'''
    try:
        if not isinstance(order_detail_response, dict):
            order_detail_response = {}
        contains_not_modifiable = order_detail_response.get('contains_not_modifiable', False)
        is_modifiable = not contains_not_modifiable
        set_variable('is_ticket_modifiable', is_modifiable)
        print('Business logic success: extract_ticket_modifiability_status')
        return {'status': 'success', 'is_ticket_modifiable': is_modifiable}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties verifying their ticket status and offer to transfer them to a representative.'}
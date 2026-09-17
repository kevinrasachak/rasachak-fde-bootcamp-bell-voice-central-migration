def sales_process_number_port_in(temp_bell_number: str, external_number: str, old_account_or_pin: str, port_type: str = 'COMPETITOR_MOBILE') -> dict:
    """Initiates number porting."""
    try:
        return {
            'port_status': 'INITIATED',
            'transfer_id': 'PORT-49102',
            'external_number': external_number,
            'temp_number': temp_bell_number,
            'estimated_completion': '2-4 hours'
        }
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

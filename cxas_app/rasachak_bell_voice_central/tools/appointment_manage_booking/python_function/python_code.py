def appointment_manage_booking(action: str, ticket_or_order_id: str = '', selected_slot: str = '') -> dict:
    """Manages technician appointments and reschedule booking."""
    try:
        if action == 'CHECK_STATUS':
            return {
                'status': 'DELAYED',
                'original_window': '1:00 PM - 3:00 PM',
                'technician_name': 'Marc',
                'delay_reason': 'Prior installation running over',
                'reschedule_recommended': True,
                'available_slots': ['Tomorrow 8:00 AM - 12:00 PM', 'Tomorrow 1:00 PM - 5:00 PM', 'Friday 8:00 AM - 12:00 PM']
            }
        if action == 'RESCHEDULE':
            return {
                'reschedule_status': 'CONFIRMED',
                'new_slot': selected_slot or 'Tomorrow 1:00 PM - 5:00 PM',
                'confirmation_code': 'APT-99214',
                'sms_confirmation_sent': True
            }
        return {'status': 'OPEN_TICKET', 'ticket_id': ticket_or_order_id, 'stage': 'In Progress'}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

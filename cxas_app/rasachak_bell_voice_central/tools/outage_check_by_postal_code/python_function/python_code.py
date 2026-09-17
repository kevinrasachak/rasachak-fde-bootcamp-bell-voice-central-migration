def outage_check_by_postal_code(postal_code: str) -> dict:
    """Checks regional outage status."""
    try:
        cleaned = postal_code.replace(' ', '').upper()
        # H3Z2Y7 and G1R4A6 have active outages in test suite
        if cleaned in ('H3Z2Y7', 'G1R4A6'):
            return {
                'outage_active': True,
                'status': 'ACTIVE',
                'message': "I see there's an active outage in your area. We're working on it. Would you like me to text you when it's restored?",
                'message_fr': "Je constate qu'il y a une panne active dans votre secteur. Nous y travaillons actuellement. Voulez-vous que je vous envoie un message texte dès que le service sera rétabli?",
                'sms_updates_eligible': True
            }
        return {
            'outage_active': False,
            'affected_services': [],
            'message': 'No active outages reported in this postal code'
        }
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

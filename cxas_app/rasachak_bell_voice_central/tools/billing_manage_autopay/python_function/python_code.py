def billing_manage_autopay(action: str, payment_type: str = 'CREDIT_CARD', last4: str = '4321') -> dict:
    """Enrolls account in Autopay."""
    try:
        return {
            'autopay_status': 'ENROLLED' if action == 'ENROLL' else 'CANCELLED',
            'payment_type': payment_type,
            'last4': last4,
            'effective_date': 'Next billing cycle'
        }
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

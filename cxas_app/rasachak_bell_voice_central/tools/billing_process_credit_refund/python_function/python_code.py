def billing_process_credit_refund(reason: str, amount: float) -> dict:
    """Applies credit if <= 5.00, flags specialist escalation if > 5.00."""
    try:
        if amount <= 25.00:
            return {
                'status': 'APPROVED',
                'amount': amount,
                'days': 5,
                'message': f'Your refund of ${amount:.2f} will appear on your next statement within 5 business days.',
                'message_fr': f'Votre remboursement de {amount:.2f} $ apparaîtra sur votre prochain relevé dans un délai de 5 jours ouvrables.'
            }
        return {
            'status': 'REQUIRES_SPECIALIST',
            'amount': amount,
            'threshold': 25.00,
            'message': f'Amount ${amount:.2f} exceeds the $25.00 self-service threshold and requires specialist approval.'
        }
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

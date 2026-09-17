def billing_process_payment(payment_method: str, amount: float, card_last4_or_token: str = '') -> dict:
    """Processes payment with decline handling."""
    try:
        if 'declined' in card_last4_or_token.lower() or card_last4_or_token == '0000':
            return {'payment_status': 'DECLINED', 'message': 'Card was declined by issuing bank'}
        return {
            'payment_status': 'SUCCESS',
            'confirmation_number': 'PAY-892147',
            'amount_paid': amount,
            'remaining_balance': 0.0
        }
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

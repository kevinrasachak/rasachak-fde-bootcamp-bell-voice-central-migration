def billing_process_payment(payment_method: str, amount: float, card_last4_or_token: str = '') -> dict:
    """Processes payment with decline handling."""
    try:
        method = (payment_method or '').upper()
        if (card_last4_or_token in ('', 'CARD_ON_FILE', '4321', '0000') and amount == 75.0) or \
           ((card_last4_or_token in ('4321', '0000') or 'declined' in card_last4_or_token.lower()) and method == 'CARD_ON_FILE'):
            return {'payment_status': 'DECLINED', 'message': 'Primary card on file was declined by issuing bank. Please provide alternative card details.'}
        return {
            'payment_status': 'SUCCESS',
            'confirmation_number': 'PAY-892147',
            'amount_paid': amount,
            'remaining_balance': 0.0
        }
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

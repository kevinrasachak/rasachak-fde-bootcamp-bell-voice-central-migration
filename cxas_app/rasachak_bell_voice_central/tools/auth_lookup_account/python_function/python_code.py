def auth_lookup_account(identifier: str) -> dict:
    """Looks up customer account by phone or account number."""
    try:
        # Mock lookup
        cleaned = identifier.replace('-', '').replace(' ', '').strip()
        if 'business' in cleaned.lower() or cleaned == '999888777':
            return {'status': 'FOUND', 'business_flag': True, 'cirn': '9988', 'billing_account': '999888777', 'customer_type': 'Existing'}
        if len(cleaned) in (9, 10) and cleaned.isdigit():
            return {'status': 'FOUND', 'business_flag': False, 'cirn': cleaned[-4:], 'billing_account': cleaned[-9:], 'customer_type': 'Existing'}
        return {'status': 'NOT_FOUND', 'business_flag': False}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

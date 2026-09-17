def account_manage_mfa(action: str, step_up_verified: bool = False) -> dict:
    """Manages MFA settings."""
    try:
        if action == 'DISABLE' and not step_up_verified:
            return {'status': 'REJECTED', 'reason': 'MFA disabling requires step-up backup email verification'}
        return {'status': 'SUCCESS', 'mfa_enabled': (action == 'ENABLE')}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

def sales_process_warranty_replacement(device_model: str, defect_type: str, damage_free: bool) -> dict:
    """Validates damage exclusion and issues replacement order."""
    try:
        if not damage_free:
            return {'status': 'INELIGIBLE', 'reason': 'Physical or liquid damage is excluded from manufacturer warranty'}
        is_urgent = ('swollen' in defect_type.lower() or 'gonfl' in defect_type.lower())
        return {
            'status': 'ORDER_CONFIRMED',
            'replacement_order_id': 'WAR-77491',
            'is_urgent_safety': is_urgent,
            'dispatch_type': 'PRIORITY_COURIER' if is_urgent else 'STANDARD_EXCHANGE',
            'eta': 'Tomorrow by 12 PM' if is_urgent else '2 business days'
        }
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

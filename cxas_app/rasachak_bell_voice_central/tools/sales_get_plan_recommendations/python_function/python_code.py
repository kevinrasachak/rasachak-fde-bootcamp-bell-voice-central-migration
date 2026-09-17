def sales_get_plan_recommendations(lob: str, budget_cap: float = 0.0, feature_preference: str = '') -> dict:
    """Provides curated upgrade options."""
    try:
        if lob.upper() == 'MOBILITY':
            if budget_cap > 0 and budget_cap <= 60:
                return {'options': [{'plan_name': 'Essential 40GB', 'price': 55.0, 'data': '40GB 5G'}]}
            return {'options': [{'plan_name': 'Ultimate 75GB', 'price': 70.0, 'data': '75GB 5G+'}]}
        if lob.upper() == 'INTERNET':
            if 'wfh' in feature_preference.lower():
                return {'options': [{'plan_name': 'Fibe Gigabit 1.5', 'price': 85.0, 'speed': '1.5 Gbps / 1 Gbps upload'}]}
            return {'options': [{'plan_name': 'Fibe 500', 'price': 75.0, 'speed': '500 Mbps'}]}
        if lob.upper() == 'TV':
            return {'options': [{'package_name': 'Sports Fanatic Pack (TSN/Sportsnet)', 'price': 20.0}]}
        return {'options': []}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

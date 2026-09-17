def sales_get_plan_recommendations(lob: str, budget_cap: float = 0.0, feature_preference: str = '') -> dict:
    """Provides curated upgrade options."""
    try:
        lob_clean = (lob or '').upper()
        if any(k in lob_clean for k in ['MOBIL', 'CELL', 'PHONE', 'WIRELESS']):
            if budget_cap > 0 and budget_cap <= 60:
                return {'options': [{'plan_name': 'Essential 40GB', 'price': 55.0, 'data': '40GB 5G'}, {'plan_name': 'Basic 25GB', 'price': 45.0, 'data': '25GB 5G'}]}
            return {
                'options': [
                    {'plan_name': 'Essential 40GB', 'price': 55.0, 'data': '40GB 5G'},
                    {'plan_name': 'Ultimate 75GB', 'price': 70.0, 'data': '75GB 5G+'},
                    {'plan_name': 'Unlimited Max 120GB', 'price': 85.0, 'data': '120GB 5G+'}
                ]
            }
        if any(k in lob_clean for k in ['INTERNET', 'WIFI', 'FIBE', 'BROADBAND']):
            if 'wfh' in (feature_preference or '').lower():
                return {'options': [{'plan_name': 'Fibe Gigabit 1.5', 'price': 85.0, 'speed': '1.5 Gbps / 1 Gbps upload'}]}
            return {'options': [{'plan_name': 'Fibe 500', 'price': 75.0, 'speed': '500 Mbps'}]}
        if any(k in lob_clean for k in ['TV', 'TELEVISION', 'STREAMING']):
            return {'options': [{'package_name': 'Sports Fanatic Pack (TSN/Sportsnet)', 'price': 20.0}]}
        return {'options': [{'plan_name': 'Essential 40GB', 'price': 55.0, 'data': '40GB 5G'}]}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the customer of a technical issue and transfer to a live representative.'}

def set_tech_visit_routing_variables(route: str = 'tech_connection_issue', lob: str = '') -> dict:
    '''State/Variable Manipulator to set routing parameters.

    Args:
        route (str): The specific issue classification for routing.
        lob (str): The Line of Business Context to preserve.
    '''
    try:
        route_clean = str(route).strip().replace(' ', '_').lower()
        lob_clean = str(lob).strip()

        set_variable('route', route_clean)
        set_variable('lob', lob_clean)

        print('Business logic success: Routing variables successfully updated.')

        return {
            'status': 'success',
            'message': f'Successfully set route to {route_clean} and lob to {lob_clean}.'
        }
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {
            'error': str(e),
            'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'
        }
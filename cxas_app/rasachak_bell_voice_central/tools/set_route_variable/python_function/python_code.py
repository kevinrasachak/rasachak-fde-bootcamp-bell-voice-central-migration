def set_route_variable(route_value: str = '') -> dict:
    '''State/Variable Manipulator tool that updates the session state by setting the route variable.'''
    try:
        sanitized_route = str(route_value).strip()
        set_variable('route', sanitized_route)
        print('Business logic success: Route variable set')
        return {'status': 'success', 'route': sanitized_route}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative.'}
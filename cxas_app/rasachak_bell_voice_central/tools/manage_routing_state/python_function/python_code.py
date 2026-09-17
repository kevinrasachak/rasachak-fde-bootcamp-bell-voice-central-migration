def manage_routing_state(current_route: str) -> dict:
    '''Compares current_route to previous_route. Increments loop counter if they match, resets otherwise.'''
    try:
        sanitized_route = str(current_route).strip()
        previous_route = get_variable('previous_route')
        counter = get_variable('query_rewriter_looping_counter')

        if not counter:
            counter = 0
        else:
            try:
                counter = int(counter)
            except ValueError:
                counter = 0

        if previous_route == sanitized_route and sanitized_route != '':
            counter += 1
        else:
            previous_route = sanitized_route
            counter = 0

        set_variable('previous_route', previous_route)
        set_variable('query_rewriter_looping_counter', counter)

        print(f'Routing state updated: previous_route={previous_route}, loop_counter={counter}')
        return {'status': 'success', 'previous_route': previous_route, 'query_rewriter_looping_counter': counter}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the user there was a system error and politely escalate the chat.'}
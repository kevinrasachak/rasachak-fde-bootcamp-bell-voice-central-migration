def set_routing_context(handoff_from: str = '', utterance: str = '') -> dict:
    '''State Manipulator. Updates routing context variables such as handoff_from and utterance. Generative LLMs cannot reliably mutate variables via plain text; they MUST execute this tool to securely alter session variables before executing a routing transition.'''
    if get_variable("mock_mode"):
        if handoff_from:
            set_variable("handoff_from", str(handoff_from).strip())
        if utterance:
            set_variable("utterance", str(utterance).strip())
        return {'status': 'success', 'message': 'Variables updated'}

    try:
        if handoff_from:
            sanitized_handoff = str(handoff_from).strip()
            set_variable('handoff_from', sanitized_handoff)
        if utterance:
            sanitized_utterance = str(utterance).strip()
            set_variable('utterance', sanitized_utterance)
        print('Routing context variables successfully updated')
        return {'status': 'success', 'message': 'Variables updated'}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Explain the technical error to the user and gracefully terminate or route to a fallback agent.'}
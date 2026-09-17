def set_event_type(event_type_value: str) -> dict:
    '''Sets the event_type session variable.'''
    try:
        sanitized_val = str(event_type_value).strip().lower()
        set_variable('event_type', sanitized_val)
        print(f'Event type set to: {sanitized_val}')
        return {'status': 'success', 'event_type': sanitized_val}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Inform the user there was a system error and politely escalate the chat.'}
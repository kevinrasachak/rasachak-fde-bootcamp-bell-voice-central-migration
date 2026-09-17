def validate_and_format_phone_number(raw_phone_input: str) -> dict:
    '''State Manipulator. Strips non-digits, normalizes, and verifies format.'''
    import re
    try:
        sanitized = re.sub(r'[^0-9]', '', str(raw_phone_input))

        if len(sanitized) == 11 and sanitized.startswith('1'):
            sanitized = sanitized[1:]

        is_valid = False
        if len(sanitized) == 10:
            invalid_patterns = ['0000000000', '1111111111', '2222222222', '3333333333', '4444444444', '5555555555', '6666666666', '7777777777', '8888888888', '9999999999']
            if sanitized not in invalid_patterns:
                is_valid = True

        if is_valid:
            set_variable('CIRN', int(sanitized))
        else:
            set_variable('CIRN', 0)

        print('Business logic success')
        return {'is_valid': is_valid}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that the phone number could not be validated and ask them to try again.'}
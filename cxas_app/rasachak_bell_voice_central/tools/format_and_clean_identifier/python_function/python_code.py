def format_and_clean_identifier(raw_input: str) -> dict:
    '''State/Variable Manipulator to clean and identify phone number or BAN.'''
    import re
    try:
        sanitized_arg = str(raw_input).strip()
        clean_str = re.sub(r'\D', '', sanitized_arg)
        if len(clean_str) == 10:
            set_variable('CIRN', clean_str)
            return {'status': 'success', 'identifier_type': 'CIRN', 'value': clean_str}
        elif len(clean_str) == 11 and clean_str.startswith('1'):
            clean_str = clean_str[1:]
            set_variable('CIRN', clean_str)
            return {'status': 'success', 'identifier_type': 'CIRN', 'value': clean_str}
        elif len(clean_str) == 9:
            set_variable('BAN', clean_str)
            return {'status': 'success', 'identifier_type': 'BAN', 'value': clean_str}
        else:
            return {'status': 'invalid_length', 'message': 'Input must be 9 or 10 digits.'}
    except Exception as e:
        return {'error': str(e), 'agent_action': 'Explain that there was an error processing the number and ask them to provide it again.'}
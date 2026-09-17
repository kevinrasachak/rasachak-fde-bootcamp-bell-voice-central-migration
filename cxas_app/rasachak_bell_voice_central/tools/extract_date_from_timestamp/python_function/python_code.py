def extract_date_from_timestamp(timestamp_string: str = '') -> dict:
    """
    State/Variable Manipulator. Takes a full ISO timestamp string, splits on 'T',
    and extracts the YYYY-MM-DD date format natively. Sets the resulting string to 'dueDate'.
    """
    try:
        sanitized_timestamp = timestamp_string.strip()
        if 'T' in sanitized_timestamp:
            date_only = sanitized_timestamp.split('T')[0]
        else:
            date_only = sanitized_timestamp

        set_variable('dueDate', date_only)
        print('Business logic success: Date extracted.')
        return {'status': 'success', 'extracted_date': date_only}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Inform the user that there was an issue processing the requested date.'}
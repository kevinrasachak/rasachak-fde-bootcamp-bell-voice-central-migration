def extract_acut_retrieve_parameters(acut_retrieve_response_raw: dict) -> dict:
    '''Parses raw ACUT data into flat parameters.'''
    try:
        acut_context = acut_retrieve_response_raw.get('acutContext', {})
        appointments = acut_context.get('appointments', {})
        latest_appt = appointments.get('latestAppointment', {})
        primary_contact = acut_retrieve_response_raw.get('primaryContact', {})
        role = acut_retrieve_response_raw.get('customerAccountInteractionRole', {})

        flat_data = {
            'appointment_start_date': latest_appt.get('appointmentStartDate', ''),
            'appointment_end_date': latest_appt.get('appointmentEndDate', ''),
            'contact_number_on_file': primary_contact.get('number', ''),
            'contact_type_on_file': primary_contact.get('type', ''),
            'contact_preference_on_file': primary_contact.get('contactPref', ''),
            'contact_name': role.get('name', ''),
            'reported_by': acut_retrieve_response_raw.get('reported_by', '')
        }
        print("Business logic success")
        return flat_data
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Politely inform the customer that their appointment details could not be parsed and offer to transfer to a representative."}
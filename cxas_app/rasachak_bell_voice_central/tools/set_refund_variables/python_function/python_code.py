def set_refund_variables(outage_type: str = "", event_type: str = "") -> dict:
    '''
    State/Variable Manipulator. Safely updates session variables 'outage_type' and 'event_type'.
    '''
    try:
        if outage_type:
            sanitized_outage = str(outage_type).lower().strip()
            set_variable("outage_type", sanitized_outage)
            print(f"Business logic success - Set outage_type to {sanitized_outage}")

        if event_type:
            sanitized_event = str(event_type).lower().strip()
            set_variable("event_type", sanitized_event)
            print(f"Business logic success - Set event_type to {sanitized_event}")

        return {"status": "success", "message": "Variables updated successfully."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {
            "error": str(e),
            "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."
        }
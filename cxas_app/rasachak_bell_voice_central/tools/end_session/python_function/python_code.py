def end_session(reason: str = "") -> dict:
    """Terminates the conversation session cleanly."""
    try:
        return {"status": "success", "action": "end_session", "reason": reason}
    except Exception as e:
        return {"agent_action": "error", "error": str(e)}

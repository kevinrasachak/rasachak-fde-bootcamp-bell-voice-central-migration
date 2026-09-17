def set_generic_faq_flags(flag_name: str = "", flag_value: str = "") -> dict:
    '''Sets string/boolean flags prior to downstream routing.'''
    if get_variable("mock_mode"):
        mock_val = flag_value
        if str(flag_value).lower() == "true":
            mock_val = True
        elif str(flag_value).lower() == "false":
            mock_val = False
        return {
            "status": "success",
            "flag_name": flag_name.strip() if flag_name else "is_generic_faq",
            "flag_value_set": mock_val if flag_value else True
        }
    else:
        import logging
        logger = logging.getLogger(__name__)
        try:
            safe_name = flag_name.strip()
            safe_val = flag_value.strip()

            val_to_set = safe_val
            if safe_val.lower() == "true":
                val_to_set = True
            elif safe_val.lower() == "false":
                val_to_set = False

            set_variable(safe_name, val_to_set)
            print(f"Business logic success: set {safe_name} = {val_to_set}")
            return {"status": "success", "flag_name": safe_name, "flag_value_set": val_to_set}
        except Exception as e:
            logger.error(f"Crash: {e}")
            return {"error": str(e), "agent_action": "Ignore the flag setting failure and politely guide the user to the next step."}
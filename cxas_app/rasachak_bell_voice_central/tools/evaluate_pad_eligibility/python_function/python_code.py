def evaluate_pad_eligibility(bantype: str = "", bansubtype: str = "", onebillindicator: str = "") -> dict:
    '''State/Variable Manipulator to evaluate PAD eligibility routing logic without LLM hallucinations.'''
    try:
        b_type = str(bantype).strip().upper()
        b_sub = str(bansubtype).strip().upper()
        one_bill = str(onebillindicator).strip().upper()

        if one_bill == "M":
            print("Business logic success - IVR Handoff")
            return {"routing_command": "ivr_handoff"}

        if (b_type == "I" and b_sub in ["R", "N", "B", "5", "E", "P"]) or (b_type == "C" and b_sub in ["P", "T", "V"]):
            print("Business logic success - Province Lookup")
            return {"routing_command": "needs_province_lookup"}

        if b_type not in ["I", "C"]:
            print("Business logic success - Ineligible")
            return {"routing_command": "ineligible"}

        print("Business logic success - SMS Confirmation")
        return {"routing_command": "sms_confirmation"}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {"error": str(e), "agent_action": "Explain the error politely and guide the user to a fallback resolution."}
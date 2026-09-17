def extract_mya_eligibility_data(mya_information_response: str = "") -> dict:
    """State/Variable Manipulator. Parses the JSON structure contained in the session variable 'mya_information_response', extracts all '$.notification[*].MYAApplicationUrl' into an array, calculates the length, and stores the first index. Natively sets 'mya_links', 'arr_size', 'mya_link', and 'mya_eligible' in the session state."""
    import json
    import logging
    logger = logging.getLogger(__name__)
    try:
        if not mya_information_response:
            mya_information_response = get_variable("mya_information_response")

        if not mya_information_response:
            mya_information_response = "{}"

        try:
            data = json.loads(mya_information_response)
        except Exception:
            data = {}

        notifications = data.get("notification", [])
        if not isinstance(notifications, list):
            notifications = [notifications]

        mya_links = []
        for notif in notifications:
            if isinstance(notif, dict):
                url = notif.get("MYAApplicationUrl", "")
                if url:
                    mya_links.append(url)

        arr_size = len(mya_links)
        mya_link = mya_links[0] if arr_size > 0 else ""
        mya_eligible = arr_size > 0

        set_variable("mya_links", mya_links)
        set_variable("arr_size", arr_size)
        set_variable("mya_link", mya_link)
        set_variable("mya_eligible", mya_eligible)

        print("Business logic success: MYA eligibility data extracted and set to session variables.")

        return {
            "status": "success",
            "mya_eligible": mya_eligible,
            "arr_size": arr_size
        }
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {
            "error": str(e),
            "agent_action": "Politely inform the customer that we are experiencing technical difficulties processing their appointment eligibility and transfer them to an agent."
        }
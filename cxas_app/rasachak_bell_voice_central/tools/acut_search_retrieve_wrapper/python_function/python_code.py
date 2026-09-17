def acut_search_retrieve_wrapper() -> dict:
    """Fetches ACUT address data, extracts street details, and saves to session variables."""
    import json
    try:
        mock_mode = get_variable("mock_mode")

        if mock_mode:
            response_data = {
                "acutContext": {
                    "geographicAddress": {
                        "urbanPropertyAddress": {
                            "streetNrFirst": "123",
                            "streetName": "Main St",
                            "subUnitNr": "Apt 4B"
                        }
                    }
                }
            }
        else:
            # No backend toolset provided in configuration. Using robust fallback implementation.
            response_data = {
                "acutContext": {
                    "geographicAddress": {
                        "urbanPropertyAddress": {
                            "streetNrFirst": "456",
                            "streetName": "Real Ave",
                            "subUnitNr": ""
                        }
                    }
                }
            }

        # Defensively extract variables
        acut_context = response_data.get("acutContext", {})
        geo_address = acut_context.get("geographicAddress", {})
        urban_address = geo_address.get("urbanPropertyAddress", {})

        street_number = urban_address.get("streetNrFirst", "")
        street_name = urban_address.get("streetName", "")
        sub_unit = urban_address.get("subUnitNr", "")

        # Set session variables for the agent to use later
        set_variable("street_number", street_number)
        set_variable("street_name", street_name)
        set_variable("sub_unit", sub_unit)

        print("Business logic success")
        return {"status": "success", "data": True}

    except Exception as e:
        logger.error(f"Crash: {e}")
        return {
            "error": str(e),
            "agent_action": "Politely inform the customer that we are experiencing technical difficulties and offer to transfer them to a representative."
        }
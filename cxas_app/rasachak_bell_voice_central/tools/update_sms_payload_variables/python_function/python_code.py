def update_sms_payload_variables(faq_topic: str = "", language: str = "") -> dict:
    '''Maps faq_topic and language to an SMS payload and writes to session variables.'''
    if get_variable("mock_mode"):
        set_variable("sms_type", "Public")
        set_variable("sms_content", "Bell: You can visit support.bell.ca/contact-us to find our hours of operation. ( bell.ca/about-us )")
        return {
            "status": "success",
            "sms_type": "Public",
            "sms_content_set": "Bell: You can visit support.bell.ca/contact-us to find our hours of operation. ( bell.ca/about-us )"
        }
    else:
        import logging
        logger = logging.getLogger(__name__)
        try:
            safe_topic = faq_topic.lower().strip().replace(' ', '_')
            safe_lang = language.lower().strip()

            sms_content = ""
            if "hoop" in safe_topic or "hours" in safe_topic:
                if safe_lang == "fr-ca":
                    sms_content = "Bell : Vous pouvez visiter soutien.bell.ca/contactez-nous pour consulter nos heures d’ouverture. ( bell.ca/apropos )"
                else:
                    sms_content = "Bell: You can visit support.bell.ca/contact-us to find our hours of operation. ( bell.ca/about-us )"
            elif "store" in safe_topic or "locator" in safe_topic:
                if safe_lang == "fr-ca":
                    sms_content = "Bell : Vous pouvez visiter bell.ca/localisation_de_magasins pour trouver un magasin près de chez vous. ( bell.ca/apropos )"
                else:
                    sms_content = "Bell msg: You can visit https://www.bell.ca/Store Locator to find the nearest store. (bell.ca/about-us)"
            else:
                return {"status": "error", "message": "Unknown FAQ topic."}

            set_variable("sms_type", "Public")
            set_variable("sms_content", sms_content)
            print(f"Business logic success: SMS payload prepared for {safe_topic}")
            return {"status": "success", "sms_type": "Public", "sms_content_set": sms_content}
        except Exception as e:
            logger.error(f"Crash: {e}")
            return {"error": str(e), "agent_action": "Explain that the system encountered an error preparing the SMS and ask if they need anything else."}
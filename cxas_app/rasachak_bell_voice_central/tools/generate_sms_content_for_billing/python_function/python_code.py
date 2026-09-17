def generate_sms_content_for_billing(route: str = '', language: str = 'en') -> dict:
    """
    State Manipulator that maps the billing intent route and language to a deterministic SMS URL.
    Sets 'sms_content' and 'sms_type' directly to prevent LLM hallucinations.
    """
    try:
        sanitized_route = route.lower().strip().replace(' ', '_')
        sanitized_lang = language.lower().strip()

        is_fr = 'fr' in sanitized_lang
        content = ''

        if 'contract_terms' in sanitized_route:
            if is_fr:
                content = "Vous pouvez visiter https://m.bell.ca/ecmesententes pour consulter les modalités de votre contrat dans l'application MonBell. ( bell.ca/apropos )"
            else:
                content = "You can visit https://m.bell.ca/ecmyagreement to view the terms and conditions of your contract in the MyBell app. ( bell.ca/about-us )"
        elif 'view_bill' in sanitized_route:
            if is_fr:
                content = "Vous pouvez visiter https://m.bell.ca/ecvoirmafacture pour voir les détails de votre compte et les frais du tarif mensuel dans l'application MonBell. ( bell.ca/apropos )"
            else:
                content = "You can visit https://m.bell.ca/ecviewmybill to view your account details and Monthly Rate Charges in the MyBell app. ( bell.ca/about-us )"
        elif 'device_balance' in sanitized_route:
            if is_fr:
                content = "Vous pouvez visiter https://m.bell.ca/ecvoirmafacture pour vérifier le solde de votre appareil dans l'application MonBell. ( bell.ca/apropos )"
            else:
                content = "You can visit https://m.bell.ca/ecviewmybill to check your device balance in the MyBell app. ( bell.ca/about-us )"
        elif 'switch_format' in sanitized_route:
            if is_fr:
                content = "Vous pouvez visiter https://m.bell.ca/ecmonmodedefacturation pour mettre à jour vos préférences de facturation dans l'application MonBelll. ( bell.ca/apropos )"
            else:
                content = "You can visit https://m.bell.ca/ecmybillformat to update your billing preferences in the MyBell app. ( bell.ca/about-us )"
        elif 'reduce_plan' in sanitized_route:
            if is_fr:
                content = "Vous pouvez visiter m.bell.ca/changemyplan pour modifier votre forfait dans l'application MonBell. ( bell.ca/apropos )"
            else:
                content = "You can visit https://m.bell.ca/changemyplan  to change your plan in the MyBell app. ( bell.ca/about-us )"
        elif 'dispute' in sanitized_route:
            if is_fr:
                content = "Vous pouvez visiter https://m.bell.ca/ecutilisation pour voir vos frais mensuels et votre utilisation dans l'application MonBell. ( bell.ca/apropos )"
            else:
                content = "You can visit https://m.bell.ca/eccheckusage to view your monthly charges and usage in the MyBell app. ( bell.ca/about-us )"
        elif 'confirm_due_date' in sanitized_route:
            if is_fr:
                content = "Vous pouvez visiter https://m.bell.ca/ecmaconnexion pour voir votre date de facturation mensuelle dans l'application MonBell. ( bell.ca/apropos )"
            else:
                content = "You can visit https://m.bell.ca/ecmylogin to view your Monthly Charge Date in the MyBell app. ( bell.ca/about-us )"
        elif 'add_promo' in sanitized_route or 'inquire_promo' in sanitized_route:
            if is_fr:
                content = "Vous pouvez visiter https://m.bell.ca/ecchangermonforfait our en savoir plus sur nos forfaits et offres dans l'application MonBell. (bell.ca/apropos)"
            else:
                content = "You can visit https://m.bell.ca/ecchangemyplan to learn more about our to learn more about our plans and offers in the MyBell app. ( bell.ca/about-us )"
        elif 'missing_promo' in sanitized_route:
            if is_fr:
                content = "Vous pouvez visiter https://m.bell.ca/ecchangermonforfait pour passer en revue vos promotions dans l'application MonBell. ( bell.ca/apropos )"
            else:
                content = "You can visit https://m.bell.ca/ecchangemyplan to review your promotions in the MyBell app. ( bell.ca/about-us )"
        else:
            if is_fr:
                content = "Visitez l'application MonBell pour plus de détails."
            else:
                content = "Visit the MyBell app for more details."

        set_variable('sms_content', content)
        set_variable('sms_type', 'Public')
        print('Business logic success: SMS mapped deterministically.')
        return {'status': 'success', 'message': 'SMS content mapped successfully.'}
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Politely inform the user that we cannot generate the SMS at the moment and transfer them.'}
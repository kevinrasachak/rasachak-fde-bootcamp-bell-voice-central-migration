def check_sales_propensity_tool(telephone_number: str, language: str) -> dict:
    '''Fetches DEAI customer information to determine sales propensity for cross-selling.'''
    import json
    try:
        mock_mode = get_variable('mock_mode')
        if mock_mode:
            api_response = {
                'sales_propensity_bell_internet_cross_sell_flg': 1,
                'sales_propensity_bell_second_line_sell_flg': 0,
                'sales_propensity_bell_tv_cross_sell_flg': 0
            }
        else:
            payload = {'telephone_number': telephone_number, 'language': language}
            # Synthesized OpenAPI call based on blueprint backend_toolset_to_call
            api_response = tools.deai_customer_information_get_customer_information(payload).json()
            print('Business logic success')

        internet_flag = int(api_response.get('sales_propensity_bell_internet_cross_sell_flg', 0))
        second_line_flag = int(api_response.get('sales_propensity_bell_second_line_sell_flg', 0))
        tv_flag = int(api_response.get('sales_propensity_bell_tv_cross_sell_flg', 0))

        eligible = (internet_flag == 1 or second_line_flag == 1 or tv_flag == 1)

        if eligible:
            set_variable('serve_to_check', 'Fail')
        else:
            set_variable('serve_to_check', 'Pass')

        return {
            'cross_sell_eligible': eligible
        }
    except Exception as e:
        logger.error(f'Crash: {e}')
        return {'error': str(e), 'agent_action': 'Proceed with session termination smoothly despite the technical error.'}
def update_test_wrapper_state(digital_tools_phase2: bool = False, infobot_flag: bool = False) -> dict:
    '''State/Variable Manipulator for setting test state routing variables safely.'''
    try:
        set_variable('digital_tools_phase2', digital_tools_phase2)
        set_variable('infobot_flag', infobot_flag)

        # Routing test target parameters based on blueprint tree
        set_variable('hardstop', True)
        set_variable('flow_id', '1819189a-3e6b-4603-aeaf-3ecc162de16e')
        set_variable('page_name', 'Check Flag')

        print("Business logic success: Routing variables stored.")
        return {"status": "success", "message": "Test parameters set successfully. The agent should now route the call to the target test flow."}
    except Exception as e:
        logger.error(f"Crash: {e}")
        return {
            "error": str(e),
            "agent_action": "Politely inform the customer that configuring the test failed."
        }
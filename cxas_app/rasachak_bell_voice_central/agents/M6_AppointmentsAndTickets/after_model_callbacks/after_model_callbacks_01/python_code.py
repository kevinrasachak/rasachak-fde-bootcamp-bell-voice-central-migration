from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Webhook error routing is handled in before_model_callback as per architectural constraints for tool responses.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    user_input = callback_context.get_last_user_input()
    input_text = ""
    if user_input:
        for part in user_input:
            if part.text:
                input_text += part.text.lower()
                
    if "no user activity detected" in input_text or "sys.no-input" in input_text:
        print("Executing No-Input check in after_model_callback.")
        local_ni = callback_context.variables.get("local_noinput_counter", 0) + 1
        global_err = callback_context.variables.get("global_error_counter", 0) + 1
        callback_context.variables["local_noinput_counter"] = local_ni
        callback_context.variables["global_error_counter"] = global_err
        
        if global_err >= 3:
            print("Global error threshold reached, transferring to bell_aqd.")
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")])
        if local_ni >= 3:
            print("Local No-Input threshold reached, transferring to bell_No_Input_3.")
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")])

    elif "sys.no-match" in input_text:
        print("Executing No-Match check in after_model_callback.")
        local_nm = callback_context.variables.get("local_nomatch_counter", 0) + 1
        global_err = callback_context.variables.get("global_error_counter", 0) + 1
        callback_context.variables["local_nomatch_counter"] = local_nm
        callback_context.variables["global_error_counter"] = global_err
        
        if global_err >= 3:
            print("Global error threshold reached, transferring to bell_aqd.")
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")])
        if local_nm >= 3:
            print("Local No-Match threshold reached, transferring to bell_No_Match_3.")
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")])
            
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # All validation, routing, and tool failure actions are safely captured in before_model_callback.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print('Executing after_model_callback - verifying logic states.')
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    global_errors = callback_context.variables.get('global_error_counter', 0)
    if global_errors >= 3:
        print('Global error limit exceeded, transferring to bell_aqd.')
        return LlmResponse.from_parts(parts=[
            Part.from_text('I am having trouble processing your request. Please hold while I transfer you to a live agent.'),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])

    webhook_success = callback_context.variables.get('webhook_success')
    if webhook_success is False:
        print('Critical webhook failed, transferring to bell_ticket_mgmt_webhook_failure.')
        callback_context.variables['ticket_mgmt_webhook_failure_type'] = 'acut'
        return LlmResponse.from_parts(parts=[
            Part.from_text('Our systems are experiencing technical difficulties updating your ticket. Let me get an agent to help.'),
            Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
        ])

    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Webhook error catching is executed mathematically during function response evaluation in before_model_callback.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None
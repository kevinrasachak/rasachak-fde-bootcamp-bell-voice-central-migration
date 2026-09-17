from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    global_errors = callback_context.variables.get("global_error_counter", 0)
    if global_errors >= 3:
        print("Global error counter reached max. Initiating transfer to TargetAgent:Bell_AQD.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("I seem to be having trouble understanding. Let me transfer you to a live agent for further assistance."),
            Part.from_agent_transfer(agent="TargetAgent:Bell_AQD")
        ])

    for part in llm_response.content.parts:
        if part.has_function_response("execute_intake_initialization"):
            result = part.function_response.response.get("result", {})
            if "error" in result:
                print("Executing Tool Failure detected for execute_intake_initialization, injecting fallback config and bypassing to fallback routing.")
                callback_context.variables["va_ibm_id"] = "BCE_Entry"
                callback_context.variables["va_entry_flow"] = "BCE_Entry"
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We are experiencing technical difficulties with our systems. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="TargetAgent:Bell_AQD")
                ])
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    for index, part in enumerate(llm_response.content.parts):
        if part.has_function_call('sys_no_input_3'):
            print('sys.no-input-3 condition triggered by LLM, transitioning to bell_No_Input_3.')
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
        if part.has_function_call('sys_no_match_3'):
            print('sys.no-match-3 condition triggered by LLM, transitioning to bell_No_Match_3.')
            return LlmResponse.from_parts(parts=[
                Part.from_text('I still didn’t get that. You can check out our frequently asked questions at bell.ca/prepaid-support. Let me transfer you.'),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])
        if part.has_function_call('wrapup'):
            print('Wrapup event triggered, executing transition to END_SESSION.')
            return LlmResponse.from_parts(parts=[Part.from_end_session(reason='wrapup')])
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # No specific custom after-model logic required; LLM relies on generative instruction for standard END_SESSION.
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

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Native fallback handling validated in before_model_callback
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("Executing after_model_callback for live agent handoff")
    for part in llm_response.content.parts:
        if part.has_function_call('bell_aqd'):
            print("Routing to bell_aqd detected. Setting hardstop parameters.")
            callback_context.variables["hardstop"] = True
            callback_context.variables["page_name"] = "End flow"
            callback_context.variables["page_id"] = "61e3b000-fab6-4426-b44c-27211f33a320"
            callback_context.variables["flow_id"] = "dc1d62a7-bbdc-4622-964c-03393de3b963"
            return llm_response
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    for part in llm_response.content.parts:
        if part.has_function_call("wrapup") or part.has_function_call("end_session"):
            print("Wrapup event detected, forcing transition to END_SESSION.")
            return LlmResponse.from_parts(parts=[
                Part.from_end_session(reason="Wrapup event triggered")
            ])
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("Executing strict routing wrap-up. Appending END_SESSION to the LLM response.")
    parts = list(llm_response.content.parts)
    parts.append(Part.from_end_session(reason="inform_under_development_wrapup"))
    return LlmResponse.from_parts(parts=parts)

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    looping_counter = callback_context.variables.get('query_rewriter_looping_counter', 0)
    try:
        looping_counter = int(looping_counter) if looping_counter else 0
    except ValueError:
        looping_counter = 0

    if looping_counter >= 2:
        print('Looping threshold met in after_model_callback. Forcing transition to bell_aqd.')
        return LlmResponse.from_parts(parts=[
            Part.from_text('Routing loop detected. Transferring to specialist.'),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])

    no_match_2 = callback_context.variables.get('no_match_2', False)
    is_no_match_intent = False
    
    for part in llm_response.content.parts:
        if part.has_function_call('update_no_match_counters'):
            is_no_match_intent = True
            break
            
    if no_match_2 is True and is_no_match_intent:
        print('no_match_2 is True and no match intended. Forcing transition to bell_No_Match_3.')
        return LlmResponse.from_parts(parts=[
            Part.from_text('Multiple misunderstood utterances. Escalating routing.'),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    noinput_counter = callback_context.variables.get("local_noinput_counter", 0)
    nomatch_counter = callback_context.variables.get("local_nomatch_counter", 0)
    sms_failure_counter = callback_context.variables.get("sms_failure_counter", 0)
    
    if noinput_counter >= 3:
        print("No-input counter reached 3, routing to bell_No_Input_3.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("We haven't heard from you. Let me transfer you."),
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])
        
    if nomatch_counter >= 3:
        print("No-match counter reached 3, routing to bell_No_Match_3.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("I'm having trouble understanding. Let me transfer you."),
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])
        
    if sms_failure_counter >= 3:
        print("SMS webhook retry counter exceeded 3, routing to bell_aqd.")
        callback_context.variables["hardstop"] = True
        return LlmResponse.from_parts(parts=[
            Part.from_text("Sorry, we've had multiple issues sending the text. Let me transfer you."),
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])
        
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Fallback validation can be implemented here if required
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # 1. Invalid phone counter
    invalid_phone_counter = callback_context.variables.get('invalid_phone_counter', 0)
    if invalid_phone_counter > 2:
        print("Invalid phone counter exceeded, routing to bell_aqd.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("Let me transfer you for further assistance."),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    # 2. No match counter
    local_nomatch_counter = callback_context.variables.get('local_nomatch_counter', 0)
    if local_nomatch_counter >= 3:
        print("No match counter exceeded, routing to bell_No_Match_3.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("I'm having trouble understanding. Let me transfer you."),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("Executing after_model_callback validation logic")
    # Webhook error catching is deterministically handled in before_model_callback via function_response evaluation.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print('Executing after_model_callback for bell_appt_mgmt_mya_pitch_1')
    
    ge_count = callback_context.variables.get('global_error_counter', 0)
    if ge_count >= 3:
        print('global_error_counter >= 3 in after_model_callback, routing to bell_aqd.')
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
    
    nm_count = callback_context.variables.get('local_nomatch_counter', 0)
    if nm_count >= 3:
        print('local_nomatch_counter >= 3 in after_model_callback, routing to bell_No_Match_3.')
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
    
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Webhook error validations are primarily handled in before_model_callback intercepting function_responses
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

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # All error handling and timeout routing has been addressed inside before_model_callback.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print('Evaluating LLM response payload for completion criteria...')
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    for index, part in enumerate(llm_response.content.parts):
        if part.has_function_call('end_session'):
            print('Executing session wrap-up detection.')
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

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # No specific post-processing logic needed for this sub-agent's flow
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

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Validate Webhook Failure Limits for Session Termination
    tester_fails = callback_context.variables.get('get_tester_details_fail_count', 0)
    intake_fails = callback_context.variables.get('intake_routing_fail_count', 0)
    
    if tester_fails > 2 or intake_fails > 2:
        print("Maximum webhook failure limit exceeded. Terminating session forcefully.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("There was a problem calling the required testing webhooks. Exiting test Wrapper."),
            Part.from_end_session(reason="Max Webhook Failures")
        ])
        
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

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    if callback_context.variables.get("webhook_success") is False:
        callback_context.variables["webhook_success"] = None
        print("Executing Tool Failure detected in state, routing to bell_wrapup.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("I couldn't complete the transfer setup. Let me route you to support."),
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("Executing after_model_callback logic gate.")
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None
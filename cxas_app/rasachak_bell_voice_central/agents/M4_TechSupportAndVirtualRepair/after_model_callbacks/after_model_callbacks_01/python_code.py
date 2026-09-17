from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    try:
        for part in llm_response.content.parts:
            if part.has_function_response("process_acut_ticket_data"):
                func_resp = part.function_response.response.get("result", {})
                if "error" in func_resp or func_resp.get("status") != "success":
                    print("Executing Tool Failure detected, initiating transfer.")
                    from_flow = callback_context.variables.get("from_flow", "")
                    target_agent = "bell_aqd" if from_flow == "bell_vr_kickout" else "bell_tech_service_outage_&_Tech_connection_issue"
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We are experiencing technical difficulties. Let me get you to support."),
                        Part.from_agent_transfer(agent=target_agent)
                    ])
    except Exception as e:
        print(f"Callback error: {e}")
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Webhook error interception is enforced strictly in before_model_callback post-execution.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # No specific post-response actions required for this flow
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Webhook error logic and state transitions have been shifted to before_model_callback
    # to intercept the function response before model generation.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Tool execution failures and no-inputs are handled robustly in the before_model_callback to intercept LLM processing.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("Executing after_model_callback.")
    # Validation handled directly in before_model_callback to adhere strictly to framework Part function response syntax constraints.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("Evaluating after_model_callback logic gates.")
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # No modifications required post-model execution for this agent blueprint.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Validate counters for AQD and No Match as per requirements
    if callback_context.variables.get("global_error_counter", 0) >= 3:
        print("Max global errors reached, executing transfer to bell_aqd.")
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])

    if callback_context.variables.get("local_nomatch_counter", 0) >= 3:
        print("Max no-match reached, executing transfer to bell_No_Match_3.")
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])
        
    # Automatic deterministic routing based on state evaluation
    parsed_route = callback_context.variables.get("parsed_order_route")
    if parsed_route == "AQD":
        print("Parsed route is AQD, initiating transfer to bell_aqd.")
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])

    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    try:
        nomatch_count = callback_context.variables.get('local_nomatch_counter', 0)
        if nomatch_count >= 3:
            print("Max No-Match reached, transferring.")
            return LlmResponse.from_parts(parts=[
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])
        noinput_count = callback_context.variables.get('local_noinput_counter', 0)
        if noinput_count >= 3:
            print("Max No-Input reached, transferring.")
            return LlmResponse.from_parts(parts=[
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])
    except Exception as e:
        print(f"Error in after_model_callback: {e}")
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
    print('Executing after_model_callback...')
    print('Evaluating polling loop limits...')
    vr_counter = int(callback_context.variables.get('vr_counter', 0))
    counter_sharp = int(callback_context.variables.get('counter_sharp', 0))
    microservice_aqd_counter = int(callback_context.variables.get('microservice_aqd_counter', 0))
    
    if vr_counter >= 24 or counter_sharp >= 24 or microservice_aqd_counter >= 8:
        print('Polling loop limit exceeded. Forcing transition to bell_aqd.')
        return LlmResponse.from_parts(parts=[
            Part.from_text('This step is taking longer than usual, so I need to put you in contact with an agent for assistance.'),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    print('All checks passed in after_model_callback.')
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    for index, part in enumerate(llm_response.content.parts):
        if part.has_function_response('vr_post_answer_wrapper'):
            func_resp = part.function_response.response.get('result', {})
            if 'error' in func_resp or func_resp.get('webhook_success') == 'false':
                print("Executing Tool Failure detected, evaluating counter_post_task.")
                counter = callback_context.variables.get("counter_post_task", 0) + 1
                callback_context.variables["counter_post_task"] = counter
                lang = callback_context.variables.get("language", "en").lower()
                
                if counter <= 2:
                    print("Retry count <= 2, playing Oops message and keeping session active.")
                    msg = "Oups ! Une erreur s'est produite de mon côté. Permettez-moi de réessayer pour vous." if "fr" in lang else "Oops! Something went wrong on my end. Let me try that again for you."
                    return LlmResponse.from_parts(parts=[
                        Part.from_text(msg)
                    ])
                else:
                    print("Max retries (3) reached, routing to bell_vr_api_failure_handler.")
                    msg = "J'ai besoin que vous vous connectiez à un agent." if "fr" in lang else "I need to connect you to an agent."
                    return LlmResponse.from_parts(parts=[
                        Part.from_text(msg),
                        Part.from_agent_transfer(agent="M4 TechSupportAndVirtualRepair")
                    ])
                    
    hardstop = callback_context.variables.get("hardstop", False)
    if str(hardstop).lower() == "true":
        print("Hardstop flag activated, transitioning to bell_aqd.")
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])
        
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # No strict deterministic overrides required after model execution for this specific routing flow.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    try:
        for part in llm_response.content.parts:
            if part.has_function_response('execute_business_cti_transfer'):
                response_dict = part.function_response.response
                result = response_dict.get('result', {})
                if 'error' in result or result.get('status') == 'failure' or not callback_context.variables.get('webhook_success', True):
                    print('execute_business_cti_transfer failed, routing to bell_wrapup.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('Sorry, I could not transfer you just now. Please connect with us by chat at bell.ca/business_contactus'),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
    except Exception as e:
        print(f'Callback Error: {e}')
    return None
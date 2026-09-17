from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print('Executing after_model_callback checks')
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # All deterministic tool failure and routing checks have been strictly enforced in before_model_callback where function responses are accessible.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    bad_amt = callback_context.variables.get('bad_amount', 0)
    if bad_amt > 2:
        print("Max invalid payment amount threshold exceeded post-generation, overriding to bell_Feedback.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("We can only take payments between $1 and $10,000."),
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
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    for index, part in enumerate(llm_response.content.parts):
        if part.has_function_call('end_session'):
            print('End session call detected.')
            pass
            
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Webhook error tracking is intercepted deterministically in before_model_callback based on tool responses
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    for part in llm_response.content.parts:
        if part.has_function_response("submit_cc_payment_details"):
            response_data = part.function_response.response.get("result", {})
            if "error" in response_data:
                print("Executing Tool Failure detected, initiating transfer to WEBHOOK_FAILURE_HANDLING.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I'm sorry, we are experiencing technical issues processing your card."),
                    Part.from_agent_transfer(agent="WEBHOOK_FAILURE_HANDLING")
                ])

        for func_name in ["validate_cc_number", "validate_expiry_date", "validate_cvv"]:
            if part.has_function_response(func_name):
                result = part.function_response.response.get("result", {})
                if not result.get("is_valid", True):
                    counter_key = f"{func_name}_error_count"
                    error_count = callback_context.variables.get(counter_key, 0) + 1
                    callback_context.variables[counter_key] = error_count
                    print(f"Validation error for {func_name}, count: {error_count}")
                    if error_count > 2:
                        print("Max validation errors reached, transitioning to PROMPT_CX_SMS.")
                        return LlmResponse.from_parts(parts=[
                            Part.from_text("It seems we're having trouble validating that information. Let's try an alternative method."),
                            Part.from_agent_transfer(agent="PROMPT_CX_SMS")
                        ])
                else:
                    print(f"{func_name} successful, resetting error counter.")
                    callback_context.variables[f"{func_name}_error_count"] = 0
                    
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    webhook_success = callback_context.variables.get("webhook_success")
    if webhook_success is None:
        has_create = False
        for part in llm_response.content.parts:
            if part.has_function_call("create_payment_order_wrapper"):
                has_create = True
        
        if not has_create:
            errors = callback_context.variables.get("global_error_counter", 0) + 1
            callback_context.variables["global_error_counter"] = errors
            print(f"Missing CREATE_PAYMENT_ORDER call detected. Error count: {errors}")
            
            if errors >= 3:
                print("Max errors exceeded. Transferring to bell_determine_handover.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I'm experiencing technical issues. Transferring you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Boilerplate available for standard post-llm intercept operations
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # No strict validation needed post-generation for this agent based on architect design.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Required error routing triggers are fully handled in before_model_callback via structural overrides.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # No-match and No-input fallback routing are handled upstream in before_model_callback
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("Evaluating after_model_callback")
    
    user_input_text = ""
    for part in callback_context.get_last_user_input():
        if part.text:
            user_input_text += part.text.lower()
            
    if "agent" in user_input_text or "representative" in user_input_text or "human" in user_input_text:
        print("other_speak_to_agent intent matched heuristically, routing to handover.")
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])
        
    is_fallback = False
    for part in llm_response.content.parts:
        if part.text:
            text_lower = part.text.lower()
            if "didn't get that" in text_lower or "say it again" in text_lower or "mal à comprendre" in text_lower:
                is_fallback = True
                
    if is_fallback:
        nm_count = callback_context.variables.get("no_match_retry_count", 0) + 1
        callback_context.variables["no_match_retry_count"] = nm_count
        if nm_count >= 3:
            print("Max no-match retries reached, transferring to bell_No_Match_3.")
            return LlmResponse.from_parts(parts=[
                Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
            ])
    else:
        callback_context.variables["no_match_retry_count"] = 0
        
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("Evaluating after_model_callback...")
    
    hardstop = callback_context.variables.get("hardstop", False)
    if hardstop:
        print("hardstop=True condition detected (likely unrecoverable webhook failure), routing to bell_aqd.")
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])
        
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # No overrides required post-model generation for this flow
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Validation complete, logic strictly handled in before_model_callback per architectural best practices
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("Evaluating after_model_callback constraints.")
    for part in llm_response.content.parts:
        if part.text and ("timeout" in part.text.lower() or "critical failure" in part.text.lower()):
            print("Unhandled critical API failure detected in model response. Transferring to bell_aqd.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("I'm sorry, I'm having trouble accessing your account. Let me transfer you to an agent."),
                Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
            ])
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    return None
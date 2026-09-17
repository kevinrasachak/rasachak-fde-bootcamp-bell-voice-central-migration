from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # Sync final status on exit if not already done deterministically
    for index, part in enumerate(llm_response.content.parts):
        if part.has_function_call('end_session') or part.has_function_call('agent_transfer'):
            if callback_context.variables.get('auth_status') in ['Pass', 'Fail']:
                print("Flow exit detected. Forcing backend auth status sync wrap-up tool execution.")
                tool_call = Part.from_function_call(
                    name="set_authentication_status",
                    args={
                        "callKey": callback_context.variables.get('callKey', ''),
                        "brand": "bell",
                        "auth_method": callback_context.variables.get('auth_method', ''),
                        "status": callback_context.variables.get('auth_status', '')
                    }
                )
                return LlmResponse.from_parts(
                    parts=(
                        llm_response.content.parts[:index]
                        + [tool_call]
                        + llm_response.content.parts[index:]
                    )
                )
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print('Executing after model callback checks.')
    # Webhook error catching is safely mapped in before_model_callback where tool output executes.
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    for part in llm_response.content.parts:
        if part.has_function_response("fetch_customized_sdl_url"):
            result = part.function_response.response.get("result", {})
            if "error" in result or callback_context.variables.get("webhook_success") is False:
                print("Executing Tool Failure detected in fetch_customized_sdl_url, ending session.")
                callback_context.variables["webhook_success"] = False
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason="Webhook Error")
                ])
                
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    print("Executing after_model_callback")
    return None

from typing import Optional

def after_model_callback(callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:
    # All routing decisions and deterministic validations managed in before_model_callback
    return None
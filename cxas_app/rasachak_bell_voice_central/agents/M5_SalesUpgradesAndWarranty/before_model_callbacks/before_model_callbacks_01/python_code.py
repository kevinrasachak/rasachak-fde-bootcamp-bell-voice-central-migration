from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # --- MIGRATION AUTO-GENERATED: SYSTEM DIRECTIVES ---
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            if any(
                part.has_function_response(t)
                for t in ["extract_entities", "routing"]
            ):
                if part.function_response and hasattr(
                    part.function_response, "response"
                ):
                    response_data = part.function_response.response

                    directives = []
                    if isinstance(response_data, dict):
                        if "__cxas_system_directives__" in response_data:
                            directives = response_data[
                                "__cxas_system_directives__"
                            ]
                        elif (
                            "result" in response_data
                            and isinstance(response_data["result"], dict)
                            and "__cxas_system_directives__"
                            in response_data["result"]
                        ):
                            directives = response_data["result"][
                                "__cxas_system_directives__"
                            ]

                    if directives:
                        parts_to_return = []
                        for directive in directives:
                            action = directive.get("action")
                            if action == "add_override":
                                t_raw = str(directive.get("target", ""))
                                target = t_raw.split(".")[-1]
                                params = directive.get("parameters", {})
                                if isinstance(params, dict):
                                    for k, v in params.items():
                                        callback_context.variables[k] = v
                                        print(f"Injected routing: {k}={v}")
                                print(f"Executing add_override: {target}")
                                if target in ["agentTransfer", "Transfer"]:
                                    parts_to_return.append(
                                        Part.from_end_session(
                                            reason="escalate_to_human",
                                            escalated=True,
                                        )
                                    )
                                else:
                                    parts_to_return.append(
                                        Part.from_agent_transfer(
                                            agent=target
                                        )
                                    )
                        if parts_to_return:
                            return LlmResponse.from_parts(parts=parts_to_return)

    for part in llm_request.contents[-1].parts:
        if part.has_function_response('update_session_route') and 'error' in part.function_response.response.get('result', {}):
            print("Executing Tool Failure detected, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    global_err = callback_context.variables.get('global_error_counter', 0)
    
    for part in callback_context.get_last_user_input():
        if part.text:
            txt = part.text.lower()
            if 'no user activity detected' in txt or 'sys.no-input' in txt:
                print('No-input detected in callback.')
                retry_count = callback_context.variables.get('local_noinput_counter', 0) + 1
                callback_context.variables['local_noinput_counter'] = retry_count
                if retry_count >= 3:
                    print('Max no-input reached, transferring to bell_No_Input_3.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('We haven\'t heard from you. Transferring you now.'),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
            elif 'sys.no-match' in txt:
                print('No-match detected in callback.')
                retry_count = callback_context.variables.get('local_nomatch_counter', 0) + 1
                callback_context.variables['local_nomatch_counter'] = retry_count
                if retry_count >= 3:
                    print('Max no-match reached, transferring to bell_No_Match_3.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('I\'m having trouble understanding. Transferring you now.'),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
                    
    for part in llm_request.contents[-1].parts:
        for tool_name in ['lookup_customer_account_wrapper', 'npa_nxx_lookup_wrapper', 'validate_and_format_phone_number']:
            if part.has_function_response(tool_name) and 'error' in part.function_response.response.get('result', {}):
                print(f'Executing Tool Failure detected for {tool_name}, incrementing error count.')
                global_err += 1
                callback_context.variables['global_error_counter'] = global_err

    if global_err >= 3:
        print('Max global errors reached, transferring to bell_aqd.')
        return LlmResponse.from_parts(parts=[
            Part.from_text('We are experiencing technical difficulties. Let me transfer you.'),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Check for tool errors (Pattern A)
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('update_sales_context_parameters') and
            'error' in part.function_response.response.get('result', {})):
            print("Executing Tool Failure detected, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='escalation_agent')
            ])

    # Check for no-input / timeout (Pattern E)
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text:
            print("No-input timeout detected, checking retry counter.")
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            if retry_count >= 3:
                print("Max retries breached, transferring to agent.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="escalation_agent")
                ])
            print("Triggering bilingual reprompt.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't get that. Can you say it again? J'ai du mal à comprendre cette question.")]
            )
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            if 'wrapup' in text_lower:
                print('Wrapup event detected, transitioning to END_SESSION.')
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason='wrapup event triggered')
                ])
            if 'no user activity detected' in text_lower or 'sys.no-match' in text_lower or 'sys.no-input' in text_lower:
                retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
                callback_context.variables['no_input_retry_count'] = retry_count
                if retry_count >= 3:
                    print('Max retries reached for no-input/no-match. Transferring to agent.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('I am having trouble understanding. Let me transfer you to a representative.'),
                        Part.from_agent_transfer(agent='escalation_agent')
                    ])
                print('No input/match detected. Prompting user again.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('I didn\'t get that. Can you say it again?')
                ])

    for part in llm_request.contents[-1].parts:
        if part.has_function_response('set_route_variable') and 'error' in part.function_response.response.get('result', {}):
            print('Executing Tool Failure detected, initiating transfer.')
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='escalation_agent')
            ])

    return None
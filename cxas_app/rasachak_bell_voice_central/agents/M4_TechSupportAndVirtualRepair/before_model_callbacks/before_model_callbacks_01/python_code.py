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

    try:
        for part in callback_context.get_last_user_input():
            text = part.text.lower() if part.text else ""
            if "no user activity detected" in text or "no-match" in text or "not understand" in text:
                err_count = callback_context.variables.get("global_error_counter", 0) + 1
                callback_context.variables["global_error_counter"] = err_count
                print(f"Error counter incremented to {err_count}")
                
                if err_count >= 3:
                    print("Max errors reached. Transferring to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We are having trouble understanding. Let me transfer you to an agent."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                
                print("Prompting retry for no-match/no-input.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I'm sorry, I didn't quite get that. Can you repeat?")
                ])
    except Exception as e:
        print(f"Callback error: {e}")
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print('Executing before_model_callback checks')
    
    # Check for Tool Failures (API Errors -> Route to bell_ticket_mgmt_webhook_failure)
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if (part.has_function_response('fetch_active_omf_and_acut_tickets') and 'error' in part.function_response.response.get('result', {})):
                print('Webhook API failure detected, transferring to bell_ticket_mgmt_webhook_failure.')
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
                ])
            if (part.has_function_response('fetch_finalized_acut_wrapper') and 'error' in part.function_response.response.get('result', {})):
                print('Webhook API failure detected, transferring to bell_ticket_mgmt_webhook_failure.')
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
                ])
                
    # Check No-Input Counters (Route to bell_No_Input_3)
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text:
            no_input_count = callback_context.variables.get('local_noinput_counter', 0) + 1
            callback_context.variables['local_noinput_counter'] = no_input_count
            print(f'No input detected. Count: {no_input_count}')
            if no_input_count >= 3:
                print('Max no-inputs reached, routing to bell_No_Input_3.')
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
                
    # Check No-Match Counters (Route to bell_No_Match_3)
    local_nomatch = callback_context.variables.get('local_nomatch_counter', 0)
    if local_nomatch >= 3:
        print('Max no-matches reached, routing to bell_No_Match_3.')
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    # Check Global Error Counters (Route to bell_aqd)
    global_err = callback_context.variables.get('global_error_counter', 0)
    if global_err >= 3:
        print('Max global errors reached, routing to bell_aqd.')
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Custom Response for No-Input / No-Match Thresholds
    for part in callback_context.get_last_user_input():
        if part.text and ("no user activity detected" in part.text.lower() or "no match" in part.text.lower() or "no-match" in part.text.lower()):
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            print(f"No-input/no-match detected. Retry count: {retry_count}")
            
            if retry_count >= 3:
                print("Max retries reached, transferring to bell_aqd fallback route.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            print("Playing localized reprompt messages.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("I didn't get that. Can you say it again? J'ai du mal à comprendre cette question.")
            ])
            
    # Deterministic Routing on Tool Execution / Failure
    for part in llm_request.contents[-1].parts:
        if part.has_function_response("trigger_sat_rehit_wrapper"):
            result = part.function_response.response.get("result", {})
            
            # Check for hard error or webhook failure
            if "error" in result or callback_context.variables.get("webhook_success") is False:
                print("Executing Tool Failure detected, initiating transfer to bell_rehit_SMS.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("Sorry, something went wrong with the system. Let me transfer you."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
                
            # Deterministic success routing
            if callback_context.variables.get("webhook_success") is True:
                print("Webhook success detected, routing to Bell_tv_rehit_SatTV_FibeTV.")
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent="M4 TechSupportAndVirtualRepair")
                ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Handle no user activity timeout patterns
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text:
            local_noinput = callback_context.variables.get("local_noinput_counter", 0) + 1
            callback_context.variables["local_noinput_counter"] = local_noinput
            global_err = callback_context.variables.get("global_error_counter", 0) + 1
            callback_context.variables["global_error_counter"] = global_err
            print(f"No-input detected. Local: {local_noinput}, Global: {global_err}")
            
            if global_err >= 3:
                print("Global error limit reached, transferring to bell_aqd")
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            if local_noinput >= 3:
                print("Local no-input limit reached, transferring to bell_No_Input_3")
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            return LlmResponse.from_parts(
                parts=[Part.from_text("Hi, are you still there?")]
            )
            
    # Enforce strict variable-based error routing overrides
    global_err_check = callback_context.variables.get("global_error_counter", 0)
    local_noinput_check = callback_context.variables.get("local_noinput_counter", 0)
    local_nomatch_check = callback_context.variables.get("local_nomatch_counter", 0)
    
    if global_err_check >= 3:
        print("Global error counter triggered, transferring to bell_aqd")
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")])
    if local_noinput_check >= 3:
        print("Local no-input counter triggered, transferring to bell_No_Input_3")
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")])
    if local_nomatch_check >= 3:
        print("Local no-match counter triggered, transferring to bell_No_Match_3")
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")])
        
    # Enforce Tool Failure Routing (webhook_success = false -> bell_rehit_SMS)
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response("execute_sat_rehit"):
                resp_dict = part.function_response.response.get("result", {})
                if "error" in resp_dict or not resp_dict.get("webhook_success", True):
                    print("execute_sat_rehit Failure detected, initiating transfer to bell_rehit_SMS.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # PATTERN A: Transfer to Another Agent on Tool Failures
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('extract_mya_eligibility_data') and
            'error' in part.function_response.response.get('result', {})):
            print("Executing Tool Failure detected for extract_mya_eligibility_data, initiating transfer to bell_aqd.")
            callback_context.variables['hardstop'] = True
            return LlmResponse.from_parts(parts=[
                Part.from_text(
                    'Sorry, something went wrong while retrieving your appointment options. Let me transfer you.'
                ),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])

    # PATTERN E: Custom Response for No-Input / Silence Timeout and No-Match Limits
    for part in callback_context.get_last_user_input():
        text_lower = part.text.lower() if part.text else ""
        if "no user activity detected" in text_lower or "no match" in text_lower:
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            if retry_count >= 3:
                print("Executing Maximum retry limit reached for no-input/no-match, transferring to bell_aqd.")
                callback_context.variables['hardstop'] = True
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't been able to understand each other. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            print(f"Executing No Input or No Match detected (Attempt {retry_count}), reprompting user.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't get that. Can you say it again?")]
            )
        else:
            # Reset retry counter on successful input
            if callback_context.variables.get("no_input_retry_count", 0) > 0:
                callback_context.variables["no_input_retry_count"] = 0

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # 1. Start Session Logic & Startover Routing
    auth_status = callback_context.variables.get('auth_status')
    if auth_status is None:
        print("Executing Session End: auth_status is null.")
        return LlmResponse.from_parts(parts=[
            Part.from_end_session(reason='Auth Status Null')
        ])

    # 2. No-Input / No-Match and Startover Event Checking
    for part in callback_context.get_last_user_input():
        text = part.text.lower() if part.text else ""
        if "start over" in text or "startover" in text:
            print("Startover intent detected, routing to default_start_flow.")
            callback_context.variables["event_type"] = "full start over"
            return LlmResponse.from_parts(parts=[
                Part.from_agent_transfer(agent="default_start_flow")
            ])

        if "no user activity detected" in text or "no-match" in text or "sys.no-input" in text:
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            if retry_count >= 3:
                print("Max no-input/no-match errors reached. Transitioning to bell_aqd.")
                callback_context.variables["route"] = "tech_change_appointment_mya_false"
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you or are having trouble understanding. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            print("Playing localized error prompt for no-input/no-match.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't quite get that. Could you please repeat?")]
            )

    # 3. Tool Failure (Webhook Error) & Deterministic Routing Logic
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('fetch_and_evaluate_mya_eligibility'):
                func_resp = part.function_response.response.get('result', {})
                if 'error' in func_resp or 'error' in part.function_response.response:
                    print("Executing Tool Failure detected (Webhook error), initiating transfer to bell_aqd.")
                    callback_context.variables["route"] = "tech_change_appointment_mya_false"
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Sorry, something went wrong while retrieving your appointment information. Let me transfer you."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                else:
                    print("Tool execution successful. Enforcing state machine transition to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('set_tech_visit_routing_variables') and
            'error' in part.function_response.response.get('result', {})):
            print('Executing Tool Failure detected, initiating transfer.')
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='escalation_agent')
            ])

    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            if 'wrapup' in text_lower:
                print('Wrapup event detected, terminating session.')
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason='Wrapup event triggered')
                ])
            
            if 'no user activity detected' in text_lower or 'sys.no-match-default' in text_lower or 'sys.no-input-default' in text_lower:
                retry_count = callback_context.variables.get('global_error_counter', 0) + 1
                callback_context.variables['global_error_counter'] = retry_count
                if retry_count >= 3:
                    print('Max retries reached for no-input/no-match, transitioning to END_SESSION.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('We haven\'t heard from you. Ending session.'),
                        Part.from_end_session(reason='Max retries exceeded')
                    ])
                print('Prompting user for retry due to no-input or no-match.')
                return LlmResponse.from_parts(
                    parts=[Part.from_text('I didn\'t get that. Can you say it again?')]
                )

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Pattern E: Custom Response for No-Input / Silence Timeout
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text.lower():
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            print(f'No-input detected. Retry count: {retry_count}')
            if retry_count >= 3:
                print('Max no-input retries reached. Routing to bell_aqd.')
                callback_context.variables['hardstop'] = True
                callback_context.variables['page_name'] = 'Webhook MYA Eligibility'
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We haven\'t heard from you. Let me transfer you to an agent.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            return LlmResponse.from_parts(parts=[Part.from_text('Hi, are you still there?')])
    
    # Pattern A: Transfer to Another Agent on Tool Failures
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('check_mya_eligibility_wrapper') or part.has_function_response('extract_service_identifier_tool'):
            if 'error' in part.function_response.response.get('result', {}):
                print('Executing Tool Failure detected, initiating transfer to bell_aqd.')
                callback_context.variables['hardstop'] = True
                callback_context.variables['page_id'] = '30a69d88-a0fc-48fc-af37-78806b591134'
                callback_context.variables['flow_id'] = 'e6fed7a7-33b0-4b41-8443-92a90435e07c'
                callback_context.variables['page_name'] = 'Webhook MYA Eligibility'
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Check for Tool Failures (Pattern A)
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('set_routing_parameters') and
            'error' in part.function_response.response.get('result', {})):
            print("Executing Tool Failure detected, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])

    # Check for No-Input/No-Match Exceeded (Pattern E)
    user_input_text = ""
    for part in callback_context.get_last_user_input():
        if part.text:
            user_input_text += part.text.lower()
            
    if "no user activity detected" in user_input_text:
        print("No-input detected. Evaluating error counter.")
        error_count = callback_context.variables.get("global_error_counter", 0) + 1
        callback_context.variables["global_error_counter"] = error_count
        
        if error_count >= 3:
            print("Max retries reached. Forcing END_SESSION.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("We haven't heard from you in a while. Goodbye."),
                Part.from_end_session(reason='Max No-Input Retries')
            ])
            
        print("Playing localized fallback message for no-input.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("I didn't get that. Can you say it again? / J'ai du mal à comprendre cette question.")
        ])
        
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("Executing before_model_callback: Checking counters and tool failures.")
    
    global_err = callback_context.variables.get("global_error_counter", 0)
    local_err = callback_context.variables.get("local_noinput_counter", 0)
    
    try:
        global_err = int(global_err)
        local_err = int(local_err)
    except:
        global_err = 0
        local_err = 0
        
    if global_err >= 3 or local_err >= 3:
        print("Executing Handover: global_error_counter or local_noinput_counter threshold met.")
        callback_context.variables["hardstop"] = True
        return LlmResponse.from_parts(parts=[
            Part.from_text("I'm having trouble assisting you today. Let me transfer you to an agent who can help."),
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])
        
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('check_service_outage_bundled'):
                result = part.function_response.response.get('result', {})
                if result.get('webhook_success') is False or 'error' in result:
                    print("Executing Tool Failure detected for check_service_outage_bundled. Bypassing model and returning FAILED_CHECK_HANDLING response.")
                    callback_context.variables['outage_status'] = 'unknown'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Sorry, due to an unexpected system issue, I was unable to verify if there's any active outage in your area. But you can easily check for service outages yourself on our website. I can send a text to the device you're calling from so you can access it quickly. Is that alright?")
                    ])
                    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("Evaluating before_model_callback logic gates.")
    
    for part in callback_context.get_last_user_input():
        if part.text and ("no user activity detected" in part.text.lower() or "sys.no-input" in part.text.lower() or "sys.no-match" in part.text.lower()):
            print("sys.no-input or sys.no-match event triggered (silence or unrecognized input).")
            
            current_errors = callback_context.variables.get("global_error_counter", 0)
            new_errors = current_errors + 1
            
            print(f"Incrementing error counters to {new_errors}.")
            callback_context.variables["global_error_counter"] = new_errors
            callback_context.variables["no_input_retry_count"] = new_errors
            
            if new_errors >= 3:
                print("Max retry threshold exceeded, triggering Live_Agent_Transfer.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I'm having trouble understanding. Let me transfer you to an agent. / J'éprouve des difficultés à comprendre. Laissez-moi vous transférer à un agent."),
                    Part.from_agent_transfer(agent="Live_Agent_Transfer")
                ])
            
            print("Threshold not met, playing bilingual reprompts.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("I didn't get that. Can you say it again? / J'ai du mal à comprendre cette question.")
            ])
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        text = (part.text or "").lower()
        if "no user activity detected" in text or "sys.no-input" in text:
            print("Detected silence/no-input event.")
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            language = callback_context.variables.get("language", "en").lower()
            if retry_count >= 3:
                print("No-input threshold exceeded. Triggering Live Agent Transfer.")
                transfer_msg = "We haven't heard from you. Let me transfer you to an agent." if "fr" not in language else "Nous n'avons pas de réponse. Je vous transfère à un agent."
                return LlmResponse.from_parts(parts=[
                    Part.from_text(transfer_msg),
                    Part.from_agent_transfer(agent="escalation_agent")
                ])
            print("No-input under threshold. Prompting user to repeat.")
            retry_msg = "I didn't get that. Can you say it again?" if "fr" not in language else "Je n'ai pas saisi ce que vous avez dit. Pouvez-vous répéter?"
            return LlmResponse.from_parts(parts=[Part.from_text(retry_msg)])
        elif "sys.no-match" in text:
            print("Detected invalid input/no-match event.")
            error_count = callback_context.variables.get("global_error_counter", 0) + 1
            callback_context.variables["global_error_counter"] = error_count
            language = callback_context.variables.get("language", "en").lower()
            if error_count >= 3:
                print("Global error counter exceeded. Triggering Live Agent Transfer.")
                transfer_msg = "I'm having trouble understanding. Let me transfer you." if "fr" not in language else "J'ai du mal à comprendre. Je vous transfère à un agent."
                return LlmResponse.from_parts(parts=[
                    Part.from_text(transfer_msg),
                    Part.from_agent_transfer(agent="escalation_agent")
                ])
            print("Global error counter under threshold. Prompting user to rephrase.")
            retry_msg = "Sorry, I didn't get that. Can you rephrase?" if "fr" not in language else "J'ai du mal à comprendre cette question. Pouvez-vous reformuler?"
            return LlmResponse.from_parts(parts=[Part.from_text(retry_msg)])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Check Global Error Limits
    if callback_context.variables.get('global_error_counter', 0) >= 3:
        print('Global error counter limit reached, initiating transfer to bell_aqd.')
        return LlmResponse.from_parts(parts=[
            Part.from_text('I am having trouble understanding. Let me transfer you to someone who can help.'),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
    
    # Check for No Input timeouts
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text.lower():
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            print(f'No input detected. Retry count is now: {retry_count}')
            
            if retry_count >= 3:
                print('Max no input retries reached, initiating transfer to bell_aqd.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We haven\'t heard from you in a while. Let me transfer you to an agent.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            
            print('Prompting user for response after inactivity.')
            return LlmResponse.from_parts(
                parts=[Part.from_text('Hi, are you still there? I can help you reschedule your appointment.')]
            )
    
    # Check for Webhook / Tool failures from previous turn
    tools_to_check = ['wfas_check_availability_wrapper', 'wfas_book_and_acut_modify_wrapper', 'acut_modify_contact_wrapper']
    for part in llm_request.contents[-1].parts:
        for tool in tools_to_check:
            if part.has_function_response(tool):
                result = part.function_response.response.get('result', {})
                if 'error' in result or callback_context.variables.get('webhook_success') is False:
                    print(f'Executing Tool Failure detected in {tool}, setting failure type and initiating transfer.')
                    callback_context.variables['ticket_mgmt_webhook_failure_type'] = 'acut'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('I apologize, but we are experiencing technical difficulties updating your ticket. Let me transfer you.'),
                        Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
                    ])
                    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Check for No-Input Timeout (Pattern E)
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            print("No input detected, incrementing local_noinput_counter.")
            retry_count = callback_context.variables.get("local_noinput_counter", 0) + 1
            callback_context.variables["local_noinput_counter"] = retry_count
            if retry_count >= 3:
                print("Max no-input reached, transferring to bell_No_Input_3.")
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't quite get that. Could you say that again?")]
            )

    # Check for Tool Failures (Pattern A)
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('fetch_omf_order_details_wrapper'):
            resp = part.function_response.response.get('result', {})
            if 'error' in resp or callback_context.variables.get('webhook_success') is False:
                print("Tool Failure detected, initiating transfer to bell_tech_service_outage_&_Tech_connection_issue.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I'm having trouble pulling up your order right now. Let's continue troubleshooting your technical issue."),
                    Part.from_agent_transfer(agent='M4 TechSupportAndVirtualRepair')
                ])
                
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    try:
        if llm_request.contents:
            for part in llm_request.contents[-1].parts:
                if part.has_function_response('search_acut_tickets_wrapper') or part.has_function_response('search_omf_orders_wrapper'):
                    resp = part.function_response.response.get('result', {})
                    if 'error' in resp:
                        print("Executing Tool Failure detected, initiating transfer to webhook failure route.")
                        callback_context.variables['ticket_mgmt_webhook_failure_type'] = 'tech_intent'
                        return LlmResponse.from_parts(parts=[
                            Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
                        ])
        for part in callback_context.get_last_user_input():
            if part.text and 'no user activity detected' in part.text.lower():
                retry_count = callback_context.variables.get('local_noinput_counter', 0) + 1
                callback_context.variables['local_noinput_counter'] = retry_count
                print(f"No Input detected. Count: {retry_count}")
                if retry_count >= 3:
                    print("Max No-Input reached, transferring.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
    except Exception as e:
        print(f"Error in before_model_callback: {e}")
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and ("no user activity detected" in part.text.lower() or "sys.no-input" in part.text.lower()):
            print("No input detected.")
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            if retry_count >= 3:
                print("Max no-input retries reached. Terminating session.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Ending the session now."),
                    Part.from_end_session(reason="Max No-Input Retries")
                ])
            print("Prompting user for input.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("Sorry, I didn't get that. Can you say that again?")]
            )
        elif part.text and "sys.no-match" in part.text.lower():
            print("No match detected.")
            error_count = callback_context.variables.get("global_error_counter", 0) + 1
            callback_context.variables["global_error_counter"] = error_count
            if error_count >= 3:
                print("Max no-match retries reached. Terminating session.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I'm having trouble understanding. Ending the session now."),
                    Part.from_end_session(reason="Max No-Match Retries")
                ])
            print("Prompting user for input.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("Sorry, what was that? One more time?")]
            )
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if callback_context.variables.get('first_turn', True):
        print('Executing unconditional transfer to bell_aqd on first turn.')
        callback_context.variables['first_turn'] = False
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
    
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text.lower():
            print('No user activity detected. Playing bilingual no-input prompt.')
            return LlmResponse.from_parts(
                parts=[Part.from_text("J'ai du mal à comprendre cette question. I didn't get that. Can you say it again?")]
            )
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response("set_kickout_variables") and "error" in part.function_response.response.get("result", {}):
                print("Executing Tool Failure detected, initiating transfer.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("Sorry, something went wrong. Let me transfer you."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])

    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            if "no user activity detected" in text_lower or "sys.no-input" in text_lower or "sys.no-match" in text_lower:
                print("No-input or no-match condition triggered.")
                retry_count = callback_context.variables.get("global_error_counter", 0) + 1
                callback_context.variables["global_error_counter"] = retry_count
                if retry_count >= 3:
                    print("Max invalid attempts reached, triggering fallback to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We haven't heard from you. Let me transfer you to an agent."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                print("Prompting user for retry.")
                return LlmResponse.from_parts(
                    parts=[Part.from_text("Sorry, I didn't get that. Can you say it again? / J'ai du mal à comprendre cette question. Pouvez-vous répéter?")]
                )

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print('Executing before_model_callback...')
    print('Checking for No-Input or No-Match conditions...')
    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or 'sys.no-match' in part.text.lower()):
            print('No-Input/No-Match condition met.')
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            if retry_count >= 3:
                print('Max retries reached. Routing to bell_aqd.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('I am having trouble understanding. Let me transfer you to an agent.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            print('Prompting user to try again.')
            return LlmResponse.from_parts(
                parts=[Part.from_text('I didn\'t quite catch that. Are you still there?')]
            )

    print('Checking for Tool Failures in get_vr_next_task_wrapper...')
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('get_vr_next_task_wrapper'):
                response = part.function_response.response.get('result', {})
                if 'error' in response:
                    print('API failure detected for get_vr_next_task_wrapper.')
                    counter = int(callback_context.variables.get('counter_next_task', 0)) + 1
                    callback_context.variables['counter_next_task'] = counter
                    if counter >= 3:
                        print('Max API failures reached. Routing to bell_vr_api_failure_handler.')
                        return LlmResponse.from_parts(parts=[
                            Part.from_text('I need to connect you to an agent due to technical difficulties.'),
                            Part.from_agent_transfer(agent='M4 TechSupportAndVirtualRepair')
                        ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            if "no user activity detected" in text_lower or "no match" in text_lower:
                print("No-input or no-match detected, evaluating retries.")
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                
                if retry_count >= 3:
                    print("Max no-input retries reached, initiating transfer to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We haven't heard from you or are having trouble understanding. Let me transfer you to an agent."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                
                print("Prompting user to repeat.")
                lang = callback_context.variables.get("language", "en").lower()
                reprompt = "J'ai du mal à comprendre cette question. Pouvez-vous répéter?" if "fr" in lang else "I didn't get that. Can you say it again?"
                return LlmResponse.from_parts(
                    parts=[Part.from_text(reprompt)]
                )
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Deterministic Hold Greeting on Start
    if callback_context.variables.get("first_turn", True):
        print("First turn detected, issuing wait message.")
        callback_context.variables["first_turn"] = False
        response = LlmResponse.from_parts([
            Part.from_text("Just a moment while I fetch some details for you.")
        ])
        response.partial = True
        return response
        
    # Handle Tool Execution Failure Routing
    for part in llm_request.contents[-1].parts:
        if part.has_function_response("extract_pre_check_details") and "error" in part.function_response.response.get("result", {}):
            print("Executing Tool Failure detected, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("I'm sorry, I'm having trouble pulling up your account details. Let me get someone to help you."),
                Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
            ])
            
    # Handle no-input / no-match routing
    for part in callback_context.get_last_user_input():
        text = part.text.lower() if part.text else ""
        if "no user activity detected" in text or "no-input" in text or "no-match" in text:
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            if retry_count >= 3:
                print("Exceeded max retries for input, transferring to fallback.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I'm having trouble understanding. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            print("Silence/No-match detected, prompting user to repeat.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("I didn't get that. Can you say it again?")
            ])
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    try:
        for part in callback_context.get_last_user_input():
            if part.text:
                user_text = part.text.lower()
                if 'no user activity detected' in user_text or 'sys.no-input' in user_text:
                    no_input_count = callback_context.variables.get('local_noinput_counter', 0) + 1
                    callback_context.variables['local_noinput_counter'] = no_input_count
                    callback_context.variables['global_error_counter'] = callback_context.variables.get('global_error_counter', 0) + 1
                    if no_input_count >= 3:
                        print('3 No-Inputs detected, routing to bell_No_Input_3.')
                        return LlmResponse.from_parts(parts=[
                            Part.from_text('We have not heard from you. Let me transfer you.'),
                            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                        ])
                    print('No-Input detected, prompting user.')
                    return LlmResponse.from_parts(parts=[Part.from_text('Hi, are you still there?')])
                elif 'sys.no-match' in user_text:
                    no_match_count = callback_context.variables.get('local_nomatch_counter', 0) + 1
                    callback_context.variables['local_nomatch_counter'] = no_match_count
                    callback_context.variables['global_error_counter'] = callback_context.variables.get('global_error_counter', 0) + 1
                    if no_match_count >= 3:
                        print('3 No-Matches detected, routing to bell_No_Match_3.')
                        return LlmResponse.from_parts(parts=[
                            Part.from_text('I am having trouble understanding. Let me transfer you.'),
                            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                        ])
                    print('No-Match detected, prompting user.')
                    return LlmResponse.from_parts(parts=[Part.from_text('I did not quite get that. Could you repeat?')])
    except Exception as e:
        print(f'Callback Error: {e}')
    return None
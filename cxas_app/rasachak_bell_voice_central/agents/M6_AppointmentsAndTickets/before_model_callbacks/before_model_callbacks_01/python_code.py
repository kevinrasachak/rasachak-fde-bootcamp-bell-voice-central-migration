from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # --- MIGRATION AUTO-GENERATED: SYSTEM DIRECTIVES ---
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            if any(
                part.has_function_response(t)
                for t in ["extract_entities"]
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

    global_err = int(callback_context.variables.get('global_error_counter', 0))
    local_err = int(callback_context.variables.get('local_nomatch_counter', 0))
    local_noinput = int(callback_context.variables.get('local_noinput_counter', 0))

    if global_err >= 3 or local_err >= 3 or local_noinput >= 3:
        print('Max errors reached, initiating transfer to bell_aqd.')
        return LlmResponse.from_parts(parts=[
            Part.from_text('I am having trouble understanding. Let me transfer you to a live agent.'),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])

    for part in llm_request.contents[-1].parts:
        if part.has_function_response('acut_ticket_orchestrator_wrapper'):
            response_data = part.function_response.response.get('result', {})
            if 'error' in response_data:
                print('Webhook failure detected in orchestrator, routing to bell_ticket_mgmt_webhook_failure')
                callback_context.variables['ticket_mgmt_webhook_failure_type'] = 'acut'
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We are experiencing technical difficulties. Let me transfer you.'),
                    Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
                ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text:
            retry_count = callback_context.variables.get("local_noinput_counter", 0) + 1
            callback_context.variables["local_noinput_counter"] = retry_count
            print(f"No-Input detected, count: {retry_count}")
            if retry_count >= 3:
                print("Max No-Input reached, transferring to bell_No_Input_3.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            return LlmResponse.from_parts(
                parts=[Part.from_text("Hi, are you still there?")]
            )
            
    no_match_count = callback_context.variables.get("local_nomatch_counter", 0)
    if no_match_count >= 3:
        print("Max No-Match reached, transferring to bell_No_Match_3.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("I'm having trouble understanding. Let me transfer you."),
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])

    for part in llm_request.contents[-1].parts:
        if (part.has_function_response("cancel_ticket_wrapper") and
            "error" in part.function_response.response.get("result", {})):
            print("Executing Tool Failure detected, initiating transfer.")
            callback_context.variables["ticket_mgmt_webhook_failure_type"] = "acut"
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, something went wrong. Let me transfer you."),
                Part.from_agent_transfer(agent="M6 AppointmentsAndTickets")
            ])
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('fetch_active_appointments_wrapper') and 'error' in part.function_response.response.get('result', {}):
            print("Executing Tool Failure detected, initiating transfer to bell_ticket_mgmt_webhook_failure.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, I'm having trouble accessing the system right now. Let me transfer you."),
                Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
            ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            for tool_name in ['extract_ticket_modifiability_status', 'check_omf_calendar_availability_wrapper', 'execute_omf_calendar_reservation_wrapper']:
                if (part.has_function_response(tool_name) and 'error' in part.function_response.response.get('result', {})):
                    print(f'Executing Tool Failure detected for {tool_name}, initiating transfer.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('Sorry, something went wrong with our systems. Let me transfer you so we can get this sorted out.'),
                        Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
                    ])

    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or 'sys.no-match' in part.text.lower() or 'sys.no-input' in part.text.lower()):
            retry_count = callback_context.variables.get('global_error_counter', 0) + 1
            callback_context.variables['global_error_counter'] = retry_count
            print(f'No-input or No-match triggered. Retry count: {retry_count}')
            if retry_count >= 3:
                print('Max errors reached, initiating transfer to bell_aqd.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('I am having trouble understanding. Let me transfer you to an agent who can help.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            retry_count = callback_context.variables.get("local_noinput_counter", 0) + 1
            callback_context.variables["local_noinput_counter"] = retry_count
            print(f"No-Input detected. Retry count: {retry_count}")
            if retry_count >= 3:
                print("Max no-input reached, routing to bell_No_Input_3")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            return LlmResponse.from_parts(parts=[Part.from_text("Are you still there?")])
    
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('evaluate_cancellation_eligibility_wrapper') or part.has_function_response('modify_close_ticket_wrapper'):
            resp = part.function_response.response.get('result', {})
            if 'error' in resp or resp.get('cancellation_eligibility_status') == 'API_FAILURE':
                print("Executing Tool Failure detected, initiating transfer to bell_ticket_mgmt_webhook_failure.")
                callback_context.variables['ticket_mgmt_webhook_failure_type'] = 'acut'
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I'm sorry, I am having trouble accessing the system right now. Let me get someone to help you."),
                    Part.from_agent_transfer(agent="M6 AppointmentsAndTickets")
                ])
    
    # Handle sys.no-match max limits
    if callback_context.variables.get("global_error_counter", 0) >= 3:
        print("Max no-match invalid responses reached, routing to bell_No_Match_3")
        return LlmResponse.from_parts(parts=[
            Part.from_text("I'm having trouble understanding your request. Let me transfer you to a representative."),
            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
        ])
        
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('fetch_and_process_customer_tickets') and 'error' in part.function_response.response.get('result', {})):
            print('Executing Tool Failure detected, initiating transfer to webhook failure flow.')
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
            ])

    for part in callback_context.get_last_user_input():
        text = part.text.lower() if part.text else ''
        
        if 'no user activity detected' in text or 'sys.no-input' in text:
            retry_count = callback_context.variables.get('local_noinput_counter', 0) + 1
            callback_context.variables['local_noinput_counter'] = retry_count
            print(f'No-Input detected. Count: {retry_count}')
            if retry_count >= 3:
                print('Max No-Input reached, initiating transfer to bell_No_Input_3.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We have not heard from you. Let me transfer you to an agent.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            return LlmResponse.from_parts(parts=[Part.from_text('Hi, are you still there? I did not quite get that.')])

        if 'sys.no-match' in text:
            retry_count = callback_context.variables.get('local_nomatch_counter', 0) + 1
            callback_context.variables['local_nomatch_counter'] = retry_count
            print(f'No-Match detected. Count: {retry_count}')
            if retry_count >= 3:
                print('Max No-Match reached, initiating transfer to bell_No_Match_3.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('I am having trouble understanding. Let me transfer you to an agent.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            return LlmResponse.from_parts(parts=[Part.from_text('I did not quite get that. Could you please rephrase?')])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text.lower():
            print('Silence timeout detected, checking thresholds.')
            retry_count = callback_context.variables.get('local_noinput_counter', 0) + 1
            callback_context.variables['local_noinput_counter'] = retry_count
            if retry_count >= 3:
                print('Max silence retries reached, routing to bell_aqd.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We haven\'t heard from you in a while. Let me transfer you to an agent.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            return LlmResponse.from_parts(parts=[
                Part.from_text('Hi, are you still there? Please let me know what day works for you.')
            ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    try:
        # Check for Webhook Tool Failures (Pattern A)
        for part in llm_request.contents[-1].parts:
            if (part.has_function_response('update_acut_contact_preferences') or \
                part.has_function_response('check_wfas_availability') or \
                part.has_function_response('book_wfas_appointment') or \
                part.has_function_response('cancel_wfas_appointment')):
                
                response_dict = part.function_response.response
                if 'error' in response_dict or 'error' in response_dict.get('result', {}):
                    print("Executing Tool Failure detected, initiating transfer to webhook failure.")
                    callback_context.variables['ticket_mgmt_webhook_failure_type'] = 'acut'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('I am experiencing technical difficulties. Let me transfer you to someone who can help.'),
                        Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
                    ])

        # Handle No-Input and No-Match Limits deterministically (Pattern E)
        last_input = callback_context.get_last_user_input()
        if last_input:
            for part in last_input:
                if part.text and "no user activity detected" in part.text.lower():
                    retry_count = callback_context.variables.get("local_noinput_counter", 0) + 1
                    callback_context.variables["local_noinput_counter"] = retry_count
                    print(f"No-input detected. Count: {retry_count}")
                    if retry_count >= 3:
                        print("Max no-input reached, transitioning to bell_No_Input_3")
                        return LlmResponse.from_parts(parts=[
                            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                        ])
                elif part.text and "no match" in part.text.lower():
                    retry_count = callback_context.variables.get("local_nomatch_counter", 0) + 1
                    callback_context.variables["local_nomatch_counter"] = retry_count
                    print(f"No-match detected. Count: {retry_count}")
                    if retry_count >= 3:
                        print("Max no-match reached, transitioning to bell_No_Match_3")
                        return LlmResponse.from_parts(parts=[
                            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                        ])
    except Exception as e:
        print(f"Error in before_model_callback: {e}")
    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    try:
        if callback_context.variables.get("first_turn", True):
            callback_context.variables["first_turn"] = False
            print("First turn detected, initiating deterministic greeting.")
            lang = callback_context.variables.get("language", "en").lower()
            if "fr" in lang:
                prompt = "Voulez-vous changer ou annuler votre rendez-vous ?"
            else:
                prompt = "Are you looking to change or cancel your appointment?"
            response = LlmResponse.from_parts([Part.from_text(prompt)])
            response.partial = True
            return response

        user_input = callback_context.get_last_user_input()
        if user_input:
            for part in user_input:
                if part.text and "no user activity detected" in part.text:
                    retry_count = callback_context.variables.get("global_error_counter", 0) + 1
                    callback_context.variables["global_error_counter"] = retry_count
                    print(f"No-input/No-match error detected. Total errors: {retry_count}")
                    
                    if retry_count >= 3:
                        print("Max consecutive errors reached (3). Executing agent transfer to bell_aqd.")
                        return LlmResponse.from_parts(parts=[
                            Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                        ])
                    
                    print("Error limit not reached. Asking the user again.")
                    lang = callback_context.variables.get("language", "en").lower()
                    if "fr" in lang:
                        prompt = "Désolé(e), je n'ai pas compris. Souhaitez-vous modifier ou annuler votre rendez-vous ?"
                    else:
                        prompt = "Sorry, I didn't get that. Are you looking to change or cancel your appointment?"
                    return LlmResponse.from_parts(parts=[Part.from_text(prompt)])

    except Exception as e:
        print(f"Error in before_model_callback: {str(e)}")

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('fetch_omf_order_details'):
                response_data = part.function_response.response.get('result', {})
                if 'error' in response_data:
                    print("Executing Tool Failure detected for fetch_omf_order_details, initiating transfer.")
                    callback_context.variables['ticket_mgmt_webhook_failure_type'] = 'omf'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('I am experiencing a technical issue retrieving your order details. Let me transfer you.'),
                        Part.from_agent_transfer(agent='M6 AppointmentsAndTickets')
                    ])

    is_no_input_or_match = False
    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or 'no-match' in part.text.lower()):
            is_no_input_or_match = True
            break
    
    if is_no_input_or_match:
        retry_count = callback_context.variables.get('global_error_counter', 0) + 1
        callback_context.variables['global_error_counter'] = retry_count
        print(f"No-input/No-match detected. Current count: {retry_count}")
        if retry_count >= 3:
            print("Max retries reached. Setting special_queue to default and transferring to bell_aqd.")
            callback_context.variables['special_queue'] = 'default'
            return LlmResponse.from_parts(parts=[
                Part.from_text('I am having trouble understanding. Let me transfer you to an agent.'),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            if (part.has_function_response('set_routing_variables') and
                'error' in part.function_response.response.get('result', {})):
                print("Executing Tool Failure detected, initiating session termination.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, something went wrong. Please call back later. / Désolé, une erreur s\'est produite. Veuillez rappeler plus tard.'),
                    Part.from_end_session(reason='Tool Failure')
                ])

    user_input = callback_context.get_last_user_input()
    if user_input:
        for part in user_input:
            if part.text and "no user activity detected" in part.text.lower():
                print("No input detected, incrementing retry count.")
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                if retry_count >= 3:
                    print("Max retries reached, ending session.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We haven't heard from you. Let me end this call. / Nous ne vous entendons pas. Au revoir."),
                        Part.from_end_session(reason='Max Retries Exceeded')
                    ])
                print("Prompting user for input again.")
                return LlmResponse.from_parts(
                    parts=[Part.from_text("I didn't get that. Can you say it again? / J'ai du mal à comprendre, pouvez-vous répéter?")]
                )
    return None
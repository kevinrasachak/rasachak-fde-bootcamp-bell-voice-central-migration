from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # --- MIGRATION AUTO-GENERATED: SYSTEM DIRECTIVES ---
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            if any(
                part.has_function_response(t)
                for t in ["no_intent", "extract_entities", "match_intent", "routing"]
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
                            if action == "respond":
                                text = directive.get("text", "")
                                parts_to_return.append(
                                    Part.from_text(text=text)
                                )
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

    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            print("No user activity detected. Incrementing local_noinput_counter.")
            retry_count = callback_context.variables.get("local_noinput_counter", 0) + 1
            callback_context.variables["local_noinput_counter"] = retry_count
            if retry_count >= 3:
                print("Max no-input retries reached. Triggering hard-route to TargetAgent:Bell_Wrapup.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me wrap up this session."),
                    Part.from_agent_transfer(agent="TargetAgent:Bell_Wrapup")
                ])
            print("Prompting user for input.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("Hi, are you still there?")]
            )
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('set_routing_context') and
            'error' in part.function_response.response.get('result', {})):
            print('Executing Tool Failure detected, initiating session end.')
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Please call back later.'),
                Part.from_end_session(reason='Tool Failure')
            ])

    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text:
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            if retry_count >= 3:
                print('No-input limit reached, triggering transition to bell_No_Input_3')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('You can check out our frequently asked questions at bell.ca/prepaid-support. Let me transfer you.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            print('No-input detected, prompting user')
            return LlmResponse.from_parts(
                parts=[Part.from_text('Are you still there? Can you repeat please?')]
            )

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text:
            print("No-input detected during termination phase. Forcing localized error and end session.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("J'ai du mal à comprendre cette question. J'ai mal compris votre demande. Je n'ai pas saisi ce que vous avez dit. Je crois que je ne vous suis pas. Je ne comprends pas de quoi vous me parlez."),
                Part.from_end_session(reason='sys.no-input')
            ])

    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('clear_sensitive_billing_data') and 'error' in part.function_response.response.get('result', {}):
                print("Executing Tool Failure detected, initiating end session.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("Désolé, un problème technique est survenu. Veuillez raccrocher et rappeler plus tard."),
                    Part.from_end_session(reason='Tool Failure')
                ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('update_sms_payload_variables') and 'error' in part.function_response.response.get('result', {}):
            print('Executing Tool Failure detected (update_sms_payload_variables), initiating transfer.')
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])
        if part.has_function_response('set_generic_faq_flags') and 'error' in part.function_response.response.get('result', {}):
            print('Executing Tool Failure detected (set_generic_faq_flags), initiating transfer.')
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])
    
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text:
            noinput_count = callback_context.variables.get('local_noinput_counter', 0) + 1
            callback_context.variables['local_noinput_counter'] = noinput_count
            global_error = callback_context.variables.get('global_error_counter', 0) + 1
            callback_context.variables['global_error_counter'] = global_error
            print(f'No Input detected. local_noinput_counter: {noinput_count}, global_error_counter: {global_error}')
            
            if noinput_count >= 3:
                print('Max no input limit reached. Routing to bell_No_Input_3.')
                return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
            if global_error >= 3:
                print('Global error limit reached via no input. Routing to bell_aqd.')
                return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
            
            msg = 'Sorry, I didn’t quite get that. Can you try again?' if noinput_count == 1 else 'Are you still there? Can you repeat please?'
            return LlmResponse.from_parts(parts=[Part.from_text(msg)])

    if callback_context.variables.get('local_nomatch_counter', 0) >= 3:
        print('Max no match limit reached. Routing to bell_No_Match_3.')
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
        
    if callback_context.variables.get('global_error_counter', 0) >= 3:
        print('Max global error limit reached. Routing to bell_aqd.')
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
        
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("Executing before_model_callback for bell_FAQ_vanity")
    
    user_inputs = callback_context.get_last_user_input()
    for part in user_inputs:
        if part.text:
            text_lower = part.text.lower()
            is_no_input = "no user activity detected" in text_lower or "sys.no-input" in text_lower
            is_no_match = "sys.no-match" in text_lower
            
            if is_no_input or is_no_match:
                print(f"Detected {'no-input' if is_no_input else 'no-match'} condition.")
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                
                if retry_count >= 3:
                    print("Max retries reached, triggering wrapup to END_SESSION.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We are unable to process your request at this time. Goodbye. / Nous ne pouvons pas traiter votre demande pour le moment. Au revoir."),
                        Part.from_end_session(reason="wrapup")
                    ])
                
                print("Sending bilingual reprompt.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I didn't get that. Can you say it again? / J'ai du mal à comprendre cette question.")
                ])
                
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('set_feedback_variables') and 'error' in part.function_response.response.get('result', {}):
                print('Executing Tool Failure detected, initiating transfer.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                    Part.from_agent_transfer(agent='escalation_agent')
                ])

    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            if 'wrapup' in text_lower:
                print('Wrapup event detected. Ending session.')
                return LlmResponse.from_parts(parts=[Part.from_end_session(reason='wrapup')])
            
            if 'no user activity detected' in text_lower or 'sys.no-input-default' in text_lower or 'sys.no-match-default' in text_lower:
                print('No-input or no-match detected. Setting event_type and routing to bell_Steering_Feedback.')
                callback_context.variables['event_type'] = 'anything_else_start_over'
                return LlmResponse.from_parts(parts=[
                    Part.from_text("J'ai du mal à comprendre cette question. J'ai mal compris votre demande. Je n'ai pas saisi ce que vous avez dit. Je crois que je ne vous suis pas. Je ne comprends pas de quoi vous me parlez."),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    if callback_context.variables.get('first_turn', True):
        print('First turn true condition detected, setting event_type and routing to bell_Steering_Feedback.')
        callback_context.variables['first_turn'] = False
        callback_context.variables['event_type'] = 'anything_else_start_over'
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if callback_context.variables.get("first_turn", True):
        callback_context.variables["first_turn"] = False
        print("Unconditional entry: Executing Bell IVR placeholder and ending session.")
        return LlmResponse.from_parts(
            parts=[
                Part.from_text("Bell IVR placeholder"),
                Part.from_end_session(reason="Placeholder unconditional exit")
            ]
        )
    
    for part in callback_context.get_last_user_input():
        text_lower = part.text.lower() if part.text else ""
        if "no user activity detected" in text_lower or "no match" in text_lower or "unrecognized" in text_lower:
            err_count = callback_context.variables.get("global_error_counter", 0) + 1
            callback_context.variables["global_error_counter"] = err_count
            print(f"No-input/No-match detected. global_error_counter is now {err_count}.")
            if err_count >= 3:
                print("Max error attempts reached, forcing END_SESSION.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We are experiencing difficulties. Ending session."),
                    Part.from_end_session(reason="Max errors reached")
                ])
    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('validate_customer_identity_wrapper') and 'error' in part.function_response.response.get('result', {})) or \
           (part.has_function_response('lookup_npa_nxx_wrapper') and 'error' in part.function_response.response.get('result', {})):
            print('Executing Tool Failure detected, initiating transfer.')
            callback_context.variables['identification_status'] = 'Fail'
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, something went wrong finding your profile. Let me transfer you."),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])
    
    global_err = int(callback_context.variables.get('global_error_counter', 0))
    agent_err = int(callback_context.variables.get('speak_to_agent_counter', 0))
    if global_err >= 3 or agent_err >= 3:
        print('Global error or speak to agent counter reached threshold. Transferring.')
        callback_context.variables['identification_status'] = 'Fail'
        return LlmResponse.from_parts(parts=[
            Part.from_text("It seems we are having some difficulty today. Let me connect you with an agent."),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text:
            no_input_counter = int(callback_context.variables.get('local_noinput_counter', 0)) + 1
            callback_context.variables['local_noinput_counter'] = no_input_counter
            print(f'No input detected. Retry count: {no_input_counter}')
            if no_input_counter >= 3:
                print('Max no input retries reached. Transferring.')
                callback_context.variables['identification_status'] = 'Fail'
                return LlmResponse.from_parts(parts=[
                    Part.from_text("Sorry, I still didn't get that. We haven't heard from you. Let me transfer you."),
                    Part.from_agent_transfer(agent='bell_End_the_Conversation')
                ])
            return LlmResponse.from_parts(parts=[
                Part.from_text("I didn't quite catch that. Are you still there?")
            ])
            
    nomatch = int(callback_context.variables.get('local_nomatch_counter', 0))
    if nomatch >= 3:
        print('Max no match retries reached. Transferring.')
        callback_context.variables['identification_status'] = 'Fail'
        return LlmResponse.from_parts(parts=[
            Part.from_text("I am having trouble understanding. Let me connect you to an agent."),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("Executing before_model_callback for live agent handoff")
    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            
            if "sys.no-match-3" in text_lower or "sys.no-input-3" in text_lower:
                print("No match or no input threshold reached. Transferring to bell_End the Conversation.")
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            
            if "wrapup" in text_lower:
                print("Wrapup event triggered. Transitioning to END_SESSION.")
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason="wrapup event")
                ])
            
            if "no user activity detected" in text_lower:
                print("No user activity detected.")
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                if retry_count >= 3:
                    print("Max retries reached. Transferring to bell_End the Conversation.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                return LlmResponse.from_parts(
                    parts=[Part.from_text("Sorry, I didn't get that. Are you still there?")]
                )
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('update_routing_variables') and
            'error' in part.function_response.response.get('result', {})):
            print("Executing Tool Failure detected, initiating transfer to bell_aqd.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, something went wrong. Let me transfer you."),
                Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
            ])

    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            if "no user activity detected" in text_lower or "sys.no-input" in text_lower or "sys.no-match" in text_lower:
                print("No-input or No-match event detected.")
                errors = callback_context.variables.get("global_error_counter", 0) + 1
                callback_context.variables["global_error_counter"] = errors
                if errors >= 3:
                    print("Max errors reached, initiating transfer to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("I am having trouble understanding. Let me transfer you. / J'ai du mal à comprendre. Laissez-moi vous transférer."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                print("Playing bilingual fallback prompt.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("J'ai du mal à comprendre cette question. I didn't get that. Can you say it again?")
                ])
            
            if "wrapup" in text_lower:
                print("Wrapup event triggered, terminating session.")
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason="Wrapup event triggered")
                ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        input_text = (part.text or "").lower()
        if "no user activity detected" in input_text or "sys.no-input" in input_text or "sys.no-match" in input_text:
            print("Deterministic error prompt triggered for no-input/no-match event.")
            lang = callback_context.variables.get("language", "en").lower()
            if "fr" in lang:
                msg = "J'ai du mal à comprendre cette question. Pouvez-vous répéter?"
            else:
                msg = "I didn't get that. Can you say it again?"
            return LlmResponse.from_parts(parts=[Part.from_text(msg)])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('set_fallback_3_flag') and 'error' in part.function_response.response.get('result', {}):
            print('Executing Tool Failure detected, initiating transfer.')
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])

    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            if 'no user activity detected' in text_lower or 'sys.no-input-default' in text_lower:
                print('Silence timeout detected, routing to bell_aqd.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('I didn\'t get that. Can you say it again?'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            if 'sys.no-match-default' in text_lower:
                print('Unrecognized input detected, routing to bell_aqd.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('I didn\'t get that. Can you say it again?'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            if 'wrapup' in text_lower:
                print('Wrapup event detected, routing to END_SESSION.')
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason='wrapup')
                ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            lang = callback_context.variables.get("language", "English")
            
            if "no user activity detected" in text_lower or "sys.no-input" in text_lower:
                print("Silence timeout / no-input detected.")
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                
                if retry_count >= 3:
                    print("Max no-input retry count reached, triggering END_SESSION.")
                    msg = "Nous n'avons rien entendu. Au revoir." if "fr" in str(lang).lower() else "We haven't heard from you. Goodbye."
                    return LlmResponse.from_parts(parts=[
                        Part.from_text(msg),
                        Part.from_end_session(reason="Max no-input threshold reached")
                    ])
                
                print("Injecting standard no-input fallback prompt.")
                msg = "J'ai du mal à comprendre cette question." if "fr" in str(lang).lower() else "I didn't get that. Can you say it again?"
                return LlmResponse.from_parts(parts=[Part.from_text(msg)])
                
            elif "sys.no-match" in text_lower or "unrecognizable" in text_lower:
                print("Unrecognizable input / no-match detected.")
                err_count = callback_context.variables.get("global_error_counter", 0) + 1
                callback_context.variables["global_error_counter"] = err_count
                
                if err_count >= 3:
                    print("Max global error counter reached, triggering END_SESSION.")
                    msg = "Je ne comprends toujours pas. Au revoir." if "fr" in str(lang).lower() else "I'm still having trouble understanding. Goodbye."
                    return LlmResponse.from_parts(parts=[
                        Part.from_text(msg),
                        Part.from_end_session(reason="Max no-match threshold reached")
                    ])
                
                print("Injecting standard no-match fallback prompt.")
                msg = "Je ne comprends pas de quoi vous me parlez." if "fr" in str(lang).lower() else "Sorry, I didn't get that. Can you rephrase?"
                return LlmResponse.from_parts(parts=[Part.from_text(msg)])
                
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text:
            print('No-input detected in before_model_callback. Processing reprompt logic.')
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            
            if retry_count >= 3:
                print('Max no-input retries reached. Forcing escalation.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We haven\'t heard from you. Let me transfer you to an agent. / Nous ne vous entendons pas. Laissez-moi vous transférer à un agent.'),
                    Part.from_agent_transfer(agent='escalation_agent')
                ])
            
            print('No input detected. Playing bilingual reprompt.')
            return LlmResponse.from_parts(
                parts=[Part.from_text('I didn\'t get that. Can you say it again? / J\'ai du mal à comprendre cette question. Pouvez-vous répéter?')]
            )
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text:
            text = part.text.lower()
            
            # Check for wrapup event trigger
            if 'wrapup' in text:
                print('Executing wrapup event, initiating end session.')
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason='Wrapup Event')
                ])
            
            # Check for silence (no-input) or unrecognized input (no-match)
            if 'no user activity detected' in text or 'sys.no-input' in text or 'sys.no-match' in text or 'unrecognized' in text:
                print('Fallback condition detected, incrementing no_match_counter.')
                counter = callback_context.variables.get('no_match_counter', 0) + 1
                callback_context.variables['no_match_counter'] = counter
                
                if counter >= 2:
                    print('Max no_match_counter reached. Initiating end session.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('I am having trouble understanding your request. Please try again later. Goodbye.'),
                        Part.from_end_session(reason='Max Fallbacks')
                    ])
    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            retry_count = callback_context.variables.get("local_noinput_counter", 0) + 1
            callback_context.variables["local_noinput_counter"] = retry_count
            print(f"No user activity detected. Counter: {retry_count}")
            if retry_count < 3:
                return LlmResponse.from_parts(
                    parts=[Part.from_text("Hi, are you still there?")]
                )
                
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('trigger_self_help_sms'):
            result = part.function_response.response.get('result', {})
            if 'error' in result:
                print("Executing Tool Failure detected, initiating transfer to bell_aqd.")
                callback_context.variables["hardstop"] = True
                return LlmResponse.from_parts(parts=[
                    Part.from_text("Sorry, something went wrong with our system. Let me transfer you."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            elif not result.get('webhook_success', True) or result.get('status') == 'fail':
                sms_failures = callback_context.variables.get("sms_failure_counter", 0) + 1
                callback_context.variables["sms_failure_counter"] = sms_failures
                print(f"SMS dispatch failed. Counter: {sms_failures}")
                
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            
            if "wrapup" in text_lower:
                print("Wrapup event detected. Routing directly to END_SESSION.")
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason="wrapup_event")
                ])
            
            if "no user activity detected" in text_lower or "sys.no-input" in text_lower or "timeout" in text_lower or "unmatched" in text_lower or "no match" in text_lower:
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                print(f"No-input/No-match detected. Retry count incremented to: {retry_count}")
                
                lang = callback_context.variables.get("language", "English").lower()
                is_french = lang in ["french", "fr", "fr-ca"]
                
                if retry_count >= 3:
                    print("Max retries (3) reached. Playing final fallback message and routing to bell_IVR_Options.")
                    if is_french:
                        msg = '<speak>Vous pouvez consulter notre foire aux questions sur <say-as interpret-as="url">bell.ca/soutien-prepaye</say-as></speak>'
                    else:
                        msg = '<speak>You can check out our frequently asked questions at <say-as interpret-as="url">bell.ca/prepaid-support</say-as></speak>'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text(msg),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                else:
                    if retry_count == 1:
                        print("Retry count 1. Prompting user to try again.")
                        msg = "Désolé, je n'ai pas bien compris. Pourriez-vous réessayer?" if is_french else "Sorry, I didn’t quite get that. Can you try again?"
                        return LlmResponse.from_parts(parts=[Part.from_text(msg)])
                    elif retry_count == 2:
                        print("Retry count 2. Prompting user to repeat.")
                        msg = "Êtes-vous toujours là? Pouvez-vous répèter?" if is_french else "Are you still there? Can you repeat please?"
                        return LlmResponse.from_parts(parts=[Part.from_text(msg)])

    if callback_context.variables.get("first_turn", True):
        print("First turn execution: Delivering VA Survey placeholder and ending session.")
        callback_context.variables["first_turn"] = False
        lang = callback_context.variables.get("language", "English").lower()
        is_french = lang in ["french", "fr", "fr-ca"]
        msg = "VA Survey placeholder"
        return LlmResponse.from_parts(parts=[
            Part.from_text(msg),
            Part.from_end_session(reason="Survey Delivered")
        ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if callback_context.variables.get('first_turn', True):
        callback_context.variables['first_turn'] = False
        print('First turn detected. Routing immediately to bell_vr_pre_checks.')
        return LlmResponse.from_parts([
            Part.from_agent_transfer(agent='M4 TechSupportAndVirtualRepair')
        ])

    for part in callback_context.get_last_user_input():
        text = (part.text or '').lower()
        if 'wrapup' in text:
            print('Wrapup event triggered, ending session.')
            return LlmResponse.from_parts(parts=[
                Part.from_end_session(reason='wrapup_event')
            ])
        if 'no user activity detected' in text or 'sys.no-input' in text:
            retry_count = int(callback_context.variables.get('no_input_retry_count', 0)) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            print(f'sys.no-input detected. Retry count: {retry_count}')
            if retry_count >= 3:
                print('Max no-input retries reached, ending session.')
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason='max_no_input')
                ])
            print('Prompting user for no-input.')
            return LlmResponse.from_parts(parts=[
                Part.from_text("I didn't get that. Can you say it again? / J'ai du mal à comprendre cette question.")
            ])
        if 'sys.no-match' in text or 'unrecognized input' in text:
            error_count = int(callback_context.variables.get('global_error_counter', 0)) + 1
            callback_context.variables['global_error_counter'] = error_count
            print(f'sys.no-match detected. Error count: {error_count}')
            if error_count >= 3:
                print('Max no-match errors reached, ending session.')
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason='max_no_match')
                ])
            print('Prompting user for no-match.')
            return LlmResponse.from_parts(parts=[
                Part.from_text("I didn't get that. Can you say it again? / J'ai du mal à comprendre cette question.")
            ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('get_apbs_for_location_wrapper'):
                resp = part.function_response.response.get('result', {})
                err = part.function_response.response.get('error')
                if err or 'error' in resp:
                    print('Webhook error detected, setting webhook_success to False and ending flow.')
                    callback_context.variables['webhook_success'] = False
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('Sorry, we are experiencing technical difficulties. Disconnecting.'),
                        Part.from_end_session(reason='Webhook Failure')
                    ])

    interruptible = callback_context.variables.get('interruptible', 'N')
    if interruptible == 'Y':
        for part in callback_context.get_last_user_input():
            if part.text and ('no user activity detected' in part.text.lower() or 'no-input' in part.text.lower()):
                print('No input during APB playback, bypassing interrupt and proceeding to routing.')
                response = LlmResponse.from_parts(parts=[
                    Part.from_text('System Note: No user input detected. Proceed to evaluate routing flags (hang_up, agent_transfer).')
                ])
                response.partial = True
                return response

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # 1. Check is_home_phone
    is_home_phone = callback_context.variables.get('is_home_phone', False)
    if is_home_phone is True:
        print("Home phone detected, routing to bell_aqd.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("This number is a home phone. Let me transfer you."),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])

    # 2. Check refusal_counter
    refusal_counter = callback_context.variables.get('refusal_counter', 0)
    if refusal_counter > 2:
        print("Refusal counter exceeded, routing to END_FLOW.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("No problem, let's continue anyway."),
            Part.from_agent_transfer(agent='END_FLOW')
        ])
        
    # 3. Handle No-Input from User
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            retry_count = callback_context.variables.get("local_noinput_counter", 0) + 1
            callback_context.variables["local_noinput_counter"] = retry_count
            print(f"No input detected. Retry count: {retry_count}")
            if retry_count >= 3:
                print("Max no input retries reached, routing to bell_No_Input_3.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me transfer you."),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            print("Prompting user again for input.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't quite get that. Could you repeat?")]
            )

    # 4. Check tool failures
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('check_home_phone_status') and 'error' in part.function_response.response.get('result', {}):
                print("Tool failure detected for check_home_phone_status, routing to bell_aqd.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("Sorry, something went wrong. Let me transfer you."),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            if part.has_function_response('validate_and_format_phone_number') and 'error' in part.function_response.response.get('result', {}):
                print("Tool failure detected for validate_and_format_phone_number, routing to bell_aqd.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("Sorry, something went wrong. Let me transfer you."),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
                
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("Executing before_model_callback routing checks")
    
    # 1. Check Tool Failures (Pattern A) - Route to bell_aqd on timeout/errors
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('acut_search_retrieve_wrapper'):
                func_response = part.function_response.response.get('result', {})
                if 'error' in func_response:
                    print("Executing Tool Failure detected, initiating transfer to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Sorry, we're having trouble accessing the address system right now. Let me transfer you to an agent."),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
    
    # 2. Check for No-Input / Timeout events (Pattern E)
    user_inputs = callback_context.get_last_user_input()
    if user_inputs:
        for part in user_inputs:
            if part.text and "no user activity detected" in part.text.lower():
                print("No-input detected in callback")
                
                # Increment counters
                no_input_count = callback_context.variables.get("local_noinput_counter", 0) + 1
                global_err_count = callback_context.variables.get("global_error_counter", 0) + 1
                
                callback_context.variables["local_noinput_counter"] = no_input_count
                callback_context.variables["global_error_counter"] = global_err_count
                
                # Route based on global error threshold
                if global_err_count >= 3:
                    print("Global error limit reached, transferring to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We seem to be having some trouble. Let me get you an agent."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                
                # Route based on consecutive no-input threshold
                if no_input_count >= 3:
                    print("Consecutive no-input limit reached, transferring to bell_No_Input_3.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("I still haven't heard from you. Let me transfer you to someone who can help."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                
                # Local retry for no-input
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I didn't quite get that. Are you still there?")
                ])
    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print('Executing before_model_callback for bell_appt_mgmt_mya_pitch_1')
    
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('evaluate_mya_eligibility_wrapper'):
            resp = part.function_response.response.get('result', {})
            if 'error' in resp:
                print('Tool Failure detected in evaluate_mya_eligibility_wrapper, initiating END_SESSION.')
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason='Webhook Error')
                ])

    is_no_input = False
    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or part.text.strip() == ''):
            is_no_input = True
            break
    
    if is_no_input:
        print('No user activity detected. Tracking counters.')
        ni_count = callback_context.variables.get('local_noinput_counter', 0) + 1
        callback_context.variables['local_noinput_counter'] = ni_count
        ge_count = callback_context.variables.get('global_error_counter', 0) + 1
        callback_context.variables['global_error_counter'] = ge_count
        
        if ge_count >= 3:
            print('global_error_counter >= 3, transferring to bell_aqd.')
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
        if ni_count >= 3:
            print('local_noinput_counter >= 3, transferring to bell_No_Input_3.')
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
        
        print('Re-prompting user for SMS offer on No Input.')
        lang = callback_context.variables.get('language', 'en').lower()
        if 'fr' in lang:
            msg = "Connaissez-vous notre appli Gérez votre rendez-vous? Il s'agit d'un moyen pratique de consulter, de replanifier ou d'annuler votre rendez-vous directement à partir de votre téléphone. Je vais envoyer un texto sur l'appareil au moyen duquel vous appelez, afin de vous permettre de commencer. Est-ce que cela vous convient?"
        else:
            msg = "Are you aware of our Manage Your Appointment App? It is a convenient way to view, reschedule, or cancel your appointment directly from your phone. I'll send you a text to the device you're calling from, so that you can get started. Is that alright? You can say 'Yes' or 'No'."
        return LlmResponse.from_parts(parts=[Part.from_text(msg)])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text:
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            if retry_count >= 3:
                print('Max no-input reached. Triggering bell_No_Input_3.')
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            print('No input detected, incrementing counter and prompting.')
            return LlmResponse.from_parts(parts=[Part.from_text('I didn\'t get that. Can you say it again?')])

    no_match_count = callback_context.variables.get('global_error_counter', 0)
    if no_match_count >= 3:
        print('Max no-match reached. Triggering bell_No_Match_3.')
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])

    if llm_request.contents and len(llm_request.contents) > 0:
        for part in llm_request.contents[-1].parts:
            for tool_name in ['get_agent_queue_details', 'send_agent_transfer_data']:
                if part.has_function_response(tool_name):
                    res = part.function_response.response.get('result', {})
                    if 'error' in res or res.get('status') == 500 or res.get('timeout'):
                        print(f'Executing Tool Failure detected in {tool_name}, transitioning to AQD_System_Error.')
                        return LlmResponse.from_parts(parts=[
                            Part.from_text('Sorry, I\'m unable to transfer you to an agent due to an unexpected system issue. Please try calling us back later.'),
                            Part.from_end_session(reason='AQD_System_Error')
                        ])
    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('evaluate_routing_rules') and 'error' in part.function_response.response.get('result', {}):
            print("Executing Tool Failure detected in evaluate_routing_rules, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, something went wrong. Let me transfer you."),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])
        if part.has_function_response('get_intent_sdl_mapping_wrapper') and 'error' in part.function_response.response.get('result', {}):
            print("Executing Tool Failure detected in get_intent_sdl_mapping_wrapper, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, something went wrong. Let me transfer you."),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])

    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            if "no user activity detected" in text_lower or "sys.no-input" in text_lower:
                no_input_counter = callback_context.variables.get("local_noinput_counter", 0) + 1
                global_err = callback_context.variables.get("global_error_counter", 0) + 1
                callback_context.variables["local_noinput_counter"] = no_input_counter
                callback_context.variables["global_error_counter"] = global_err
                
                print(f"No-input detected. Local: {no_input_counter}, Global: {global_err}")
                
                if global_err >= 3:
                    print("Max global errors reached, routing to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We are having trouble. Let me transfer you to an agent."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                if no_input_counter >= 3:
                    print("Max no-input reached, routing to bell_No_Input_3.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We haven't heard from you. Let me transfer you."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                return LlmResponse.from_parts(parts=[Part.from_text("Hi, are you still there?")])
                
            elif "sys.no-match" in text_lower or "unrecognized input" in text_lower:
                no_match_counter = callback_context.variables.get("local_nomatch_counter", 0) + 1
                global_err = callback_context.variables.get("global_error_counter", 0) + 1
                callback_context.variables["local_nomatch_counter"] = no_match_counter
                callback_context.variables["global_error_counter"] = global_err
                
                print(f"No-match detected. Local: {no_match_counter}, Global: {global_err}")
                
                if global_err >= 3:
                    print("Max global errors reached, routing to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We are having trouble. Let me transfer you to an agent."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                if no_match_counter >= 3:
                    print("Max no-match reached, routing to bell_No_Match_3.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("I'm still having trouble understanding. Let me transfer you."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                return LlmResponse.from_parts(parts=[Part.from_text("I didn't quite get that. Could you repeat?")])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('set_session_variable') and 'error' in part.function_response.response.get('result', {}):
            print("Executing Tool Failure detected, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, something went wrong. Let me transfer you."),
                Part.from_agent_transfer(agent="escalation_agent")
            ])

    for part in callback_context.get_last_user_input():
        if part.text:
            text = part.text.lower()
            if "wrapup" in text:
                print("Executing wrapup detected, ending session.")
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason="wrapup")
                ])
            
            if "no user activity detected" in text or "sys.no-match" in text:
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                print(f"Executing no-match/no-input check. Count: {retry_count}")
                if retry_count >= 3:
                    print("Executing Max retries reached, transferring.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We haven't heard from you or couldn't understand. Let me transfer you to an agent."),
                        Part.from_agent_transfer(agent="escalation_agent")
                    ])
                return LlmResponse.from_parts(
                    parts=[Part.from_text("I didn't get that. Can you say it again?")]
                )
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    lang = str(callback_context.variables.get('language', 'en')).lower()
    
    for part in callback_context.get_last_user_input():
        if part.text:
            text = part.text.lower()
            
            if 'wrapup' in text:
                print('Wrapup event triggered, ending session.')
                return LlmResponse.from_parts(parts=[
                    Part.from_end_session(reason='Wrapup event')
                ])
            
            if 'no user activity detected' in text or 'sys.no-input' in text:
                print('Silence/timeout detected, incrementing retry count.')
                retry_count = int(callback_context.variables.get('no_input_retry_count', 0)) + 1
                callback_context.variables['no_input_retry_count'] = retry_count
                
                if retry_count >= 3:
                    print('Max no-input retries exceeded. Terminating session.')
                    end_msg = "We haven't heard from you. Let me transfer you or disconnect." if 'en' in lang else "Nous n'avons rien entendu. Au revoir."
                    return LlmResponse.from_parts(parts=[
                        Part.from_text(end_msg),
                        Part.from_end_session(reason='Max no-input retries')
                    ])
                
                print('Returning standard localized reprompt for no-input.')
                reprompt = "Sorry, I didn't get that. Can you say it again?" if 'en' in lang else "J'ai du mal à comprendre cette question. Pouvez-vous répéter ?"
                return LlmResponse.from_parts(parts=[Part.from_text(reprompt)])
            
            if 'sys.no-match' in text:
                print('Unrecognized input detected, incrementing error counter.')
                error_count = int(callback_context.variables.get('global_error_counter', 0)) + 1
                callback_context.variables['global_error_counter'] = error_count
                
                if error_count >= 3:
                    print('Max no-match retries exceeded. Escalating/Ending Session.')
                    end_msg = "I am having trouble understanding. Goodbye." if 'en' in lang else "J'ai du mal à comprendre. Au revoir."
                    return LlmResponse.from_parts(parts=[
                        Part.from_text(end_msg),
                        Part.from_end_session(reason='Max no-match retries')
                    ])
                
                print('Returning standard localized reprompt for no-match.')
                reprompt = "Sorry, what was that?" if 'en' in lang else "Je n'ai pas saisi ce que vous avez dit."
                return LlmResponse.from_parts(parts=[Part.from_text(reprompt)])
                
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text:
            print("No input detected. Playing bilingual error prompt.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("I didn't get that. Can you say it again? J'ai du mal à comprendre cette question. J'ai mal compris votre demande.")
            ])

    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('increment_global_error_counter'):
                result = part.function_response.response.get('result', {})
                if 'error' in result:
                    print("Tool failure detected. Initiating transfer to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Sorry, something went wrong. Let me transfer you."),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
                
                counter = result.get('global_error_counter', 0)
                if counter >= 3:
                    print("Global error counter >= 3. Transferring to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
                else:
                    print("Global error counter < 3. Ending Flow.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_end_session(reason='End Flow')
                    ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # PATTERN B: Terminate/Transfer Session on Tool Failures
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if (part.has_function_response('get_did_data_wrapper') and
                'error' in part.function_response.response.get('result', {})):
                print("Executing Tool Failure detected for get_did_data_wrapper, initiating transfer.")
                callback_context.variables['identification_status'] = 'Fail'
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, there was a problem on our side. I will still do my best to help you.'),
                    Part.from_agent_transfer(agent='target_default_start')
                ])
            if (part.has_function_response('customer_identification_wrapper') and
                'error' in part.function_response.response.get('result', {})):
                print("Executing Tool Failure detected for customer_identification_wrapper, initiating transfer.")
                callback_context.variables['identification_status'] = 'Fail'
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, there was a problem on our side and I cannot find your profile. I will still do my best to help you.'),
                    Part.from_agent_transfer(agent='target_default_start')
                ])

    # PATTERN E: Custom Response for No-Input / No-Match Timeout
    user_inputs = callback_context.get_last_user_input()
    if user_inputs:
        for part in user_inputs:
            if part.text and ("no user activity detected" in part.text.lower() or "sys.no-match" in part.text.lower()):
                retry_count = callback_context.variables.get('global_error_counter', 0) + 1
                callback_context.variables['global_error_counter'] = retry_count
                if retry_count >= 3:
                    print("Max retries reached for no-input/no-match. Initiating transfer to AQD.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('I am having a hard time understanding. Let me transfer you to an agent.'),
                        Part.from_agent_transfer(agent='target_aqd')
                    ])
                print("No input or match detected. Letting agent reprompt user.")

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text.lower():
            print('No input detected, incrementing global_error_counter')
            err_count = callback_context.variables.get('global_error_counter', 0) + 1
            callback_context.variables['global_error_counter'] = err_count

    global_err = callback_context.variables.get('global_error_counter', 0)
    if global_err >= 3:
        print('Global error limit reached. Routing to bell_aqd.')
        callback_context.variables['identification_status'] = 'Fail'
        return LlmResponse.from_parts(parts=[
            Part.from_text('We seem to be having trouble. Let me get someone to help you.'),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])

    no_match_count = callback_context.variables.get('no_match_counter', 0)
    if no_match_count >= 2:
        print('No match limit reached. Routing to bell_aqd.')
        callback_context.variables['identification_status'] = 'Fail'
        return LlmResponse.from_parts(parts=[
            Part.from_text('I cannot seem to find that account. Let me transfer you.'),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])

    for part in llm_request.contents[-1].parts:
        if part.has_function_response('extract_multiban_profile_metrics') or part.has_function_response('filter_customer_accounts_by_criteria'):
            if 'error' in part.function_response.response.get('result', {}):
                print('Executing Tool Failure detected, initiating transfer.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, something went wrong retrieving your account. Let me transfer you.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    cc_failed = callback_context.variables.get('cc_failed_attempt', 0)
    if cc_failed >= 3:
        print('Executing CC max failures detected, initiating transfer to Feedback.')
        return LlmResponse.from_parts(parts=[
            Part.from_text("Unfortunately, your credit card payment didn't go through. Please contact your credit card provider for more information."),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])

    for part in llm_request.contents[-1].parts:
        if part.has_function_response('process_clp_payment_wrapper') or part.has_function_response('get_clp_ban_profile_wrapper'):
            response_data = part.function_response.response.get('result', {})
            if 'error' in response_data:
                print('Executing Tool Failure detected, playing webhook failure confirmation and transferring to Feedback.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text("Thanks for your patience. It looks like I'm having trouble processing your payment at this time. There's nothing wrong on your end. Please call again later to learn about your updated credit limit balance."),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    for part in callback_context.get_last_user_input():
        text_content = part.text.lower() if part.text else ""
        if "no user activity detected" in text_content or "unrecognized" in text_content:
            retry_count = callback_context.variables.get('global_error_counter', 0) + 1
            callback_context.variables['global_error_counter'] = retry_count
            if retry_count >= 3:
                print('Executing Max No-Input / No-Match reached, transferring to handover.')
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
        elif text_content:
            callback_context.variables['global_error_counter'] = 0

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            if 'no user activity detected' in text_lower or 'sys.no-match' in text_lower or 'sys.no-input' in text_lower or 'no match' in text_lower:
                retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
                callback_context.variables['no_input_retry_count'] = retry_count
                if retry_count >= 3:
                    print('Max no-input/no-match threshold reached. Transferring to bell_determine_handover.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('We haven\'t heard from you or are having trouble understanding. Let me transfer you to an agent.'),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
                print('No input/match detected, incrementing retry count.')
                
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('process_payment_wrapper') or part.has_function_response('fetch_account_profile_wrapper'):
                if 'error' in part.function_response.response.get('result', {}):
                    print('Webhook API timeout or error detected. Transitioning to HANDLE_SYSTEM_FAILURE.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('Thanks for your patience. It looks like I\'m having trouble getting your updated account information right now. I can send a text to the device you\'re calling from, so that you may view your account details yourself in the MyBell App. Is that alright?')
                    ])
                    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if callback_context.variables.get('first_turn', True):
        callback_context.variables['first_turn'] = False
        callback_context.variables['apb_location_id'] = 70012
        callback_context.variables['coming_from'] = 'bell_rehit'
        print('Initialized session context variables for bell_rehit.')

    for part in callback_context.get_last_user_input():
        text = part.text or ''
        if 'no user activity detected' in text.lower() or 'sys.no-match' in text.lower() or 'sys.no-input' in text.lower():
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            print(f'Retry triggered. Count: {retry_count}')
            if retry_count >= 3:
                callback_context.variables['hardstop'] = True
                callback_context.variables['flow_id'] = '29168022-af9d-47b0-8051-575528402df8'
                callback_context.variables['page_name'] = 'Authentication Check'
                print('Max retries reached. Initiating transfer to bell_aqd.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We are having trouble understanding. Let me transfer you to a specialist.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            return LlmResponse.from_parts(
                parts=[Part.from_text('I didn\'t quite get that. Can you try again?')]
            )

    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('search_by_tn_wrapper') or part.has_function_response('extract_tv_account_details'):
                resp = part.function_response.response.get('result', {})
                if 'error' in resp or callback_context.variables.get('webhook_success') is False:
                    print('Executing Tool Failure detected, initiating transfer to bell_rehit_SMS.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('I am currently unable to access your profile. Let me transfer you to an alternative system.'),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
                    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or 'sys.no-input' in part.text.lower()):
            callback_context.variables['local_noinput_counter'] = callback_context.variables.get('local_noinput_counter', 0) + 1
            callback_context.variables['global_error_counter'] = callback_context.variables.get('global_error_counter', 0) + 1
            print('No input detected. Incremented counters.')

    global_error_counter = callback_context.variables.get('global_error_counter', 0)
    if global_error_counter >= 3:
        print('Global error counter limit reached, routing to bell_aqd.')
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])

    local_noinput_counter = callback_context.variables.get('local_noinput_counter', 0)
    if local_noinput_counter >= 3:
        print('No input counter limit reached, routing to bell_No_Input_3.')
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])

    local_nomatch_counter = callback_context.variables.get('local_nomatch_counter', 0)
    if local_nomatch_counter >= 3:
        print('No match counter limit reached, routing to bell_No_Match_3.')
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    try:
        if not llm_request.contents:
            return None

        # Tool Failure Routing
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('set_tv_sync_sms_variables') and 'error' in part.function_response.response.get('result', {}):
                print('Executing Tool Failure detected, initiating transfer.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

        # No Input / Silence Timeout Overrides
        for part in callback_context.get_last_user_input():
            if part.text and 'no user activity detected' in part.text.lower():
                retry_count = callback_context.variables.get('local_noinput_counter', 0) + 1
                callback_context.variables['local_noinput_counter'] = retry_count
                if retry_count >= 2:
                    print('Max no-input retries reached, routing to bell_aqd.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('We have not heard from you. Let me transfer you.'),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
                print('No-input detected, playing prompt.')
                lang = str(callback_context.variables.get('language', 'en')).lower()
                prompt = 'Hi, are you still there?' if 'en' in lang else 'Bonjour, êtes-vous toujours là?'
                return LlmResponse.from_parts(parts=[Part.from_text(prompt)])

        # No Match / Hallucination Escapes
        global_err = callback_context.variables.get('global_error_counter', 0)
        if global_err >= 3:
            print('Max consecutive errors detected, routing to bell_No_Match_3.')
            return LlmResponse.from_parts(parts=[
                Part.from_text('I am having trouble understanding. Let me transfer you.'),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])

    except Exception as e:
        print(f'Callback crash: {e}')

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    global_err = int(callback_context.variables.get('global_error_counter') or 0)
    local_nomatch = int(callback_context.variables.get('local_nomatch_counter') or 0)
    local_noinput = int(callback_context.variables.get('local_noinput_counter') or 0)
    
    if global_err >= 3:
        print('Global error counter reached, transferring to bell_aqd')
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
        
    if local_nomatch >= 3:
        print('Local no-match counter reached, transferring to bell_No_Match_3')
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
        
    if local_noinput >= 3:
        print('Local no-input counter reached, transferring to bell_No_Input_3')
        return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
        
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text:
            local_noinput += 1
            global_err += 1
            callback_context.variables['local_noinput_counter'] = local_noinput
            callback_context.variables['global_error_counter'] = global_err
            
            if global_err >= 3:
                print('Global error counter reached via no-input, transferring to bell_aqd')
                return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
                
            if local_noinput >= 3:
                print('Max no-input reached, transferring to bell_No_Input_3')
                return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')])
                
            print(f'No-input detected. Retry {local_noinput}')
            lang = str(callback_context.variables.get('language', '')).lower()
            if lang == 'fr-ca':
                msg = "Je n'ai pas saisi ce que vous avez dit. J'ai du mal à comprendre cette question."
            else:
                msg = "I didn't quite catch that. I'm having trouble understanding."
            return LlmResponse.from_parts(parts=[Part.from_text(msg)])
            
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('prepare_sms_variables') and 'error' in part.function_response.response.get('result', {})):
            print('Tool error detected in prepare_sms_variables, escalating.')
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # 1. Handle explicit wrapup event
    if callback_context.variables.get('event_type') == 'wrapup':
        print('Wrapup event detected, terminating session.')
        return LlmResponse.from_parts(parts=[Part.from_end_session(reason='wrapup event')])

    # 2. Deterministic Routing Evaluation on First Turn
    if callback_context.variables.get('first_turn', True):
        callback_context.variables['first_turn'] = False
        route = callback_context.variables.get('route')
        print(f'Evaluating routing for target: {route}')

        if route == 'sales_add_to_existing_account':
            print('Routing to sales_add_to_existing_account')
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='sales_add_to_existing_account')])
        elif route == 'sales_plans_inquiry':
            print('Routing to sales_plans_inquiry')
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent='sales_plans_inquiry')])
        else:
            print('No valid route identified, ending session to return to parent.')
            return LlmResponse.from_parts(parts=[Part.from_end_session(reason='Invalid or missing route')])

    # 3. No-Input & No-Match Reprompting
    user_input = ''
    for part in callback_context.get_last_user_input():
        if part.text:
            user_input += part.text.lower()

    if user_input:
        if 'no user activity detected' in user_input:
            print('sys.no-input-default triggered.')
        else:
            print('sys.no-match-default triggered.')

        err_count = callback_context.variables.get('global_error_counter', 0)
        callback_context.variables['global_error_counter'] = err_count + 1

        return LlmResponse.from_parts(parts=[
            Part.from_text("I didn't get that. Can you say it again? J'ai du mal à comprendre cette question.")
        ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    try:
        user_inputs = callback_context.get_last_user_input()
        if user_inputs:
            for part in user_inputs:
                if part.text:
                    text_lower = part.text.lower()
                    if "no user activity detected" in text_lower or "sys.no-input-default" in text_lower:
                        print("Silence/No-input detected, playing standard bilingual reprompt.")
                        fallback_counter = callback_context.variables.get("fallback_counter", 0) + 1
                        callback_context.variables["fallback_counter"] = fallback_counter
                        reprompt = "Je n'ai pas compris. Pouvez-vous répéter, s'il vous plaît ? I didn't get that. Can you say it again?"
                        return LlmResponse.from_parts(parts=[Part.from_text(reprompt)])
                    
                    if "sys.no-match-default" in text_lower:
                        print("No-match event detected, playing standard bilingual reprompt.")
                        fallback_counter = callback_context.variables.get("fallback_counter", 0) + 1
                        callback_context.variables["fallback_counter"] = fallback_counter
                        reprompt = "Je n'ai pas compris. Pouvez-vous répéter, s'il vous plaît ? I didn't get that. Can you say it again?"
                        return LlmResponse.from_parts(parts=[Part.from_text(reprompt)])
                    
                    if "wrapup" in text_lower:
                        print("Wrapup event detected, routing to END_SESSION.")
                        return LlmResponse.from_parts(parts=[
                            Part.from_end_session(reason="Wrapup event")
                        ])
                        
        if llm_request.contents:
            for part in llm_request.contents[-1].parts:
                if part.has_function_response('reset_session_counters'):
                    result = part.function_response.response.get('result', {})
                    if 'error' in result:
                        print("Tool failure detected in reset_session_counters, terminating session.")
                        return LlmResponse.from_parts(parts=[
                            Part.from_text("Sorry, something went wrong. Please call back later."),
                            Part.from_end_session(reason='Tool Failure')
                        ])
    except Exception as e:
        print(f"Error in before_model_callback: {e}")
        
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    try:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('get_full_customer_profile_wrapper') and 'error' in part.function_response.response.get('result', {}):
                print('Executing Tool Failure detected, bypassing validation and routing to bell_aqd.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('I am having trouble accessing your profile. Let me connect you with an agent who can help.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
        for part in callback_context.get_last_user_input():
            if part.text and 'no user activity detected' in part.text:
                retry_count = callback_context.variables.get('local_noinput_counter', 0) + 1
                callback_context.variables['local_noinput_counter'] = retry_count
                if retry_count >= 3:
                    print('Max no-input limit reached. Routing to bell_No_Input_3.')
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('We haven\'t heard from you. Let me transfer you.'),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
                print('No-input detected, prompting user.')
                return LlmResponse.from_parts(
                    parts=[Part.from_text('I didn\'t catch that. Are you still there?')]
                )
    except Exception as e:
        print(f'Error in before_model_callback: {e}')
    return None

from typing import Optional
import re

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # 1. Evaluate No-Input Retries
    user_input = callback_context.get_last_user_input()
    if user_input:
        for part in user_input:
            if part.text and "no user activity detected" in part.text.lower():
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                print(f"No input detected. Retry count: {retry_count}")
                if retry_count > 3:
                    print("Max no-input retries reached, ending session.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We haven't received a valid response. Exiting test wrapper."),
                        Part.from_end_session(reason="Max No-Input Retries")
                    ])

    # 2. Sanitize Exactly 10-Digit Inputs for CLID/TFN Collection
    if user_input:
        for part in user_input:
            if part.text:
                digits = re.sub(r'\D', '', part.text)
                if len(digits) == 10:
                    print("Exact 10 digits found. Stripping formatting to ensure strict numerical representation for LLM.")
                    part.text = digits

    # 3. Track Tool Failures to trigger END_SESSION externally
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('get_tester_details_wrapper'):
                res = part.function_response.response.get('result', {})
                if 'error' in res or not res.get('success', False):
                    count = callback_context.variables.get('get_tester_details_fail_count', 0) + 1
                    callback_context.variables['get_tester_details_fail_count'] = count
                    print(f"get_tester_details_wrapper failed. New count: {count}")

            if part.has_function_response('intake_routing_wrapper'):
                res = part.function_response.response.get('result', {})
                if 'error' in res or not res.get('success', False):
                    count = callback_context.variables.get('intake_routing_fail_count', 0) + 1
                    callback_context.variables['intake_routing_fail_count'] = count
                    print(f"intake_routing_wrapper failed. New count: {count}")

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Check for tool failures
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('clear_infobot_flag') and
            'error' in part.function_response.response.get('result', {})):
            print("Executing Tool Failure detected, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, something went wrong. Let me transfer you."),
                Part.from_agent_transfer(agent="escalation_agent")
            ])

    # Check for No-Input / No-Match conditions
    for part in callback_context.get_last_user_input():
        if part.text:
            text_input = part.text.lower()
            if "no user activity detected" in text_input or "sys.no-input" in text_input or "sys.no-match" in text_input:
                print("No input or match detected, incrementing retry counter.")
                retry_count = callback_context.variables.get("global_error_counter", 0) + 1
                callback_context.variables["global_error_counter"] = retry_count
                if retry_count >= 3:
                    print("Max retries exceeded, ending session.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("I am having trouble understanding. Please call back later."),
                        Part.from_end_session(reason="Max Retries Exceeded")
                    ])
                
                print("Playing standard retry prompt.")
                lang = callback_context.variables.get("language", "en").lower()
                if lang == "fr":
                    prompt = "J'ai du mal à comprendre cette question. J'ai mal compris votre demande. Je n'ai pas saisi ce que vous avez dit."
                else:
                    prompt = "I didn't get that. Can you say it again? I missed what you said."
                
                return LlmResponse.from_parts(parts=[Part.from_text(prompt)])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    no_input_val = callback_context.variables.get('local_noinput_counter', 0)
    no_match_val = callback_context.variables.get('local_nomatch_counter', 0)
    
    last_input = callback_context.get_last_user_input()
    if last_input:
        for part in last_input:
            if part.text and "no user activity detected" in part.text.lower():
                no_input_val += 1
                callback_context.variables['local_noinput_counter'] = no_input_val
                print(f"No input detected. Counter: {no_input_val}")
                
    if no_input_val >= 3:
        print("Max no-input reached. Transferring to bell_No_Input_3.")
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    if no_match_val >= 3:
        print("Max no-match reached. Transferring to bell_No_Match_3.")
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])
        
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('fetch_routing_configuration_wrapper') or part.has_function_response('execute_dam_transfer_wrapper'):
                result = part.function_response.response.get('result', {})
                if 'error' in result:
                    print("Executing Tool Failure detected, initiating transfer to bell_wrapup.")
                    callback_context.variables['webhook_success'] = False
                    return LlmResponse.from_parts(parts=[
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
                    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    global_error = callback_context.variables.get('global_error_counter', 0)
    global_error = int(global_error) if str(global_error).isdigit() else 0
    if global_error >= 3:
        print("Global error counter reached 3. Routing to bell_aqd_agent.")
        callback_context.variables['global_error_counter'] = 0
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent='bell_aqd_agent')
        ])
        
    local_noinput = callback_context.variables.get('local_noinput_counter', 0)
    local_noinput = int(local_noinput) if str(local_noinput).isdigit() else 0
    if local_noinput >= 3:
        print("No-input counter reached 3. Routing to bell_no_input_3_agent.")
        callback_context.variables['local_noinput_counter'] = 0
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent='bell_no_input_3_agent')
        ])

    local_nomatch = callback_context.variables.get('local_nomatch_counter', 0)
    local_nomatch = int(local_nomatch) if str(local_nomatch).isdigit() else 0
    if local_nomatch >= 3:
        print("No-match counter reached 3. Routing to bell_no_match_3_agent.")
        callback_context.variables['local_nomatch_counter'] = 0
        return LlmResponse.from_parts(parts=[
            Part.from_agent_transfer(agent='bell_no_match_3_agent')
        ])
        
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('execute_business_transfer_protocol'):
                response_dict = part.function_response.response
                if 'error' in response_dict.get('result', {}):
                    print("Tool Failure detected in transfer protocol, initiating wrapup.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_agent_transfer(agent='bell_wrapup_agent')
                    ])
                    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            if retry_count >= 3:
                print("Max no-input retries reached, transferring to bell_wrapup.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            print(f"No-input detected, retry {retry_count}.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("Hi, are you still there?")]
            )
            
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response("execute_ivr_handoff_bundle") and "error" in part.function_response.response.get("result", {}):
                print("Executing Tool Failure detected, initiating transfer to bell_wrapup.")
                callback_context.variables["webhook_success"] = False
                return LlmResponse.from_parts(parts=[
                    Part.from_text("Sorry, something went wrong with the transfer setup. Let me transfer you to support."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
                
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        text = part.text.lower() if part.text else ''
        if 'no user activity detected' in text or 'silence' in text:
            print('No user activity detected. Handling retry logic.')
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            if retry_count >= 3:
                print('Max no-input retries reached, escalating.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('I didn\'t get that. Let me connect you to an agent.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            return LlmResponse.from_parts(parts=[
                Part.from_text('I didn\'t get that. Can you say it again?')
            ])

    for part in llm_request.contents[-1].parts:
        if part.has_function_response('vr_start_process_wrapper'):
            response_dict = part.function_response.response.get('result', {})
            if not response_dict.get('webhook_success', True):
                error_str = str(response_dict.get('error', '')).lower()
                print(f'Executing Tool Failure detected: {error_str}')
                
                known_errors = ['500', 'timeout', 'bad-request', 'not-found', 'rejected', 'unavailable']
                is_known = any(err in error_str for err in known_errors)
                
                if is_known:
                    counter = callback_context.variables.get('counter_start_task', 0) + 1
                    callback_context.variables['counter_start_task'] = counter
                    
                    if counter <= 2:
                        print(f'Retrying start-process, attempt {counter}')
                        response = LlmResponse.from_parts(parts=[
                            Part.from_text('Oops! Something went wrong on my end. Let me try that again for you.')
                        ])
                        response.partial = True
                        return response
                    else:
                        print('Max API retries reached. Routing to failure handler.')
                        return LlmResponse.from_parts(parts=[
                            Part.from_text('I need to connect you to an agent.'),
                            Part.from_agent_transfer(agent='M4 TechSupportAndVirtualRepair')
                        ])
                else:
                    print('Unrecognized error detected. Hardstop and route to AQD.')
                    callback_context.variables['hardstop'] = True
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('Oops! Something went wrong on my end. I need to connect you to an agent.'),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    user_input = ""
    for part in callback_context.get_last_user_input():
        if part.text:
            user_input += part.text.lower()
    
    error_msg = "J'ai du mal à comprendre cette question. J'ai mal compris votre demande. Je n'ai pas saisi ce que vous avez dit. Je crois que je ne vous suis pas. Je ne comprends pas de quoi vous me parlez."
    
    if "no user activity detected" in user_input:
        print("No input detected (sys.no-input), forcing end session.")
        return LlmResponse.from_parts(parts=[
            Part.from_text(error_msg),
            Part.from_end_session(reason="sys.no-input")
        ])
        
    if callback_context.variables.get("first_turn", True):
        print("First turn detected: Executing deterministic wrapup message based on language.")
        callback_context.variables["first_turn"] = False
        lang = str(callback_context.variables.get("language", "english")).lower()
        
        if "fr" in lang or "french" in lang:
            wrapup_msg = "Merci d'avoir appelé. Au revoir!"
        else:
            wrapup_msg = "Thanks for calling. Goodbye!"
            
        return LlmResponse.from_parts(parts=[
            Part.from_text(wrapup_msg),
            Part.from_end_session(reason="wrapup")
        ])
        
    print("Unexpected speech detected (sys.no-match), forcing end session.")
    return LlmResponse.from_parts(parts=[
        Part.from_text(error_msg),
        Part.from_end_session(reason="sys.no-match")
    ])

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("Executing before_model_callback logic gate.")
    
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('update_routing_context') and 'error' in part.function_response.response.get('result', {}):
            print("Executing Tool Failure detected, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, something went wrong. Let me transfer you."),
                Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
            ])
            
    error_type = None
    for part in callback_context.get_last_user_input():
        text = part.text.lower() if part.text else ""
        if not text or "no user activity detected" in text or "sys.no-input" in text:
            error_type = "no_input"
        elif "sys.no-match" in text:
            error_type = "no_match"
            
    if error_type:
        print(f"Decision: {error_type} detected.")
        retry_count = callback_context.variables.get("global_error_counter", 0) + 1
        callback_context.variables["global_error_counter"] = retry_count
        
        if retry_count >= 3:
            print(f"Decision: Max retry reached for {error_type}, transferring.")
            agent_target = "bell_No_Input_3" if error_type == "no_input" else "bell_No_Match_3"
            return LlmResponse.from_parts(parts=[
                Part.from_text("Let me transfer you to an agent."),
                Part.from_agent_transfer(agent=agent_target)
            ])
            
        print("Decision: Prompting user for retry with bilingual message.")
        return LlmResponse.from_parts(parts=[
            Part.from_text("I didn't get that. Can you say it again? / J'ai du mal à comprendre cette question.")
        ])
        
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('set_route_state') and 'error' in part.function_response.response.get('result', {}):
                print("Executing Tool Failure detected, initiating transfer.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                    Part.from_agent_transfer(agent='Live_Agent_Transfer')
                ])

    user_inputs = callback_context.get_last_user_input()
    if user_inputs:
        for part in user_inputs:
            if part.text and ("no user activity detected" in part.text.lower() or "sys.no-match" in part.text.lower()):
                retry_count = int(callback_context.variables.get("no_input_retry_count", 0)) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                print(f"No-input/No-match event detected. Count: {retry_count}")
                if retry_count >= 3:
                    print("Max retries reached. Initiating Live_Agent_Transfer.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("I'm having trouble understanding. Let me transfer you to someone who can help."),
                        Part.from_agent_transfer(agent="Live_Agent_Transfer")
                    ])
                print("Prompting user to repeat.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I didn't get that. Can you say it again? / J'ai du mal à comprendre cette question. Pouvez-vous répéter?")
                ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # 1. Tool Failure Handling - Terminate Session
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response("trigger_business_dam_transfer") and
            "error" in part.function_response.response.get("result", {})):
            print("Executing Tool Failure detected, ending session.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, something went wrong with the transfer. Please call back later."),
                Part.from_end_session(reason="Tool Failure")
            ])

    # 2. No-Input / Silence Timeout Handling
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text:
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            print(f"No-input detected. Retry count: {retry_count}")
            
            if retry_count >= 3:
                print("Max no-input retries reached, ending session.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Ending the session."),
                    Part.from_end_session(reason="Max no-input retries reached")
                ])
            
            print("Prompting for retry due to silence.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't get that. Can you say it again?")]
            )

    return None
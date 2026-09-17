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

    print('Executing before_model_callback checks')
    
    for part in callback_context.get_last_user_input():
        text_lower = part.text.lower() if part.text else ''
        if 'no user activity detected' in text_lower or 'sys.no-input' in text_lower or 'sys.no-match' in text_lower:
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            print(f'No-input/No-match retry count: {retry_count}')
            
            if retry_count >= 3:
                print('Max retries reached, transitioning to fallback.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We seem to be having trouble. Let me direct you to more information.'),
                    Part.from_agent_transfer(agent='M2 AuthenticationAndIdentity')
                ])
            return LlmResponse.from_parts(
                parts=[Part.from_text('I did not quite catch that. Could you please try again?')]
            )

    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('create_one_time_payment_order'):
                resp = part.function_response.response.get('result', {})
                if 'error' in resp:
                    print('Webhook error on create_one_time_payment_order detected. Force setting webhook_success to false.')
                    callback_context.variables['webhook_success'] = False
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('I am unable to retrieve your due date at the moment. Let me offer you a link to check it on the MyBell app.'),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Check for No-Input and No-Match timeouts (sys events or text matches)
    for part in callback_context.get_last_user_input():
        text = part.text.lower() if part.text else ''
        
        if 'no user activity detected' in text or 'sys.no-input' in text or 'no input' in text:
            retry_count = callback_context.variables.get('local_noinput_counter', 0) + 1
            callback_context.variables['local_noinput_counter'] = retry_count
            print(f'No Input detected. Current retry count: {retry_count}')
            
            if retry_count >= 3:
                print('No Input limit reached, transferring to bell_No_Input_3.')
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
                
        elif 'sys.no-match' in text:
            retry_count = callback_context.variables.get('local_nomatch_counter', 0) + 1
            callback_context.variables['local_nomatch_counter'] = retry_count
            print(f'No Match detected. Current retry count: {retry_count}')
            
            if retry_count >= 3:
                print('No Match limit reached, transferring to bell_No_Match_3.')
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    # Check for Tool Failures (Webhook timeout or critical error)
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('evaluate_cc_expiry_status_tool'):
            response = part.function_response.response.get('result', {})
            if 'error' in response:
                print('Executing Tool Failure detected for evaluate_cc_expiry_status_tool, initiating transfer to bell_aqd.')
                callback_context.variables['hardstop'] = 'True'
                return LlmResponse.from_parts(parts=[
                    Part.from_text('I am having some trouble validating your profile. Let me transfer you so we can get this resolved.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
                
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # 1. Tool Error Handling / Webhook Success Check
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('get_clp_and_bill_details_wrapper'):
            response_dict = part.function_response.response.get('result', {})
            webhook_success = callback_context.variables.get('webhook_success', True)
            if 'error' in response_dict or not webhook_success:
                print("Executing Tool Failure detected, initiating transfer to bell_Feedback.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We are currently performing maintenance on our systems so unfortunately I am unable to proceed with providing your credit limit details at this moment. Please call again tomorrow."),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    # 2. No-Input Handling
    last_input = callback_context.get_last_user_input()
    if last_input:
        for part in last_input:
            if part.text:
                text_lower = part.text.lower().strip()
                if 'no user activity detected' in text_lower:
                    retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
                    callback_context.variables['no_input_retry_count'] = retry_count
                    print(f"No-input detected. Count: {retry_count}")
                    if retry_count >= 3:
                        print("Max no-input reached, transferring to bell_No_Input_3.")
                        return LlmResponse.from_parts(parts=[
                            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                        ])
                    return None
                else:
                    callback_context.variables['no_input_retry_count'] = 0
    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text:
            print('No user activity detected, checking retry count.')
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            if retry_count >= 3:
                print('Max retries reached. Executing agent transfer.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We have not heard from you. Let me transfer you to an agent.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            return LlmResponse.from_parts(
                parts=[Part.from_text('Hi, are you still there? I did not quite catch that.')]
            )
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            print(f"No-input detected. Count: {retry_count}")
            if retry_count >= 3:
                print("Max no-input retries reached, initiating transfer to bell_determine_handover.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            return LlmResponse.from_parts(parts=[Part.from_text("Hi, are you still there?")])

    if llm_request.contents and len(llm_request.contents) > 0:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('validate_and_format_amount'):
                bad_amt = callback_context.variables.get('bad_amount', 0)
                if bad_amt > 2:
                    print("Max invalid payment amount threshold exceeded, initiating transfer to bell_Feedback.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We can only take payments between $1 and $10,000."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in llm_request.contents[-1].parts:
        if part.has_function_response("set_payment_arrangement_sms_params") and "error" in part.function_response.response.get("result", {}):
            print("Executing Tool Failure detected, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text("Sorry, something went wrong. Let me transfer you."),
                Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
            ])

    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            print("No input detected, incrementing retry count.")
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            
            if retry_count >= 3:
                state = callback_context.variables.get("current_state", "START_PAGE")
                if state == "PROMPT_SMS_CONFIRMATION":
                    print("Max no-inputs reached during SMS confirmation. Routing to bell_Feedback.")
                    lang = callback_context.variables.get("language", "en").lower()
                    if lang in ["fr-ca", "fr"]:
                        text = "Si vous souhaitez toujours prendre une entente de paiement, vous pouvez le faire dans MonBell. Veuillez consulter le site bell.ca/soutien pour plus d'information."
                    else:
                        text = "If you'd still like to set up Payment Arrangement, you can do so in MyBell. Please visit bell.ca/support for more information."
                    return LlmResponse.from_parts(parts=[
                        Part.from_text(text),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                else:
                    print("Max no-inputs reached at start page. Routing to bell_No_Input_3.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
            
            return LlmResponse.from_parts(parts=[Part.from_text("Hi, are you still there?")])
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text:
            text_lower = part.text.lower()
            if "no user activity detected" in text_lower or "sys.no-input" in text_lower or "sys.no-match" in text_lower:
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                print(f"No input or match detected, retry count: {retry_count}")
                if retry_count >= 3:
                    print("Max retries reached. Trigger transition to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("I am having trouble understanding. Let me transfer you to an agent."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
            if "other_speak_to_agent" in text_lower or "agent" in text_lower or "representative" in text_lower or "human" in text_lower:
                print("Handover request detected. Trigger transition to bell_determine_handover.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("Let me get someone to help you."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            print(f"No-input detected. Retry count: {retry_count}")
            
            if retry_count >= 3:
                print("Max invalid no-input attempts reached, transferring to bell_Feedback.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("If you'd still like to cancel Pre-Authorized payment, you can do so in MyBell. Please visit bell.ca/support for more information."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
                
            print("Prompting user to retry input.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't quite get that. Can you try again?")]
            )
        elif part.text:
            callback_context.variables["no_input_retry_count"] = 0
            print("Valid user input detected. Resetting retry count.")
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or 'no_input' in part.text.lower() or 'sys.no-match' in part.text.lower()):
            retry_count = callback_context.variables.get('global_error_counter', 0) + 1
            callback_context.variables['global_error_counter'] = retry_count
            if retry_count >= 3:
                print('Max no-input/no-match retries reached. Forcing transition to bell_Feedback.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('If you\'d still like to check your Pre-Authorized payments status, you can do so in MyBell. Please visit bell.ca/support for more information.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            print('No-input detected. Prompting user to retry.')
            return LlmResponse.from_parts(parts=[Part.from_text('I didn\'t quite get that. Can you try again?')])
            
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('get_nm1_billing_profile') and 'error' in part.function_response.response.get('result', {}):
                print('Webhook error detected in nm1_get. Forcing transition to FAILURE_SMS_OFFER.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, it looks like I\'m having trouble completing the next step. I\'ll send a text to the device you\'re calling from so that you can check your Pre-Authorized payments status in the MyBell app. Is that alright?'),
                    Part.from_agent_transfer(agent='FAILURE_SMS_OFFER')
                ])
            if part.has_function_response('lookup_province_by_phone') and 'error' in part.function_response.response.get('result', {}):
                print('Webhook error detected in province lookup. Forcing transition to FAILURE_SMS_OFFER.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, it looks like I\'m having trouble completing the next step. I\'ll send a text to the device you\'re calling from so that you can check your Pre-Authorized payments status in the MyBell app. Is that alright?'),
                    Part.from_agent_transfer(agent='FAILURE_SMS_OFFER')
                ])
                
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or 'sys.no-match' in part.text.lower() or 'sys.no-input' in part.text.lower()):
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            print(f'No-input retry count: {retry_count}')
            if retry_count >= 3:
                print('Executing Max Retries reached, initiating transfer to Feedback.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text("If you'd still like to update Pre-Authorized payments, you can do so in MyBell. Please visit bell.ca/support on how to update Pre-Authorized payments."),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            return LlmResponse.from_parts(parts=[Part.from_text("I didn't quite get that. Can you try again?")])
            
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            tool_names = ['tool_get_customer_profile', 'tool_lookup_province', 'tool_check_preauth_payment', 'tool_process_pacc_order']
            for tool_name in tool_names:
                if part.has_function_response(tool_name) and 'error' in part.function_response.response.get('result', {}):
                    print(f'Executing Tool Failure detected for {tool_name}, forcing fallback.')
                    callback_context.variables['webhook_success'] = False
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("I am having trouble accessing your account right now. Would you like me to send you an SMS with instructions to update your payment method online?")
                    ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('fetch_billing_profile'):
                result = part.function_response.response.get('result', {})
                if 'error' in result:
                    print('Executing Tool Failure detected in fetch_billing_profile.')
                    callback_context.variables['consolidated_status'] = 'Fail'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('Sorry, we are experiencing technical difficulties. Please call back later.'),
                        Part.from_end_session(reason='Tool Failure')
                    ])
                if result.get('returnCode') == 0:
                    print('NM1 Outage detected. Terminating Session.')
                    callback_context.variables['consolidated_status'] = 'Outage'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('Our systems are currently undergoing maintenance. Please try again later.'),
                        Part.from_end_session(reason='NM1 Outage')
                    ])
            
            if part.has_function_response('resolve_npa_and_province'):
                result = part.function_response.response.get('result', {})
                if 'error' in result:
                    print('Executing Tool Failure detected in resolve_npa_and_province.')
                    callback_context.variables['consolidated_status'] = 'Fail'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text('Sorry, we are experiencing technical difficulties. Please call back later.'),
                        Part.from_end_session(reason='Tool Failure')
                    ])

    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or 'no-input' in part.text.lower() or 'no-match' in part.text.lower()):
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            print('No input/match detected. Retry count: ' + str(retry_count))
            if retry_count >= 3:
                print('Max retries reached, ending session.')
                callback_context.variables['consolidated_status'] = 'Fail'
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We haven\'t heard from you. Please call back later.'),
                    Part.from_end_session(reason='No Input Limit Exceeded')
                ])
            print('Prompting user for retry.')
            return LlmResponse.from_parts(
                parts=[Part.from_text('I didn\'t get that. Can you say it again?')]
            )
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            print(f"No-input detected, count: {retry_count}")
            if retry_count >= 3:
                print("Max no-input reached, transitioning to bell_determine_handover")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            return LlmResponse.from_parts(
                parts=[Part.from_text("Hi, are you still there?")]
            )
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        text = part.text or ""
        text_lower = text.lower()
        if "no user activity detected" in text_lower or "sys.no-match" in text_lower:
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            print(f"No-match/no-input detected. Retry count: {retry_count}")
            if retry_count >= 3:
                clp_balance = callback_context.variables.get("clp_balance", 0)
                if clp_balance <= 0:
                    print("Amount Collection limit reached. Transferring to bell_Feedback.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Sorry, we are unable to process this. Let me transfer you."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                else:
                    print("Early balance check limit reached. Transferring to bell_determine_handover.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("I'm having trouble. Let me transfer you to an agent."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
            return LlmResponse.from_parts(parts=[Part.from_text("I didn't quite get that. Can you try again?")])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("Checking user input for no-input or unrecognized match timeouts")
    for part in callback_context.get_last_user_input():
        if part.text and ("no user activity detected" in part.text.lower() or "unrecognized input" in part.text.lower()):
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            
            if retry_count >= 3:
                print("Max retries reached in fallback state, initiating transfer to bell_aqd.")
                lang = callback_context.variables.get("language", "en")
                if lang == "fr-ca":
                    msg = "Si vous souhaitez toujours effectuer une demande de paiements pré-autorisés, vous pouvez le faire dans l'appli Mon compte. Veuillez visiter https://vpc.ca/soutien pour en savoir plus."
                else:
                    msg = "If you'd still like to complete your Pre-Authorized payment request, you can do so in the My Account app. Please visit vpc.ca/support for more information."
                
                return LlmResponse.from_parts(parts=[
                    Part.from_text(msg),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
                
            print("Incremented retry count, allowing LLM to handle reprompt.")
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if (part.has_function_response('get_account_balance_details_wrapper') and 'error' in part.function_response.response.get('result', {})):
                print('Executing Tool Failure detected, initiating transfer to bell_aqd.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, something went wrong while retrieving your payment details. Let me transfer you.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    last_input = callback_context.get_last_user_input()
    if last_input:
        for part in last_input:
            if part.text:
                text_lower = part.text.lower()
                if 'no user activity detected' in text_lower or 'no match' in text_lower:
                    retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
                    callback_context.variables['no_input_retry_count'] = retry_count
                    if retry_count >= 3:
                        print('Max retries reached for no-input/no-match, ending session.')
                        return LlmResponse.from_parts(parts=[
                            Part.from_text('I am having trouble understanding. Please call back later. Goodbye.'),
                            Part.from_end_session(reason='wrapup')
                        ])
                    print('No input or match detected, prompting user again.')
                    return LlmResponse.from_parts(
                        parts=[Part.from_text('I did not get that. Can you say it again?')] 
                    )
                else:
                    if callback_context.variables.get('no_input_retry_count', 0) > 0:
                        print('Valid input received, resetting retry counter.')
                        callback_context.variables['no_input_retry_count'] = 0
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and ("no user activity detected" in part.text or "no-input" in part.text.lower() or "no-match" in part.text.lower()):
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            print(f"Executing No-Input / No-Match threshold check, attempt {retry_count}")
            if retry_count >= 3:
                print("Max retries reached, transferring to bell_determine_handover.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you or understood your request. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            return LlmResponse.from_parts(parts=[
                Part.from_text("I didn't quite get that. Can you try again?")
            ])

    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if (part.has_function_response("get_account_profile_and_eligibility") or
                part.has_function_response("create_payment_order") or
                part.has_function_response("finalize_payment_notification")):
                resp_data = part.function_response.response
                if "error" in resp_data.get("result", {}) or "error" in resp_data:
                    print("Executing Tool Failure detected, initiating WEBHOOK_FAILURE_FALLBACK messaging.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We are currently performing maintenance on our systems. I'll send a text to the device you're calling from, so that you can view your payment notification yourself in the MyBell App. Is that alright?")
                    ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Enforcing custom response and routing for No-Input / Silence Timeout
    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or 'sys.no-match' in part.text.lower() or 'sys.no-input' in part.text.lower()):
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            if retry_count >= 3:
                print('Max retries reached. Triggering routing to bell_determine_handover.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('I am having trouble understanding. Let me transfer you to someone who can help.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            print('No input or no match detected, prompting retry.')
            return LlmResponse.from_parts(
                parts=[Part.from_text('I didn\'t quite get that. Could you please say it again or rephrase?')]
            )
            
    # Deterministically catch webhook tool errors to force transition to HANDLE_WEBHOOK_FAILURE pattern
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('fetch_customer_and_province_profile') or part.has_function_response('evaluate_eligibility_and_create_order'):
            result = part.function_response.response.get('result', {})
            if 'error' in result:
                print('Executing Tool Failure detected, forcing transition to HANDLE_WEBHOOK_FAILURE.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, it looks like I\'m having trouble completing the next step. There\'s nothing wrong on your end. I\'ll send a text to the device you\'re calling from so that you can make a payment in the MyBell app. Is that alright?')
                ])
    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # PATTERN A: Transfer to Another Agent on Tool Failures
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('get_clp_details_wrapper'):
            response_data = part.function_response.response
            if 'error' in response_data.get('result', {}) or 'error' in response_data:
                print('Executing Tool Failure detected, initiating transfer to bell_Feedback.')
                callback_context.variables['webhook_success'] = False
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I'm sorry, I can't help you with confirming your Credit Limit Balance or account details at this time."),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    # PATTERN E: Custom Response for No-Input Timeout
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text.lower():
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            print(f'No-input detected. Current count: {retry_count}')
            
            if retry_count >= 3:
                print('Max no-input reached, initiating routing to bell_Feedback.')
                special_status = callback_context.variables.get('special_status', '')
                
                if special_status == 'bell_clp_aul':
                    limit = callback_context.variables.get('clp_aul_limit', 0)
                    msg = f"You won't be able to make outbound calls until you bring your Credit Limit Balance Below ${limit}. To restore your service, you can pay down your credit limit balance on bell.ca or call again to learn about your Credit Limit details."
                elif special_status == 'bell_clp_sus':
                    limit = callback_context.variables.get('clp_sus_limit', 0)
                    msg = f"You won't be able to use your phone until you bring your Credit Limit Balance Below ${limit}. To restore your service, you can pay down your credit limit balance on bell.ca or call again to learn about your Credit Limit details."
                else:
                    msg = "You can pay down your credit limit balance on bell.ca, or call again to learn about credit limit details."
                
                return LlmResponse.from_parts(parts=[
                    Part.from_text(msg),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't quite get that. Can you try again?")]
            )

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            print("No user activity detected.")
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            if retry_count >= 3:
                print("Max no-input retries reached, transferring to bell_No_Input_3.")
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            return LlmResponse.from_parts(parts=[
                Part.from_text("I didn't get that. Can you say it again?")
            ])
            
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('check_existing_payment_method') or part.has_function_response('check_payment_arrangement_eligibility'):
                response_data = part.function_response.response.get('result', {})
                error_detected = 'error' in part.function_response.response or 'error' in response_data
                if error_detected or not callback_context.variables.get('webhook_success', True):
                    print("API failure detected, forcing HANDLE_API_FAILURE state.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Thanks for your patience. It looks like I'm having trouble confirming your payment method right now. I'll send a text to the device you're calling from so that you can make a payment in the MyBell app. Is that alright?")
                    ])
                    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("Evaluating before_model_callback...")
    
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text:
            print("Silence timeout detected.")
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            if retry_count >= 3:
                print("Max no input retries reached, transferring to bell_determine_handover")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't quite get that. Can you try again?")]
            )
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or 'sys.no-match' in part.text.lower()):
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            print(f'No input/match detected. Retry count: {retry_count}')
            
            if retry_count >= 3:
                print('Max retries reached, routing to bell_Feedback.')
                return LlmResponse.from_parts(parts=[
                    Part.from_text("If you'd still like to complete your Pre-Authorized payment request, you can do so in MyBell. Please visit bell.ca/support for more information."),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            
            print('Prompting user to try again.')
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't quite get that. Can you try again?")]
            )
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # 1. Handle Tool Failures (Pattern A)
    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            if (part.has_function_response('set_refund_variables') and
                'error' in part.function_response.response.get('result', {})):
                print("Executing Tool Failure detected, initiating transfer to bell_Feedback.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    # 2. Enforce Deterministic Start Page Routing (Pattern C)
    if callback_context.variables.get("first_turn", True):
        callback_context.variables["first_turn"] = False
        status = callback_context.variables.get("consolidated_status", "")
        if status == "Fail":
            print("consolidated_status is Fail. Routing deterministically to bell_aqd.")
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")])
        elif status == "Outage":
            print("consolidated_status is Outage. Routing deterministically to bell_Feedback.")
            return LlmResponse.from_parts(parts=[Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")])
        print("consolidated_status is Pass. Advancing to generative interaction.")

    # 3. Handle No-Input and No-Match Retry Timeouts (Pattern E)
    for part in callback_context.get_last_user_input():
        if part.text and "no user activity detected" in part.text.lower():
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            
            if retry_count >= 3:
                print("sys.no-input-3 reached. Triggering routing to bell_Feedback.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't heard from you. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
                
            print(f"sys.no-input triggered. Retry count: {retry_count}")
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't get that. Can you say it again?")]
            )

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    user_inputs = callback_context.get_last_user_input()
    if user_inputs:
        for part in user_inputs:
            if part.text and ("no user activity detected" in part.text.lower() or "sys.no-match" in part.text.lower() or "sys.no-input" in part.text.lower()):
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                if retry_count >= 3:
                    print("3 consecutive no-inputs/matches detected. Escalating to Feedback.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Okay. If you'd still like to set up Pre-Authorized payment, you can do so in MyBell. Please visit bell.ca/support for more information."),
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                print(f"No-input/match retry count: {retry_count}")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I didn't quite get that. Can you try again?")
                ])
                
    failed = False
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            for tool in ['fetch_billing_profile_tool', 'lookup_province_tool', 'check_preauth_eligibility_tool', 'create_preauth_order_tool', 'fetch_intent_sdl_mapping_tool']:
                if part.has_function_response(tool):
                    res = part.function_response.response.get('result', {})
                    if 'error' in res or res.get('webhook_success') is False:
                        failed = True
                        break
            if failed:
                break
                
    if failed:
        print("Executing Tool Failure detected, initiating handle_flow_failure routing.")
        callback_context.variables['webhook_success'] = False
        response = LlmResponse.from_parts(parts=[
            Part.from_text("SYSTEM DIRECTIVE: The backend webhook returned an error. You MUST transition to the <handle_flow_failure> state immediately.")
        ])
        response.partial = True
        return response
        
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("Evaluating before_model_callback constraints.")
    
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('evaluate_payment_eligibility_wrapper'):
                resp = part.function_response.response.get('result', {})
                if 'error' in resp or resp.get('unified_status') == 'OUTAGE_OR_ERROR':
                    print("Executing Tool Failure detected, initiating transfer to bell_aqd.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("We are currently experiencing technical difficulties. Let me transfer you."),
                        Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                    ])

    user_input_parts = callback_context.get_last_user_input()
    if user_input_parts:
        for part in user_input_parts:
            if part.text and "no user activity detected" in part.text:
                print("No user activity detected.")
                retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
                callback_context.variables["no_input_retry_count"] = retry_count
                if retry_count >= 3:
                    print("Max no-input retries reached, transferring to bell_No_Input_3.")
                    return LlmResponse.from_parts(parts=[
                        Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                    ])
                return LlmResponse.from_parts(parts=[
                    Part.from_text("I didn't get that. Are you still there?")
                ])
            
            if part.text and "sys.no-match-3" in part.text:
                print("Sys no-match-3 event detected, transferring to bell_No_Match_3.")
                return LlmResponse.from_parts(parts=[
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
                
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Handle sys.no-input-default and sys.no-match-default intercepts
    for part in callback_context.get_last_user_input():
        text_lower = part.text.lower() if part.text else ""
        if "no user activity detected" in text_lower or "sys.no-input" in text_lower or "sys.no-match" in text_lower:
            print("Conversational error intercepted (no-input/no-match). Incrementing global_error_counter.")
            error_count = callback_context.variables.get("global_error_counter", 0) + 1
            callback_context.variables["global_error_counter"] = error_count
            
            fallback_msg = "I didn't get that. Can you say it again? / J'ai du mal à comprendre cette question."
            return LlmResponse.from_parts(parts=[
                Part.from_text(fallback_msg)
            ])
            
    # Fallback to handle tool execution failures as a standard defensive mechanism
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('update_state_variables') and 'error' in part.function_response.response.get('result', {}):
            print("Executing Tool Failure detected, initiating transfer.")
            return LlmResponse.from_parts(parts=[
                Part.from_text('Sorry, something went wrong. Let me transfer you.'),
                Part.from_agent_transfer(agent='escalation_agent')
            ])
            
    return None
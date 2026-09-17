from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # 1. No Match / No Input Detection
    for part in callback_context.get_last_user_input():
        if part.text and ('no user activity detected' in part.text.lower() or 'no match' in part.text.lower()):
            retry_count = callback_context.variables.get('local_error_counter', 0) + 1
            callback_context.variables['local_error_counter'] = retry_count
            if retry_count >= 3:
                print("Max No-Input/No-Match retries reached. Failing Auth.")
                callback_context.variables['auth_status'] = 'Fail'
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We are having trouble receiving your input. Authentication has failed."),
                    Part.from_end_session(reason="Max Auth Prompt Errors")
                ])

    # 2. Tool Webhook Error Interceptions
    if llm_request.contents and llm_request.contents[-1].parts:
        for part in llm_request.contents[-1].parts:
            if part.has_function_response('init_auth_and_get_profile'):
                res = part.function_response.response.get('result', {})
                if 'error' in res:
                    print("start-auth-session error detected. Terminating flow.")
                    callback_context.variables['auth_status'] = 'Fail'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Sorry, we are experiencing technical difficulties and cannot verify your identity right now. Please try again later."),
                        Part.from_end_session(reason="Auth Init Webhook Error")
                    ])

            if part.has_function_response('validate_pin'):
                res = part.function_response.response.get('result', {})
                if 'error' in res:
                    print("validate-pin error detected. Triggering fallback override.")
                    callback_context.variables['status'] = 'PINUnavailable'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Sorry, there was a problem validating your PIN. Let's try sending a verification code to your phone instead.")
                    ])

            if part.has_function_response('send_verification_otp'):
                res = part.function_response.response.get('result', {})
                if 'error' in res:
                    print("send-otp error detected. Terminating flow.")
                    callback_context.variables['status'] = 'SMSUnavailable'
                    callback_context.variables['auth_status'] = 'Fail'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Sorry, there was a problem sending your verification code. Authentication has failed."),
                        Part.from_end_session(reason="OTP Send Webhook Error")
                    ])

            if part.has_function_response('validate_verification_otp'):
                res = part.function_response.response.get('result', {})
                if 'error' in res:
                    print("validate-otp error detected. Terminating flow.")
                    callback_context.variables['status'] = 'SMSUnavailable'
                    callback_context.variables['auth_status'] = 'Fail'
                    return LlmResponse.from_parts(parts=[
                        Part.from_text("Sorry, there was a problem verifying your code. Authentication has failed."),
                        Part.from_end_session(reason="OTP Validate Webhook Error")
                    ])
    
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Check for tool errors indicating webhook failure to enforce early exit and handoff
    for part in llm_request.contents[-1].parts:
        if (part.has_function_response('initialize_auth_session') or 
            part.has_function_response('send_otp_wrapper') or 
            part.has_function_response('validate_pin_wrapper') or 
            part.has_function_response('validate_otp_wrapper') or 
            part.has_function_response('get_sms_vanity_url')):
            result = part.function_response.response.get('result', {})
            if 'error' in result:
                print('Executing Tool Failure detected, setting auth_status to Fail and initiating transfer.')
                callback_context.variables['auth_status'] = 'Fail'
                return LlmResponse.from_parts(parts=[
                    Part.from_text('Sorry, something went wrong on our end. Let me transfer you.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    # Evaluate strict limits on consecutive No-Input scenarios
    for part in callback_context.get_last_user_input():
        if part.text and 'no user activity detected' in part.text.lower():
            no_input_count = callback_context.variables.get('local_noinput_counter', 0) + 1
            callback_context.variables['local_noinput_counter'] = no_input_count
            print(f'Executing No Input detected: count {no_input_count}')
            if no_input_count >= 3:
                print('Executing Max No Input reached, initiating transfer to bell_No_Input_3.')
                callback_context.variables['auth_status'] = 'Fail'
                return LlmResponse.from_parts(parts=[
                    Part.from_text('We haven\'t heard from you. Let me transfer you to an agent.'),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    # Evaluate strict limits on consecutive No-Match / Global errors stored in context
    nomatch_count = callback_context.variables.get('local_nomatch_counter', 0)
    if nomatch_count >= 3:
        print('Executing Max No Match reached, initiating transfer to bell_No_Match_3.')
        callback_context.variables['auth_status'] = 'Fail'
        return LlmResponse.from_parts(parts=[
            Part.from_text('I\'m having trouble understanding. Let me transfer you.'),
            Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
        ])

    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    for part in callback_context.get_last_user_input():
        if part.text and ("no user activity detected" in part.text.lower() or "sys.no-match" in part.text.lower()):
            print("Executing sys.no-input/no-match failure logic.")
            error_count = callback_context.variables.get("global_error_counter", 0) + 1
            callback_context.variables["global_error_counter"] = error_count
            
            if error_count >= 3:
                print("Max global errors reached, initiating session end.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We seem to be having trouble. Please try again later."),
                    Part.from_end_session(reason="Max Errors Reached")
                ])
            
            print("Playing reprompt for no-input/no-match.")
            lang = callback_context.variables.get("language", "en")
            if "fr" in str(lang).lower():
                return LlmResponse.from_parts(parts=[Part.from_text("J'ai du mal à comprendre cette question. Pouvez-vous répéter?")])
            return LlmResponse.from_parts(parts=[Part.from_text("I didn't get that. Can you say it again?")])
            
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    print("Executing before_model_callback for bell_payment_arrangement_setup_id_auth_eligibility_Checks")
    
    for part in callback_context.get_last_user_input():
        if part.text and ("no user activity detected" in part.text.lower() or "sys.no-match" in part.text.lower()):
            print("No-input or no-match detected")
            retry_count = callback_context.variables.get("no_input_retry_count", 0) + 1
            callback_context.variables["no_input_retry_count"] = retry_count
            if retry_count >= 3:
                print("Max retries reached, initiating handover.")
                return LlmResponse.from_parts(parts=[
                    Part.from_text("We haven't been able to understand you. Let me transfer you to an agent."),
                    Part.from_agent_transfer(agent="M1 SessionLifecycleAndRouting")
                ])
            print("Prompting user to try again.")
            return LlmResponse.from_parts(
                parts=[Part.from_text("I didn't quite get that. Can you try again?")]
            )

    if llm_request.contents:
        for part in llm_request.contents[-1].parts:
            for tool_name in ["get_account_profile_wrapper", "evaluate_consolidated_customer_logic", "npa_nxx_lookup_wrapper", "process_pa_eligibility_and_order_wrapper"]:
                if part.has_function_response(tool_name):
                    result_data = part.function_response.response.get("result", {})
                    if "error" in result_data:
                        print(f"Executing Tool Failure detected for {tool_name}, transitioning to SMS_FALLBACK_OFFER.")
                        return LlmResponse.from_parts(parts=[
                            Part.from_text("I'm unable to proceed with your payment arrangement at this time. I'll send a text to the device you're calling from so that you can set up your payment arrangement on the MyBell app. Is that alright?")
                        ])
    return None

from typing import Optional

def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    # Intercept Webhook Tool Failures
    for part in llm_request.contents[-1].parts:
        if part.has_function_response('fetch_account_profile_wrapper') or part.has_function_response('fetch_province_info_wrapper') or part.has_function_response('fetch_intent_vanity_url_wrapper'):
            resp = part.function_response.response.get('result', {})
            if 'error' in resp:
                print('Executing Tool Failure detected, initiating fallback routing.')
                lang = callback_context.variables.get('language', 'en').lower()
                msg = "Okay. If you'd still like to set up Pre-Authorized debit, you can do so in MyBell. Please visit bell.ca/support for more information."
                if 'fr' in lang:
                    msg = "D’accord. Si vous souhaitez quand même configurer le prélèvement automatique, vous pouvez le faire dans MonBell. Veuillez consulter le site bell.ca/soutien pour obtenir plus d’informations."
                return LlmResponse.from_parts(parts=[
                    Part.from_text(msg),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])

    # Handle sys.no-input timeout and retries
    for part in callback_context.get_last_user_input():
        text = (part.text or '').lower()
        if 'no user activity detected' in text or 'no match' in text:
            retry_count = callback_context.variables.get('no_input_retry_count', 0) + 1
            callback_context.variables['no_input_retry_count'] = retry_count
            print('Executing No-Input timeout retry count increment.')
            if retry_count >= 3:
                print('Executing Max retries reached, initiating feedback transfer.')
                lang = callback_context.variables.get('language', 'en').lower()
                msg = "Okay. If you'd still like to set up Pre-Authorized debit, you can do so in MyBell. Please visit bell.ca/support for more information."
                if 'fr' in lang:
                    msg = "D’accord. Si vous souhaitez quand même configurer le prélèvement automatique, vous pouvez le faire dans MonBell. Veuillez consulter le site bell.ca/soutien pour obtenir plus d’informations."
                return LlmResponse.from_parts(parts=[
                    Part.from_text(msg),
                    Part.from_agent_transfer(agent='M1 SessionLifecycleAndRouting')
                ])
            
            reprompt = "I didn't quite get that. Can you try again?"
            if 'fr' in callback_context.variables.get('language', 'en').lower():
                reprompt = "Je n’ai pas tout à fait compris. Pouvez-vous réessayer?"
            return LlmResponse.from_parts(parts=[Part.from_text(reprompt)])

    return None
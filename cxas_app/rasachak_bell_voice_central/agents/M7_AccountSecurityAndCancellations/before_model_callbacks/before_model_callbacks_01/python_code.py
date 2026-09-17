from typing import Optional
def before_model_callback(
    callback_context: CallbackContext,
    llm_request: LlmRequest,
) -> Optional[LlmResponse]:

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

    return None


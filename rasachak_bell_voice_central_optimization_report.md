# CXAS Optimization Audit Report
**Generated:** `2026-09-16 23:36:24 UTC`

## App Details
- **Source DFCX Agent:** `(see bundle)`
- **Target CXAS App:** `rasachak_bell_voice_central`
- **App Resource:** `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8`
- **Console URL:** https://ces.cloud.google.com/projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8

## Consolidation Summary
- **1:1 IR agents (before grouping):** 187
- **Consolidated agents (after):** 8
- **Grouping JSON artifact:** `rasachak_bell_voice_central_grouping.json`

### Grouping Detail
| Group | Members | Journey | Root |
|---|---|---|---|
| `M1_SessionLifecycleAndRouting` | Default Start Flow, Routing only, bell_End the Conversation, bell_FAQ, bell_FAQ_vanity, bell_Feedback, bell_IVR_Options, bell_Identification, bell_Live Agent Handoff, bell_Manage_plan_and_feature_routing, bell_NLU_Query_Rewriter, bell_No_Input_3, bell_No_Match_3, bell_PPV, bell_Query_Rewriter, bell_Query_Rewriter(no codeblock), bell_SMS Trigger, bell_Steering_Feedback, bell_Steering_Global Fallback, bell_Steering_Wrap-up, bell_UC_Automation_testing, bell_UC_CIAM, bell_UC_Disambiguation, bell_UC_Disconnect, bell_UC_Get_LOB, bell_UC_New_Customer_Context_Rentention, bell_UC_Other, bell_UC_Postal_Code, bell_UC_Temporary Suspension, bell_UC_Usage, bell_VA_Survey, bell_VR, bell_apb, bell_app_mgmt_change_contact_method, bell_app_mgmt_create_dispatch_start, bell_appt_mgmt_mya_pitch_1, bell_aqd, bell_clp_faq_test, bell_determine_handover, bell_equipment_order_or_upgrade_device_routing, bell_equipment_routing, bell_global_error_count_check, bell_ivr_to_va_handoff, bell_multiban, bell_payment_clp_process_payment_and_wrapup, bell_payment_process_payment_and_wrapup, bell_rehit, bell_rehit_Check_Subscription, bell_rehit_SMS, bell_rehit_confirmation, bell_sales_routing_flow, bell_sms_no_match_handling, bell_sms_trigger - old, bell_specialty_flow, bell_test_wrapper, bell_topic_transitions, bell_uc_ask_LOB, bell_uc_disambiguation_for_vague_account_management, bell_uc_disambiguation_for_vague_billing, bell_uc_disambiguation_for_vague_disconnect, bell_uc_disambiguation_for_vague_equipment, bell_uc_disambiguation_for_vague_others, bell_uc_disambiguation_for_vague_payment, bell_uc_disambiguation_for_vague_sales, bell_uc_disambiguation_for_vague_service, bell_uc_disambiguation_for_vague_tech_support, bell_uc_omf_tkt_chk_appt_mgmt_appt_info_retriever, bell_va_to_ivr_handoff, bell_va_to_ivr_handoff_BBM_BNM_SMB, bell_va_to_ivr_handoff_prepaid, bell_vr_start_process, bell_wrapup, nga_handling, nga_nlu_entity_extraction, service_add_feature_flow, temp |  | yes |
| `M2_AuthenticationAndIdentity` | bell_agent_transfer_authentication, bell_authentication, bell_get_sdl_mapping_url, bell_payment_arrangment_setup_id_auth_eligibility_Checks, bell_payment_setup_preAuth_pad |  |  |
| `M3_BillingAndPayments` | bell_UC_Billing, bell_UC_Payments, bell_billing, bell_expired_credit_card, bell_payment_CLP_details, bell_payment_account_balance_and_last_payment_details, bell_payment_amount_otcc, bell_payment_arrangement_setup_mutilple_installments, bell_payment_arrangement_setup_pa_amount_date_and_processing, bell_payment_autopay_cancel, bell_payment_autopay_status, bell_payment_autopay_update, bell_payment_billing_consolidated_flow_identification, bell_payment_cc_details_input, bell_payment_clp_payment_amount, bell_payment_dts_token, bell_payment_not_processing, bell_payment_notification, bell_payment_one_time_CC_payment, bell_payment_pitch_one_time_CC_payment, bell_payment_pitch_one_time_CC_payment 2, bell_payment_pitch_pacc_otcc, bell_payment_process_pacc_registration, bell_payment_request_refund, bell_payment_setup_pacc_or_payment_not_stated, bell_payment_update_payment_arrangements, bell_request_for_bill_statement |  |  |
| `M4_TechSupportAndVirtualRepair` | Bell_UC_Tech_intents_lob, Bell_UC_Technical_Support_Infobot, Bell_UC_Technical_Support_Infobot_deprecated, Bell_tech_lob, Bell_tv_rehit_SatTV_FibeTV, bell_UC_Get_TV_SUB_Type, bell_UC_Technical Support, bell_UC_Technical Support-1, bell_UC_Technical Support-2, bell_acut_ticket_chk_troubleshooting_intents, bell_app_mgmt_Tech_visit_Entry, bell_rehit_Fibe_TV, bell_rehit_Sat_TV, bell_rehit_Send_Troubleshooting_SMS, bell_tech_change_appointment, bell_tech_change_appointment_flow, bell_tech_field_tech_visit, bell_tech_field_tech_visit_cancel_flow, bell_tech_intent_apb, bell_tech_service_outage_&_Tech_connection_issue, bell_tech_service_outage_connection_issue_main, bell_tech_support_intents, bell_ticket_mgmt_acut_change_reschedule_ticket_technical_intents, bell_ticket_mgmt_omf_ticket_check_technical_intents, bell_troubleshooting_intents_entry, bell_va_to_ivr_smarthome, bell_vr_CDA, bell_vr_CDA_CFL, bell_vr_CFB, bell_vr_api_failure_handler, bell_vr_consent, bell_vr_kickout, bell_vr_kickout_sms, bell_vr_microservice, bell_vr_next_task, bell_vr_post_answer, bell_vr_pre_checks, va_to_ivr_business_id_sales |  |  |
| `M5_SalesUpgradesAndWarranty` | Bell_UC_Equipment_Inquires_Infobot, Bell_UC_Equipment_Inquires_Infobot_deprecated, Bell_UC_Sales_Plans_inquiry, bell_UC_Equipment, bell_UC_Equipment Warranty Claim Related, bell_UC_Manage Plans and Features, bell_UC_Manage Plans and Features Phase2, bell_UC_Manage Plans and Features Phase2_1, bell_UC_Sales, bell_UC_Sales Add To Existing Account, bell_UC_sales_device_related, bell_equipment_warranty_claim_cpo_update, bell_mob_sales_pitch, bell_sales_intent_handling, bell_uc_sales_service_coverage, sales_add_to_existing_account_flow, service_change_plan_flow |  |  |
| `M6_AppointmentsAndTickets` | Bell_appt_mgmt_acut_ticket_chk, bell_app_mgmt_cancel_ticket, bell_app_mgmt_cancel_ticket_entry, bell_app_mgmt_omf_change_reschedule_ticket, bell_app_mgmt_ticket_check_for_cancel_ticket, bell_app_mgmt_ticket_status_and_change_entry, bell_ticket_mgmt_acut_change_reschedule_ticket, bell_ticket_mgmt_acut_create_a_dispatch, bell_ticket_mgmt_change_cancel_ticket, bell_ticket_mgmt_omf_ticket_check_appointment_mgmt, bell_ticket_mgmt_webhook_failure, bell_uc_reschedule_change_ticket_multiple_appointment, bell_uc_reschedule_change_ticket_single_appointment |  |  |
| `M7_AccountSecurityAndCancellations` | bell_UC_Account Management, bell_UC_Account Management 2 |  |  |
| `M8_FrenchCanadianSupport` | Bell_UC_Equipment_Inquires_Infobot_fr, Bell_UC_Equipment_Inquires_Infobot_fr_deprecated, Bell_UC_Technical_Support_Infobot_Fr, Bell_UC_Technical_Support_Infobot_Fr_deprecated, bell_UC_AccountManagement_Infobot_en_fr, bell_UC_AccountManagement_Infobot_en_fr_deprecated, bell_UC_ManagePlansAndFeatures_Infobot_en_fr, bell_UC_ManagePlansAndFeatures_Infobot_en_fr_deprecated |  |  |

## CXASOptimizer Logs
### Stage 2 — Instruction State Machines + Tool Mocks
| Stage | Action | Details |
|---|---|---|
| `Stage 2 Instructions` | `Start` | Restructuring instructions to State Machine XML. |
| `Stage 2 Tool Mocks` | `Start` | Injecting native mock_mode branches into Python tools. |
| `Stage 2 Instructions` | `Complete` | Restructured 8 Playbook agents successfully. |
| `Stage 2 Tool Mocks` | `Complete` | Injected native mock_mode into 236 Python tools. |
| `Stage 2 Instructions` | `Self-Healing Gate` | All optimized playbooks passed canonical-schema validation. No healing required. |

## CXAS Version Checkpoints
| Display Name | Description |
|---|---|
| `0.0.3` | Stage 1 Part B: structural consolidation |

## Deterministic Unit Tests
- **Artifact:** `rasachak_bell_voice_central_unit_tests.json`
- **Tests per agent:**
  - `M1_SessionLifecycleAndRouting`: 17
  - `M2_AuthenticationAndIdentity`: 11
  - `M3_BillingAndPayments`: 3
  - `M4_TechSupportAndVirtualRepair`: 11
  - `M5_SalesUpgradesAndWarranty`: 5
  - `M6_AppointmentsAndTickets`: 8
  - `M7_AccountSecurityAndCancellations`: 5
  - `M8_FrenchCanadianSupport`: 10

## Lint
- **Status:** ⚠️ issues found

<details><summary>Lint output (excerpt)</summary>

```
Linting app: rasachak_bell_voice_central
============================================================
  Agents: 8
  Tools: 200
  Callbacks: 14
  Evals: 0

============================================================
LINT RESULTS
============================================================
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central [V001] Missing required fields for  Schema: ['required']
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M1_SessionLifecycleAndRouting/instruction.txt:91 [S002] Instruction references tool 'extract_lob_services_wrapper' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M1_SessionLifecycleAndRouting/instruction.txt:125 [S002] Instruction references tool 'get_ban_profile' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M2_AuthenticationAndIdentity/M2_AuthenticationAndIdentity.json [S007] Agent 'M2_AuthenticationAndIdentity' is referenced as a child by multiple parents: ['M1_SessionLifecycleAndRouting', 'M3_BillingAndPayments', 'M6_AppointmentsAndTickets']. Each sub-agent must have at most one parent.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M2_AuthenticationAndIdentity/instruction.txt:146 [S002] Instruction references tool 'prepare_sms_content_tool' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M2_AuthenticationAndIdentity/instruction.txt:142 [S002] Instruction references tool 'get_intent_sdl_mapping_wrapper' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M2_AuthenticationAndIdentity/instruction.txt:97 [S002] Instruction references tool 'validate_verification_otp' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M2_AuthenticationAndIdentity/instruction.txt:89 [S002] Instruction references tool 'send_verification_otp' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M2_AuthenticationAndIdentity/instruction.txt:131 [S002] Instruction references tool 'get_account_profile_and_eligibility' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M3_BillingAndPayments/M3_BillingAndPayments.json [S007] Agent 'M3_BillingAndPayments' is referenced as a child by multiple parents: ['M1_SessionLifecycleAndRouting', 'M4_TechSupportAndVirtualRepair']. Each sub-agent must have at most one parent.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M4_TechSupportAndVirtualRepair/M4_TechSupportAndVirtualRepair.json [S007] Agent 'M4_TechSupportAndVirtualRepair' is referenced as a child by multiple parents: ['M1_SessionLifecycleAndRouting', 'M7_AccountSecurityAndCancellations']. Each sub-agent must have at most one parent.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M4_TechSupportAndVirtualRepair/instruction.txt:184 [S002] Instruction references tool 'FR_Bell_vr_cda_faq' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M4_TechSupportAndVirtualRepair/instruction.txt:120 [S002] Instruction references tool 'Fr_Bell_Tech_Support_Wireless' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M4_TechSupportAndVirtualRepair/instruction.txt:179 [S002] Instruction references tool 'EN_Bell_vr_cda_faq' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M4_TechSupportAndVirtualRepair/instruction.txt:115 [S002] Instruction references tool 'EN_Bell_Tech_Support_Wireless' but it's not in the agent's tool list.
  [E] /tmp/cxas_lint_dwxuxm_v/rasachak_bell_voice_central/agents/M5_SalesUpgradesAndWarranty/M5_SalesUpgradesAndWarranty.json [S007] Agent 'M5_SalesUpgradesAndWarranty' is referenced as a child by multiple pare
```

</details>

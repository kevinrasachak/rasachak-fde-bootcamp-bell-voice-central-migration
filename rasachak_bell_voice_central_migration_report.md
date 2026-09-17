# CXAS Migration Audit Report
**Generated:** `2026-09-16 22:39:04 UTC`

## 📦 App Details
- **Source DFCX Agent:** `uploaded-agent`
- **Target CXAS App:** `rasachak_bell_voice_central`
- **Target App ID:** `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8`

## ⚠️ Skipped Resources (Action Required)
| Category | Resource Name | Reason |
|---|---|---|
| `Data Store Tool` | `EN_Bell_CLP_FAQs` | No datastore selected in source agent. |


## 🔠 App Variables Migrated
| Original Name | CXAS Name | Type |
|---|---|---|
| `route` | `route` | `STRING` |
| `sim_activation_type` | `sim_activation_type` | `STRING` |
| `sim_type` | `sim_type` | `STRING` |
| `line_type` | `line_type` | `STRING` |
| `brand` | `brand` | `STRING` |
| `CLID` | `CLID` | `NUMBER` |
| `language` | `language` | `STRING` |
| `utterance` | `utterance` | `STRING` |
| `billing_account_status` | `billing_account_status` | `STRING` |
| `BAN` | `BAN` | `NUMBER` |
| `caller_channel` | `caller_channel` | `NUMBER` |
| `identification_status` | `identification_status` | `STRING` |
| `auth_status` | `auth_status` | `STRING` |
| `LOB` | `LOB` | `STRING` |
| `device_type` | `device_type` | `STRING` |
| `customer_type` | `customer_type` | `STRING` |
| `faq_link` | `faq_link` | `STRING` |
| `global_error_counter` | `global_error_counter` | `NUMBER` |
| `special_queue` | `special_queue` | `STRING` |
| `event_type` | `event_type` | `STRING` |
| `apb_location_id` | `apb_location_id` | `NUMBER` |
| `province` | `province` | `STRING` |
| `lob` | `lob` | `STRING` |
| `mobility_sub_type` | `mobility_sub_type` | `STRING` |
| `streaming_services` | `streaming_services` | `STRING` |
| `business` | `business` | `STRING` |
| `unique_services` | `unique_services` | `ARRAY` |
| `shr_int_partner_nw_elig_flg` | `shr_int_partner_nw_elig_flg` | `NUMBER` |
| `additional_query` | `additional_query` | `STRING` |
| `utterance_raw` | `utterance_raw` | `STRING` |
| `wml_eligible` | `wml_eligible` | `NUMBER` |
| `tv_sub_type` | `tv_sub_type` | `STRING` |
| `speak_to_agent_counter` | `speak_to_agent_counter` | `NUMBER` |
| `second_intent_true` | `second_intent_true` | `BOOLEAN` |
| `calling_feature` | `calling_feature` | `STRING` |
| `payment_method` | `payment_method` | `STRING` |
| `usage_type` | `usage_type` | `STRING` |
| `suspension_type` | `suspension_type` | `STRING` |
| `login_assistance_type` | `login_assistance_type` | `STRING` |
| `plans` | `plans` | `STRING` |
| `add_ons` | `add_ons` | `STRING` |
| `appointment_type` | `appointment_type` | `STRING` |
| `competitor_brand` | `competitor_brand` | `STRING` |
| `issue_type` | `issue_type` | `STRING` |
| `ppv` | `ppv` | `STRING` |
| `manufacturer` | `manufacturer` | `STRING` |
| `mfa` | `mfa` | `STRING` |
| `account_detail_type` | `account_detail_type` | `STRING` |
| `device_issue` | `device_issue` | `STRING` |
| `internal_brand` | `internal_brand` | `STRING` |
| `tracking_method` | `tracking_method` | `STRING` |
| `prev_msg` | `prev_msg` | `STRING` |
| `serve_to_check` | `serve_to_check` | `STRING` |
| `ibm_application_id` | `ibm_application_id` | `STRING` |
| `CIRN` | `CIRN` | `NUMBER` |
| `Expired_credit_card_check` | `Expired_credit_card_check` | `STRING` |
| `sales_feedback` | `sales_feedback` | `NUMBER` |
| `prev_conv_summary` | `prev_conv_summary` | `STRING` |
| `feedback_sentiment` | `feedback_sentiment` | `STRING` |
| `feedback_description` | `feedback_description` | `STRING` |
| `number_of_services` | `number_of_services` | `NUMBER` |
| `is_mobility` | `is_mobility` | `BOOLEAN` |
| `caller_id` | `caller_id` | `NUMBER` |
| `sms_content` | `sms_content` | `STRING` |
| `sms_type` | `sms_type` | `STRING` |
| `sms_send_status` | `sms_send_status` | `STRING` |
| `initial_utterance` | `initial_utterance` | `STRING` |
| `noinput_flag` | `noinput_flag` | `STRING` |
| `different_number` | `different_number` | `BOOLEAN` |
| `caller_chanel` | `caller_chanel` | `STRING` |
| `infobot_flag` | `infobot_flag` | `BOOLEAN` |
| `coming_from` | `coming_from` | `STRING` |
| `lob_agent` | `lob_agent` | `STRING` |
| `lob_agent_2` | `lob_agent_2` | `STRING` |
| `clid` | `clid` | `NUMBER` |
| `identfication_status` | `identfication_status` | `STRING` |
| `id_channel` | `id_channel` | `STRING` |
| `otp_device` | `otp_device` | `NUMBER` |
| `aqd_device_confirm` | `aqd_device_confirm` | `BOOLEAN` |
| `summary` | `summary` | `STRING` |
| `entry_route_postal` | `entry_route_postal` | `STRING` |
| `entry_route_again` | `entry_route_again` | `STRING` |
| `postcode` | `postcode` | `STRING` |
| `postal_agent` | `postal_agent` | `STRING` |
| `postal_agent_2` | `postal_agent_2` | `STRING` |
| `mya_link` | `mya_link` | `STRING` |
| `ticket_lob` | `ticket_lob` | `STRING` |
| `service_type` | `service_type` | `STRING` |
| `shr_int_partner_new_elig_flg` | `shr_int_partner_new_elig_flg` | `NUMBER` |
| `lob_agent_3` | `lob_agent_3` | `STRING` |
| `lob_Prepaid` | `lob_Prepaid` | `STRING` |
| `merged_calendar_context` | `merged_calendar_context` | `ARRAY` |
| `appointments_count` | `appointments_count` | `STRING` |
| `line_of_business_multiple` | `line_of_business_multiple` | `STRING` |
| `info_retrieval_done` | `info_retrieval_done` | `STRING` |
| `date_available` | `date_available` | `STRING` |
| `all_appointment_done` | `all_appointment_done` | `STRING` |
| `appointment_done` | `appointment_done` | `STRING` |
| `line_of_business_selected` | `line_of_business_selected` | `STRING` |
| `last_appointment` | `last_appointment` | `STRING` |
| `calendarIdentifier` | `calendarIdentifier` | `STRING` |
| `today_date` | `today_date` | `STRING` |
| `end_time_5` | `end_time_5` | `STRING` |
| `end_time` | `end_time` | `STRING` |
| `start_time` | `start_time` | `STRING` |
| `day_of_week` | `day_of_week` | `STRING` |
| `date` | `date` | `STRING` |
| `interval` | `interval` | `STRING` |
| `day` | `day` | `STRING` |
| `estimatedStartTime` | `estimatedStartTime` | `STRING` |
| `line_of_business` | `line_of_business` | `STRING` |
| `original_appointment_date` | `original_appointment_date` | `STRING` |
| `user_interval` | `user_interval` | `STRING` |
| `acceptable_answers` | `acceptable_answers` | `STRING` |
| `dcx_action_code` | `dcx_action_code` | `STRING` |
| `eta_CDA` | `eta_CDA` | `STRING` |
| `vr_type` | `vr_type` | `STRING` |
| `title` | `title` | `STRING` |
| `description` | `description` | `STRING` |
| `faq_question_answer` | `faq_question_answer` | `STRING` |
| `customer_answer1_id` | `customer_answer1_id` | `STRING` |
| `customer_answer2_id` | `customer_answer2_id` | `STRING` |
| `ftth` | `ftth` | `BOOLEAN` |
| `calling_from_landline` | `calling_from_landline` | `BOOLEAN` |
| `FTTH_home` | `FTTH_home` | `BOOLEAN` |
| `multiple_services` | `multiple_services` | `BOOLEAN` |
| `generative_utterance` | `generative_utterance` | `STRING` |
| `vr_next_task_response_PB` | `vr_next_task_response_PB` | `STRING` |
| `title_microservice` | `title_microservice` | `STRING` |
| `description_microservice` | `description_microservice` | `STRING` |
| `eta_microservice` | `eta_microservice` | `STRING` |
| `status_changed` | `status_changed` | `STRING` |
| `postal_code` | `postal_code` | `STRING` |
| `decom_3g` | `decom_3g` | `STRING` |
| `postal_code_last_three` | `postal_code_last_three` | `STRING` |
| `internet_issue_error_code` | `internet_issue_error_code` | `STRING` |
| `payment_arragement_amount` | `payment_arragement_amount` | `STRING` |
| `compensation_refund` | `compensation_refund` | `STRING` |
| `Phone_Number` | `Phone_Number` | `STRING` |
| `outage_type` | `outage_type` | `STRING` |
| `time_slot` | `time_slot` | `STRING` |
| `ban_number_sequence` | `ban_number_sequence` | `STRING` |
| `pin` | `pin` | `NUMBER` |
| `northamerican_phone_number` | `northamerican_phone_number` | `STRING` |
| `aeroplan` | `aeroplan` | `STRING` |
| `error_code_outage` | `error_code_outage` | `STRING` |
| `phone_number` | `phone_number` | `NUMBER` |
| `telephone_otp` | `telephone_otp` | `NUMBER` |
| `interruptibletempinput` | `interruptibletempinput` | `STRING` |
| `Contact_Number` | `Contact_Number` | `NUMBER` |
| `postal_code_three` | `postal_code_three` | `STRING` |
| `account_number` | `account_number` | `NUMBER` |
| `other_payment_amount` | `other_payment_amount` | `NUMBER` |
| `customer_mentioned_amount` | `customer_mentioned_amount` | `NUMBER` |
| `pmtMethodInput` | `pmtMethodInput` | `STRING` |
| `card_number` | `card_number` | `NUMBER` |
| `cvv_number` | `cvv_number` | `NUMBER` |
| `expiry_date` | `expiry_date` | `NUMBER` |
| `clp_amount_paid` | `clp_amount_paid` | `NUMBER` |
| `amount_paid_by_user` | `amount_paid_by_user` | `NUMBER` |
| `cx_input_wait` | `cx_input_wait` | `STRING` |
| `cx_input_wait1` | `cx_input_wait1` | `STRING` |
| `no_input_parameter` | `no_input_parameter` | `STRING` |
| `internet_issue_error_code_param` | `internet_issue_error_code_param` | `STRING` |
| `error_code_outage_param` | `error_code_outage_param` | `STRING` |
| `spoof_clid` | `spoof_clid` | `NUMBER` |
| `intake_tfn` | `intake_tfn` | `NUMBER` |
| `tester_id` | `tester_id` | `NUMBER` |
| `selected_timeslot` | `selected_timeslot` | `STRING` |
| `on` | `on` | `STRING` |
| `sources` | `sources` | `STRING` |
| `conversation` | `conversation` | `STRING` |
| `original_query` | `original_query` | `STRING` |
| `dfcx_session_id` | `dfcx_session_id` | `STRING` |
| `agent_id` | `agent_id` | `STRING` |
| `phone` | `phone` | `STRING` |
| `billing_account` | `billing_account` | `STRING` |
| `subscriber_number` | `subscriber_number` | `STRING` |
| `menu_id` | `menu_id` | `STRING` |
| `tfn` | `tfn` | `STRING` |
| `call_id` | `call_id` | `STRING` |
| `dam_id` | `dam_id` | `STRING` |
| `department` | `department` | `STRING` |
| `account_type` | `account_type` | `STRING` |
| `cti_at` | `cti_at` | `STRING` |
| `cti_rt` | `cti_rt` | `STRING` |
| `cti_sd` | `cti_sd` | `STRING` |
| `cirn` | `cirn` | `STRING` |
| `additional_info` | `additional_info` | `STRING` |
| `customer_authentication` | `customer_authentication` | `BOOLEAN` |
| `callKey` | `callKey` | `STRING` |
| `tag` | `tag` | `STRING` |
| `va_ibm_id` | `va_ibm_id` | `STRING` |
| `menu_type` | `menu_type` | `STRING` |
| `ticket_number` | `ticket_number` | `STRING` |
| `operation_context` | `operation_context` | `STRING` |
| `contact_phone` | `contact_phone` | `STRING` |
| `contact_preference` | `contact_preference` | `STRING` |
| `contact_name` | `contact_name` | `STRING` |
| `reported_by` | `reported_by` | `STRING` |
| `wfas_context` | `wfas_context` | `STRING` |
| `autofill_template_name` | `autofill_template_name` | `STRING` |
| `number_of_days_interval` | `number_of_days_interval` | `NUMBER` |
| `ticket_state` | `ticket_state` | `STRING` |
| `internet_account_number` | `internet_account_number` | `STRING` |
| `tv_account_number` | `tv_account_number` | `STRING` |
| `wireline_telephone_number` | `wireline_telephone_number` | `STRING` |
| `service_identifier` | `service_identifier` | `STRING` |
| `order_identifier` | `order_identifier` | `STRING` |
| `omf_selections` | `omf_selections` | `STRING` |
| `accountNumber` | `accountNumber` | `STRING` |
| `internet_order_reference` | `internet_order_reference` | `STRING` |
| `selected_date` | `selected_date` | `STRING` |
| `selected_start_time` | `selected_start_time` | `STRING` |
| `selected_end_time` | `selected_end_time` | `STRING` |
| `selected_interval_name` | `selected_interval_name` | `STRING` |
| `released_preferred` | `released_preferred` | `STRING` |
| `date_range_begin` | `date_range_begin` | `STRING` |
| `date_range_end` | `date_range_end` | `STRING` |
| `acut_context` | `acut_context` | `STRING` |
| `telephone_number` | `telephone_number` | `STRING` |
| `is_prepaid` | `is_prepaid` | `STRING` |
| `domain` | `domain` | `STRING` |
| `l2_brand` | `l2_brand` | `STRING` |
| `vr_context` | `vr_context` | `STRING` |
| `service_id` | `service_id` | `STRING` |
| `callback_number` | `callback_number` | `STRING` |
| `preferred_contact_method` | `preferred_contact_method` | `STRING` |
| `otp_tns` | `otp_tns` | `ARRAY` |
| `skip_validation` | `skip_validation` | `STRING` |
| `status` | `status` | `STRING` |
| `auth_method` | `auth_method` | `STRING` |
| `calling_number` | `calling_number` | `STRING` |
| `otp` | `otp` | `STRING` |
| `billing_account_number` | `billing_account_number` | `STRING` |
| `dispatch_status` | `dispatch_status` | `STRING` |
| `dispatch_type` | `dispatch_type` | `STRING` |
| `trouble_ticket_state` | `trouble_ticket_state` | `STRING` |
| `task_type` | `task_type` | `STRING` |
| `tz_offset` | `tz_offset` | `STRING` |
| `trouble_type_code` | `trouble_type_code` | `STRING` |
| `worked_on_code` | `worked_on_code` | `STRING` |
| `worked_on_sub_code` | `worked_on_sub_code` | `STRING` |
| `customer_profile` | `customer_profile` | `STRING` |
| `pf_id` | `pf_id` | `STRING` |
| `has_outage` | `has_outage` | `STRING` |
| `is_finished` | `is_finished` | `STRING` |
| `services` | `services` | `STRING` |
| `npa` | `npa` | `STRING` |
| `nxx` | `nxx` | `STRING` |
| `transaction_id` | `transaction_id` | `STRING` |
| `cc_token` | `cc_token` | `STRING` |
| `expiry_year` | `expiry_year` | `STRING` |
| `expiry_month` | `expiry_month` | `STRING` |
| `security_code` | `security_code` | `STRING` |
| `amount_paid` | `amount_paid` | `STRING` |
| `cc_type` | `cc_type` | `STRING` |
| `installments` | `installments` | `STRING` |
| `amount` | `amount` | `STRING` |
| `startDate` | `startDate` | `STRING` |
| `endDate` | `endDate` | `STRING` |
| `intervals` | `intervals` | `ARRAY` |
| `calendar_context` | `calendar_context` | `STRING` |
| `message_text` | `message_text` | `STRING` |
| `mya_pitch` | `mya_pitch` | `BOOLEAN` |
| `local_nomatch_counter` | `local_nomatch_counter` | `NUMBER` |
| `local_noinput_counter` | `local_noinput_counter` | `NUMBER` |
| `local_trigger` | `local_trigger` | `STRING` |
| `webhook_success` | `webhook_success` | `STRING` |
| `acut_retrieve_response` | `acut_retrieve_response` | `STRING` |
| `closedTime` | `closedTime` | `STRING` |
| `street_number` | `street_number` | `STRING` |
| `street_name` | `street_name` | `STRING` |
| `sub_unit` | `sub_unit` | `STRING` |
| `address` | `address` | `STRING` |
| `street_address` | `street_address` | `STRING` |
| `notificationDetails` | `notificationDetails` | `STRING` |
| `closedTimeObj` | `closedTimeObj` | `STRING` |
| `acut_trouble_type_response` | `acut_trouble_type_response` | `STRING` |
| `apptStartTime` | `apptStartTime` | `STRING` |
| `apptEndTime` | `apptEndTime` | `STRING` |
| `apptStartTimeObj` | `apptStartTimeObj` | `STRING` |
| `apptEndTimeObj` | `apptEndTimeObj` | `STRING` |
| `trouble_type_message` | `trouble_type_message` | `STRING` |
| `dispatch_task_status_message` | `dispatch_task_status_message` | `STRING` |
| `ticket_day` | `ticket_day` | `STRING` |
| `ticket_month` | `ticket_month` | `STRING` |
| `ticket_date` | `ticket_date` | `STRING` |
| `ticket_year` | `ticket_year` | `STRING` |
| `start_time_hours` | `start_time_hours` | `STRING` |
| `end_time_hours` | `end_time_hours` | `STRING` |
| `ticket_day_fr` | `ticket_day_fr` | `STRING` |
| `ticket_month_fr` | `ticket_month_fr` | `STRING` |
| `ticket_date_fr` | `ticket_date_fr` | `STRING` |
| `ticket_year_fr` | `ticket_year_fr` | `STRING` |
| `start_time_hours_fr` | `start_time_hours_fr` | `STRING` |
| `end_time_hours_fr` | `end_time_hours_fr` | `STRING` |
| `acut_task_status_response` | `acut_task_status_response` | `STRING` |
| `categoryValue` | `categoryValue` | `STRING` |
| `active_dispatch_count` | `active_dispatch_count` | `STRING` |
| `pattern_id` | `pattern_id` | `STRING` |
| `hardstop` | `hardstop` | `BOOLEAN` |
| `page_id` | `page_id` | `STRING` |
| `flow_id` | `flow_id` | `STRING` |
| `page_name` | `page_name` | `STRING` |
| `filter_dispatch` | `filter_dispatch` | `STRING` |
| `acut_find_response` | `acut_find_response` | `STRING` |
| `acut_main_task_status_response` | `acut_main_task_status_response` | `STRING` |
| `acut_disposition_code_response` | `acut_disposition_code_response` | `STRING` |
| `local_noinput_counter1` | `local_noinput_counter1` | `STRING` |
| `local_nomatch_counter1` | `local_nomatch_counter1` | `STRING` |
| `ticket_mgmt_webhook_failure_type` | `ticket_mgmt_webhook_failure_type` | `STRING` |
| `NGA` | `NGA` | `STRING` |
| `handoff_from` | `handoff_from` | `STRING` |
| `language_tmp` | `language_tmp` | `STRING` |
| `transferred_call_flag` | `transferred_call_flag` | `NUMBER` |
| `repeat_flag` | `repeat_flag` | `NUMBER` |
| `no_match_1` | `no_match_1` | `BOOLEAN` |
| `no_match_2` | `no_match_2` | `BOOLEAN` |
| `invalid_clid_counter` | `invalid_clid_counter` | `NUMBER` |
| `speciality` | `speciality` | `STRING` |
| `skip_id` | `skip_id` | `BOOLEAN` |
| `bell_speciality` | `bell_speciality` | `STRING` |
| `call_id_ref` | `call_id_ref` | `STRING` |
| `tfn_tmp` | `tfn_tmp` | `STRING` |
| `clid_tmp` | `clid_tmp` | `STRING` |
| `ivr_va_get_did_fail` | `ivr_va_get_did_fail` | `BOOLEAN` |
| `ivr_va_cpm_check_fail` | `ivr_va_cpm_check_fail` | `BOOLEAN` |
| `OOV_CLASS_DIGIT_SEQUENCE` | `OOV_CLASS_DIGIT_SEQUENCE` | `STRING` |
| `va_ibm_id_pass` | `va_ibm_id_pass` | `BOOLEAN` |
| `temp_flag` | `temp_flag` | `NUMBER` |
| `special_status` | `special_status` | `STRING` |
| `test_bell_rehit_Check_Subscription` | `test_bell_rehit_Check_Subscription` | `STRING` |
| `bell_rehit_confirmation` | `bell_rehit_confirmation` | `STRING` |
| `Error_Count` | `Error_Count` | `NUMBER` |
| `_temp_clid` | `_temp_clid` | `STRING` |
| `id_again` | `id_again` | `BOOLEAN` |
| `Loud_Counter` | `Loud_Counter` | `NUMBER` |
| `event_other_number` | `event_other_number` | `STRING` |
| `va_entry_flow` | `va_entry_flow` | `STRING` |
| `ibm_entry_point` | `ibm_entry_point` | `STRING` |
| `_empty_string` | `_empty_string` | `STRING` |
| `nga_agent_id` | `nga_agent_id` | `STRING` |
| `test_agent_auth` | `test_agent_auth` | `STRING` |
| `agent_flag` | `agent_flag` | `BOOLEAN` |
| `test_auth` | `test_auth` | `STRING` |
| `bbm_smb_flag` | `bbm_smb_flag` | `STRING` |
| `digital_tools_phase2` | `digital_tools_phase2` | `BOOLEAN` |
| `no_input_counter_dfs` | `no_input_counter_dfs` | `STRING` |
| `va_caller_channel` | `va_caller_channel` | `STRING` |
| `intake_routing_lookup_response` | `intake_routing_lookup_response` | `STRING` |
| `menu_id_ref` | `menu_id_ref` | `STRING` |
| `department_id` | `department_id` | `STRING` |
| `department_id_ref` | `department_id_ref` | `STRING` |
| `get_department_id_response` | `get_department_id_response` | `STRING` |
| `test_multiban` | `test_multiban` | `STRING` |
| `banType` | `banType` | `STRING` |
| `banSubType` | `banSubType` | `STRING` |
| `marketSegment` | `marketSegment` | `STRING` |
| `nm1_get_cust_profile_response` | `nm1_get_cust_profile_response` | `STRING` |
| `session` | `session` | `STRING` |
| `config` | `config` | `STRING` |
| `ivr_to_va_entry` | `ivr_to_va_entry` | `BOOLEAN` |
| `BBM_flag` | `BBM_flag` | `BOOLEAN` |
| `credit_card_number` | `credit_card_number` | `STRING` |
| `card_expiry_date` | `card_expiry_date` | `STRING` |
| `Agent_Counter` | `Agent_Counter` | `NUMBER` |
| `semantic_void` | `semantic_void` | `NUMBER` |
| `identification_repeat` | `identification_repeat` | `NUMBER` |
| `PHN_Invalid_Counter` | `PHN_Invalid_Counter` | `NUMBER` |
| `CPM_Invalid_Counter` | `CPM_Invalid_Counter` | `NUMBER` |
| `PHN_Incorrect_Counter` | `PHN_Incorrect_Counter` | `NUMBER` |
| `aqd_counter` | `aqd_counter` | `NUMBER` |
| `va_ivr_cirn_check` | `va_ivr_cirn_check` | `BOOLEAN` |
| `va_ivr_cpm_route` | `va_ivr_cpm_route` | `BOOLEAN` |
| `BBM` | `BBM` | `BOOLEAN` |
| `crn_check` | `crn_check` | `STRING` |
| `ivr_handoff_identification` | `ivr_handoff_identification` | `BOOLEAN` |
| `clid_pass` | `clid_pass` | `BOOLEAN` |
| `More_Time_Counter` | `More_Time_Counter` | `NUMBER` |
| `Mistake_Counter` | `Mistake_Counter` | `NUMBER` |
| `No_Input_Counter` | `No_Input_Counter` | `NUMBER` |
| `No_Match_Counter` | `No_Match_Counter` | `NUMBER` |
| `dwt_counter` | `dwt_counter` | `NUMBER` |
| `global_error_counter_` | `global_error_counter_` | `STRING` |
| `stt_count` | `stt_count` | `NUMBER` |
| `db_get_bbm_mkseg_dip_response` | `db_get_bbm_mkseg_dip_response` | `STRING` |
| `business_type` | `business_type` | `STRING` |
| `temp_number` | `temp_number` | `STRING` |
| `npa_nxx_lookup_response` | `npa_nxx_lookup_response` | `STRING` |
| `va_ivr_cirn` | `va_ivr_cirn` | `STRING` |
| `nm1_grant` | `nm1_grant` | `BOOLEAN` |
| `CCC_asked` | `CCC_asked` | `STRING` |
| `identification_fallback_flag` | `identification_fallback_flag` | `STRING` |
| `fallback_flag` | `fallback_flag` | `BOOLEAN` |
| `regional_identity` | `regional_identity` | `BOOLEAN` |
| `ivr_handoff` | `ivr_handoff` | `BOOLEAN` |
| `is_business` | `is_business` | `BOOLEAN` |
| `unique_service_count` | `unique_service_count` | `STRING` |
| `active_services` | `active_services` | `ARRAY` |
| `counter` | `counter` | `NUMBER` |
| `CIRN_1` | `CIRN_1` | `STRING` |
| `CIRN_Len` | `CIRN_Len` | `STRING` |
| `CIRN_1st_Pos` | `CIRN_1st_Pos` | `STRING` |
| `CIRN_11_digit_Valid` | `CIRN_11_digit_Valid` | `STRING` |
| `CIRN_11_digit_Invalid` | `CIRN_11_digit_Invalid` | `STRING` |
| `CIRN_10_digit_Valid` | `CIRN_10_digit_Valid` | `STRING` |
| `CIRN_Invalid` | `CIRN_Invalid` | `STRING` |
| `CIRN_10` | `CIRN_10` | `STRING` |
| `CIRN_flag` | `CIRN_flag` | `STRING` |
| `utterance_fallback` | `utterance_fallback` | `STRING` |
| `active_lob` | `active_lob` | `STRING` |
| `ban_yes` | `ban_yes` | `BOOLEAN` |
| `clid_not_found` | `clid_not_found` | `BOOLEAN` |
| `identificaton_status` | `identificaton_status` | `STRING` |
| `nm1_flag` | `nm1_flag` | `BOOLEAN` |
| `nm1_message` | `nm1_message` | `STRING` |
| `nm1_ban` | `nm1_ban` | `STRING` |
| `nm1_service_type` | `nm1_service_type` | `STRING` |
| `nm1_account` | `nm1_account` | `BOOLEAN` |
| `n_billing_account` | `n_billing_account` | `NUMBER` |
| `contain_mobility` | `contain_mobility` | `STRING` |
| `delinquent_flag` | `delinquent_flag` | `STRING` |
| `billing_account_number_ref` | `billing_account_number_ref` | `STRING` |
| `nm1_account_found` | `nm1_account_found` | `STRING` |
| `CIRN_999` | `CIRN_999` | `STRING` |
| `ban_provided_instead_cirn` | `ban_provided_instead_cirn` | `BOOLEAN` |
| `cirn_grp1` | `cirn_grp1` | `STRING` |
| `cirn_grp2` | `cirn_grp2` | `STRING` |
| `cirn_grp3` | `cirn_grp3` | `STRING` |
| `cirn_grp4` | `cirn_grp4` | `STRING` |
| `test4806` | `test4806` | `STRING` |
| `customer_id_search_response` | `customer_id_search_response` | `STRING` |
| `billing_account_number_list` | `billing_account_number_list` | `STRING` |
| `billing_account_info_list` | `billing_account_info_list` | `ARRAY` |
| `is_prepaid_list` | `is_prepaid_list` | `STRING` |
| `brand_value` | `brand_value` | `STRING` |
| `regional_flag` | `regional_flag` | `BOOLEAN` |
| `customer_id_search_region_response` | `customer_id_search_region_response` | `STRING` |
| `region` | `region` | `STRING` |
| `_temp_number` | `_temp_number` | `STRING` |
| `is_canadian` | `is_canadian` | `STRING` |
| `db_status_check` | `db_status_check` | `BOOLEAN` |
| `first_user_account` | `first_user_account` | `STRING` |
| `search_by_tn_ws` | `search_by_tn_ws` | `STRING` |
| `print_test` | `print_test` | `STRING` |
| `is_preapid_value_list` | `is_preapid_value_list` | `STRING` |
| `cpm_ban` | `cpm_ban` | `STRING` |
| `nm1_multiban` | `nm1_multiban` | `BOOLEAN` |
| `customer_data` | `customer_data` | `STRING` |
| `is_preapid` | `is_preapid` | `STRING` |
| `ROC` | `ROC` | `ARRAY` |
| `ATL` | `ATL` | `ARRAY` |
| `Central` | `Central` | `ARRAY` |
| `MTS` | `MTS` | `ARRAY` |
| `different_cirn` | `different_cirn` | `STRING` |
| `regional_grant` | `regional_grant` | `BOOLEAN` |
| `va_to_ccaip` | `va_to_ccaip` | `BOOLEAN` |
| `customer_name` | `customer_name` | `STRING` |
| `intent` | `intent` | `STRING` |
| `aqd_lob` | `aqd_lob` | `STRING` |
| `cx_cornerstone` | `cx_cornerstone` | `BOOLEAN` |
| `X_DNIS` | `X_DNIS` | `STRING` |
| `X_G2Mkey` | `X_G2Mkey` | `STRING` |
| `sip_uri` | `sip_uri` | `STRING` |
| `fallback_3_triggered` | `fallback_3_triggered` | `BOOLEAN` |
| `no_match_counter` | `no_match_counter` | `NUMBER` |
| `previous_route` | `previous_route` | `STRING` |
| `query_rewriter_looping_counter` | `query_rewriter_looping_counter` | `NUMBER` |
| `test_private_sms` | `test_private_sms` | `STRING` |
| `fallback_counter` | `fallback_counter` | `NUMBER` |
| `contact_numbers_list` | `contact_numbers_list` | `STRING` |
| `is_in_account` | `is_in_account` | `STRING` |
| `sms_not_received_counter` | `sms_not_received_counter` | `NUMBER` |
| `webhook_succes` | `webhook_succes` | `STRING` |
| `vanity_link` | `vanity_link` | `STRING` |
| `noinput` | `noinput` | `BOOLEAN` |
| `intent_sdl_map_response` | `intent_sdl_map_response` | `STRING` |
| `sms_sending` | `sms_sending` | `STRING` |
| `from_flow` | `from_flow` | `STRING` |
| `pin_validation_counter` | `pin_validation_counter` | `NUMBER` |
| `PIN_Resend_Counter` | `PIN_Resend_Counter` | `NUMBER` |
| `Wrong_PIN_Counter` | `Wrong_PIN_Counter` | `NUMBER` |
| `local_no_match` | `local_no_match` | `NUMBER` |
| `local_no_input` | `local_no_input` | `NUMBER` |
| `local_no_match_counter` | `local_no_match_counter` | `NUMBER` |
| `local_no_input_counter` | `local_no_input_counter` | `NUMBER` |
| `_ban_account` | `_ban_account` | `STRING` |
| `_wsc_on_ban` | `_wsc_on_ban` | `STRING` |
| `clid_wsc_on_ban` | `clid_wsc_on_ban` | `STRING` |
| `clid_in_otp_tns` | `clid_in_otp_tns` | `STRING` |
| `auth_options_response` | `auth_options_response` | `STRING` |
| `n_wsc_on_ban` | `n_wsc_on_ban` | `STRING` |
| `_contact_number_on_ban` | `_contact_number_on_ban` | `STRING` |
| `n_otp_tns` | `n_otp_tns` | `STRING` |
| `contact_number_on_ban` | `contact_number_on_ban` | `STRING` |
| `cnban_in_otp_tns` | `cnban_in_otp_tns` | `STRING` |
| `local_no_match_phone` | `local_no_match_phone` | `NUMBER` |
| `hp_in_ban_response` | `hp_in_ban_response` | `STRING` |
| `is_old` | `is_old` | `BOOLEAN` |
| `_temp_date_parts_list` | `_temp_date_parts_list` | `STRING` |
| `_temp_year_num` | `_temp_year_num` | `STRING` |
| `_temp_month_num` | `_temp_month_num` | `STRING` |
| `___temp_day_num` | `___temp_day_num` | `STRING` |
| `__temp_day_num` | `__temp_day_num` | `STRING` |
| `_temp_day_num` | `_temp_day_num` | `STRING` |
| `_temp_date_obj` | `_temp_date_obj` | `STRING` |
| `_temp_date_plus_45` | `_temp_date_plus_45` | `STRING` |
| `_temp_date_plus_45_parts` | `_temp_date_plus_45_parts` | `STRING` |
| `_temp_year_plus_45_num` | `_temp_year_plus_45_num` | `STRING` |
| `_temp_month_plus_45_num` | `_temp_month_plus_45_num` | `STRING` |
| `___temp_day_plus_45_num` | `___temp_day_plus_45_num` | `STRING` |
| `__temp_day_plus_45_num` | `__temp_day_plus_45_num` | `STRING` |
| `_temp_day_plus_45_num` | `_temp_day_plus_45_num` | `STRING` |
| `_temp_date_plus_45_obj` | `_temp_date_plus_45_obj` | `STRING` |
| `idenfication_status` | `idenfication_status` | `STRING` |
| `authentication_status` | `authentication_status` | `STRING` |
| `count_otp_tns` | `count_otp_tns` | `STRING` |
| `repeat_attempt_count` | `repeat_attempt_count` | `NUMBER` |
| `otp_has_phone` | `otp_has_phone` | `BOOLEAN` |
| `PINTimeout` | `PINTimeout` | `STRING` |
| `from_pin` | `from_pin` | `BOOLEAN` |
| `number_is_wsc_on_ban` | `number_is_wsc_on_ban` | `STRING` |
| `number_is_contact_on_ban` | `number_is_contact_on_ban` | `STRING` |
| `telephone_otp_counter` | `telephone_otp_counter` | `NUMBER` |
| `CIRN1` | `CIRN1` | `STRING` |
| `auth_repeat` | `auth_repeat` | `NUMBER` |
| `otp_validation_response` | `otp_validation_response` | `STRING` |
| `is_authenticated` | `is_authenticated` | `STRING` |
| `pin_validation_response` | `pin_validation_response` | `STRING` |
| `is_home_phone` | `is_home_phone` | `STRING` |
| `get_ras_apb_response` | `get_ras_apb_response` | `STRING` |
| `hang_up` | `hang_up` | `STRING` |
| `agent_transfer` | `agent_transfer` | `STRING` |
| `apb_skip` | `apb_skip` | `BOOLEAN` |
| `apb_message` | `apb_message` | `STRING` |
| `apb_status` | `apb_status` | `STRING` |
| `n_acut_tickets` | `n_acut_tickets` | `NUMBER` |
| `n_omf_tickets` | `n_omf_tickets` | `NUMBER` |
| `ticket_number_ref` | `ticket_number_ref` | `STRING` |
| `ticket_number2` | `ticket_number2` | `STRING` |
| `ticket_state2` | `ticket_state2` | `STRING` |
| `ticket__number` | `ticket__number` | `STRING` |
| `ticket_state1` | `ticket_state1` | `STRING` |
| `ticket_number1` | `ticket_number1` | `STRING` |
| `date_formatted2` | `date_formatted2` | `STRING` |
| `order_identifier2` | `order_identifier2` | `STRING` |
| `internet_order_reference2` | `internet_order_reference2` | `STRING` |
| `specialty_queue` | `specialty_queue` | `STRING` |
| `order_identifier1` | `order_identifier1` | `STRING` |
| `internet_order_reference1` | `internet_order_reference1` | `STRING` |
| `recent_service_type2` | `recent_service_type2` | `STRING` |
| `lob_list` | `lob_list` | `STRING` |
| `lob_service_ids` | `lob_service_ids` | `STRING` |
| `_lob_count` | `_lob_count` | `STRING` |
| `lob_count` | `lob_count` | `STRING` |
| `recent_service_type1` | `recent_service_type1` | `STRING` |
| `date_formatted` | `date_formatted` | `STRING` |
| `ticket_summaries` | `ticket_summaries` | `STRING` |
| `ticket_summary1` | `ticket_summary1` | `STRING` |
| `ticket_creation_time1` | `ticket_creation_time1` | `STRING` |
| `month` | `month` | `STRING` |
| `year` | `year` | `STRING` |
| `ticket_summary2` | `ticket_summary2` | `STRING` |
| `ticket_creation_time2` | `ticket_creation_time2` | `STRING` |
| `day2` | `day2` | `STRING` |
| `month2` | `month2` | `STRING` |
| `year2` | `year2` | `STRING` |
| `omf_summary_failure` | `omf_summary_failure` | `NUMBER` |
| `order_summaries` | `order_summaries` | `STRING` |
| `recent_order1` | `recent_order1` | `STRING` |
| `recent_order2` | `recent_order2` | `STRING` |
| `order_summary_response` | `order_summary_response` | `STRING` |
| `is_historic` | `is_historic` | `BOOLEAN` |
| `Phone_Incorrect_Counter` | `Phone_Incorrect_Counter` | `NUMBER` |
| `Landline_Incorrect_Counter` | `Landline_Incorrect_Counter` | `NUMBER` |
| `Phone_Invalid_Counter` | `Phone_Invalid_Counter` | `NUMBER` |
| `Landline_Invalid_Counter` | `Landline_Invalid_Counter` | `NUMBER` |
| `Incorrect_Counter_User_NOT_GIVING_NUMBER` | `Incorrect_Counter_User_NOT_GIVING_NUMBER` | `NUMBER` |
| `otp_number_list` | `otp_number_list` | `STRING` |
| `number` | `number` | `STRING` |
| `type` | `type` | `STRING` |
| `is_clid_wsn` | `is_clid_wsn` | `STRING` |
| `contact_method_completed` | `contact_method_completed` | `BOOLEAN` |
| `Contact_Number_1` | `Contact_Number_1` | `STRING` |
| `Contact_Number_len` | `Contact_Number_len` | `STRING` |
| `Contact_Number_1st_Pos` | `Contact_Number_1st_Pos` | `STRING` |
| `Contact_Number_11_digit_Valid` | `Contact_Number_11_digit_Valid` | `STRING` |
| `Contact_Number_11_digit_Invalid` | `Contact_Number_11_digit_Invalid` | `STRING` |
| `Contact_Number_10_digit_Valid` | `Contact_Number_10_digit_Valid` | `STRING` |
| `Contact_Number_Invalid` | `Contact_Number_Invalid` | `STRING` |
| `Contact_Number_10` | `Contact_Number_10` | `STRING` |
| `Contact_Number_flag` | `Contact_Number_flag` | `STRING` |
| `temp_clid` | `temp_clid` | `STRING` |
| `appointment_counter` | `appointment_counter` | `NUMBER` |
| `calendarInformationList` | `calendarInformationList` | `STRING` |
| `consistent_calendars` | `consistent_calendars` | `STRING` |
| `input_start_date_string` | `input_start_date_string` | `STRING` |
| `input_end_date_string` | `input_end_date_string` | `STRING` |
| `omf_selected_interval_response_raw` | `omf_selected_interval_response_raw` | `STRING` |
| `omf_selected_interval_response` | `omf_selected_interval_response` | `STRING` |
| `omf_selections_obj` | `omf_selections_obj` | `STRING` |
| `contains_not_modifiable` | `contains_not_modifiable` | `STRING` |
| `order_detail_response` | `order_detail_response` | `STRING` |
| `contains_not_modfiable` | `contains_not_modfiable` | `STRING` |
| `calendarInformationList_1` | `calendarInformationList_1` | `STRING` |
| `list_of_date_offered` | `list_of_date_offered` | `STRING` |
| `calender_availibility_response` | `calender_availibility_response` | `STRING` |
| `omf_calendaring_response` | `omf_calendaring_response` | `STRING` |
| `calendar_data` | `calendar_data` | `STRING` |
| `category_value` | `category_value` | `STRING` |
| `ticket_dispatch_status` | `ticket_dispatch_status` | `STRING` |
| `disposition_code_message` | `disposition_code_message` | `STRING` |
| `main_task_status_message` | `main_task_status_message` | `STRING` |
| `resolution_date_formatted` | `resolution_date_formatted` | `STRING` |
| `ticket_status` | `ticket_status` | `STRING` |
| `active_dispatch_count_1` | `active_dispatch_count_1` | `STRING` |
| `dispatch_id` | `dispatch_id` | `STRING` |
| `resolution_comment` | `resolution_comment` | `STRING` |
| `closed_time` | `closed_time` | `STRING` |
| `acut_context_raw` | `acut_context_raw` | `STRING` |
| `appointment_start_date` | `appointment_start_date` | `STRING` |
| `resolution_date` | `resolution_date` | `STRING` |
| `day1` | `day1` | `STRING` |
| `month1` | `month1` | `STRING` |
| `year1` | `year1` | `STRING` |
| `mya_information_response` | `mya_information_response` | `STRING` |
| `id_cirn_check` | `id_cirn_check` | `BOOLEAN` |
| `oneBillIndicator` | `oneBillIndicator` | `STRING` |
| `segment` | `segment` | `STRING` |
| `aqd_sub_flow` | `aqd_sub_flow` | `STRING` |
| `nm1_get_col_agency_info_response` | `nm1_get_col_agency_info_response` | `STRING` |
| `apb_transfer_location` | `apb_transfer_location` | `STRING` |
| `deai_search_by_tn_response` | `deai_search_by_tn_response` | `STRING` |
| `from_vr` | `from_vr` | `BOOLEAN` |
| `DEFAULT_DEPARTMENT_ID` | `DEFAULT_DEPARTMENT_ID` | `STRING` |
| `deparmtent_id` | `deparmtent_id` | `STRING` |
| `configs` | `configs` | `STRING` |
| `DEFAULT_MENU_ID` | `DEFAULT_MENU_ID` | `STRING` |
| `deparment_id_ref` | `deparment_id_ref` | `STRING` |
| `aqd_response` | `aqd_response` | `STRING` |
| `ccaip_call_id` | `ccaip_call_id` | `STRING` |
| `get_segment_response` | `get_segment_response` | `STRING` |
| `PIN_Invalid_Counter` | `PIN_Invalid_Counter` | `NUMBER` |
| `PIN_Not_Received` | `PIN_Not_Received` | `NUMBER` |
| `from_custom_fallback` | `from_custom_fallback` | `NUMBER` |
| `service_account_number` | `service_account_number` | `STRING` |
| `eligibile_for_otp` | `eligibile_for_otp` | `STRING` |
| `postal_code_three_backend` | `postal_code_three_backend` | `STRING` |
| `sp0` | `sp0` | `STRING` |
| `sp1` | `sp1` | `STRING` |
| `sp2` | `sp2` | `STRING` |
| `sp3` | `sp3` | `STRING` |
| `sp4` | `sp4` | `STRING` |
| `sp5` | `sp5` | `STRING` |
| `sp6` | `sp6` | `STRING` |
| `sp7` | `sp7` | `STRING` |
| `sp8` | `sp8` | `STRING` |
| `sp9` | `sp9` | `STRING` |
| `wrong_postal` | `wrong_postal` | `NUMBER` |
| `handoff_to` | `handoff_to` | `STRING` |
| `init_getpos` | `init_getpos` | `BOOLEAN` |
| `len_otp_number_list` | `len_otp_number_list` | `STRING` |
| `billing_contact_number` | `billing_contact_number` | `STRING` |
| `len_billing_contact_number` | `len_billing_contact_number` | `STRING` |
| `billing_contact_number1` | `billing_contact_number1` | `STRING` |
| `service_types` | `service_types` | `STRING` |
| `len_services` | `len_services` | `STRING` |
| `pin_available` | `pin_available` | `STRING` |
| `is_telephone_otp_wsn` | `is_telephone_otp_wsn` | `STRING` |
| `billing_account_info_list2` | `billing_account_info_list2` | `STRING` |
| `s_postcodes` | `s_postcodes` | `STRING` |
| `url` | `url` | `STRING` |
| `from_wsc` | `from_wsc` | `STRING` |
| `is_locked` | `is_locked` | `STRING` |
| `from_billing` | `from_billing` | `STRING` |
| `consolidated_status` | `consolidated_status` | `STRING` |
| `dueDateFull` | `dueDateFull` | `STRING` |
| `dueDate` | `dueDate` | `STRING` |
| `start_one_time_pmt_response` | `start_one_time_pmt_response` | `STRING` |
| `last_payment_amount` | `last_payment_amount` | `STRING` |
| `use_case_fr` | `use_case_fr` | `STRING` |
| `use_case_en` | `use_case_en` | `STRING` |
| `balance_payment_details_response` | `balance_payment_details_response` | `STRING` |
| `payment_flag_otcc` | `payment_flag_otcc` | `BOOLEAN` |
| `force_ss_exception` | `force_ss_exception` | `STRING` |
| `bee_testing` | `bee_testing` | `STRING` |
| `current_year` | `current_year` | `STRING` |
| `current_month` | `current_month` | `STRING` |
| `ivr_va_no_ban_counter` | `ivr_va_no_ban_counter` | `NUMBER` |
| `ivr_va_ban_count` | `ivr_va_ban_count` | `STRING` |
| `lob_from_ivr` | `lob_from_ivr` | `STRING` |
| `ivr_va_lob_translation` | `ivr_va_lob_translation` | `OBJECT` |
| `did_number` | `did_number` | `STRING` |
| `get_did_data_response` | `get_did_data_response` | `STRING` |
| `ivr_va_cpm_data` | `ivr_va_cpm_data` | `STRING` |
| `ivr_va_ban_list` | `ivr_va_ban_list` | `STRING` |
| `sales_queue_open` | `sales_queue_open` | `STRING` |
| `smb_ban` | `smb_ban` | `STRING` |
| `cc_ban` | `cc_ban` | `STRING` |
| `ccc_ban` | `ccc_ban` | `STRING` |
| `non_central` | `non_central` | `STRING` |
| `s2a_counter` | `s2a_counter` | `NUMBER` |
| `POSTALCODE` | `POSTALCODE` | `STRING` |
| `OOV_CLASS_POSTALCODE` | `OOV_CLASS_POSTALCODE` | `STRING` |
| `_subscriber_number` | `_subscriber_number` | `STRING` |
| `SMB` | `SMB` | `STRING` |
| `CCC` | `CCC` | `STRING` |
| `atlantic` | `atlantic` | `STRING` |
| `BNQ` | `BNQ` | `STRING` |
| `entry` | `entry` | `STRING` |
| `entry_route` | `entry_route` | `STRING` |
| `account_number_present_` | `account_number_present_` | `STRING` |
| `smb_ccc_present` | `smb_ccc_present` | `STRING` |
| `ccc_present` | `ccc_present` | `STRING` |
| `smb_present` | `smb_present` | `STRING` |
| `consumer` | `consumer` | `BOOLEAN` |
| `postcode_count` | `postcode_count` | `STRING` |
| `i` | `i` | `NUMBER` |
| `n_postcode` | `n_postcode` | `STRING` |
| `i_postcode` | `i_postcode` | `STRING` |
| `unique_postcode_list_all` | `unique_postcode_list_all` | `STRING` |
| `postcode_list_all` | `postcode_list_all` | `STRING` |
| `lob_postcode_count` | `lob_postcode_count` | `STRING` |
| `lob_i` | `lob_i` | `NUMBER` |
| `lob_postcode_list_all` | `lob_postcode_list_all` | `STRING` |
| `account_number_present` | `account_number_present` | `STRING` |
| `billing_accounts_lob` | `billing_accounts_lob` | `STRING` |
| `n_billing_accounts_lob` | `n_billing_accounts_lob` | `STRING` |
| `n_lob_postcode_list_all` | `n_lob_postcode_list_all` | `STRING` |
| `billing_address_postcode` | `billing_address_postcode` | `STRING` |
| `n_billing_accounts_postcoode` | `n_billing_accounts_postcoode` | `STRING` |
| `service_address_postcode` | `service_address_postcode` | `STRING` |
| `n_service_address_postcode` | `n_service_address_postcode` | `STRING` |
| `billing_account_mobility` | `billing_account_mobility` | `STRING` |
| `n_billing_account_mobility` | `n_billing_account_mobility` | `STRING` |
| `billing_account_internet` | `billing_account_internet` | `STRING` |
| `n_billing_account_internet` | `n_billing_account_internet` | `STRING` |
| `billing_account_tv` | `billing_account_tv` | `STRING` |
| `n_billing_account_tv` | `n_billing_account_tv` | `STRING` |
| `billing_account_homephone` | `billing_account_homephone` | `STRING` |
| `n_billing_account_homephone` | `n_billing_account_homephone` | `STRING` |
| `n_postcode_list_all` | `n_postcode_list_all` | `STRING` |
| `consumer_ban_count_ccc` | `consumer_ban_count_ccc` | `STRING` |
| `consumer_ban_count_smb` | `consumer_ban_count_smb` | `STRING` |
| `consumer_count_all` | `consumer_count_all` | `STRING` |
| `a_test` | `a_test` | `STRING` |
| `temp_list` | `temp_list` | `STRING` |
| `clp_program` | `clp_program` | `STRING` |
| `clp_aul_limit` | `clp_aul_limit` | `STRING` |
| `clp_balance` | `clp_balance` | `STRING` |
| `clp_sus_limit` | `clp_sus_limit` | `STRING` |
| `10_days` | `10_days` | `STRING` |
| `bill_date_month` | `bill_date_month` | `STRING` |
| `bill_date_year` | `bill_date_year` | `STRING` |
| `bill_date` | `bill_date` | `STRING` |
| `nm1_get_bill_details_response` | `nm1_get_bill_details_response` | `STRING` |
| `formatted_date` | `formatted_date` | `STRING` |
| `billingcycle_status` | `billingcycle_status` | `STRING` |
| `get_clp_info_response` | `get_clp_info_response` | `STRING` |
| `bypass_wh` | `bypass_wh` | `STRING` |
| `last_payment_amount_number` | `last_payment_amount_number` | `STRING` |
| `account_balance_number` | `account_balance_number` | `STRING` |
| `accountBalance` | `accountBalance` | `STRING` |
| `last_payment_date` | `last_payment_date` | `STRING` |
| `fr_date` | `fr_date` | `STRING` |
| `error_return_code` | `error_return_code` | `STRING` |
| `accountType` | `accountType` | `STRING` |
| `accountSubType` | `accountSubType` | `STRING` |
| `account_balance` | `account_balance` | `STRING` |
| `pastDueAmount` | `pastDueAmount` | `STRING` |
| `nm1_get_ban_profile_response` | `nm1_get_ban_profile_response` | `STRING` |
| `clp_spending_limit` | `clp_spending_limit` | `STRING` |
| `ibm_application_id_` | `ibm_application_id_` | `STRING` |
| `formatDate` | `formatDate` | `STRING` |
| `md_list` | `md_list` | `STRING` |
| `nm1_get_last_payment_info_response` | `nm1_get_last_payment_info_response` | `STRING` |
| `webhook_status` | `webhook_status` | `STRING` |
| `bad_amount` | `bad_amount` | `NUMBER` |
| `amount_correction_required` | `amount_correction_required` | `NUMBER` |
| `suggest_amount_flag` | `suggest_amount_flag` | `NUMBER` |
| `from_restricted` | `from_restricted` | `STRING` |
| `from_non_restricted` | `from_non_restricted` | `STRING` |
| `from_already_provided` | `from_already_provided` | `BOOLEAN` |
| `amount_paid_number` | `amount_paid_number` | `STRING` |
| `amount_paid_length` | `amount_paid_length` | `STRING` |
| `amount_paid_sub` | `amount_paid_sub` | `STRING` |
| `has_decimal` | `has_decimal` | `STRING` |
| `amount_decimal` | `amount_decimal` | `STRING` |
| `amount_integer` | `amount_integer` | `STRING` |
| `suggested_amount_value` | `suggested_amount_value` | `STRING` |
| `otccp_exit_2` | `otccp_exit_2` | `BOOLEAN` |
| `current_account_balance` | `current_account_balance` | `STRING` |
| `due_amount` | `due_amount` | `STRING` |
| `other_amount_counter` | `other_amount_counter` | `NUMBER` |
| `other_amount_value` | `other_amount_value` | `STRING` |
| `message_type_group` | `message_type_group` | `NUMBER` |
| `spending_limit` | `spending_limit` | `STRING` |
| `curSpendingLimitBal` | `curSpendingLimitBal` | `STRING` |
| `OOV_CLASS_NUMERIC_SEQUENCE` | `OOV_CLASS_NUMERIC_SEQUENCE` | `STRING` |
| `other_amount_mentioned` | `other_amount_mentioned` | `BOOLEAN` |
| `paDays` | `paDays` | `STRING` |
| `start_pmt_arrangement_response` | `start_pmt_arrangement_response` | `STRING` |
| `payment_amount` | `payment_amount` | `STRING` |
| `payment_attempt` | `payment_attempt` | `NUMBER` |
| `decimal_payment_attempt` | `decimal_payment_attempt` | `NUMBER` |
| `currentBalance` | `currentBalance` | `STRING` |
| `calculated_payment_date` | `calculated_payment_date` | `STRING` |
| `payment_amount_number` | `payment_amount_number` | `STRING` |
| `currentBalance_number` | `currentBalance_number` | `STRING` |
| `pastDueAmount_number` | `pastDueAmount_number` | `STRING` |
| `substituted_amount` | `substituted_amount` | `STRING` |
| `decimalx1000` | `decimalx1000` | `STRING` |
| `paDaysResponse` | `paDaysResponse` | `STRING` |
| `payment_type` | `payment_type` | `STRING` |
| `confirmationNumber` | `confirmationNumber` | `STRING` |
| `errorCodeID` | `errorCodeID` | `STRING` |
| `submit_pmt_arrangement_response` | `submit_pmt_arrangement_response` | `STRING` |
| `bank_account` | `bank_account` | `STRING` |
| `contains_mobility` | `contains_mobility` | `STRING` |
| `active_service` | `active_service` | `STRING` |
| `profile_not_found` | `profile_not_found` | `BOOLEAN` |
| `countInstallment` | `countInstallment` | `STRING` |
| `countInsatllment1` | `countInsatllment1` | `STRING` |
| `amountRemaining` | `amountRemaining` | `STRING` |
| `pmt_arrangement_eligibility_response` | `pmt_arrangement_eligibility_response` | `STRING` |
| `installmentCheck` | `installmentCheck` | `STRING` |
| `date_today` | `date_today` | `STRING` |
| `pa_days_num` | `pa_days_num` | `STRING` |
| `pa_date` | `pa_date` | `STRING` |
| `actual_date` | `actual_date` | `STRING` |
| `calculated_date` | `calculated_date` | `STRING` |
| `calculated_date1` | `calculated_date1` | `STRING` |
| `delinquentStatus` | `delinquentStatus` | `STRING` |
| `Y` | `Y` | `STRING` |
| `delinquency_details_response` | `delinquency_details_response` | `STRING` |
| `eligibilityCriteria` | `eligibilityCriteria` | `STRING` |
| `installmentDetails` | `installmentDetails` | `STRING` |
| `current_time` | `current_time` | `STRING` |
| `current_time_override` | `current_time_override` | `STRING` |
| `onebillindicator` | `onebillindicator` | `STRING` |
| `errorCode` | `errorCode` | `STRING` |
| `Bantype` | `Bantype` | `STRING` |
| `Bansubtype` | `Bansubtype` | `STRING` |
| `Province` | `Province` | `STRING` |
| `preauth_exit_3` | `preauth_exit_3` | `BOOLEAN` |
| `preauth_exit_5` | `preauth_exit_5` | `BOOLEAN` |
| `get_pre_auth_payment_response` | `get_pre_auth_payment_response` | `STRING` |
| `vanity_url` | `vanity_url` | `STRING` |
| `preauth_exit_4` | `preauth_exit_4` | `BOOLEAN` |
| `eligInd` | `eligInd` | `STRING` |
| `eligibilityInfo` | `eligibilityInfo` | `STRING` |
| `nm1_get_pa_eligibility_response` | `nm1_get_pa_eligibility_response` | `STRING` |
| `start_pre_auth_pmt_response` | `start_pre_auth_pmt_response` | `STRING` |
| `npa_status` | `npa_status` | `STRING` |
| `faq_flag` | `faq_flag` | `NUMBER` |
| `cc_invalid_counter` | `cc_invalid_counter` | `NUMBER` |
| `mod_counter` | `mod_counter` | `NUMBER` |
| `incorrect_cvv` | `incorrect_cvv` | `NUMBER` |
| `n_incorrect_date` | `n_incorrect_date` | `NUMBER` |
| `card_len_check_counter` | `card_len_check_counter` | `NUMBER` |
| `wrong_cc_number_counter` | `wrong_cc_number_counter` | `NUMBER` |
| `total_cc_attempts` | `total_cc_attempts` | `NUMBER` |
| `len_cvv_number` | `len_cvv_number` | `STRING` |
| `card_brand` | `card_brand` | `STRING` |
| `cc_from_utterance` | `cc_from_utterance` | `STRING` |
| `len_alpha_from_utterance` | `len_alpha_from_utterance` | `STRING` |
| `len_cc_from_utterance` | `len_cc_from_utterance` | `STRING` |
| `check_credit_card_number` | `check_credit_card_number` | `BOOLEAN` |
| `len_credit_card_number` | `len_credit_card_number` | `STRING` |
| `amex_check_digits` | `amex_check_digits` | `STRING` |
| `number_from_utterance` | `number_from_utterance` | `STRING` |
| `alpha_from_utterance` | `alpha_from_utterance` | `STRING` |
| `cc_from_uttrance` | `cc_from_uttrance` | `STRING` |
| `dts_token_details_response` | `dts_token_details_response` | `STRING` |
| `expired_count` | `expired_count` | `NUMBER` |
| `year_today` | `year_today` | `STRING` |
| `month_today` | `month_today` | `STRING` |
| `len_card_expiry_date` | `len_card_expiry_date` | `STRING` |
| `cc_details_valid` | `cc_details_valid` | `STRING` |
| `cc_error_code_id` | `cc_error_code_id` | `STRING` |
| `update_pre_auth_cc_details_response` | `update_pre_auth_cc_details_response` | `STRING` |
| `clp_bad_amount` | `clp_bad_amount` | `NUMBER` |
| `paid_full` | `paid_full` | `BOOLEAN` |
| `cc_failed_attempt` | `cc_failed_attempt` | `NUMBER` |
| `newSpendingLimitBal` | `newSpendingLimitBal` | `STRING` |
| `newSpendingLimitClpBal` | `newSpendingLimitClpBal` | `STRING` |
| `current_special_status` | `current_special_status` | `STRING` |
| `current_special_queue` | `current_special_queue` | `STRING` |
| `clp_balance_number` | `clp_balance_number` | `STRING` |
| `amount_paid_clp_number` | `amount_paid_clp_number` | `STRING` |
| `no_change_col_status` | `no_change_col_status` | `BOOLEAN` |
| `isValid` | `isValid` | `STRING` |
| `update_otp_cc_details_response` | `update_otp_cc_details_response` | `STRING` |
| `submit_one_time_pmt_response` | `submit_one_time_pmt_response` | `STRING` |
| `confirmationCode` | `confirmationCode` | `STRING` |
| `dueAmount` | `dueAmount` | `STRING` |
| `contains_tv` | `contains_tv` | `STRING` |
| `contains_internet` | `contains_internet` | `STRING` |
| `active_service2` | `active_service2` | `STRING` |
| `contains_mobility2` | `contains_mobility2` | `STRING` |
| `contains_tv2` | `contains_tv2` | `STRING` |
| `contains_internet2` | `contains_internet2` | `STRING` |
| `showPaymentArrangementLink` | `showPaymentArrangementLink` | `STRING` |
| `amountPaid` | `amountPaid` | `STRING` |
| `past_due_amount` | `past_due_amount` | `STRING` |
| `current_balance` | `current_balance` | `STRING` |
| `due_date` | `due_date` | `STRING` |
| `start_pmt_notification_response` | `start_pmt_notification_response` | `STRING` |
| `showNotifyLink` | `showNotifyLink` | `STRING` |
| `isAccountSuspended` | `isAccountSuspended` | `STRING` |
| `remaining_balance` | `remaining_balance` | `STRING` |
| `submit_pmt_notification_response` | `submit_pmt_notification_response` | `STRING` |
| `payment_confirmation` | `payment_confirmation` | `BOOLEAN` |
| `id_auth_fail` | `id_auth_fail` | `BOOLEAN` |
| `proceed_with_ot_payment` | `proceed_with_ot_payment` | `BOOLEAN` |
| `offer_type` | `offer_type` | `STRING` |
| `otccp_exit_1` | `otccp_exit_1` | `STRING` |
| `speciality_1` | `speciality_1` | `STRING` |
| `get_pre_auth_payment_response_override` | `get_pre_auth_payment_response_override` | `STRING` |
| `webhook_success_override` | `webhook_success_override` | `STRING` |
| `speciality_flow` | `speciality_flow` | `STRING` |
| `clp_status` | `clp_status` | `STRING` |
| `specialty_flag` | `specialty_flag` | `STRING` |
| `moved_out_of_col` | `moved_out_of_col` | `BOOLEAN` |
| `from_pacc_otcc` | `from_pacc_otcc` | `STRING` |
| `ErrorCodeID` | `ErrorCodeID` | `STRING` |
| `submit_pre_auth_pmt_response` | `submit_pre_auth_pmt_response` | `STRING` |
| `completed_topup_flag` | `completed_topup_flag` | `NUMBER` |
| `amountBeingPaid` | `amountBeingPaid` | `STRING` |
| `paymentConfirmationNumber` | `paymentConfirmationNumber` | `STRING` |
| `incorrect_payment_method_counter` | `incorrect_payment_method_counter` | `NUMBER` |
| `preauth_exit_2` | `preauth_exit_2` | `BOOLEAN` |
| `payment_method_check` | `payment_method_check` | `STRING` |
| `preauth_exit_1` | `preauth_exit_1` | `BOOLEAN` |
| `customer_id_search_response_raw` | `customer_id_search_response_raw` | `STRING` |
| `tech_type` | `tech_type` | `STRING` |
| `SAT_COUNT` | `SAT_COUNT` | `STRING` |
| `service_id_temp` | `service_id_temp` | `STRING` |
| `dth_acc_no` | `dth_acc_no` | `STRING` |
| `FIBE_COUNT` | `FIBE_COUNT` | `STRING` |
| `iptv_acc_no` | `iptv_acc_no` | `STRING` |
| `sat_tv_obj_raw` | `sat_tv_obj_raw` | `STRING` |
| `sat_tv_obj` | `sat_tv_obj` | `STRING` |
| `sat_tv_count` | `sat_tv_count` | `STRING` |
| `flow_name` | `flow_name` | `STRING` |
| `bell_rehit_Sat_TV` | `bell_rehit_Sat_TV` | `STRING` |
| `page_sat_tv` | `page_sat_tv` | `STRING` |
| `service_type_list` | `service_type_list` | `STRING` |
| `n_service_type` | `n_service_type` | `STRING` |
| `multiban_sales_lob` | `multiban_sales_lob` | `STRING` |
| `SMS_Counter` | `SMS_Counter` | `NUMBER` |
| `repeat_counter` | `repeat_counter` | `NUMBER` |
| `banStatus` | `banStatus` | `STRING` |
| `mobility` | `mobility` | `STRING` |
| `tv` | `tv` | `STRING` |
| `internet` | `internet` | `STRING` |
| `smarthome` | `smarthome` | `STRING` |
| `homephone` | `homephone` | `STRING` |
| `soc_cap` | `soc_cap` | `STRING` |
| `soc` | `soc` | `STRING` |
| `flagD` | `flagD` | `STRING` |
| `sus_deliquent` | `sus_deliquent` | `STRING` |
| `flag_D` | `flag_D` | `STRING` |
| `flow` | `flow` | `STRING` |
| `special_stauts` | `special_stauts` | `STRING` |
| `colInd` | `colInd` | `STRING` |
| `statActvRsnCode` | `statActvRsnCode` | `STRING` |
| `soc_COLAUL` | `soc_COLAUL` | `STRING` |
| `code1` | `code1` | `STRING` |
| `code2` | `code2` | `STRING` |
| `code3` | `code3` | `STRING` |
| `billing_status_list` | `billing_status_list` | `STRING` |
| `billing_reason_code_list` | `billing_reason_code_list` | `STRING` |
| `looping` | `looping` | `STRING` |
| `test_auth_skip_cshead_intent` | `test_auth_skip_cshead_intent` | `STRING` |
| `network_type` | `network_type` | `STRING` |
| `pitch_exposure_rate` | `pitch_exposure_rate` | `NUMBER` |
| `pitch_exposure_roll` | `pitch_exposure_roll` | `STRING` |
| `soc_itp_effDate` | `soc_itp_effDate` | `STRING` |
| `eff_year` | `eff_year` | `STRING` |
| `eff_month` | `eff_month` | `STRING` |
| `eff_day` | `eff_day` | `STRING` |
| `eff_hours` | `eff_hours` | `STRING` |
| `eff_minutes` | `eff_minutes` | `STRING` |
| `eff_seconds` | `eff_seconds` | `STRING` |
| `effDate_struct` | `effDate_struct` | `STRING` |
| `effDate_object` | `effDate_object` | `STRING` |
| `nm1_get_soc_info_list_response` | `nm1_get_soc_info_list_response` | `STRING` |
| `soc_ITP` | `soc_ITP` | `STRING` |
| `flag_Y` | `flag_Y` | `STRING` |
| `preferred_flag` | `preferred_flag` | `STRING` |
| `previlege_flag` | `previlege_flag` | `STRING` |
| `priv_flag_Y` | `priv_flag_Y` | `STRING` |
| `current_day` | `current_day` | `STRING` |
| `current_hour` | `current_hour` | `STRING` |
| `is_weekday` | `is_weekday` | `STRING` |
| `province_list` | `province_list` | `STRING` |
| `total_active_services` | `total_active_services` | `STRING` |
| `total_unique_services` | `total_unique_services` | `STRING` |
| `n_unique_service` | `n_unique_service` | `STRING` |
| `application_id` | `application_id` | `STRING` |
| `siOwner` | `siOwner` | `STRING` |
| `comcentric_no_match_counter` | `comcentric_no_match_counter` | `NUMBER` |
| `comcentric_brand` | `comcentric_brand` | `STRING` |
| `atl_prvlg` | `atl_prvlg` | `STRING` |
| `soc_aul` | `soc_aul` | `STRING` |
| `code_frd` | `code_frd` | `STRING` |
| `arBalance` | `arBalance` | `STRING` |
| `coll_flg` | `coll_flg` | `STRING` |
| `deliquentFlag` | `deliquentFlag` | `STRING` |
| `com_brand_options` | `com_brand_options` | `STRING` |
| `status_suspended` | `status_suspended` | `STRING` |
| `sus_code1` | `sus_code1` | `STRING` |
| `sus_code2` | `sus_code2` | `STRING` |
| `pending_order2` | `pending_order2` | `STRING` |
| `pending_order` | `pending_order` | `STRING` |
| `is_cornerstone_value_list` | `is_cornerstone_value_list` | `STRING` |
| `npe_cs_friendlies` | `npe_cs_friendlies` | `ARRAY` |
| `prod_cs_friendlies` | `prod_cs_friendlies` | `ARRAY` |
| `prod_project_id` | `prod_project_id` | `STRING` |
| `cs_friendlies` | `cs_friendlies` | `STRING` |
| `mya_links` | `mya_links` | `STRING` |
| `arr_size` | `arr_size` | `STRING` |
| `mya_eligible` | `mya_eligible` | `STRING` |
| `sids_internet` | `sids_internet` | `STRING` |
| `sids_tv` | `sids_tv` | `STRING` |
| `service_identifiers` | `service_identifiers` | `STRING` |
| `type_sub_type` | `type_sub_type` | `STRING` |
| `typr_sub_type` | `typr_sub_type` | `STRING` |
| `outage_status` | `outage_status` | `STRING` |
| `test_no_active_2861` | `test_no_active_2861` | `STRING` |
| `aglobal_error_counter` | `aglobal_error_counter` | `STRING` |
| `link` | `link` | `STRING` |
| `etr_time` | `etr_time` | `STRING` |
| `client_local_time_response` | `client_local_time_response` | `STRING` |
| `from_date` | `from_date` | `STRING` |
| `to_date` | `to_date` | `STRING` |
| `from_time` | `from_time` | `STRING` |
| `to_time` | `to_time` | `STRING` |
| `current_date` | `current_date` | `STRING` |
| `new_date` | `new_date` | `STRING` |
| `new_time` | `new_time` | `STRING` |
| `longest_etr_from` | `longest_etr_from` | `STRING` |
| `longest_etr_to` | `longest_etr_to` | `STRING` |
| `formatted_time_obj` | `formatted_time_obj` | `STRING` |
| `formatted_time` | `formatted_time` | `STRING` |
| `from_Time_fr` | `from_Time_fr` | `STRING` |
| `to_time_fr` | `to_time_fr` | `STRING` |
| `services_list_temp` | `services_list_temp` | `STRING` |
| `services_object_temp` | `services_object_temp` | `STRING` |
| `services_list` | `services_list` | `STRING` |
| `services_object` | `services_object` | `STRING` |
| `test3101` | `test3101` | `STRING` |
| `formatted_etr_raw` | `formatted_etr_raw` | `STRING` |
| `formatted_etr` | `formatted_etr` | `STRING` |
| `month_date` | `month_date` | `STRING` |
| `fromTime` | `fromTime` | `STRING` |
| `toTime` | `toTime` | `STRING` |
| `month_date_fr` | `month_date_fr` | `STRING` |
| `fromTime_fr` | `fromTime_fr` | `STRING` |
| `toTime_fr` | `toTime_fr` | `STRING` |
| `from_time_fr` | `from_time_fr` | `STRING` |
| `oc_status_response` | `oc_status_response` | `STRING` |
| `postalcode` | `postalcode` | `STRING` |
| `oc_start_response` | `oc_start_response` | `STRING` |
| `outage_counter` | `outage_counter` | `NUMBER` |
| `longest_etr` | `longest_etr` | `STRING` |
| `is_available` | `is_available` | `STRING` |
| `etr` | `etr` | `STRING` |
| `oc_details_response` | `oc_details_response` | `STRING` |
| `get_tester_details_fail_count` | `get_tester_details_fail_count` | `NUMBER` |
| `intake_routing_fail_count` | `intake_routing_fail_count` | `NUMBER` |
| `Flag` | `Flag` | `STRING` |
| `tester_firstname` | `tester_firstname` | `STRING` |
| `spoof_tfn` | `spoof_tfn` | `STRING` |
| `test_vr_phase2` | `test_vr_phase2` | `BOOLEAN` |
| `get_tester_details_response` | `get_tester_details_response` | `STRING` |
| `acut_retrieve_response_raw` | `acut_retrieve_response_raw` | `STRING` |
| `appointment_end_date` | `appointment_end_date` | `STRING` |
| `contact_number_on_file` | `contact_number_on_file` | `STRING` |
| `contact_type_on_file` | `contact_type_on_file` | `STRING` |
| `contact_preference_on_file` | `contact_preference_on_file` | `STRING` |
| `original_appointment_object` | `original_appointment_object` | `STRING` |
| `appointmentStartDate` | `appointmentStartDate` | `STRING` |
| `appointmentEndDate` | `appointmentEndDate` | `STRING` |
| `ask_date_again` | `ask_date_again` | `STRING` |
| `unav_response` | `unav_response` | `STRING` |
| `dynamic_intervals_trimmed` | `dynamic_intervals_trimmed` | `STRING` |
| `ask_time_slot_error_flag` | `ask_time_slot_error_flag` | `STRING` |
| `dynamic_intervals` | `dynamic_intervals` | `STRING` |
| `first_available_md` | `first_available_md` | `STRING` |
| `last_available_md` | `last_available_md` | `STRING` |
| `appointment_date_range` | `appointment_date_range` | `STRING` |
| `first_available` | `first_available` | `STRING` |
| `last_available` | `last_available` | `STRING` |
| `stored_contact_number` | `stored_contact_number` | `STRING` |
| `stored_contact_type` | `stored_contact_type` | `STRING` |
| `day_object` | `day_object` | `STRING` |
| `full_date` | `full_date` | `STRING` |
| `day_of_the_week` | `day_of_the_week` | `STRING` |
| `date_of_month` | `date_of_month` | `STRING` |
| `day_of_the_week_fr` | `day_of_the_week_fr` | `STRING` |
| `month_fr` | `month_fr` | `STRING` |
| `availability` | `availability` | `STRING` |
| `date_within_range` | `date_within_range` | `STRING` |
| `date_within_range_second_time` | `date_within_range_second_time` | `STRING` |
| `dates_array_count` | `dates_array_count` | `STRING` |
| `dates_available` | `dates_available` | `STRING` |
| `availability_check_second_time` | `availability_check_second_time` | `STRING` |
| `ivr_menu` | `ivr_menu` | `STRING` |
| `original_start_date` | `original_start_date` | `STRING` |
| `original_end_date` | `original_end_date` | `STRING` |
| `orginal_end_date` | `orginal_end_date` | `STRING` |
| `availability_details` | `availability_details` | `STRING` |
| `interval_name` | `interval_name` | `STRING` |
| `day_of_week_fr` | `day_of_week_fr` | `STRING` |
| `start_time_2` | `start_time_2` | `STRING` |
| `end_time_2` | `end_time_2` | `STRING` |
| `start_time_fr_2` | `start_time_fr_2` | `STRING` |
| `end_time_fr_2` | `end_time_fr_2` | `STRING` |
| `wfas_context_raw` | `wfas_context_raw` | `STRING` |
| `wfas_availability_response` | `wfas_availability_response` | `STRING` |
| `rejected_date` | `rejected_date` | `STRING` |
| `interval_availability_raw` | `interval_availability_raw` | `STRING` |
| `interval_availability` | `interval_availability` | `STRING` |
| `interval_available` | `interval_available` | `STRING` |
| `interval_available_second_time` | `interval_available_second_time` | `STRING` |
| `slot_count` | `slot_count` | `STRING` |
| `available_slots_string_2` | `available_slots_string_2` | `STRING` |
| `available_slots_string_fr_2` | `available_slots_string_fr_2` | `STRING` |
| `slot_details` | `slot_details` | `STRING` |
| `slot_details_raw` | `slot_details_raw` | `STRING` |
| `available_slots_string` | `available_slots_string` | `STRING` |
| `available_slots_string_fr` | `available_slots_string_fr` | `STRING` |
| `time_input` | `time_input` | `STRING` |
| `time_pair_string` | `time_pair_string` | `STRING` |
| `time_slot_object` | `time_slot_object` | `STRING` |
| `makeAppointment_response` | `makeAppointment_response` | `STRING` |
| `len_merged_calendar_context` | `len_merged_calendar_context` | `STRING` |
| `month_name` | `month_name` | `STRING` |
| `startTime` | `startTime` | `STRING` |
| `endTime` | `endTime` | `STRING` |
| `endTimeUpdated` | `endTimeUpdated` | `STRING` |
| `order_status` | `order_status` | `STRING` |
| `account_action` | `account_action` | `STRING` |
| `is_siahcc` | `is_siahcc` | `STRING` |
| `onebox_shipping_required` | `onebox_shipping_required` | `STRING` |
| `state_restriction` | `state_restriction` | `STRING` |
| `early_termination_penalty` | `early_termination_penalty` | `STRING` |
| `contains_coded_orders` | `contains_coded_orders` | `STRING` |
| `no_shipping_changes` | `no_shipping_changes` | `STRING` |
| `order_detail_response_raw` | `order_detail_response_raw` | `STRING` |
| `field_work` | `field_work` | `STRING` |
| `customer_work` | `customer_work` | `STRING` |
| `cutoff_time` | `cutoff_time` | `STRING` |
| `date_time_object` | `date_time_object` | `STRING` |
| `special_queue_` | `special_queue_` | `STRING` |
| `input_time_string` | `input_time_string` | `STRING` |
| `input_date_string` | `input_date_string` | `STRING` |
| `current_time_utc` | `current_time_utc` | `STRING` |
| `cutoff_time_utc` | `cutoff_time_utc` | `STRING` |
| `current_date_utc` | `current_date_utc` | `STRING` |
| `cutoff_date_utc` | `cutoff_date_utc` | `STRING` |
| `local_nomatch_countera` | `local_nomatch_countera` | `STRING` |
| `recent_order_summary_raw_1` | `recent_order_summary_raw_1` | `STRING` |
| `recent_order_summary_1` | `recent_order_summary_1` | `STRING` |
| `lineOfBusiness_1` | `lineOfBusiness_1` | `STRING` |
| `recent_ticket_creation_time_obj2` | `recent_ticket_creation_time_obj2` | `STRING` |
| `lineOfBusiness_2` | `lineOfBusiness_2` | `STRING` |
| `recent_order_summary_2` | `recent_order_summary_2` | `STRING` |
| `recent_ticket_creation_time` | `recent_ticket_creation_time` | `STRING` |
| `recent_order_summary_raw_2` | `recent_order_summary_raw_2` | `STRING` |
| `recent_ticket_creation_time_obj1` | `recent_ticket_creation_time_obj1` | `STRING` |
| `not_eligible_for_rdam` | `not_eligible_for_rdam` | `STRING` |
| `tv_check` | `tv_check` | `BOOLEAN` |
| `ivr_ccc` | `ivr_ccc` | `BOOLEAN` |
| `cti_rt_1` | `cti_rt_1` | `STRING` |
| `ban` | `ban` | `STRING` |
| `_billing_accounts` | `_billing_accounts` | `STRING` |
| `_other_services` | `_other_services` | `STRING` |
| `ban_with_lob` | `ban_with_lob` | `STRING` |
| `n_ban_with_lob` | `n_ban_with_lob` | `STRING` |
| `vr_outcome` | `vr_outcome` | `STRING` |
| `counter_next_task` | `counter_next_task` | `NUMBER` |
| `query` | `query` | `STRING` |
| `prev_ms_dcx_action_code` | `prev_ms_dcx_action_code` | `STRING` |
| `prev_cfb_dcx_action_code` | `prev_cfb_dcx_action_code` | `STRING` |
| `prev_cda_dcx_action_code` | `prev_cda_dcx_action_code` | `STRING` |
| `vr_no_input` | `vr_no_input` | `STRING` |
| `is_expecting_answer` | `is_expecting_answer` | `STRING` |
| `sp_id` | `sp_id` | `STRING` |
| `more_info` | `more_info` | `STRING` |
| `dcx_action_code_ref` | `dcx_action_code_ref` | `STRING` |
| `vr_next_task_response` | `vr_next_task_response` | `STRING` |
| `microservice_counter` | `microservice_counter` | `NUMBER` |
| `microservice_aqd_counter` | `microservice_aqd_counter` | `NUMBER` |
| `counter_sharp` | `counter_sharp` | `NUMBER` |
| `category` | `category` | `STRING` |
| `sub_category` | `sub_category` | `STRING` |
| `vr_counter` | `vr_counter` | `NUMBER` |
| `cdo_start_time` | `cdo_start_time` | `STRING` |
| `6590_customer_answer1_id` | `6590_customer_answer1_id` | `STRING` |
| `6590_customer_answer2_id` | `6590_customer_answer2_id` | `STRING` |
| `counter_post_task` | `counter_post_task` | `NUMBER` |
| `vr_post_answer_response` | `vr_post_answer_response` | `STRING` |
| `counter_start_task` | `counter_start_task` | `NUMBER` |
| `lob_upper` | `lob_upper` | `STRING` |
| `clid_home_phone_service_ids` | `clid_home_phone_service_ids` | `STRING` |
| `account_details_payload` | `account_details_payload` | `STRING` |
| `p_clean_length` | `p_clean_length` | `STRING` |
| `search_clid` | `search_clid` | `STRING` |
| `service_homephone` | `service_homephone` | `STRING` |
| `service_tv` | `service_tv` | `STRING` |
| `service_internet` | `service_internet` | `STRING` |
| `n_service_homephone` | `n_service_homephone` | `STRING` |
| `n_service_tv` | `n_service_tv` | `STRING` |
| `n_service_internet` | `n_service_internet` | `STRING` |
| `clid_home_phone_service_id` | `clid_home_phone_service_id` | `STRING` |
| `clid_home_phone_service_id_counter` | `clid_home_phone_service_id_counter` | `STRING` |
| `network_type_flag` | `network_type_flag` | `STRING` |
| `homephonejson` | `homephonejson` | `STRING` |
| `homephone_access_code` | `homephone_access_code` | `STRING` |
| `internet_homephone_service_id` | `internet_homephone_service_id` | `STRING` |
| `internet_homephone_service_id_flag` | `internet_homephone_service_id_flag` | `STRING` |
| `tvjson` | `tvjson` | `STRING` |
| `tvjson_access_code` | `tvjson_access_code` | `STRING` |
| `internet_tv_service_id` | `internet_tv_service_id` | `STRING` |
| `internet_tv_service_id_flag` | `internet_tv_service_id_flag` | `STRING` |
| `homephone_tv_service_id` | `homephone_tv_service_id` | `STRING` |
| `homephone_tv_service_id_flag` | `homephone_tv_service_id_flag` | `STRING` |
| `vr_start_response` | `vr_start_response` | `STRING` |
| `next_action` | `next_action` | `STRING` |
| `agent` | `agent` | `STRING` |
| `Business` | `Business` | `STRING` |
| `Q` | `Q` | `STRING` |
| `last_action` | `last_action` | `STRING` |
| `active_lob1` | `active_lob1` | `STRING` |
| `selectedStartTime` | `selectedStartTime` | `STRING` |
| `selectedEndTime` | `selectedEndTime` | `STRING` |
| `sy` | `sy` | `STRING` |
| `patternTime` | `patternTime` | `STRING` |
| `service` | `service` | `STRING` |
| `last_user_utterance` | `last_user_utterance` | `STRING` |
| `text` | `text` | `STRING` |
| `date_time` | `date_time` | `STRING` |
| `ip_amount` | `ip_amount` | `STRING` |
| `com_brand_name` | `com_brand_name` | `STRING` |
| `services_json` | `services_json` | `STRING` |
| `lob_value` | `lob_value` | `STRING` |
| `last_agent_response` | `last_agent_response` | `STRING` |
| `filtered_ticket_creation_times` | `filtered_ticket_creation_times` | `STRING` |
| `prev_agent_response` | `prev_agent_response` | `STRING` |
| `kickout_description` | `kickout_description` | `STRING` |
| `kickout_title` | `kickout_title` | `STRING` |
| `request_last_agent_utterance` | `request_last_agent_utterance` | `STRING` |
| `account_service_transfer_testing` | `account_service_transfer_testing` | `STRING` |
| `number_of_services_testing` | `number_of_services_testing` | `STRING` |
| `is_mobility_testing` | `is_mobility_testing` | `STRING` |
| `route_` | `route_` | `STRING` |
| `coming_from_rewriter` | `coming_from_rewriter` | `BOOLEAN` |

## 🛠️ Tools & Toolsets Migrated
| Type | Original Name | CXAS ID | Operations / Notes |
|---|---|---|---|
| `PYTHON` | `match_intent` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/match_intent` | `-` |
| `PYTHON` | `no_intent` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_intent` | `-` |
| `PYTHON` | `_no_input_1` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_1` | `-` |
| `PYTHON` | `_no_input_1_extend` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_1_extend` | `-` |
| `PYTHON` | `_no_input_2` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_2` | `-` |
| `PYTHON` | `_no_input_2_extend` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_2_extend` | `-` |
| `PYTHON` | `_no_input_3` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_3` | `-` |
| `PYTHON` | `_no_input_3_extend` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_3_extend` | `-` |
| `PYTHON` | `_no_input_4` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_4` | `-` |
| `PYTHON` | `_no_input_4_extend` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_4_extend` | `-` |
| `PYTHON` | `_no_input_5` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_5` | `-` |
| `PYTHON` | `_no_input_5_extend` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_5_extend` | `-` |
| `PYTHON` | `_no_input_6` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input_6` | `-` |
| `PYTHON` | `_check_faq` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_faq` | `-` |
| `PYTHON` | `routing` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/routing` | `-` |
| `PYTHON` | `_no_input` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/no_input` | `-` |
| `PYTHON` | `extract_entities` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_entities` | `-` |
| `PYTHON` | `set_fallback_flag` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_fallback_flag` | `-` |
| `PYTHON` | `clear_sensitive_billing_data` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/clear_sensitive_billing_data` | `-` |
| `PYTHON` | `set_fallback_3_flag` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_fallback_3_flag` | `-` |
| `PYTHON` | `update_routing_variables` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/update_routing_variables` | `-` |
| `PYTHON` | `format_handoff_parameters` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/format_handoff_parameters` | `-` |
| `PYTHON` | `set_routing_context` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_routing_context` | `-` |
| `PYTHON` | `acut_ticket_orchestrator_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/acut_ticket_orchestrator_wrapper` | `-` |
| `PYTHON` | `format_ticket_details_manipulator` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/format_ticket_details_manipulator` | `-` |
| `PYTHON` | `update_sms_payload_variables` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/update_sms_payload_variables` | `-` |
| `PYTHON` | `set_generic_faq_flags` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_generic_faq_flags` | `-` |
| `PYTHON` | `execute_intake_initialization` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/execute_intake_initialization` | `-` |
| `PYTHON` | `fetch_location_apbs` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_location_apbs` | `-` |
| `PYTHON` | `execute_ivr_telephony_transfer` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/execute_ivr_telephony_transfer` | `-` |
| `PYTHON` | `format_and_validate_phone_number` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/format_and_validate_phone_number` | `-` |
| `PYTHON` | `cancel_ticket_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/cancel_ticket_wrapper` | `-` |
| `PYTHON` | `format_and_clean_identifier` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/format_and_clean_identifier` | `-` |
| `PYTHON` | `validate_customer_identity_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/validate_customer_identity_wrapper` | `-` |
| `PYTHON` | `lookup_npa_nxx_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/lookup_npa_nxx_wrapper` | `-` |
| `PYTHON` | `manage_routing_state` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/manage_routing_state` | `-` |
| `PYTHON` | `update_no_match_counters` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/update_no_match_counters` | `-` |
| `PYTHON` | `set_event_type` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_event_type` | `-` |
| `PYTHON` | `get_apbs_for_location_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_apbs_for_location_wrapper` | `-` |
| `PYTHON` | `extract_apb_data_manipulator` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_apb_data_manipulator` | `-` |
| `PYTHON` | `trigger_self_help_sms` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/trigger_self_help_sms` | `-` |
| `PYTHON` | `get_intent_sdl_mapping` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_intent_sdl_mapping` | `-` |
| `PYTHON` | `check_number_in_account` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_number_in_account` | `-` |
| `PYTHON` | `acut_search_retrieve_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/acut_search_retrieve_wrapper` | `-` |
| `PYTHON` | `process_acut_ticket_data` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/process_acut_ticket_data` | `-` |
| `PYTHON` | `filter_lob_services_manipulator` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/filter_lob_services_manipulator` | `-` |
| `PYTHON` | `fetch_active_appointments_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_active_appointments_wrapper` | `-` |
| `PYTHON` | `evaluate_cancellation_eligibility_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/evaluate_cancellation_eligibility_wr` | `-` |
| `PYTHON` | `modify_close_ticket_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/modify_close_ticket_wrapper` | `-` |
| `PYTHON` | `fetch_and_process_customer_tickets` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_and_process_customer_tickets` | `-` |
| `PYTHON` | `set_session_variable` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_session_variable` | `-` |
| `PYTHON` | `extract_otp_numbers` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_otp_numbers` | `-` |
| `PYTHON` | `validate_and_format_phone_number` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/validate_and_format_phone_number` | `-` |
| `PYTHON` | `check_home_phone_status` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_home_phone_status` | `-` |
| `PYTHON` | `increment_global_error_counter` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/increment_global_error_counter` | `-` |
| `PYTHON` | `evaluate_mya_eligibility_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/evaluate_mya_eligibility_wrapper` | `-` |
| `PYTHON` | `format_mya_sms_content_manipulator` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/format_mya_sms_content_manipulator` | `-` |
| `PYTHON` | `extract_ticket_modifiability_status` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_ticket_modifiability_status` | `-` |
| `PYTHON` | `check_omf_calendar_availability_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_omf_calendar_availability_wrap` | `-` |
| `PYTHON` | `execute_omf_calendar_reservation_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/execute_omf_calendar_reservation_wra` | `-` |
| `PYTHON` | `fetch_customized_sdl_url` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_customized_sdl_url` | `-` |
| `PYTHON` | `set_default_faq_url` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_default_faq_url` | `-` |
| `PYTHON` | `process_lob_and_services` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/process_lob_and_services` | `-` |
| `PYTHON` | `fetch_active_omf_and_acut_tickets` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_active_omf_and_acut_tickets` | `-` |
| `PYTHON` | `fetch_finalized_acut_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_finalized_acut_wrapper` | `-` |
| `PYTHON` | `evaluate_routing_rules` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/evaluate_routing_rules` | `-` |
| `PYTHON` | `get_intent_sdl_mapping_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_intent_sdl_mapping_wrapper` | `-` |
| `PYTHON` | `initialize_aqd_variables` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/initialize_aqd_variables` | `-` |
| `PYTHON` | `get_agent_queue_details` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_agent_queue_details` | `-` |
| `PYTHON` | `send_agent_transfer_data` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/send_agent_transfer_data` | `-` |
| `PYTHON` | `evaluate_cc_expiry_status_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/evaluate_cc_expiry_status_tool` | `-` |
| `PYTHON` | `check_sales_propensity_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_sales_propensity_tool` | `-` |
| `PYTHON` | `set_payment_arrangement_sms_params` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_payment_arrangement_sms_params` | `-` |
| `PYTHON` | `update_session_route` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/update_session_route` | `-` |
| `PYTHON` | `initialize_auth_session` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/initialize_auth_session` | `-` |
| `PYTHON` | `send_otp_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/send_otp_wrapper` | `-` |
| `PYTHON` | `validate_pin_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/validate_pin_wrapper` | `-` |
| `PYTHON` | `validate_otp_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/validate_otp_wrapper` | `-` |
| `PYTHON` | `validate_postal_code` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/validate_postal_code` | `-` |
| `PYTHON` | `get_sms_vanity_url` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_sms_vanity_url` | `-` |
| `PYTHON` | `get_account_balance_details` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_account_balance_details` | `-` |
| `PYTHON` | `create_one_time_payment_order` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/create_one_time_payment_order` | `-` |
| `PYTHON` | `generate_sms_content_for_billing` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/generate_sms_content_for_billing` | `-` |
| `PYTHON` | `extract_date_from_timestamp` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_date_from_timestamp` | `-` |
| `PYTHON` | `check_autopay_cancellation_eligibility` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_autopay_cancellation_eligibili` | `-` |
| `PYTHON` | `set_autopay_sms_payload` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_autopay_sms_payload` | `-` |
| `PYTHON` | `get_ban_profile` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_ban_profile` | `-` |
| `PYTHON` | `evaluate_payment_amount` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/evaluate_payment_amount` | `-` |
| `PYTHON` | `submit_payment_arrangement_order` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/submit_payment_arrangement_order` | `-` |
| `PYTHON` | `extract_multiban_profile_metrics` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_multiban_profile_metrics` | `-` |
| `PYTHON` | `filter_customer_accounts_by_criteria` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/filter_customer_accounts_by_criteria` | `-` |
| `PYTHON` | `get_clp_details_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_clp_details_wrapper` | `-` |
| `PYTHON` | `create_payment_order_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/create_payment_order_wrapper` | `-` |
| `PYTHON` | `validate_and_format_amount` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/validate_and_format_amount` | `-` |
| `PYTHON` | `prepare_sms_content` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/prepare_sms_content` | `-` |
| `PYTHON` | `fetch_billing_profile` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_billing_profile` | `-` |
| `PYTHON` | `resolve_npa_and_province` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/resolve_npa_and_province` | `-` |
| `PYTHON` | `get_clp_and_bill_details_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_clp_and_bill_details_wrapper` | `-` |
| `PYTHON` | `fetch_account_balance_and_profile_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_account_balance_and_profile_wr` | `-` |
| `PYTHON` | `set_sms_payload_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_sms_payload_tool` | `-` |
| `PYTHON` | `get_account_profile_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_account_profile_wrapper` | `-` |
| `PYTHON` | `evaluate_consolidated_customer_logic` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/evaluate_consolidated_customer_logic` | `-` |
| `PYTHON` | `npa_nxx_lookup_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/npa_nxx_lookup_wrapper` | `-` |
| `PYTHON` | `process_pa_eligibility_and_order_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/process_pa_eligibility_and_order_wra` | `-` |
| `PYTHON` | `validate_payment_amount` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/validate_payment_amount` | `-` |
| `PYTHON` | `set_sms_payload` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_sms_payload` | `-` |
| `PYTHON` | `get_dts_token_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_dts_token_wrapper` | `-` |
| `PYTHON` | `format_sms_content_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/format_sms_content_tool` | `-` |
| `PYTHON` | `process_clp_payment_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/process_clp_payment_wrapper` | `-` |
| `PYTHON` | `get_clp_ban_profile_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_clp_ban_profile_wrapper` | `-` |
| `PYTHON` | `calculate_clp_status_manipulator` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/calculate_clp_status_manipulator` | `-` |
| `PYTHON` | `get_account_balance_details_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_account_balance_details_wrapper` | `-` |
| `PYTHON` | `tool_get_customer_profile` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/tool_get_customer_profile` | `-` |
| `PYTHON` | `tool_lookup_province` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/tool_lookup_province` | `-` |
| `PYTHON` | `tool_check_preauth_payment` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/tool_check_preauth_payment` | `-` |
| `PYTHON` | `tool_process_pacc_order` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/tool_process_pacc_order` | `-` |
| `PYTHON` | `tool_get_intent_sdl` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/tool_get_intent_sdl` | `-` |
| `PYTHON` | `set_refund_variables` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_refund_variables` | `-` |
| `PYTHON` | `validate_cc_number` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/validate_cc_number` | `-` |
| `PYTHON` | `validate_expiry_date` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/validate_expiry_date` | `-` |
| `PYTHON` | `validate_cvv` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/validate_cvv` | `-` |
| `PYTHON` | `submit_cc_payment_details` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/submit_cc_payment_details` | `-` |
| `PYTHON` | `set_speciality_flow_flag` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_speciality_flow_flag` | `-` |
| `PYTHON` | `check_system_outage` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_system_outage` | `-` |
| `PYTHON` | `get_nm1_billing_profile` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_nm1_billing_profile` | `-` |
| `PYTHON` | `lookup_province_by_phone` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/lookup_province_by_phone` | `-` |
| `PYTHON` | `get_preauth_status` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_preauth_status` | `-` |
| `PYTHON` | `get_vanity_url_mapping` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_vanity_url_mapping` | `-` |
| `PYTHON` | `format_sms_payload` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/format_sms_payload` | `-` |
| `PYTHON` | `get_account_profile_and_eligibility` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_account_profile_and_eligibility` | `-` |
| `PYTHON` | `create_payment_order` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/create_payment_order` | `-` |
| `PYTHON` | `finalize_payment_notification` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/finalize_payment_notification` | `-` |
| `PYTHON` | `evaluate_account_and_services` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/evaluate_account_and_services` | `-` |
| `PYTHON` | `trigger_sat_rehit_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/trigger_sat_rehit_wrapper` | `-` |
| `PYTHON` | `set_tv_sync_sms_variables` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_tv_sync_sms_variables` | `-` |
| `PYTHON` | `submit_pre_auth_payment_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/submit_pre_auth_payment_wrapper` | `-` |
| `PYTHON` | `check_existing_payment_method_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_existing_payment_method_wrappe` | `-` |
| `PYTHON` | `process_pacc_enrollment_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/process_pacc_enrollment_wrapper` | `-` |
| `PYTHON` | `get_sdl_vanity_url_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_sdl_vanity_url_wrapper` | `-` |
| `PYTHON` | `clear_cc_data_manipulator` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/clear_cc_data_manipulator` | `-` |
| `PYTHON` | `set_sms_content_manipulator` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_sms_content_manipulator` | `-` |
| `PYTHON` | `search_by_tn_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/search_by_tn_wrapper` | `-` |
| `PYTHON` | `extract_tv_account_details` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_tv_account_details` | `-` |
| `PYTHON` | `check_existing_payment_method` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_existing_payment_method` | `-` |
| `PYTHON` | `check_payment_arrangement_eligibility` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_payment_arrangement_eligibilit` | `-` |
| `PYTHON` | `set_routing_parameters` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_routing_parameters` | `-` |
| `PYTHON` | `evaluate_payment_eligibility_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/evaluate_payment_eligibility_wrapper` | `-` |
| `PYTHON` | `update_state_variables` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/update_state_variables` | `-` |
| `PYTHON` | `fetch_account_profile_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_account_profile_wrapper` | `-` |
| `PYTHON` | `evaluate_pad_eligibility` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/evaluate_pad_eligibility` | `-` |
| `PYTHON` | `fetch_province_info_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_province_info_wrapper` | `-` |
| `PYTHON` | `fetch_intent_vanity_url_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_intent_vanity_url_wrapper` | `-` |
| `PYTHON` | `prepare_sms_variables` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/prepare_sms_variables` | `-` |
| `PYTHON` | `execute_sat_rehit` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/execute_sat_rehit` | `-` |
| `PYTHON` | `set_tech_visit_routing_variables` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_tech_visit_routing_variables` | `-` |
| `PYTHON` | `reset_session_counters` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/reset_session_counters` | `-` |
| `PYTHON` | `fetch_billing_profile_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_billing_profile_tool` | `-` |
| `PYTHON` | `lookup_province_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/lookup_province_tool` | `-` |
| `PYTHON` | `check_preauth_eligibility_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_preauth_eligibility_tool` | `-` |
| `PYTHON` | `create_preauth_order_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/create_preauth_order_tool` | `-` |
| `PYTHON` | `fetch_intent_sdl_mapping_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_intent_sdl_mapping_tool` | `-` |
| `PYTHON` | `increment_payment_counter_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/increment_payment_counter_tool` | `-` |
| `PYTHON` | `prepare_sms_content_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/prepare_sms_content_tool` | `-` |
| `PYTHON` | `process_payment_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/process_payment_wrapper` | `-` |
| `PYTHON` | `evaluate_collection_status` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/evaluate_collection_status` | `-` |
| `PYTHON` | `extract_service_identifier_tool` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_service_identifier_tool` | `-` |
| `PYTHON` | `check_mya_eligibility_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_mya_eligibility_wrapper` | `-` |
| `PYTHON` | `extract_mya_eligibility_data` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_mya_eligibility_data` | `-` |
| `PYTHON` | `clear_infobot_flag` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/clear_infobot_flag` | `-` |
| `PYTHON` | `lookup_customer_account_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/lookup_customer_account_wrapper` | `-` |
| `PYTHON` | `extract_customer_postal_code` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_customer_postal_code` | `-` |
| `PYTHON` | `check_service_outage_bundled` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_service_outage_bundled` | `-` |
| `PYTHON` | `set_routing_variables` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_routing_variables` | `-` |
| `PYTHON` | `get_tester_details_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/get_tester_details_wrapper` | `-` |
| `PYTHON` | `intake_routing_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/intake_routing_wrapper` | `-` |
| `PYTHON` | `update_test_wrapper_state` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/update_test_wrapper_state` | `-` |
| `PYTHON` | `update_different_number_state` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/update_different_number_state` | `-` |
| `PYTHON` | `execute_business_transfer_protocol` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/execute_business_transfer_protocol` | `-` |
| `PYTHON` | `extract_acut_ticket_data` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_acut_ticket_data` | `-` |
| `PYTHON` | `wfas_check_availability_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/wfas_check_availability_wrapper` | `-` |
| `PYTHON` | `wfas_book_and_acut_modify_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/wfas_book_and_acut_modify_wrapper` | `-` |
| `PYTHON` | `acut_modify_contact_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/acut_modify_contact_wrapper` | `-` |
| `PYTHON` | `fetch_omf_order_details_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/fetch_omf_order_details_wrapper` | `-` |
| `PYTHON` | `parse_order_details_and_dates` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/parse_order_details_and_dates` | `-` |
| `PYTHON` | `extract_lob_services_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_lob_services_wrapper` | `-` |
| `PYTHON` | `search_acut_tickets_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/search_acut_tickets_wrapper` | `-` |
| `PYTHON` | `search_omf_orders_wrapper` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/search_omf_orders_wrapper` | `-` |
| `PYTHON` | `extract_acut_retrieve_parameters` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_acut_retrieve_parameters` | `-` |
| `PYTHON` | `update_acut_contact_preferences` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/update_acut_contact_preferences` | `-` |
| `PYTHON` | `check_wfas_availability` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/check_wfas_availability` | `-` |
| `PYTHON` | `format_date_and_validate` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/format_date_and_validate` | `-` |
| `PYTHON` | `extract_time_slot_object` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_time_slot_object` | `-` |
| `PYTHON` | `book_wfas_appointment` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/book_wfas_appointment` | `-` |
| `PYTHON` | `cancel_wfas_appointment` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/cancel_wfas_appointment` | `-` |
| `PYTHON` | `set_route_variable` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_route_variable` | `-` |
| `PYTHON` | `extract_acut_appointment_details` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_acut_appointment_details` | `-` |
| `PYTHON` | `format_availability_options` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/format_availability_options` | `-` |
| `PYTHON` | `extract_selected_timeslot` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/extract_selected_timeslot` | `-` |
| `PYTHON` | `cancel_wfas_transaction` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/cancel_wfas_transaction` | `-` |
| `PYTHON` | `set_route_state` | `projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8/tools/set_route_state` | `-` |

## 🤖 Agents Migrated
| Original Playbook/Flow | CXAS Agent ID | Model | Generated Description |
|---|---|---|---|
| - | - | - | - |

## 🔗 AST Code Block Dependencies
| Agent | Injected Toolset Dependency |
|---|---|
| - | - |

## 🔄 Instruction Rewrites & Transformations
| Category | Original Reference | Migrated Reference | Notes |
|---|---|---|---|
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Equipment_Inquires_Infobot_fr}` | `{@AGENT: Bell_UC_Equipment_Inquires_Infobot_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support-1}` | `{@AGENT: bell_UC_Technical Support-1}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment Warranty Claim Related}` | `{@AGENT: bell_UC_Equipment Warranty Claim Related}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_sales_device_related}` | `{@AGENT: bell_UC_sales_device_related}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_sales_device_related}` | `{@AGENT: bell_UC_sales_device_related}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support-1}` | `{@AGENT: bell_UC_Technical Support-1}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment Warranty Claim Related}` | `{@AGENT: bell_UC_Equipment Warranty Claim Related}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_sales_device_related}` | `{@AGENT: bell_UC_sales_device_related}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_sales_device_related}` | `{@AGENT: bell_UC_sales_device_related}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$province` | `{province}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${agent:bell_uc_sales_service_coverage}` | `{@AGENT: bell_uc_sales_service_coverage}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:sales_add_to_existing_account_flow}` | `{@AGENT: sales_add_to_existing_account_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:sales_add_to_existing_account_flow}` | `{@AGENT: sales_add_to_existing_account_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_change_plan_flow}` | `{@AGENT: service_change_plan_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:sales_add_to_existing_account_flow}` | `{@AGENT: sales_add_to_existing_account_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_change_plan_flow}` | `{@AGENT: service_change_plan_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_handoff_prepaid}` | `{@AGENT: bell_va_to_ivr_handoff_prepaid}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_handoff_prepaid}` | `{@AGENT: bell_va_to_ivr_handoff_prepaid}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$LOB` | `{LOB}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Technical_Support_Infobot_Fr}` | `{@AGENT: Bell_UC_Technical_Support_Infobot_Fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_intent_apb}` | `{@AGENT: bell_tech_intent_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Sales_Plans_inquiry}` | `{@AGENT: Bell_UC_Sales_Plans_inquiry}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_intent_apb}` | `{@AGENT: bell_tech_intent_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Sales_Plans_inquiry}` | `{@AGENT: Bell_UC_Sales_Plans_inquiry}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Technical_Support_Infobot_Fr_deprecated}` | `{@AGENT: Bell_UC_Technical_Support_Infobot_Fr_deprecated}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Technical_Support_Infobot}` | `{@AGENT: Bell_UC_Technical_Support_Infobot}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Tech_intents_lob}` | `{@AGENT: Bell_UC_Tech_intents_lob}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_rehit_Check_Subscription}` | `{@AGENT: bell_rehit_Check_Subscription}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_rehit_Check_Subscription}` | `{@AGENT: bell_rehit_Check_Subscription}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_rehit_confirmation}` | `{@AGENT: bell_rehit_confirmation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_rehit_Check_Subscription}` | `{@AGENT: bell_rehit_Check_Subscription}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_rehit_confirmation}` | `{@AGENT: bell_rehit_confirmation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_rehit_confirmation}` | `{@AGENT: bell_rehit_confirmation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$session` | `{session}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `match_intent` | `{@TOOL: match_intent}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `no_intent` | `{@TOOL: no_intent}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Wrap-up}` | `{@AGENT: bell_Steering_Wrap-up}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_expired_credit_card}` | `{@AGENT: bell_expired_credit_card}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Wrap-up}` | `{@AGENT: bell_Steering_Wrap-up}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Wrap-up}` | `{@AGENT: bell_Steering_Wrap-up}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_IVR_Options}` | `{@AGENT: bell_IVR_Options}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_IVR_Options}` | `{@AGENT: bell_IVR_Options}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Wrap-up}` | `{@AGENT: bell_Steering_Wrap-up}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$faq_link` | `{faq_link}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features}` | `{@AGENT: bell_UC_Manage Plans and Features}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Disambiguation}` | `{@AGENT: bell_UC_Disambiguation}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_AccountManagement_Infobot_en_fr}` | `{@AGENT: bell_UC_AccountManagement_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features}` | `{@AGENT: bell_UC_Manage Plans and Features}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_AccountManagement_Infobot_en_fr}` | `{@AGENT: bell_UC_AccountManagement_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Sales}` | `{@AGENT: bell_UC_Sales}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_AccountManagement_Infobot_en_fr}` | `{@AGENT: bell_UC_AccountManagement_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_AccountManagement_Infobot_en_fr}` | `{@AGENT: bell_UC_AccountManagement_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_AccountManagement_Infobot_en_fr}` | `{@AGENT: bell_UC_AccountManagement_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_AccountManagement_Infobot_en_fr}` | `{@AGENT: bell_UC_AccountManagement_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Disambiguation}` | `{@AGENT: bell_UC_Disambiguation}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_AccountManagement_Infobot_en_fr}` | `{@AGENT: bell_UC_AccountManagement_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_AccountManagement_Infobot_en_fr}` | `{@AGENT: bell_UC_AccountManagement_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_AccountManagement_Infobot_en_fr}` | `{@AGENT: bell_UC_AccountManagement_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Wrap-up}` | `{@AGENT: bell_Steering_Wrap-up}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_IVR_Options}` | `{@AGENT: bell_IVR_Options}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Wrap-up}` | `{@AGENT: bell_Steering_Wrap-up}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_billing}` | `{@AGENT: bell_billing}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_NLU_Query_Rewriter}` | `{@AGENT: bell_NLU_Query_Rewriter}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_topic_transitions}` | `{@AGENT: bell_topic_transitions}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_topic_transitions}` | `{@AGENT: bell_topic_transitions}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_equipment_warranty_claim_cpo_update}` | `{@AGENT: bell_equipment_warranty_claim_cpo_update}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support-1}` | `{@AGENT: bell_UC_Technical Support-1}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_FAQ_vanity}` | `{@AGENT: bell_FAQ_vanity}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_FAQ_vanity}` | `{@AGENT: bell_FAQ_vanity}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_FAQ_vanity}` | `{@AGENT: bell_FAQ_vanity}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_FAQ_vanity}` | `{@AGENT: bell_FAQ_vanity}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_topic_transitions}` | `{@AGENT: bell_topic_transitions}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_intent_apb}` | `{@AGENT: bell_tech_intent_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_equipment_order_or_upgrade_device_routing}` | `{@AGENT: bell_equipment_order_or_upgrade_device_routing}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_equipment_order_or_upgrade_device_routing}` | `{@AGENT: bell_equipment_order_or_upgrade_device_routing}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_equipment_routing}` | `{@AGENT: bell_equipment_routing}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Variable Syntax` | `$LOB` | `{LOB}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$LOB` | `{LOB}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$tv_sub_type` | `{tv_sub_type}` | Updated DFCX $ variable to CXAS {} format |
| `Variable Syntax` | `$tv_sub_type` | `{tv_sub_type}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Sales_Plans_inquiry}` | `{@AGENT: Bell_UC_Sales_Plans_inquiry}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Sales_Plans_inquiry}` | `{@AGENT: Bell_UC_Sales_Plans_inquiry}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_ManagePlansAndFeatures_Infobot_en_fr}` | `{@AGENT: bell_UC_ManagePlansAndFeatures_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_ManagePlansAndFeatures_Infobot_en_fr}` | `{@AGENT: bell_UC_ManagePlansAndFeatures_Infobot_en_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Sales_Plans_inquiry}` | `{@AGENT: Bell_UC_Sales_Plans_inquiry}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Disambiguation}` | `{@AGENT: bell_UC_Disambiguation}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Sales_Plans_inquiry}` | `{@AGENT: Bell_UC_Sales_Plans_inquiry}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Sales_Plans_inquiry}` | `{@AGENT: Bell_UC_Sales_Plans_inquiry}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_get_sdl_mapping_url}` | `{@AGENT: bell_get_sdl_mapping_url}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Disambiguation}` | `{@AGENT: bell_UC_Disambiguation}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${FLOW:Default Start Flow}` | `{@AGENT: Default Start Flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Equipment_Inquires_Infobot}` | `{@AGENT: Bell_UC_Equipment_Inquires_Infobot}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Technical_Support_Infobot}` | `{@AGENT: Bell_UC_Technical_Support_Infobot}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Technical_Support_Infobot}` | `{@AGENT: Bell_UC_Technical_Support_Infobot}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_change_plan_flow}` | `{@AGENT: service_change_plan_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Equipment_Inquires_Infobot_fr}` | `{@AGENT: Bell_UC_Equipment_Inquires_Infobot_fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Technical_Support_Infobot_Fr}` | `{@AGENT: Bell_UC_Technical_Support_Infobot_Fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Technical_Support_Infobot_Fr}` | `{@AGENT: Bell_UC_Technical_Support_Infobot_Fr}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_change_plan_flow}` | `{@AGENT: service_change_plan_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_IVR_Options}` | `{@AGENT: bell_IVR_Options}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_NLU_Query_Rewriter}` | `{@AGENT: bell_NLU_Query_Rewriter}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Wrap-up}` | `{@AGENT: bell_Steering_Wrap-up}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_NLU_Query_Rewriter}` | `{@AGENT: bell_NLU_Query_Rewriter}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_one_time_CC_payment}` | `{@AGENT: bell_payment_one_time_CC_payment}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_update_payment_arrangements}` | `{@AGENT: bell_payment_update_payment_arrangements}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_arrangment_setup_id_auth_eligibility_Checks}` | `{@AGENT: bell_payment_arrangment_setup_id_auth_eligibility_Checks}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_autopay_status}` | `{@AGENT: bell_payment_autopay_status}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_autopay_cancel}` | `{@AGENT: bell_payment_autopay_cancel}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_setup_pacc_or_payment_not_stated}` | `{@AGENT: bell_payment_setup_pacc_or_payment_not_stated}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_autopay_update}` | `{@AGENT: bell_payment_autopay_update}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_billing}` | `{@AGENT: bell_billing}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_billing}` | `{@AGENT: bell_billing}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_notification}` | `{@AGENT: bell_payment_notification}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$province` | `{province}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:va_to_ivr_business_id_sales}` | `{@AGENT: va_to_ivr_business_id_sales}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Sales}` | `{@AGENT: bell_UC_Sales}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_handoff_prepaid}` | `{@AGENT: bell_va_to_ivr_handoff_prepaid}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:va_to_ivr_business_id_sales}` | `{@AGENT: va_to_ivr_business_id_sales}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$Business` | `{Business}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_ivr_to_va_handoff}` | `{@AGENT: bell_ivr_to_va_handoff}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Technical_Support_Infobot}` | `{@AGENT: Bell_UC_Technical_Support_Infobot}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Sales_Plans_inquiry}` | `{@AGENT: Bell_UC_Sales_Plans_inquiry}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_change_plan_flow}` | `{@AGENT: service_change_plan_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_add_feature_flow}` | `{@AGENT: service_add_feature_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:service_change_plan_flow}` | `{@AGENT: service_change_plan_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_handoff_prepaid}` | `{@AGENT: bell_va_to_ivr_handoff_prepaid}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_sales_routing_flow}` | `{@AGENT: bell_sales_routing_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:Bell_UC_Technical_Support_Infobot}` | `{@AGENT: Bell_UC_Technical_Support_Infobot}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_intent_apb}` | `{@AGENT: bell_tech_intent_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_intent_apb}` | `{@AGENT: bell_tech_intent_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_intent_apb}` | `{@AGENT: bell_tech_intent_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_handoff_prepaid}` | `{@AGENT: bell_va_to_ivr_handoff_prepaid}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Sales}` | `{@AGENT: bell_UC_Sales}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_field_tech_visit}` | `{@AGENT: bell_tech_field_tech_visit}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_field_tech_visit}` | `{@AGENT: bell_tech_field_tech_visit}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_field_tech_visit}` | `{@AGENT: bell_tech_field_tech_visit}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_authentication}` | `{@AGENT: bell_authentication}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_field_tech_visit_cancel_flow}` | `{@AGENT: bell_tech_field_tech_visit_cancel_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_field_tech_visit_cancel_flow}` | `{@AGENT: bell_tech_field_tech_visit_cancel_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_field_tech_visit_cancel_flow}` | `{@AGENT: bell_tech_field_tech_visit_cancel_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_authentication}` | `{@AGENT: bell_authentication}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_change_appointment_flow}` | `{@AGENT: bell_tech_change_appointment_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_change_appointment_flow}` | `{@AGENT: bell_tech_change_appointment_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_tech_change_appointment_flow}` | `{@AGENT: bell_tech_change_appointment_flow}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Wrap-up}` | `{@AGENT: bell_Steering_Wrap-up}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features Phase2}` | `{@AGENT: bell_UC_Manage Plans and Features Phase2}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_arrangment_setup_id_auth_eligibility_Checks}` | `{@AGENT: bell_payment_arrangment_setup_id_auth_eligibility_Checks}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_arrangment_setup_id_auth_eligibility_Checks}` | `{@AGENT: bell_payment_arrangment_setup_id_auth_eligibility_Checks}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Wrap-up}` | `{@AGENT: bell_Steering_Wrap-up}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Sales}` | `{@AGENT: bell_UC_Sales}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_PPV}` | `{@AGENT: bell_PPV}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support-1}` | `{@AGENT: bell_UC_Technical Support-1}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_rehit_Send_Troubleshooting_SMS}` | `{@AGENT: bell_rehit_Send_Troubleshooting_SMS}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_NLU_Query_Rewriter}` | `{@AGENT: bell_NLU_Query_Rewriter}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_handoff_prepaid}` | `{@AGENT: bell_va_to_ivr_handoff_prepaid}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Temporary Suspension}` | `{@AGENT: bell_UC_Temporary Suspension}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support-2}` | `{@AGENT: bell_UC_Technical Support-2}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Billing}` | `{@AGENT: bell_UC_Billing}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Billing}` | `{@AGENT: bell_UC_Billing}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Billing}` | `{@AGENT: bell_UC_Billing}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Billing}` | `{@AGENT: bell_UC_Billing}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Billing}` | `{@AGENT: bell_UC_Billing}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Billing}` | `{@AGENT: bell_UC_Billing}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Billing}` | `{@AGENT: bell_UC_Billing}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_account_balance_and_last_payment_details}` | `{@AGENT: bell_payment_account_balance_and_last_payment_details}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${agent:bell_UC_Disconnect}` | `{@AGENT: bell_UC_Disconnect}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Disconnect}` | `{@AGENT: bell_UC_Disconnect}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Disconnect}` | `{@AGENT: bell_UC_Disconnect}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_sales_device_related}` | `{@AGENT: bell_UC_sales_device_related}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Equipment}` | `{@AGENT: bell_UC_Equipment}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_sales_device_related}` | `{@AGENT: bell_UC_sales_device_related}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${agent:bell_UC_Other}` | `{@AGENT: bell_UC_Other}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Other}` | `{@AGENT: bell_UC_Other}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Other}` | `{@AGENT: bell_UC_Other}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Other}` | `{@AGENT: bell_UC_Other}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_autopay_status}` | `{@AGENT: bell_payment_autopay_status}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_account_balance_and_last_payment_details}` | `{@AGENT: bell_payment_account_balance_and_last_payment_details}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_one_time_CC_payment}` | `{@AGENT: bell_payment_one_time_CC_payment}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_setup_preAuth_pad}` | `{@AGENT: bell_payment_setup_preAuth_pad}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_autopay_update}` | `{@AGENT: bell_payment_autopay_update}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_disambiguation_for_vague_billing}` | `{@AGENT: bell_uc_disambiguation_for_vague_billing}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_arrangment_setup_id_auth_eligibility_Checks}` | `{@AGENT: bell_payment_arrangment_setup_id_auth_eligibility_Checks}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_update_payment_arrangements}` | `{@AGENT: bell_payment_update_payment_arrangements}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Payments}` | `{@AGENT: bell_UC_Payments}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Payments}` | `{@AGENT: bell_UC_Payments}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_payment_account_balance_and_last_payment_details}` | `{@AGENT: bell_payment_account_balance_and_last_payment_details}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Sales}` | `{@AGENT: bell_UC_Sales}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Sales}` | `{@AGENT: bell_UC_Sales}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Sales}` | `{@AGENT: bell_UC_Sales}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features Phase2}` | `{@AGENT: bell_UC_Manage Plans and Features Phase2}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features Phase2}` | `{@AGENT: bell_UC_Manage Plans and Features Phase2}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features Phase2}` | `{@AGENT: bell_UC_Manage Plans and Features Phase2}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features Phase2}` | `{@AGENT: bell_UC_Manage Plans and Features Phase2}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features}` | `{@AGENT: bell_UC_Manage Plans and Features}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features}` | `{@AGENT: bell_UC_Manage Plans and Features}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features}` | `{@AGENT: bell_UC_Manage Plans and Features}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Manage Plans and Features Phase2_1}` | `{@AGENT: bell_UC_Manage Plans and Features Phase2_1}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Account Management}` | `{@AGENT: bell_UC_Account Management}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support-1}` | `{@AGENT: bell_UC_Technical Support-1}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support}` | `{@AGENT: bell_UC_Technical Support}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${agent:bell_UC_Technical Support-2}` | `{@AGENT: bell_UC_Technical Support-2}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_Steering_Feedback}` | `{@AGENT: bell_Steering_Feedback}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_ticket_mgmt_omf_ticket_check_appointment_mgmt}` | `{@AGENT: bell_ticket_mgmt_omf_ticket_check_appointment_mgmt}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_app_mgmt_omf_change_reschedule_ticket}` | `{@AGENT: bell_app_mgmt_omf_change_reschedule_ticket}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_app_mgmt_omf_change_reschedule_ticket}` | `{@AGENT: bell_app_mgmt_omf_change_reschedule_ticket}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_app_mgmt_omf_change_reschedule_ticket}` | `{@AGENT: bell_app_mgmt_omf_change_reschedule_ticket}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_app_mgmt_omf_change_reschedule_ticket}` | `{@AGENT: bell_app_mgmt_omf_change_reschedule_ticket}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_app_mgmt_omf_change_reschedule_ticket}` | `{@AGENT: bell_app_mgmt_omf_change_reschedule_ticket}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_apb}` | `{@AGENT: bell_apb}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${agent:bell_uc_ask_LOB}` | `{@AGENT: bell_uc_ask_LOB}` | Updated AGENT Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_va_to_ivr_smarthome}` | `{@AGENT: bell_va_to_ivr_smarthome}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_determine_handover}` | `{@AGENT: bell_determine_handover}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_End the Conversation}` | `{@AGENT: bell_End the Conversation}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$Q` | `{Q}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$Q` | `{Q}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$Q` | `{Q}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_post_answer}` | `{@AGENT: bell_vr_post_answer}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_start_process}` | `{@AGENT: bell_vr_start_process}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_start_process}` | `{@AGENT: bell_vr_start_process}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_SMS Trigger}` | `{@AGENT: bell_SMS Trigger}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Match_3}` | `{@AGENT: bell_No_Match_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_global_error_count_check}` | `{@AGENT: bell_global_error_count_check}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_No_Input_3}` | `{@AGENT: bell_No_Input_3}` | Updated FLOW Reference syntax |
| `Variable Syntax` | `$Q` | `{Q}` | Updated DFCX $ variable to CXAS {} format |
| `Instruction Rewrite` | `${FLOW:bell_vr_next_task}` | `{@AGENT: bell_vr_next_task}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_next_task}` | `{@AGENT: bell_vr_next_task}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_next_task}` | `{@AGENT: bell_vr_next_task}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_next_task}` | `{@AGENT: bell_vr_next_task}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_aqd}` | `{@AGENT: bell_aqd}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Feedback}` | `{@AGENT: bell_Feedback}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_vr_next_task}` | `{@AGENT: bell_vr_next_task}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:Routing only}` | `{@AGENT: Routing only}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `routing` | `{@TOOL: routing}` | Mapped Python Function to Tool |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `${FLOW:bell_Query_Rewriter}` | `{@AGENT: bell_Query_Rewriter}` | Updated FLOW Reference syntax |
| `Instruction Rewrite` | `extract_entities` | `{@TOOL: extract_entities}` | Mapped Python Function to Tool |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_input_retry_count}` | `{no_input_retry_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_match_counter}` | `{no_match_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_match_counter}` | `{no_match_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_to_ccaip}` | `{va_to_ccaip}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_input_retry_count}` | `{no_input_retry_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{NGA}` | `{NGA}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{utterance}` | `{utterance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{utterance}` | `{utterance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_pitch}` | `{mya_pitch}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_pitch}` | `{mya_pitch}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_state}` | `{ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_state}` | `{ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_state}` | `{ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_state}` | `{ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{acut_retrieve_response}` | `{acut_retrieve_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{acut_retrieve_response}` | `{acut_retrieve_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{categoryValue}` | `{categoryValue}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{active_dispatch_count}` | `{active_dispatch_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pattern_id}` | `{pattern_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_ticket_state}` | `{trouble_ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vrOutcome}` | `{vrOutcome}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vrOutcome}` | `{vrOutcome}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vrOutcome}` | `{vrOutcome}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vrOutcome}` | `{vrOutcome}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{patternClearFlag}` | `{patternClearFlag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{patternClearFlag}` | `{patternClearFlag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{patternClearFlag}` | `{patternClearFlag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{patternClearFlag}` | `{patternClearFlag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_ticket_state}` | `{trouble_ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{isPast_patternTime}` | `{isPast_patternTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{patternTimeResponse}` | `{patternTimeResponse}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{patternTimeResponse}` | `{patternTimeResponse}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{isPast_patternTime}` | `{isPast_patternTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_day}` | `{ticket_day}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_month}` | `{ticket_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_date}` | `{ticket_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_year}` | `{ticket_year}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_hours}` | `{start_time_hours}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours}` | `{end_time_hours}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_hours}` | `{start_time_hours}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours}` | `{end_time_hours}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours}` | `{end_time_hours}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_day_fr}` | `{ticket_day_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_month_fr}` | `{ticket_month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_date_fr}` | `{ticket_date_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_year_fr}` | `{ticket_year_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_hours_fr}` | `{start_time_hours_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours_fr}` | `{end_time_hours_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_hours_fr}` | `{start_time_hours_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours_fr}` | `{end_time_hours_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours_fr}` | `{end_time_hours_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_ticket_state}` | `{trouble_ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{main_task_status_message}` | `{main_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{main_task_status_message}` | `{main_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{main_task_status_message}` | `{main_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{main_task_status_message}` | `{main_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{acut_retrieve_response}` | `{acut_retrieve_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{acut_retrieve_response}` | `{acut_retrieve_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{acut_retrieve_response}` | `{acut_retrieve_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{main_task_status_message}` | `{main_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{disposition_code_message}` | `{disposition_code_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{main_task_status_message}` | `{main_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{disposition_code_message}` | `{disposition_code_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{utterance_raw}` | `{utterance_raw}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{utterance_raw}` | `{utterance_raw}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{utterance_raw}` | `{utterance_raw}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{utterance_raw}` | `{utterance_raw}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{NGA}` | `{NGA}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_match_1}` | `{no_match_1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_match_2}` | `{no_match_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{speciality}` | `{speciality}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{skip_id}` | `{skip_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bell_speciality}` | `{bell_speciality}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_va_get_did_fail}` | `{ivr_va_get_did_fail}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_va_cpm_check_fail}` | `{ivr_va_cpm_check_fail}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{temp_flag}` | `{temp_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{speak_to_agent_counter}` | `{speak_to_agent_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{speaktoagent}` | `{speaktoagent}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{speaktoagent}` | `{speaktoagent}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{test_bell_rehit_Check_Subscription}` | `{test_bell_rehit_Check_Subscription}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bell_rehit_confirmation}` | `{bell_rehit_confirmation}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{response}` | `{response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{response}` | `{response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CLID}` | `{CLID}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{invalid_clid_counter}` | `{invalid_clid_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{response}` | `{response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{response}` | `{response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_nomatch_counter}` | `{local_nomatch_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_nomatch_counter}` | `{local_nomatch_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_nomatch_counter}` | `{local_nomatch_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_noinput_counter}` | `{local_noinput_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_noinput_counter}` | `{local_noinput_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_noinput_counter}` | `{local_noinput_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_nomatch_counter}` | `{local_nomatch_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{response}` | `{response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{response}` | `{response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_nomatch_counter}` | `{local_nomatch_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_noinput_counter}` | `{local_noinput_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_nomatch_counter}` | `{local_nomatch_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_trigger}` | `{local_trigger}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{local_noinput_counter}` | `{local_noinput_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{test_auth}` | `{test_auth}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{NGA}` | `{NGA}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{NGA}` | `{NGA}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{speak_to_agent_counter}` | `{speak_to_agent_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{agent_flag}` | `{agent_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bbm_smb_flag}` | `{bbm_smb_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{digital_tools_phase2}` | `{digital_tools_phase2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{infobot_flag}` | `{infobot_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{test_multiban}` | `{test_multiban}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_to_va_entry}` | `{ivr_to_va_entry}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_pitch}` | `{mya_pitch}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_pitch}` | `{mya_pitch}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{task_type}` | `{task_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{NGA}` | `{NGA}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Error_Count}` | `{Error_Count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_handoff_identification}` | `{ivr_handoff_identification}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_other_number}` | `{event_other_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{regional_identity}` | `{regional_identity}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_handoff}` | `{ivr_handoff}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CCC_asked}` | `{CCC_asked}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_handoff}` | `{ivr_handoff}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_fallback_flag}` | `{identification_fallback_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{BAN}` | `{BAN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{BAN}` | `{BAN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_account}` | `{n_billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_account}` | `{n_billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_prepaid}` | `{is_prepaid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_account}` | `{n_billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_prepaid}` | `{is_prepaid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_account}` | `{n_billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{business_type}` | `{business_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_prepaid}` | `{is_prepaid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{query_rewriter_looping_counter}` | `{query_rewriter_looping_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{query_rewriter_looping_counter}` | `{query_rewriter_looping_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_match_2}` | `{no_match_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_match_2}` | `{no_match_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_match_1}` | `{no_match_1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{get_ras_apb_response}` | `{get_ras_apb_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_message}` | `{apb_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{interruptible}` | `{interruptible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_message}` | `{apb_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{interruptible}` | `{interruptible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_message}` | `{apb_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hang_up}` | `{hang_up}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{agent_transfer}` | `{agent_transfer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hang_up}` | `{hang_up}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hang_up}` | `{hang_up}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{agent_transfer}` | `{agent_transfer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_message}` | `{apb_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hang_up}` | `{hang_up}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hang_up}` | `{hang_up}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{agent_transfer}` | `{agent_transfer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_send_status}` | `{sms_send_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_content}` | `{sms_content}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{test_private_sms}` | `{test_private_sms}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{fallback_counter}` | `{fallback_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{fallback_counter}` | `{fallback_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{fallback_counter}` | `{fallback_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{phone_number}` | `{phone_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_in_account}` | `{is_in_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_in_account}` | `{is_in_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_type}` | `{sms_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_type}` | `{sms_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_type}` | `{sms_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_in_account}` | `{is_in_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn_grp1}` | `{cirn_grp1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn_grp2}` | `{cirn_grp2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn_grp3}` | `{cirn_grp3}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn_grp4}` | `{cirn_grp4}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn_grp1}` | `{cirn_grp1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn_grp2}` | `{cirn_grp2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn_grp3}` | `{cirn_grp3}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn_grp4}` | `{cirn_grp4}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_content}` | `{sms_content}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{telephone_number}` | `{telephone_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_content}` | `{sms_content}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{brand}` | `{brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{street_number}` | `{street_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{street_name}` | `{street_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sub_unit}` | `{sub_unit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{street_number}` | `{street_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{street_name}` | `{street_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sub_unit}` | `{sub_unit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_pitch}` | `{mya_pitch}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_pitch}` | `{mya_pitch}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{isPast_patternTime}` | `{isPast_patternTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{patternTimeResponse}` | `{patternTimeResponse}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{patternTimeResponse}` | `{patternTimeResponse}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{isPast_patternTime}` | `{isPast_patternTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_day_fr}` | `{ticket_day_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_month_fr}` | `{ticket_month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_date_fr}` | `{ticket_date_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_year_fr}` | `{ticket_year_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_hours_fr}` | `{start_time_hours_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours_fr}` | `{end_time_hours_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_hours_fr}` | `{start_time_hours_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours_fr}` | `{end_time_hours_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours_fr}` | `{end_time_hours_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_day}` | `{ticket_day}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_month}` | `{ticket_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_date}` | `{ticket_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_year}` | `{ticket_year}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_hours}` | `{start_time_hours}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours}` | `{end_time_hours}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_hours}` | `{start_time_hours}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours}` | `{end_time_hours}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_hours}` | `{end_time_hours}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{categoryValue}` | `{categoryValue}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{categoryValue}` | `{categoryValue}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{active_dispatch_count}` | `{active_dispatch_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pattern_id}` | `{pattern_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pattern_id}` | `{pattern_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_ticket_state}` | `{trouble_ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_outcome}` | `{vr_outcome}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{isPast_patternTime}` | `{isPast_patternTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{isPast_patternTime}` | `{isPast_patternTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{acut_retrieve_response}` | `{acut_retrieve_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_state}` | `{ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_state}` | `{ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{from_flow}` | `{from_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{acut_retrieve_response}` | `{acut_retrieve_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_state}` | `{ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_state}` | `{ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{active_dispatch_count}` | `{active_dispatch_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_ticket_state}` | `{trouble_ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_type}` | `{dispatch_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_ticket_state}` | `{trouble_ticket_state}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted}` | `{date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted2}` | `{date_formatted2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appointment_type}` | `{appointment_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appointment_type}` | `{appointment_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_omf_tickets}` | `{n_omf_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_acut_tickets}` | `{n_acut_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_omf_tickets}` | `{n_omf_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_acut_tickets}` | `{n_acut_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_acut_tickets}` | `{n_acut_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted}` | `{date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted}` | `{date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted2}` | `{date_formatted2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted2}` | `{date_formatted2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_acut_tickets}` | `{n_acut_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cancellation_eligibility_status}` | `{cancellation_eligibility_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cancellation_eligibility_status}` | `{cancellation_eligibility_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cancellation_eligibility_status}` | `{cancellation_eligibility_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cancellation_eligibility_status}` | `{cancellation_eligibility_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cancellation_eligibility_status}` | `{cancellation_eligibility_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appointment_date_formatted}` | `{appointment_date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_task_status_message}` | `{dispatch_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appointment_date_formatted}` | `{appointment_date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{main_task_status_message}` | `{main_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{trouble_type_message}` | `{trouble_type_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{main_task_status_message}` | `{main_task_status_message}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted}` | `{date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted}` | `{date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted2}` | `{date_formatted2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted2}` | `{date_formatted2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{recent_service_type1}` | `{recent_service_type1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{recent_service_type1}` | `{recent_service_type1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{recent_service_type2}` | `{recent_service_type2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{recent_service_type2}` | `{recent_service_type2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account_info_list}` | `{billing_account_info_list}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_method_completed}` | `{contact_method_completed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{telephone_otp}` | `{telephone_otp}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{otp_number_list}` | `{otp_number_list}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_number}` | `{contact_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_number}` | `{contact_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_number}` | `{contact_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{invalid_phone_counter}` | `{invalid_phone_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{invalid_phone_counter}` | `{invalid_phone_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_number}` | `{contact_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_number}` | `{contact_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{refusal_counter}` | `{refusal_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{refusal_counter}` | `{refusal_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_number}` | `{contact_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_number}` | `{contact_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_service_ids}` | `{lob_service_ids}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_is_eligible}` | `{mya_is_eligible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_is_eligible}` | `{mya_is_eligible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_is_eligible}` | `{mya_is_eligible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_application_url}` | `{mya_application_url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{order_detail_response}` | `{order_detail_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account_number}` | `{billing_account_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day}` | `{day}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{calendarIdentifier}` | `{calendarIdentifier}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{interval}` | `{interval}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{estimatedStartTime}` | `{estimatedStartTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{line_of_business_selected}` | `{line_of_business_selected}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week}` | `{day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date}` | `{date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time}` | `{start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time}` | `{end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{line_of_business_selected}` | `{line_of_business_selected}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week}` | `{day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date}` | `{date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time}` | `{start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time}` | `{end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day}` | `{day}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{calendarIdentifier}` | `{calendarIdentifier}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{interval}` | `{interval}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{estimatedStartTime}` | `{estimatedStartTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day}` | `{day}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{calendarIdentifier}` | `{calendarIdentifier}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{interval}` | `{interval}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{estimatedStartTime}` | `{estimatedStartTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{variable_name}` | `{variable_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_omf_tickets}` | `{n_omf_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_acut_tickets}` | `{n_acut_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_omf_tickets}` | `{n_omf_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_acut_tickets}` | `{n_acut_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_acut_tickets}` | `{n_acut_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_omf_tickets}` | `{n_omf_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{recent_service_type1}` | `{recent_service_type1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{recent_service_type1}` | `{recent_service_type1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{recent_service_type2}` | `{recent_service_type2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{recent_service_type2}` | `{recent_service_type2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted}` | `{date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted}` | `{date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted2}` | `{date_formatted2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_formatted2}` | `{date_formatted2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_acut_tickets}` | `{n_acut_tickets}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{force_ss_exception}` | `{force_ss_exception}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_queue}` | `{special_queue}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{intent}` | `{intent}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{url}` | `{url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{url}` | `{url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mock_mode}` | `{mock_mode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{unique_services}` | `{unique_services}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{unique_services}` | `{unique_services}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{unique_services}` | `{unique_services}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_queue}` | `{special_queue}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mob_sales_pitch_flag}` | `{mob_sales_pitch_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mob_sales_pitch_flag}` | `{mob_sales_pitch_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_match_error_flag}` | `{no_match_error_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sales_queue_open}` | `{sales_queue_open}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sales_queue_open}` | `{sales_queue_open}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{province}` | `{province}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{province}` | `{province}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{province}` | `{province}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$40` | `{40}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$35` | `{35}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{caller_channel}` | `{caller_channel}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{caller_channel}` | `{caller_channel}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{caller_channel}` | `{caller_channel}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{caller_channel}` | `{caller_channel}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn}` | `{cirn}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn}` | `{cirn}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pin_available}` | `{pin_available}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pin_available}` | `{pin_available}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{url}` | `{url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{url}` | `{url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{nga}` | `{nga}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{from_billing}` | `{from_billing}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dueDate}` | `{dueDate}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dueDate}` | `{dueDate}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dueDate}` | `{dueDate}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dueDate}` | `{dueDate}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{use_case_fr}` | `{use_case_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{use_case_en}` | `{use_case_en}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account}` | `{billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{calculated_payment_date}` | `{calculated_payment_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_amount}` | `{payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_amount}` | `{payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{currentBalance}` | `{currentBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{currentBalance}` | `{currentBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{currentBalance}` | `{currentBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{currentBalance}` | `{currentBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_amount}` | `{payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_amount}` | `{payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{calculated_payment_date}` | `{calculated_payment_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{calculated_payment_date}` | `{calculated_payment_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{calculated_payment_date}` | `{calculated_payment_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$50` | `{50}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$50` | `{50}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$49` | `{49}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$49` | `{49}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account_number_list}` | `{billing_account_number_list}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{NGA}` | `{NGA}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{NGA}` | `{NGA}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{marketSegment}` | `{marketSegment}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{marketSegment}` | `{marketSegment}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{marketSegment}` | `{marketSegment}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{marketSegment}` | `{marketSegment}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{marketSegment}` | `{marketSegment}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{marketSegment}` | `{marketSegment}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{non_central}` | `{non_central}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{nm1_ban}` | `{nm1_ban}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_number}` | `{account_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CCC}` | `{CCC}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{BNQ}` | `{BNQ}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{SMB}` | `{SMB}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{BBM}` | `{BBM}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{region}` | `{region}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{region}` | `{region}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_number}` | `{account_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postcode_count}` | `{postcode_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{i}` | `{i}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_postcode}` | `{n_postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_postcode_count}` | `{lob_postcode_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_i}` | `{lob_i}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_postcode}` | `{n_postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{global_error_counter}` | `{global_error_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_match_counter}` | `{no_match_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_number}` | `{account_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{smb_ban}` | `{smb_ban}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_number}` | `{account_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ccc_ban}` | `{ccc_ban}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{region}` | `{region}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{region}` | `{region}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{BBM}` | `{BBM}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CCC}` | `{CCC}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_handoff_identification}` | `{ivr_handoff_identification}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_prepaid}` | `{is_prepaid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_prepaid}` | `{is_prepaid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_agent}` | `{lob_agent}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_postcode}` | `{n_postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{atlantic}` | `{atlantic}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{BNQ}` | `{BNQ}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{MTS}` | `{MTS}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_accounts_lob}` | `{n_billing_accounts_lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_accounts_lob}` | `{n_billing_accounts_lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_postcode}` | `{n_postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{nm1_account}` | `{nm1_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{nm1_account}` | `{nm1_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postcode}` | `{postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postal_agent}` | `{postal_agent}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postal_agent_2}` | `{postal_agent_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postcode}` | `{postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postcode}` | `{postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_accounts_postcoode}` | `{n_billing_accounts_postcoode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_service_address_postcode}` | `{n_service_address_postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postal_agent}` | `{postal_agent}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postcode}` | `{postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postcode}` | `{postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_postcode}` | `{n_postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_id_search_response}` | `{customer_id_search_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_account_internet}` | `{n_billing_account_internet}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_account_tv}` | `{n_billing_account_tv}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_account_mobility}` | `{n_billing_account_mobility}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_account_homephone}` | `{n_billing_account_homephone}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_postcode}` | `{n_postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_accounts_lob}` | `{n_billing_accounts_lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_billing_accounts_lob}` | `{n_billing_accounts_lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_agent_2}` | `{lob_agent_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_postcode}` | `{n_postcode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consumer_ban_count_ccc}` | `{consumer_ban_count_ccc}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consumer_ban_count_smb}` | `{consumer_ban_count_smb}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consumer_ban_count_ccc}` | `{consumer_ban_count_ccc}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consumer_ban_count_smb}` | `{consumer_ban_count_smb}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consumer_count_all}` | `{consumer_count_all}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ccc_present}` | `{ccc_present}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{smb_present}` | `{smb_present}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ccc_present}` | `{ccc_present}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{smb_present}` | `{smb_present}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{atlantic}` | `{atlantic}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{BNQ}` | `{BNQ}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{MTS}` | `{MTS}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{SMB}` | `{SMB}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CCC}` | `{CCC}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{BBM}` | `{BBM}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$1` | `{1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$10` | `{10}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$1` | `{1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$10` | `{10}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account}` | `{billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{spending_limit}` | `{spending_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{spending_limit}` | `{spending_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account}` | `{billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{other_payment_amount}` | `{other_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bad_amount}` | `{bad_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$1` | `{1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$10` | `{10}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bad_amount}` | `{bad_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bad_amount}` | `{bad_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$1` | `{1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$10` | `{10}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bad_amount}` | `{bad_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{amount_paid}` | `{amount_paid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{amount_paid}` | `{amount_paid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bad_amount}` | `{bad_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bad_amount}` | `{bad_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountType}` | `{accountType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountSubType}` | `{accountSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountType}` | `{accountType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountSubType}` | `{accountSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{oneBillIndicator}` | `{oneBillIndicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountType}` | `{accountType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountType}` | `{accountType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{oneBillIndicator}` | `{oneBillIndicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{province}` | `{province}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{oneBillIndicator}` | `{oneBillIndicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{BAN}` | `{BAN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billingcycle_status}` | `{billingcycle_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billingcycle_status}` | `{billingcycle_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_bill_date_within_10_days}` | `{is_bill_date_within_10_days}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bill_date_formatted}` | `{bill_date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bill_date_formatted}` | `{bill_date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billingcycle_status}` | `{billingcycle_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_bill_date_within_10_days}` | `{is_bill_date_within_10_days}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billingcycle_status}` | `{billingcycle_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_sus_limit}` | `{clp_sus_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billingcycle_status}` | `{billingcycle_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_bill_date_within_10_days}` | `{is_bill_date_within_10_days}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bill_date_formatted}` | `{bill_date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bill_date_formatted}` | `{bill_date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billingcycle_status}` | `{billingcycle_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_bill_date_within_10_days}` | `{is_bill_date_within_10_days}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_program}` | `{clp_program}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billingcycle_status}` | `{billingcycle_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billingcycle_status}` | `{billingcycle_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_bill_date_within_10_days}` | `{is_bill_date_within_10_days}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bill_date_formatted}` | `{bill_date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{bill_date_formatted}` | `{bill_date_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billingcycle_status}` | `{billingcycle_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_bill_date_within_10_days}` | `{is_bill_date_within_10_days}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_faq_response}` | `{payment_faq_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_balance}` | `{account_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_date}` | `{last_payment_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_balance}` | `{account_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_balance}` | `{account_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_balance}` | `{account_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_date}` | `{last_payment_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_balance}` | `{account_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_balance}` | `{account_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_spending_limit}` | `{clp_spending_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_spending_limit}` | `{clp_spending_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{oneBillIndicator}` | `{oneBillIndicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{oneBillIndicator}` | `{oneBillIndicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{oneBillIndicator}` | `{oneBillIndicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_faq}` | `{clp_faq}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$1` | `{1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$10` | `{10}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_bad_amount}` | `{clp_bad_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_bad_amount}` | `{clp_bad_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_amount_paid}` | `{clp_amount_paid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_amount_paid}` | `{clp_amount_paid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_bad_amount}` | `{clp_bad_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_bad_amount}` | `{clp_bad_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_faq_response}` | `{payment_faq_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{card_number}` | `{card_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_faq}` | `{clp_faq}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_failed_attempt}` | `{cc_failed_attempt}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{current_special_status}` | `{current_special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{current_special_status}` | `{current_special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{current_special_status}` | `{current_special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{current_special_status}` | `{current_special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{current_special_status}` | `{current_special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{current_special_status}` | `{current_special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{current_special_status}` | `{current_special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_failed_attempt}` | `{cc_failed_attempt}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_date}` | `{last_payment_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_date}` | `{last_payment_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_date}` | `{last_payment_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_amount}` | `{last_payment_amount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_payment_date}` | `{last_payment_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{errorCode}` | `{errorCode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{errorCode}` | `{errorCode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bantype}` | `{Bantype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bansubtype}` | `{Bansubtype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bantype}` | `{Bantype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bansubtype}` | `{Bansubtype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bantype}` | `{Bantype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bantype}` | `{Bantype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{eligInd}` | `{eligInd}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{eligInd}` | `{eligInd}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vanity_url}` | `{vanity_url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vanity_url}` | `{vanity_url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vanity_url}` | `{vanity_url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_faq_response}` | `{payment_faq_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_invalid_counter}` | `{cc_invalid_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_invalid_counter}` | `{cc_invalid_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{card_brand}` | `{card_brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{card_brand}` | `{card_brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{card_brand}` | `{card_brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{wrong_cc_number_counter}` | `{wrong_cc_number_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{credit_card_number}` | `{credit_card_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_from_utterance}` | `{cc_from_utterance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{card_number}` | `{card_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{card_number}` | `{card_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{check_credit_card_number}` | `{check_credit_card_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{check_credit_card_number}` | `{check_credit_card_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{check_credit_card_number}` | `{check_credit_card_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dts_token_details_response}` | `{dts_token_details_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{card_number}` | `{card_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cvv_number}` | `{cvv_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{expiry_date}` | `{expiry_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_details_valid}` | `{cc_details_valid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_details_valid}` | `{cc_details_valid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_details_valid}` | `{cc_details_valid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_balance}` | `{clp_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_sus_limit}` | `{clp_sus_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_sus_limit}` | `{clp_sus_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clp_aul_limit}` | `{clp_aul_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{specialty_flag}` | `{specialty_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{specialty_flag}` | `{specialty_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{province}` | `{province}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{province}` | `{province}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vanity_url}` | `{vanity_url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vanity_url}` | `{vanity_url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{variable_name}` | `{variable_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{current_balance}` | `{current_balance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{due_date}` | `{due_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{amount_paid_by_user}` | `{amount_paid_by_user}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{amount_paid_by_user}` | `{amount_paid_by_user}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{confirmation_number}` | `{confirmation_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{amount_paid_by_user}` | `{amount_paid_by_user}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{confirmation_number}` | `{confirmation_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{amount_paid_by_user}` | `{amount_paid_by_user}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{confirmation_number}` | `{confirmation_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$50` | `{50}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$50` | `{50}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `$50` | `{50}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{completed_topup_flag}` | `{completed_topup_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_type}` | `{sms_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_content}` | `{sms_content}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{from_pacc_otcc}` | `{from_pacc_otcc}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_failed_attempt}` | `{cc_failed_attempt}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{completed_topup_flag}` | `{completed_topup_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{different_number}` | `{different_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_type}` | `{sms_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_content}` | `{sms_content}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_type}` | `{sms_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{sms_content}` | `{sms_content}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{spending_limit}` | `{spending_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{spending_limit}` | `{spending_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{spending_limit}` | `{spending_limit}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{moved_out_of_col}` | `{moved_out_of_col}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{no_change_col_status}` | `{no_change_col_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vanity_url}` | `{vanity_url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{coming_from}` | `{coming_from}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hardstop}` | `{hardstop}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_id}` | `{page_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{flow_id}` | `{flow_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_name}` | `{page_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{telephone_number}` | `{telephone_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hardstop}` | `{hardstop}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_id}` | `{page_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{flow_id}` | `{flow_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_name}` | `{page_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{FIBE_COUNT}` | `{FIBE_COUNT}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{FIBE_COUNT}` | `{FIBE_COUNT}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hardstop}` | `{hardstop}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_id}` | `{page_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{flow_id}` | `{flow_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_name}` | `{page_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{SAT_COUNT}` | `{SAT_COUNT}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{SAT_COUNT}` | `{SAT_COUNT}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hardstop}` | `{hardstop}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_id}` | `{page_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{flow_id}` | `{flow_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_name}` | `{page_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{faq_link}` | `{faq_link}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{BAN}` | `{BAN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{brand}` | `{brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{consolidated_status}` | `{consolidated_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Province}` | `{Province}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Province}` | `{Province}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vanity_url}` | `{vanity_url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vanity_url}` | `{vanity_url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account}` | `{billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{errorCode}` | `{errorCode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account}` | `{billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{errorCode}` | `{errorCode}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bantype}` | `{Bantype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bansubtype}` | `{Bansubtype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bantype}` | `{Bantype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bansubtype}` | `{Bansubtype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bantype}` | `{Bantype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Bantype}` | `{Bantype}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Province}` | `{Province}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{Province}` | `{Province}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account}` | `{billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method_check}` | `{payment_method_check}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method_check}` | `{payment_method_check}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{eligInd}` | `{eligInd}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{eligInd}` | `{eligInd}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_method}` | `{payment_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{incorrect_payment_method_counter}` | `{incorrect_payment_method_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{incorrect_payment_method_counter}` | `{incorrect_payment_method_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account}` | `{billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vanity_url}` | `{vanity_url}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{repeat_response}` | `{repeat_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_failed_attempt}` | `{cc_failed_attempt}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{isValid}` | `{isValid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{isValid}` | `{isValid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{paymentConfirmationNumber}` | `{paymentConfirmationNumber}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{paymentConfirmationNumber}` | `{paymentConfirmationNumber}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{errorCodeID}` | `{errorCodeID}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{errorCodeID}` | `{errorCodeID}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{errorCodeID}` | `{errorCodeID}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{errorCodeID}` | `{errorCodeID}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{errorCodeID}` | `{errorCodeID}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{errorCodeID}` | `{errorCodeID}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cc_failed_attempt}` | `{cc_failed_attempt}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banType}` | `{banType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{banSubType}` | `{banSubType}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pastDueAmount}` | `{pastDueAmount}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{accountBalance}` | `{accountBalance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contains_mobility}` | `{contains_mobility}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contains_internet}` | `{contains_internet}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contains_tv}` | `{contains_tv}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contains_mobility}` | `{contains_mobility}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contains_internet}` | `{contains_internet}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contains_tv}` | `{contains_tv}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{utterance}` | `{utterance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{utterance}` | `{utterance}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{service_identifier}` | `{service_identifier}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_eligible}` | `{mya_eligible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_eligible}` | `{mya_eligible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hardstop}` | `{hardstop}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_id}` | `{page_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{flow_id}` | `{flow_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_name}` | `{page_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_information_response}` | `{mya_information_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_eligible}` | `{mya_eligible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_eligible}` | `{mya_eligible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hardstop}` | `{hardstop}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_id}` | `{page_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{flow_id}` | `{flow_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{page_name}` | `{page_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{infobot_flag}` | `{infobot_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{infobot_flag}` | `{infobot_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{infobot_flag}` | `{infobot_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{infobot_flag}` | `{infobot_flag}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{issue_type}` | `{issue_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{issue_type}` | `{issue_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_id_search_response}` | `{customer_id_search_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{multiple_postal_codes_exist}` | `{multiple_postal_codes_exist}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postal_code}` | `{postal_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{postal_code}` | `{postal_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{brand}` | `{brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn}` | `{cirn}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{outage_status}` | `{outage_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_date}` | `{month_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{fromTime}` | `{fromTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{toTime}` | `{toTime}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_date_fr}` | `{month_date_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{fromTime_fr}` | `{fromTime_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{toTime_fr}` | `{toTime_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{outage_status}` | `{outage_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{outage_status}` | `{outage_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{outage_status}` | `{outage_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{outage_status}` | `{outage_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_queue}` | `{special_queue}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_queue}` | `{special_queue}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{device_type}` | `{device_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{device_type}` | `{device_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{device_type}` | `{device_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mobility_sub_type}` | `{mobility_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{device_type}` | `{device_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mobility_sub_type}` | `{mobility_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mobility_sub_type}` | `{mobility_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hardstop}` | `{hardstop}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{hardstop}` | `{hardstop}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{type_sub_type}` | `{type_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{typr_sub_type}` | `{typr_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{type_sub_type}` | `{type_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{typr_sub_type}` | `{typr_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{apb_location_id}` | `{apb_location_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{type_sub_type}` | `{type_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_mgmt_webhook_failure_type}` | `{ticket_mgmt_webhook_failure_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_mgmt_webhook_failure_type}` | `{ticket_mgmt_webhook_failure_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_mgmt_webhook_failure_type}` | `{ticket_mgmt_webhook_failure_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_mgmt_webhook_failure_type}` | `{ticket_mgmt_webhook_failure_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_mgmt_webhook_failure_type}` | `{ticket_mgmt_webhook_failure_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appointment_type}` | `{appointment_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tester_id}` | `{tester_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tester_firstname}` | `{tester_firstname}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tester_firstname}` | `{tester_firstname}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{business}` | `{business}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{business}` | `{business}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tfn}` | `{tfn}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn}` | `{cirn}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_ibm_id}` | `{va_ibm_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{acut_retrieve_response}` | `{acut_retrieve_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week_fr}` | `{day_of_week_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_fr}` | `{month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_fr_2}` | `{start_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_fr_2}` | `{end_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week}` | `{day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month}` | `{month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_2}` | `{start_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_2}` | `{end_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{first_available_md}` | `{first_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_available_md}` | `{last_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{first_available_md}` | `{first_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_available_md}` | `{last_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_the_week_fr}` | `{day_of_the_week_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_fr}` | `{month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_the_week}` | `{day_of_the_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month}` | `{month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dynamic_intervals}` | `{dynamic_intervals}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{unav_response}` | `{unav_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dynamic_intervals_trimmed}` | `{dynamic_intervals_trimmed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{available_slots_string_fr}` | `{available_slots_string_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{available_slots_string}` | `{available_slots_string}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week_fr}` | `{day_of_week_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_fr}` | `{month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_fr_2}` | `{start_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_fr_2}` | `{end_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_fr_2}` | `{start_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_fr_2}` | `{end_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_formatted}` | `{end_time_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week}` | `{day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month}` | `{month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_2}` | `{start_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_2}` | `{end_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_2}` | `{start_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_2}` | `{end_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_formatted}` | `{end_time_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{order_detail_response}` | `{order_detail_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{parsed_order_route}` | `{parsed_order_route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{parsed_order_route}` | `{parsed_order_route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{parsed_order_route}` | `{parsed_order_route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{parsed_order_route}` | `{parsed_order_route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{line_of_business}` | `{line_of_business}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{line_of_business}` | `{line_of_business}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{line_of_business}` | `{line_of_business}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{line_of_business}` | `{line_of_business}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{from_flow}` | `{from_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_count}` | `{lob_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_count}` | `{lob_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_count}` | `{lob_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{from_flow}` | `{from_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_count}` | `{lob_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{from_flow}` | `{from_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lineOfBusiness_1}` | `{lineOfBusiness_1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lineOfBusiness_1}` | `{lineOfBusiness_1}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lineOfBusiness_2}` | `{lineOfBusiness_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lineOfBusiness_2}` | `{lineOfBusiness_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{from_flow}` | `{from_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week}` | `{day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month}` | `{month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_2}` | `{start_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_2}` | `{end_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week_fr}` | `{day_of_week_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_fr}` | `{month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_fr_2}` | `{start_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_fr_2}` | `{end_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{first_available_md}` | `{first_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_available_md}` | `{last_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{first_available_md}` | `{first_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_available_md}` | `{last_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_the_week}` | `{day_of_the_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month}` | `{month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_the_week_fr}` | `{day_of_the_week_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_fr}` | `{month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{unav_response}` | `{unav_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{available_slots_string}` | `{available_slots_string}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{available_slots_string_fr}` | `{available_slots_string_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week}` | `{day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month}` | `{month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_2}` | `{start_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_2}` | `{end_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_2}` | `{start_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_2}` | `{end_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_formatted}` | `{end_time_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week_fr}` | `{day_of_week_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_fr}` | `{month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_fr_2}` | `{start_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_fr_2}` | `{end_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_fr_2}` | `{start_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_fr_2}` | `{end_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_formatted}` | `{end_time_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{acut_retrieve_response}` | `{acut_retrieve_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dispatch_status}` | `{dispatch_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_number_on_file}` | `{contact_number_on_file}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_number}` | `{ticket_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_preference}` | `{contact_preference}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{contact_phone}` | `{contact_phone}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_number}` | `{ticket_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_range_begin}` | `{date_range_begin}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_range_end}` | `{date_range_end}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{wfas_availability_response}` | `{wfas_availability_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week}` | `{day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month}` | `{month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_2}` | `{start_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_2}` | `{end_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week_fr}` | `{day_of_week_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_fr}` | `{month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_fr_2}` | `{start_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_fr_2}` | `{end_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{first_available_md}` | `{first_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_available_md}` | `{last_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{first_available_md}` | `{first_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{last_available_md}` | `{last_available_md}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{user_selected_day}` | `{user_selected_day}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{user_selected_time}` | `{user_selected_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{wfas_availability_response}` | `{wfas_availability_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_the_week}` | `{day_of_the_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month}` | `{month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_the_week_fr}` | `{day_of_the_week_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_fr}` | `{month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dynamic_intervals}` | `{dynamic_intervals}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ticket_number}` | `{ticket_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{wfas_context}` | `{wfas_context}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{selected_date}` | `{selected_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{selected_start_time}` | `{selected_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{selected_end_time}` | `{selected_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{selected_interval_name}` | `{selected_interval_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week}` | `{day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month}` | `{month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_2}` | `{start_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_2}` | `{end_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_2}` | `{start_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_2}` | `{end_time_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_formatted}` | `{end_time_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{day_of_week_fr}` | `{day_of_week_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{date_of_month}` | `{date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{month_fr}` | `{month_fr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_fr_2}` | `{start_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_fr_2}` | `{end_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{start_time_fr_2}` | `{start_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_fr_2}` | `{end_time_fr_2}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{end_time_formatted}` | `{end_time_formatted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{wfas_context}` | `{wfas_context}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{kickout_response}` | `{kickout_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{kickout_response}` | `{kickout_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mobility_sub_type}` | `{mobility_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_Prepaid}` | `{lob_Prepaid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_prepaid}` | `{is_prepaid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_id_search_response}` | `{customer_id_search_response}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{NGA}` | `{NGA}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_ban_with_lob}` | `{n_ban_with_lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_ban_with_lob}` | `{n_ban_with_lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{n_ban_with_lob}` | `{n_ban_with_lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{service_type}` | `{service_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{service_type}` | `{service_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{service_type}` | `{service_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{domain}` | `{domain}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cti_sd}` | `{cti_sd}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{brand}` | `{brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account_info_list}` | `{billing_account_info_list}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_expecting_answer}` | `{is_expecting_answer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_answer1_id}` | `{customer_answer1_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_answer2_id}` | `{customer_answer2_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_expecting_answer}` | `{is_expecting_answer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{6590_customer_answer1_id}` | `{6590_customer_answer1_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_answer1_id}` | `{customer_answer1_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_answer2_id}` | `{customer_answer2_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_answer1_id}` | `{customer_answer1_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_answer2_id}` | `{customer_answer2_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{counter_post_task}` | `{counter_post_task}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{counter_post_task}` | `{counter_post_task}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{counter_post_task}` | `{counter_post_task}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{service_id}` | `{service_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{service_id}` | `{service_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{counter_start_task}` | `{counter_start_task}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{counter_start_task}` | `{counter_start_task}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{call_id}` | `{call_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn}` | `{cirn}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dfcx_session_id}` | `{dfcx_session_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_from}` | `{handoff_from}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_from}` | `{handoff_from}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{handoff_to}` | `{handoff_to}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{counter_next_task}` | `{counter_next_task}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{counter_next_task}` | `{counter_next_task}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{prev_cfb_dcx_action_code}` | `{prev_cfb_dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{prev_cda_dcx_action_code}` | `{prev_cda_dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_expecting_answer}` | `{is_expecting_answer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{microservice_counter}` | `{microservice_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status_changed}` | `{status_changed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{microservice_aqd_counter}` | `{microservice_aqd_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{prev_ms_dcx_action_code}` | `{prev_ms_dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status_changed}` | `{status_changed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{counter_sharp}` | `{counter_sharp}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status_changed}` | `{status_changed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{counter_sharp}` | `{counter_sharp}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_finished}` | `{is_finished}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status_changed}` | `{status_changed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{microservice_counter}` | `{microservice_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status_changed}` | `{status_changed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{microservice_aqd_counter}` | `{microservice_aqd_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{microservice_counter}` | `{microservice_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status_changed}` | `{status_changed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{microservice_aqd_counter}` | `{microservice_aqd_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{microservice_aqd_counter}` | `{microservice_aqd_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{6590_customer_answer1_id}` | `{6590_customer_answer1_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_expecting_answer}` | `{is_expecting_answer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_expecting_answer}` | `{is_expecting_answer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{dcx_action_code}` | `{dcx_action_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{6590_customer_answer1_id}` | `{6590_customer_answer1_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_type}` | `{vr_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_expecting_answer}` | `{is_expecting_answer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_expecting_answer}` | `{is_expecting_answer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status_changed}` | `{status_changed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_expecting_answer}` | `{is_expecting_answer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status_changed}` | `{status_changed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_counter}` | `{vr_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status_changed}` | `{status_changed}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_expecting_answer}` | `{is_expecting_answer}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{vr_counter}` | `{vr_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tfn}` | `{tfn}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{phone_number}` | `{phone_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tfn}` | `{tfn}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{clid}` | `{clid}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{CIRN}` | `{CIRN}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{business_type}` | `{business_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{region}` | `{region}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{region}` | `{region}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_business}` | `{is_business}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{not_eligible_for_rdam}` | `{not_eligible_for_rdam}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{not_eligible_for_rdam}` | `{not_eligible_for_rdam}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tv_sub_type}` | `{tv_sub_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{va_entry_flow}` | `{va_entry_flow}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{business_type}` | `{business_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_ccc}` | `{ivr_ccc}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{region}` | `{region}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{region}` | `{region}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebillindicator}` | `{onebillindicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_confirmation}` | `{payment_confirmation}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{payment_confirmation}` | `{payment_confirmation}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{proceed_with_ot_payment}` | `{proceed_with_ot_payment}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{identification_status}` | `{identification_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_home_phone}` | `{is_home_phone}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{proceed_with_ot_payment}` | `{proceed_with_ot_payment}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{oneBillIndicator}` | `{oneBillIndicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{oneBillIndicator}` | `{oneBillIndicator}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{special_status}` | `{special_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{eligInd}` | `{eligInd}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{eligInd}` | `{eligInd}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{webhook_success}` | `{webhook_success}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{billing_account}` | `{billing_account}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{calling_number}` | `{calling_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{brand}` | `{brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_method}` | `{auth_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_old}` | `{is_old}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{callKey}` | `{callKey}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{brand}` | `{brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{pin}` | `{pin}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status}` | `{status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status}` | `{status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_profile_data}` | `{customer_profile_data}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{caller_id}` | `{caller_id}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{otp_tns_list}` | `{otp_tns_list}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{target_otp_number}` | `{target_otp_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status}` | `{status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{target_otp_number}` | `{target_otp_number}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status}` | `{status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{callKey}` | `{callKey}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{brand}` | `{brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{otp_code}` | `{otp_code}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status}` | `{status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status}` | `{status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status}` | `{status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{callKey}` | `{callKey}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{brand}` | `{brand}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_method}` | `{auth_method}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{status}` | `{status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{tfn}` | `{tfn}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_from_ivr}` | `{lob_from_ivr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_from_ivr}` | `{lob_from_ivr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob_from_ivr}` | `{lob_from_ivr}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cirn}` | `{cirn}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_va_ban_count}` | `{ivr_va_ban_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_va_ban_count}` | `{ivr_va_ban_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_va_ban_count}` | `{ivr_va_ban_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_va_no_ban_counter}` | `{ivr_va_no_ban_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_va_ban_count}` | `{ivr_va_ban_count}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{ivr_va_no_ban_counter}` | `{ivr_va_no_ban_counter}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{order_status}` | `{order_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_action}` | `{account_action}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_siahcc}` | `{is_siahcc}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{field_work}` | `{field_work}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_work}` | `{customer_work}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_action}` | `{account_action}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{onebox_shipping_required}` | `{onebox_shipping_required}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_action}` | `{account_action}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_siahcc}` | `{is_siahcc}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_action}` | `{account_action}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_action}` | `{account_action}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{account_action}` | `{account_action}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{early_termination_penalty}` | `{early_termination_penalty}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_day_of_week}` | `{appt_day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_month_name}` | `{appt_month_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_date_of_month}` | `{appt_date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_start_time}` | `{appt_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_start_time}` | `{appt_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{shipping_changes_restricted}` | `{shipping_changes_restricted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{shipping_changes_restricted}` | `{shipping_changes_restricted}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cutoff_date}` | `{cutoff_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cutoff_time}` | `{cutoff_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_after_cutoff}` | `{is_after_cutoff}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{is_after_cutoff}` | `{is_after_cutoff}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_day_of_week}` | `{appt_day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_month_name}` | `{appt_month_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_date_of_month}` | `{appt_date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_start_time}` | `{appt_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_start_time}` | `{appt_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{language}` | `{language}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{field_work}` | `{field_work}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_day_of_week}` | `{appt_day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_month_name}` | `{appt_month_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_date_of_month}` | `{appt_date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_start_time}` | `{appt_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_start_time}` | `{appt_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_work}` | `{customer_work}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{field_work}` | `{field_work}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{field_work}` | `{field_work}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{customer_work}` | `{customer_work}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_day_of_week}` | `{appt_day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_month_name}` | `{appt_month_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_date_of_month}` | `{appt_date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_day_of_week}` | `{appt_day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_month_name}` | `{appt_month_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_date_of_month}` | `{appt_date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_start_time}` | `{appt_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_start_time}` | `{appt_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{lob}` | `{lob}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_day_of_week}` | `{appt_day_of_week}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_month_name}` | `{appt_month_name}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_date_of_month}` | `{appt_date_of_month}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_start_time}` | `{appt_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_start_time}` | `{appt_start_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{appt_end_time}` | `{appt_end_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cutoff_date}` | `{cutoff_date}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{cutoff_time}` | `{cutoff_time}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{event_type}` | `{event_type}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{auth_status}` | `{auth_status}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_eligible}` | `{mya_eligible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{mya_eligible}` | `{mya_eligible}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |
| `Variable Syntax` | `{route}` | `{route}` | Updated DFCX variable reference in Flow instructions to CXAS {} format |

## ⚙️ System Actions & Linking
| Category | Description |
|---|---|
| `Pre-processing` | Executed global text replacement: 'playbook' -> 'agent' |

## 🛠️ Manual Steps Required
The following items are not covered by this tool and must be migrated manually:
1. **Examples:** If the source app has any examples, they need to be recreated in CXAS.
2. **Flows:** If the source app has any flows, they need to be manually transitioned or implemented.
import json
import os
import statistics
from collections import defaultdict

RESULTS_FILE = "evals/simulations/public_simulations_results.json"
REPORT_MD = "cuj_simulation_eval_report.md"
ARTIFACT_MD = "/usr/local/google/home/rasachak/.gemini/jetski/brain/22920fc1-2f34-4b92-b727-d734266fc8a5/cuj_simulation_eval_report.md"

with open(RESULTS_FILE, "r", encoding="utf-8") as f:
    results = json.load(f)

total_tests = len(results)
passed_tests = sum(1 for r in results if r.get("passed", False))
failed_tests = total_tests - passed_tests
pass_rate = (passed_tests / total_tests) * 100

total_goals = 0
goals_met = 0
total_expectations = 0
expectations_met = 0
durations = []
turns_list = []

for r in results:
    durations.append(r.get("duration_s", 0))
    turns_list.append(r.get("turns", 0))
    for g in r.get("step_details", []):
        total_goals += 1
        if g.get("status") == "Completed":
            goals_met += 1
    for e in r.get("expectation_details", []):
        total_expectations += 1
        if e.get("status") == "Met":
            expectations_met += 1

goal_rate = (goals_met / total_goals) * 100 if total_goals else 0
exp_rate = (expectations_met / total_expectations) * 100 if total_expectations else 0
avg_duration = statistics.mean(durations) if durations else 0
avg_turns = statistics.mean(turns_list) if turns_list else 0

# Mapping tests to CUJs
cuj_mapping = {
    "CUJ-01: High-Speed Internet Outage & ONT Reset": [
        "sim__check_outage_active_postal_code", "sim__check_outage_none_found_sms_troubleshoot",
        "sim__troubleshoot_slow_wifi_channels", "sim__check_outage_french_active"
    ],
    "CUJ-02: Internet WiFi Password & Channel Diagnostics": [
        "sim__troubleshoot_slow_wifi_channels"
    ],
    "CUJ-03: TV & Set-Top Box Error Codes & Reboot": [
        "sim__troubleshoot_satellite_tv_error", "sim__troubleshoot_app_cache_clear", "sim__troubleshoot_tv_black_screen"
    ],
    "CUJ-04: Mobile Data Overages & Flex Plan Upgrade": [
        "sim__upgrade_mobile_plan_budget", "sim__upgrade_mobile_plan_data", "sim__upgrade_internet_speed_french"
    ],
    "CUJ-05: Mobile International Roaming Pass": [
        "sim__check_roaming_rates_us", "sim__check_roaming_rates_europe"
    ],
    "CUJ-06: Billing Disputes, Explanation & $25 Refund Cap": [
        "sim__dispute_unrecognized_streaming_charge", "sim__dispute_billing_charge_french",
        "sim__request_credit_outage_days", "sim__request_refund_overcharge_french",
        "sim__request_refund_exceeding_threshold_escalation", "sim__dispute_charge_auth_retry",
        "sim__dispute_charge_business_account_deflection"
    ],
    "CUJ-07: Account Payment Arrangements & Extension": [
        "sim__pay_bill_saved_card", "sim__pay_bill_declined_card_retry", "sim__setup_autopay_standard",
        "sim__setup_autopay_french", "sim__pay_bill_then_setup_autopay", "sim__pay_bill_past_due_amount",
        "sim__pay_bill_french_dtmf", "sim__restore_service_payment_arrangement", "sim__restore_service_already_paid",
        "sim__restore_service_standard", "sim__restore_service_french"
    ],
    "CUJ-08: Technician Appointment Scheduling & Window": [
        "sim__schedule_tech_install", "sim__reschedule_tech_appointment", "sim__cancel_tech_appointment",
        "sim__check_tech_status_standard"
    ],
    "CUJ-09: Home Phone Voicemail & Call Forwarding Setup": [
        "sim__setup_call_forwarding_phone", "sim__reset_voicemail_pin_phone", "sim__cancel_home_phone_french"
    ],
    "CUJ-10: Asymmetric Step-Up Authentication & Fraud Deflection": [
        "sim__reset_password_standard", "sim__reset_password_wrong_number_retry", "sim__reset_password_sms_escalation",
        "sim__manage_mfa_enable", "sim__manage_mfa_french_disable", "sim__manage_mfa_auth_failure",
        "sim__report_fraud_standard", "sim__report_fraud_french", "sim__report_fraud_phishing",
        "sim__report_fraud_mid_call_switch", "sim__report_fraud_sim_swap"
    ],
    "CUJ-11: Zero-Damage Warranty & Swollen Battery Protocol": [
        "sim__warranty_claim_valid_standard", "sim__warranty_claim_damaged_denial", "sim__warranty_claim_swollen_battery"
    ],
    "CUJ-12: Full French Bilingual Parity": [
        "sim__cancel_service_mobility_french", "sim__cancel_home_phone_french", "sim__dispute_billing_charge_french",
        "sim__request_refund_overcharge_french", "sim__check_outage_french_active", "sim__setup_autopay_french",
        "sim__pay_bill_french_dtmf", "sim__manage_mfa_french_disable", "sim__report_fraud_french",
        "sim__restore_service_french", "sim__upgrade_internet_speed_french", "sim__speak_immediate_french",
        "sim__speak_mid_call_tech_french"
    ],
    "CUJ-13: Unconditional Escalation & Sentiment Handoff": [
        "sim__speak_immediate_english", "sim__speak_immediate_french", "sim__speak_mid_call_billing_english",
        "sim__speak_frustrated_english", "sim__speak_mid_call_tech_french"
    ],
    "CUJ-14: Cancellation & Port-Out Mandatory Disclosures": [
        "sim__cancel_service_internet_english", "sim__cancel_service_mobility_french", "sim__port_out_number_english",
        "sim__cancel_tv_service_english", "sim__cancel_home_phone_french"
    ]
}

print("Statistics computed.")
print(f"Total: {total_tests}, Passed: {passed_tests}, Failed: {failed_tests}, Pass Rate: {pass_rate:.1f}%")
print(f"Goal Rate: {goal_rate:.1f}%, Expectation Rate: {exp_rate:.1f}%")
print(f"Avg Turns: {avg_turns:.1f}, Avg Duration: {avg_duration:.1f}s")

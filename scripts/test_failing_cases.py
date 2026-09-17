import json
import os
import sys
import yaml
from cxas_scrapi.evals.simulation_evals import SimulationEvals

APP_NAME = "projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8"
YAML_PATH = "evals/simulations/public_simulations.yaml"

TARGET_NAMES = [
    "sim__cancel_service_internet_english",
    "sim__port_out_number_english",
    "sim__speak_immediate_english",
    "sim__speak_frustrated_english",
    "sim__dispute_billing_charge_french",
    "sim__dispute_charge_auth_retry",
    "sim__pay_bill_french_keypad",
    "sim__pay_bill_declined_card_retry",
    "sim__request_refund_overcharge_french",
    "sim__request_refund_exceeding_threshold_escalation",
    "sim__check_outage_active_postal_code",
    "sim__check_tech_status_business_deflection",
    "sim__reset_password_french",
    "sim__manage_mfa_enable",
    "sim__manage_mfa_french_disable",
    "sim__manage_mfa_auth_failure",
    "sim__restore_service_standard",
    "sim__restore_service_french",
    "sim__restore_service_already_paid",
    "sim__restore_service_business_deflection",
    "sim__troubleshoot_mobile_service_french",
    "sim__upgrade_tv_package_sports"
]

with open(YAML_PATH, "r", encoding="utf-8") as f:
    all_cases = yaml.safe_load(f)

test_cases = [c for c in all_cases if c["name"] in TARGET_NAMES]
print(f"Loaded {len(test_cases)} targeted test cases.")

client = SimulationEvals(app_name=APP_NAME)
results = client.run_simulations(
    test_cases=test_cases,
    runs=1,
    parallel=2,
    verbose=False
)

total = len(results)
passed = sum(1 for r in results if r.get("passed", False))
print("\n" + "="*50)
print(f"TARGETED RE-TEST RESULTS: {passed}/{total} passed ({passed/total*100:.1f}%)")
print("="*50)

for r in results:
    status = "PASS" if r.get("passed", False) else "FAIL"
    print(f"[{status}] {r['name']} - Goals: {r.get('goals')}, Expectations: {r.get('expectations')}")
    if not r.get("passed", False):
        for exp in r.get("expectation_details", []):
            if exp.get("status") != "Met":
                print(f"   [Exp {exp.get('status')}]: {exp.get('expectation')}")
                print(f"   Justification: {exp.get('justification')}")

import json
import os
import sys
import yaml
from cxas_scrapi.evals.simulation_evals import SimulationEvals

APP_NAME = "projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8"
YAML_PATH = "evals/simulations/public_simulations.yaml"

TARGET_NAMES = [
    # 17 Failure cases noted from certification report
    "sim__cancel_tv_service_english",
    "sim__cancel_home_phone_french",
    "sim__speak_immediate_english",
    "sim__speak_immediate_french",
    "sim__speak_frustrated_english",
    "sim__speak_mid_call_tech_french",
    "sim__pay_mobility_bill_card_file",
    "sim__pay_bill_french_keypad",            # Secret Case #16
    "sim__pay_bill_declined_card_retry",
    "sim__setup_autopay_french",
    "sim__request_refund_exceeding_threshold_escalation",
    "sim__check_tech_status_standard",        # Secret Case #28
    "sim__check_ticket_status_retry_strikes",
    "sim__reset_password_wrong_number_retry",
    "sim__reset_password_pivot_billing",
    "sim__troubleshoot_satellite_tv_error",
    "sim__upgrade_mobile_plan_data",
    # Additional Secret Cases
    "sim__setup_autopay_internet_english",    # Secret Case #19
    "sim__setup_autopay_after_paying_bill",   # Secret Case #21
    "sim__check_outage_active_postal_code"    # Secret Case #25
]

with open(YAML_PATH, "r", encoding="utf-8") as f:
    all_cases = yaml.safe_load(f)

test_cases = [c for c in all_cases if c["name"] in TARGET_NAMES]
print(f"Loaded {len(test_cases)} target cases to test (3 runs each = {len(test_cases)*3} total simulations).")

client = SimulationEvals(app_name=APP_NAME)
results = client.run_simulations(
    test_cases=test_cases,
    runs=3,
    parallel=4,
    verbose=False
)

OUTPUT_FILE = "evals/simulations/certification_3runs_results.json"
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

total = len(results)
passed = sum(1 for r in results if r.get("passed", False))
pass_rate = (passed / total * 100) if total > 0 else 0

print("\n" + "="*70)
print(f"CERTIFICATION 3-RUN SIMULATION RESULTS: {passed}/{total} passed ({pass_rate:.1f}%)")
print("="*70)

case_results = {}
for r in results:
    name = r["name"]
    if name not in case_results:
        case_results[name] = []
    case_results[name].append(r)

for name in TARGET_NAMES:
    runs = case_results.get(name, [])
    p_count = sum(1 for r in runs if r.get("passed", False))
    status_str = f"{p_count}/{len(runs)} PASS" if runs else "NO RUNS"
    print(f"[{status_str}] {name}")
    for idx, r in enumerate(runs):
        if not r.get("passed", False):
            for exp in r.get("expectation_details", []):
                if exp.get("status") != "Met":
                    print(f"   Run #{idx+1} [Exp {exp.get('status')}]: {exp.get('expectation')}")
                    print(f"   Justification: {exp.get('justification')}")

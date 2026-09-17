import json
import os
import sys
import time
import yaml
from cxas_scrapi.evals.simulation_evals import SimulationEvals

APP_NAME = "projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8"
YAML_PATH = "evals/simulations/public_simulations.yaml"
OUTPUT_JSON_PATH = "evals/simulations/public_simulations_results.json"

def main():
    print(f"Loading test cases from {YAML_PATH}...")
    with open(YAML_PATH, "r", encoding="utf-8") as f:
        test_cases = yaml.safe_load(f)

    total_tests = len(test_cases)
    print(f"Loaded {total_tests} test cases.")

    print(f"Initializing SimulationEvals for app: {APP_NAME}")
    client = SimulationEvals(app_name=APP_NAME)

    start_time = time.time()
    print(f"Starting simulation run with parallel=5...")
    
    # Progress callback
    def on_progress(completed, total):
        print(f"Progress: {completed}/{total} ({completed/total*100:.1f}%)", flush=True)

    results = client.run_simulations(
        test_cases=test_cases,
        runs=1,
        parallel=5,
        verbose=False,
        progress_callback=on_progress
    )

    elapsed_time = time.time() - start_time
    print(f"\nAll simulations completed in {elapsed_time:.2f} seconds ({elapsed_time/60:.2f} minutes).", flush=True)

    # Save results
    os.makedirs(os.path.dirname(OUTPUT_JSON_PATH), exist_ok=True)
    with open(OUTPUT_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Results saved to {OUTPUT_JSON_PATH}", flush=True)

    # Summary calculations
    total_runs = len(results)
    passed_runs = sum(1 for r in results if r.get("passed", False))
    failed_runs = total_runs - passed_runs
    pass_rate = (passed_runs / total_runs * 100) if total_runs > 0 else 0

    print("\n" + "="*50)
    print("SIMULATION SUITE EXECUTION SUMMARY")
    print("="*50)
    print(f"Total Test Cases: {total_tests}")
    print(f"Total Executed Runs: {total_runs}")
    print(f"Passed: {passed_runs}")
    print(f"Failed: {failed_runs}")
    print(f"Pass Rate: {pass_rate:.1f}%")
    print("="*50)

    # Print failed cases if any
    if failed_runs > 0:
        print("\nFailed Test Cases:")
        for r in results:
            if not r.get("passed", False):
                print(f" - {r.get('name')}: Goals {r.get('goals')}, Expectations {r.get('expectations')}")
                for exp in r.get("expectation_details", []):
                    if exp.get("status") != "Met":
                        print(f"    Expectation [{exp.get('status')}]: {exp.get('expectation')}")
                        print(f"    Justification: {exp.get('justification')}")

if __name__ == "__main__":
    main()

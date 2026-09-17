import yaml
from cxas_scrapi.evals.simulation_evals import SimulationEvals

APP_NAME = "projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8"
with open("evals/simulations/public_simulations.yaml") as f:
    cases = yaml.safe_load(f)
c = [case for case in cases if case["name"] == "sim__speak_mid_call_tech_french"]
client = SimulationEvals(app_name=APP_NAME)
res = client.run_simulations(test_cases=c, runs=1, verbose=False)
print(f"[{res[0].get('name')}] passed={res[0].get('passed')}")
print(res[0].get("transcript"))
print("DETAILS:", res[0].get("expectation_details"))

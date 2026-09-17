import yaml
from cxas_scrapi.evals.simulation_evals import SimulationEvals

APP_NAME = "projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8"
with open("evals/simulations/public_simulations.yaml") as f:
    cases = yaml.safe_load(f)
c = [case for case in cases if case["name"] in ("sim__speak_immediate_english", "sim__speak_frustrated_english")]
client = SimulationEvals(app_name=APP_NAME)
res = client.run_simulations(test_cases=c, runs=1, verbose=False)
for r in res:
    print(f"[{r.get('name')}] passed={r.get('passed')}")
    print(r.get("transcript"))
    print("DETAILS:", r.get("expectation_details"))

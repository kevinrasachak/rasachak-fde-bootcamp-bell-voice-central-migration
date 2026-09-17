import json
import subprocess
import sys

APP_JSON_PATH = "cxas_app/rasachak_bell_voice_central/app.json"
CMD = [
    "uv", "run", "cxas",
    "push",
    "--app-dir", "./cxas_app/rasachak_bell_voice_central",
    "--to", "projects/fde-bootcamp/locations/us/apps/1d5bf51d-1c25-4ebd-ae25-8e6ef940b3c8",
    "--project-id", "fde-bootcamp",
    "--location", "us"
]

print("1. Updating rootAgent in app.json for remote push...")
with open(APP_JSON_PATH, "r") as f:
    app_data = json.load(f)

app_data["rootAgent"] = "M1 SessionLifecycleAndRouting"
with open(APP_JSON_PATH, "w") as f:
    json.dump(app_data, f, indent=2)

try:
    print("2. Running cxas push...")
    res = subprocess.run(CMD, capture_output=True, text=True)
    print("STDOUT:\n", res.stdout)
    if res.stderr:
        print("STDERR:\n", res.stderr)
    if res.returncode != 0:
        print(f"Push failed with exit code {res.returncode}")
        sys.exit(res.returncode)
    print("Push succeeded!")
finally:
    print("3. Restoring rootAgent in app.json for local linter compatibility...")
    app_data["rootAgent"] = "M1_SessionLifecycleAndRouting"
    with open(APP_JSON_PATH, "w") as f:
        json.dump(app_data, f, indent=2)
    print("app.json restored.")

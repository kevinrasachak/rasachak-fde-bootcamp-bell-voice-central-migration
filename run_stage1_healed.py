#!/usr/bin/env python3
import os
import sys

import cxas_scrapi.migration.structural_consolidator as sc

orig_validate = sc.validate_groupings


def healed_validate_groupings(ir, groupings, root_key):
    ir_keys = set(ir.agents.keys())
    norm_map = {
        k.lower().replace(" ", "_").replace("-", "_"): k for k in ir_keys
    }
    seen = set()
    for gname, payload in groupings.items():
        healed_members = []
        for m in payload.get("agents") or []:
            exact = (
                m
                if m in ir_keys
                else norm_map.get(
                    m.lower().replace(" ", "_").replace("-", "_")
                )
            )
            if exact and exact not in seen:
                healed_members.append(exact)
                seen.add(exact)
        payload["agents"] = healed_members
    missing = sorted(ir_keys - seen)
    if missing:
        root_g = next(
            (g for g, p in groupings.items() if p.get("is_root")),
            list(groupings.keys())[0],
        )
        groupings[root_g]["agents"].extend(missing)
    return orig_validate(ir, groupings, root_key)


sc.validate_groupings = healed_validate_groupings

# Run stage_1
skill_scripts_dir = os.path.abspath(
    ".agents/skills/cxas-dfcx-migration/scripts"
)
sys.path.insert(0, skill_scripts_dir)
import stage_1

if __name__ == "__main__":
    stage_1.main()

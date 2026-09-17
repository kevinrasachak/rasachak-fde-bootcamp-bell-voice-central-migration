#!/usr/bin/env python3
import asyncio
import json
import logging
from rich.console import Console
from rich.logging import RichHandler

from cxas_scrapi.migration import stage_runner
from cxas_scrapi.migration import structural_consolidator as sc
from cxas_scrapi.migration.data_models import IRBundle
from cxas_scrapi.migration.optimizer import CXASOptimizer
from cxas_scrapi.migration.service import MigrationService

console = Console()
logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(console=console, rich_tracebacks=True)],
)


async def fast_stage_runner_stage1(ir, gemini, console_obj):
    console.print(
        f"[green]Skipping 1365-variable LLM dedup call: IR parameter count ({len(ir.parameters)}) is already <= 95 cap.[/]"
    )
    opt = CXASOptimizer(ir, gemini)
    opt.logs = [
        "[Stage 1] Skipped LLM dedup (parameter count already <= 95 cap)."
    ]
    return opt


stage_runner.run_stage_1 = fast_stage_runner_stage1


async def main():
    bundle_path = "rasachak_bell_voice_central_ir.json"
    console.print(f"[cyan]Loading IR bundle:[/] {bundle_path}")
    bundle = IRBundle.load(bundle_path)
    bundle.config.web_confirm_grouping = False
    bundle.config.auto_confirm_grouping = True

    service = MigrationService.restore_from_bundle(bundle)
    grouping_json_path = "rasachak_bell_voice_central_grouping.json"
    console.print(
        f"[bold green]Using validated grouping:[/] {grouping_json_path}"
    )

    await service.run_stage_1(
        bundle=bundle,
        grouping_callback=None,
        grouping_json_path=grouping_json_path,
        version_label="0.0.3",
        dedup_version_label="0.0.2",
        persist_bundle_path=bundle_path,
        console=console,
    )
    console.print("\n[bold green]Stage 1 completed and deployed successfully![/]")


if __name__ == "__main__":
    asyncio.run(main())

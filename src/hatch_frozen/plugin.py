import logging
from pathlib import Path
from typing import Any
from hatchling.builders.hooks.plugin.interface import BuildHookInterface


log = logging.getLogger(__name__)


class FrozenDependenciesHook(BuildHookInterface):
    """
    A hook to add pinned dependencies to the build.
    """

    PLUGIN_NAME = "frozen"

    def initialize(self, version: str, build_data: dict[str, Any]):
        """
        Called before the build process starts.
        In this case, build_data is modified to include dependencies
        from requirements.txt.
        """
        requirements_file = "requirements.txt"
        if not Path(requirements_file).exists():
            log.warning(f"{requirements_file} not found. No dependencies injected.")
            return

        dependencies = _parse_requirements_file(requirements_file)
        build_data["dependencies"] = dependencies


def _parse_requirements_file(requirements_file: str):
    with open(requirements_file, "r") as f:
        dependencies = [
            line.strip() for line in f.readlines() if not line.strip().startswith("#")
        ]

        return dependencies

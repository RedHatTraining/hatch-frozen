import pytest
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory


@pytest.fixture
def test_project():
    # Copy the test project to a tmp dir to make every test session independent
    with TemporaryDirectory() as tmpdir:
        source_dir = Path(__file__).resolve().parent / "_utils/test_project"
        tmp_project = Path(tmpdir) / "hatch-frozen-test-project"
        shutil.copytree(source_dir, tmp_project)

        pyproject_toml = tmp_project / "pyproject.toml"
        plugin_root_dir = Path(__file__).resolve().parent.parent
        with open(pyproject_toml, "r") as f:
            content = f.read()
            new_content = content.replace(
                "<<<hatch_frozen_cwd>>>", plugin_root_dir.as_uri()
            )
        with open(pyproject_toml, "w") as f:
            f.write(new_content)

        yield tmp_project

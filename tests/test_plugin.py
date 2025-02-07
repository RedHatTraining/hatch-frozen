import email
from tempfile import TemporaryDirectory
from pathlib import Path
import zipfile
from _utils import run_hatch_build


def test_frozen_wheel(test_project):
    """
    Test that the plugin freezes the wheel by including
    the dependencies from pyproject.toml
    and the pinned dependencies from requirements.txt.
    (from tests/_utils/test_project)
    """

    run_hatch_build(cwd=test_project)

    # Extract depedencies from the wheel metadata
    wheel_path = test_project / "dist/test_app-1.0.0-py3-none-any.whl"
    metadata = _read_wheel_metadata(wheel_path)
    requires_dist = metadata.get_all("Requires-Dist") or []

    # Verify that the wheel contains:
    # - the dependencies from pyproject
    assert "requests<2.33,>=2.32" in requires_dist
    # - the pinned dependencies from requirements.txt
    assert "urllib3==2.2.2" in requires_dist


def _read_wheel_metadata(wheel_path: Path):
    with TemporaryDirectory() as temp_dir:
        with zipfile.ZipFile(wheel_path, "r") as zip_in:
            zip_in.extractall(temp_dir)

        metadata_path = next(Path(temp_dir).rglob("METADATA"))

        # The METADATA file of the wheel can be parsed with the "email" module
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = email.message_from_file(f)
            return metadata

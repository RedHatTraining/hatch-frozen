# `hatch-frozen`: A Hatch build hook plug-in for freezing dependencies

## Usage

In your `pyproject.toml` file, add `hatch-frozen` as a build requirements, then add the `[tool.hatch.build.hooks.frozen]` table.

<pre><code>
[build-system]
requires = ["hatchling>=1.24.0,<2", <b>"hatch-frozen"</b>]
build-backend = "hatchling.build"

<b>[tool.hatch.build.hooks.frozen]</b>
</code></pre>

The plug-in reads the frozen dependencies from the `requirements.txt` file of your project, so make sure this file exists.

### Example with with `uv`

1. Configure the `pyproject.toml` file as explained above.

2. Generate the `requirements.txt` file:

```shell
$ uv pip compile pyproject.toml -o requirements.txt
```

3. Build your package:

```shell
$ uv build
```

4. Clean the requirements file:

```shell
$ rm requirements.txt
```

## Hacking

The project uses `uv` as the package manager.

To run the tests, use:

    uv run pytest

To verify the code style, use:

    uvx ruff check

### Releasing

To release a new version of the package, bump the version in `pyproject.toml` and create and push a new git tag.
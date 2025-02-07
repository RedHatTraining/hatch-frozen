from hatchling.plugin import hookimpl

from hatch_frozen.plugin import FrozenDependenciesHook


@hookimpl
def hatch_register_build_hook():
    return FrozenDependenciesHook


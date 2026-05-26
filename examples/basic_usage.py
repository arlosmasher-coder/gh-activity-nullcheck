#!/usr/bin/env python3
"""Basic usage example for gh_activity_nullcheck."""

from gh_activity_nullcheck import GhActivityNullcheck, GhActivityNullcheckOptions


def main() -> None:
    # Create with default options
    instance = GhActivityNullcheck()
    result = instance.run()
    print(f"Default run: success={result.success}, data={result.data}")

    # Create with custom options
    options = GhActivityNullcheckOptions(verbose=True)
    instance = GhActivityNullcheck(options)
    result = instance.run()
    print(f"Verbose run: success={result.success}, data={result.data}")


if __name__ == "__main__":
    main()

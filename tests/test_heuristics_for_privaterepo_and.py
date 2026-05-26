"""Tests for gh_activity_nullcheck."""

from gh_activity_nullcheck import GhActivityNullcheck, GhActivityNullcheckOptions


class TestGhActivityNullcheck:
    def test_create_instance_with_defaults(self) -> None:
        instance = GhActivityNullcheck()
        assert instance is not None

    def test_create_instance_with_options(self) -> None:
        options = GhActivityNullcheckOptions(verbose=True)
        instance = GhActivityNullcheck(options)
        assert instance.options.verbose is True

    def test_run_successfully(self) -> None:
        instance = GhActivityNullcheck()
        result = instance.run()
        assert result.success is True
        assert result.data is not None

    def test_run_returns_result_type(self) -> None:
        instance = GhActivityNullcheck()
        result = instance.run()
        assert result.error is None

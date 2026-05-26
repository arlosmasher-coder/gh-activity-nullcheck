# gh_activity_nullcheck

Detect missing GitHub activity signals and explain likely configuration or visibility causes.

## Installation

```bash
pip install gh_activity_nullcheck
```

## Quick Start

```python
from gh_activity_nullcheck import GhActivityNullcheck

instance = GhActivityNullcheck()
result = instance.run()
print(result)
```

## Features

- Heuristics for private-repo and org-visibility scenarios
- Confidence-scored explanations and remediation hints
- Batch processing for lists of usernames
- Export to CSV/JSON for downstream systems

## API Reference

### `GhActivityNullcheck`

#### Constructor

```python
GhActivityNullcheck(options: GhActivityNullcheckOptions | None = None)
```

#### Methods

- `run()` - Execute the main operation. Returns `GhActivityNullcheckResult`.

## Development

```bash
# Install with dev dependencies
make install

# Run tests
make test

# Lint and type-check
make lint

# Format code
make format

# Build
make build
```

## Publishing

1. Update version in `pyproject.toml` and `src/gh_activity_nullcheck/__init__.py`
2. Create a GitHub release with tag `v0.x.0`
3. The GitHub Action will automatically publish to PyPI

## License

MIT

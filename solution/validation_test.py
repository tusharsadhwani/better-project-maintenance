import ast
from pathlib import Path
import pytest


def get_python_files():
    """Returns all python files in the codebase"""
    return Path(__file__).parent.parent.glob("src/**/*.py")


def raise_issue(file, line, message):
    raise pytest.fail(f"File {file} on line {line}: {message}")


def test_api_version_prefix():
    """If `app.get('/api/...')` is called, it should have a `/v1` prefix."""
    for file in get_python_files():
        tree = ast.parse(file.read_text())

        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Constant)
                and isinstance(node.value, str)
                and node.value.startswith("/api")
                and not node.value.startswith("/api/v1")
            ):
                raise_issue(file, node.lineno, "api endpoint missing version prefix")

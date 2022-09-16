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


class ModelVerifier(ast.NodeVisitor):
    def __init__(self, file) -> None:
        self.file = file

    def visit_ClassDef(self, node):
        """Ensures every class extending `BaseModel` has an id field (UUID)"""
        if node.bases[0].id == "BaseModel":
            properties = [item for item in node.body if isinstance(item, ast.AnnAssign)]
            for prop in properties:
                if (
                    isinstance(prop.annotation, ast.Name)
                    and prop.annotation.id == "UUID"
                ):
                    break
            else:
                raise_issue(self.file, node.lineno, "UUID field not present in model")


def test_model_must_use_uuid():
    for file in get_python_files():
        tree = ast.parse(file.read_text())
        ModelVerifier(file).visit(tree)

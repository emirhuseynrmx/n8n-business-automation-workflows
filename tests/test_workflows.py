from __future__ import annotations

import json
from pathlib import Path


def workflow_paths() -> list[Path]:
    return sorted(Path("workflows").glob("*.json"))


def test_workflow_files_exist() -> None:
    assert len(workflow_paths()) >= 4


def test_workflows_have_required_structure() -> None:
    for path in workflow_paths():
        workflow = json.loads(path.read_text(encoding="utf-8"))

        assert workflow["name"]
        assert workflow["active"] is False
        assert workflow["nodes"]
        assert workflow["connections"]
        assert workflow["meta"]["templateNote"]


def test_node_ids_and_names_are_unique() -> None:
    for path in workflow_paths():
        workflow = json.loads(path.read_text(encoding="utf-8"))
        ids = [node["id"] for node in workflow["nodes"]]
        names = [node["name"] for node in workflow["nodes"]]

        assert len(ids) == len(set(ids)), path
        assert len(names) == len(set(names)), path

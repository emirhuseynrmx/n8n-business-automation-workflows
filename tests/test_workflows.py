from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class WorkflowNode(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: str
    name: str
    type: str
    typeVersion: int | float
    position: list[int]
    parameters: dict[str, Any] = Field(default_factory=dict)


class WorkflowMeta(BaseModel):
    model_config = ConfigDict(extra="allow")

    templateNote: str


class N8nWorkflow(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str
    active: bool
    nodes: list[WorkflowNode]
    connections: dict[str, Any]
    meta: WorkflowMeta


class CatalogTemplate(BaseModel):
    file: str
    use_case: str
    requires: list[str]


class WorkflowCatalog(BaseModel):
    category: str
    templates: list[CatalogTemplate]


def workflow_paths() -> list[Path]:
    return sorted(Path("workflows").glob("*.json"))


def test_workflow_files_exist() -> None:
    assert len(workflow_paths()) >= 4


def test_workflows_have_required_structure() -> None:
    for path in workflow_paths():
        workflow = json.loads(path.read_text(encoding="utf-8"))
        parsed = N8nWorkflow.model_validate(workflow)

        assert parsed.name
        assert parsed.active is False
        assert parsed.nodes
        assert parsed.connections
        assert parsed.meta.templateNote


def test_node_ids_and_names_are_unique() -> None:
    for path in workflow_paths():
        workflow = json.loads(path.read_text(encoding="utf-8"))
        ids = [node["id"] for node in workflow["nodes"]]
        names = [node["name"] for node in workflow["nodes"]]

        assert len(ids) == len(set(ids)), path
        assert len(names) == len(set(names)), path


def test_workflow_catalog_references_existing_templates() -> None:
    catalog = WorkflowCatalog.model_validate_json(
        Path("workflow_catalog.json").read_text(encoding="utf-8")
    )
    existing = {str(path).replace("\\", "/") for path in workflow_paths()}

    assert catalog.category == "small-business-automation"
    assert {template.file for template in catalog.templates} == existing
    assert all(template.use_case for template in catalog.templates)

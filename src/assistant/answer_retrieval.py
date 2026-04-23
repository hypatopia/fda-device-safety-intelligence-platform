from __future__ import annotations

from pathlib import Path


KNOWLEDGE_BASE_PATH = "docs/fda_reporting_knowledge_base.md"


def load_knowledge_base(path: str = KNOWLEDGE_BASE_PATH) -> str:
    file_path = Path(path)
    if not file_path.exists():
        return ""
    return file_path.read_text(encoding="utf-8")


def answer_report_field_help(question: str) -> dict:
    kb = load_knowledge_base()
    if not kb:
        return {
            "answer_type": "report_field_help",
            "status": "no_data",
            "summary": "Reporting knowledge base is not available yet.",
            "data": [],
            "sources": [KNOWLEDGE_BASE_PATH],
        }

    return {
        "answer_type": "report_field_help",
        "status": "ok",
        "summary": (
            "This question falls under FDA reporting field guidance. "
            "The current copilot can explain field purpose, likely source information needs, "
            "and reporting context, but it does not complete or submit reports."
        ),
        "data": [
            {"topic": "field_guidance", "note": "Use reporter records and workflow context for actual report values."},
            {"topic": "limitations", "note": "Public FDA materials explain expectations, not organization-specific source values."},
        ],
        "sources": [KNOWLEDGE_BASE_PATH],
    }


def answer_reporting_workflow_help(question: str) -> dict:
    kb = load_knowledge_base()
    if not kb:
        return {
            "answer_type": "reporting_workflow_help",
            "status": "no_data",
            "summary": "Reporting workflow guidance is not available yet.",
            "data": [],
            "sources": [KNOWLEDGE_BASE_PATH],
        }

    return {
        "answer_type": "reporting_workflow_help",
        "status": "ok",
        "summary": (
            "The current reporting workflow guidance covers MDR as a postmarket surveillance process, "
            "the distinction between mandatory and voluntary reporters, MedWatch form concepts, "
            "and eMDR as an electronic reporting pathway."
        ),
        "data": [
            {"topic": "mandatory_vs_voluntary", "note": "Mandatory and voluntary reporting paths are different and should not be confused."},
            {"topic": "medwatch", "note": "MedWatch forms support safety reporting workflows."},
            {"topic": "emdr", "note": "eMDR supports electronic medical device reporting workflows for mandatory reporters."},
        ],
        "sources": [KNOWLEDGE_BASE_PATH],
    }
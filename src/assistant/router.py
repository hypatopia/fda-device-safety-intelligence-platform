from __future__ import annotations


def classify_question(question: str) -> str:
    q = question.strip().lower()

    problem_keywords = ["device problem", "problem type", "trend", "trending", "event pattern"]
    manufacturer_keywords = ["manufacturer", "manufacturers", "highest event", "summary"]
    field_keywords = ["field", "section", "what does this field mean", "report field"]
    workflow_keywords = ["report", "reporting", "medwatch", "mdr", "emdr", "workflow", "submit"]

    if any(k in q for k in problem_keywords):
        return "device_problem_trend"

    if any(k in q for k in manufacturer_keywords):
        return "manufacturer_summary"

    if any(k in q for k in field_keywords):
        return "report_field_help"

    if any(k in q for k in workflow_keywords):
        return "reporting_workflow_help"

    return "unsupported"
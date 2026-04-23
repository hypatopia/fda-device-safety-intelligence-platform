from src.assistant.router import classify_question
from src.assistant.format_response import format_response


def test_classify_question():
    assert classify_question("Which device problem types are trending highest?") == "device_problem_trend"
    assert classify_question("Which manufacturers have the highest event counts?") == "manufacturer_summary"
    assert classify_question("What does this report field mean?") == "report_field_help"
    assert classify_question("How do I report through MedWatch or MDR?") == "reporting_workflow_help"
    assert classify_question("Do something completely unrelated") == "unsupported"


def test_format_response():
    payload = {
        "answer_type": "device_problem_trend",
        "status": "ok",
        "summary": "Example summary.",
        "data": [{"device_problem": "battery issue", "event_count": 10}],
        "sources": ["data/processed/device_problem_year_summary.csv"],
    }
    text = format_response(payload)
    assert "Answer type: device_problem_trend" in text
    assert "Example summary." in text
    assert "data/processed/device_problem_year_summary.csv" in text
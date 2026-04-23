from __future__ import annotations

from src.assistant.router import classify_question
from src.assistant.answer_numeric import answer_device_problem_trend, answer_manufacturer_summary
from src.assistant.answer_retrieval import answer_report_field_help, answer_reporting_workflow_help
from src.assistant.format_response import format_response


def answer_question(question: str) -> str:
    question_type = classify_question(question)

    if question_type == "device_problem_trend":
        payload = answer_device_problem_trend()
    elif question_type == "manufacturer_summary":
        payload = answer_manufacturer_summary()
    elif question_type == "report_field_help":
        payload = answer_report_field_help(question)
    elif question_type == "reporting_workflow_help":
        payload = answer_reporting_workflow_help(question)
    else:
        payload = {
            "answer_type": "unsupported",
            "status": "unsupported",
            "summary": (
                "This question is outside the current Week 5 MVP. "
                "Supported categories are device problem trends, manufacturer summaries, "
                "reporting field help, and reporting workflow guidance."
            ),
            "data": [],
            "sources": [],
        }

    return format_response(payload)


if __name__ == "__main__":
    sample_questions = [
        "Which device problem types are trending highest?",
        "Which manufacturers have the highest event counts?",
        "What does this FDA reporting field mean?",
        "What is the difference between MedWatch and mandatory MDR reporting?",
        "Can you predict patient-level risk?",
    ]

    for q in sample_questions:
        print("=" * 80)
        print(f"Question: {q}")
        print(answer_question(q))
        print()
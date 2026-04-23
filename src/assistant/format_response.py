from __future__ import annotations


def format_response(payload: dict) -> str:
    answer_type = payload.get("answer_type", "unknown")
    status = payload.get("status", "unknown")
    summary = payload.get("summary", "")
    data = payload.get("data", [])
    sources = payload.get("sources", [])

    lines = []
    lines.append(f"Answer type: {answer_type}")
    lines.append(f"Status: {status}")
    lines.append("")
    lines.append(summary)

    if data:
        lines.append("")
        lines.append("Details:")
        for item in data[:10]:
            lines.append(f"- {item}")

    if sources:
        lines.append("")
        lines.append("Sources:")
        for source in sources:
            lines.append(f"- {source}")

    return "\n".join(lines)
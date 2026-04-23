from pathlib import Path

from src.transform.clean_device_events import clean_device_events
from src.transform.clean_device_problems import clean_device_problems
from src.transform.clean_reporting_guidance import clean_reporting_guidance
from src.analytics.build_summaries import main as build_summaries_main


def main() -> None:
    Path("data/processed").mkdir(parents=True, exist_ok=True)

    events = clean_device_events()
    if not events.empty:
        events.to_csv("data/processed/device_events_clean.csv", index=False)

    problems = clean_device_problems()
    if not problems.empty:
        problems.to_csv("data/processed/device_problems_clean.csv", index=False)

    guidance = clean_reporting_guidance()
    if not guidance.empty:
        guidance.to_csv("data/processed/reporting_workflow_dictionary_seed.csv", index=False)

    build_summaries_main()
    print("Week 4 pipeline finished.")


if __name__ == "__main__":
    main()
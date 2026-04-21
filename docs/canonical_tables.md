# Canonical Tables Plan

## 1. device_events_clean
Grain: one row per event report
Purpose: structured event analysis
Candidate columns:
- report_id
- manufacturer_name
- report_year
- event_date
- device_name
- device_type_or_code
- event_type
- device_problem
- patient_problem
- report_source
- source_name
- extract_date

## 2. manufacturer_year_summary
Grain: one row per manufacturer per year
Purpose: comparison, benchmarking, trend analysis
Candidate columns:
- manufacturer_name
- report_year
- event_count
- serious_event_count_if_available
- device_problem_counts
- normalized_fields_if_later_available

## 3. device_problem_year_summary
Grain: one row per device problem per year
Purpose: trend analysis
Candidate columns:
- device_problem
- report_year
- event_count
- serious_event_count_if_available

## 4. report_field_dictionary
Grain: one row per reporting field or reporting concept
Purpose: reporting copilot support
Candidate columns:
- form_name
- section_name
- field_name
- field_definition
- expected_source
- workflow_type
- validation_notes

## 5. reporting_workflow_dictionary
Grain: one row per workflow concept
Purpose: reporting guidance support
Candidate columns:
- workflow_name
- workflow_type
- reporter_type
- description
- related_form
- notes
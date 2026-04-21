# FDA Schema Notes

## Why this document exists
This file tracks the practical schema and interpretation issues that affect ingestion, analytics, and assistant behavior.

## Core Source Groups
1. MAUDE / MDR event data
2. downloadable MDR data files
3. MedWatch forms and instructions
4. eMDR workflow guidance
5. MDR regulatory and reporting context

## Initial Data Modeling Assumptions
- The MVP focuses on device-event safety intelligence and reporting support.
- Manufacturer-year will be a core analytical grain.
- Device-problem-year will be a secondary comparison grain.
- Event-level data and reporting-guidance text should remain separate canonical sources.
- Reporting instructions and workflow pages will be treated as text knowledge sources rather than structured analytics tables.

## Known Risks
- Public event data may contain duplicate-looking reports or varying completeness.
- Field names and downloadable file structures may vary by source family.
- Reporting workflows differ for voluntary vs mandatory reporters.
- eMDR guidance is especially relevant for manufacturers/importers and should not be confused with all MedWatch use cases.
- Public FDA data supports aggregate and workflow intelligence, not causal adjudication or clinical decision-making.

## Canonical Entity Concepts
- report
- manufacturer
- device
- report year
- event type
- device problem
- patient problem
- reporting form / workflow concept
- reporting field / instruction item

## Planned Canonical Tables
- device_events_clean
- manufacturer_year_summary
- device_problem_year_summary
- report_field_dictionary
- reporting_workflow_dictionary

## Notes to Update in Week 3+
- exact raw file names
- exact join keys
- field-type normalization rules
- duplicate/record-link logic
- date parsing rules
- voluntary vs mandatory workflow distinctions
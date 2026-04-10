# FDA Device Safety Intelligence Platform

An analytics and reporting copilot built on FDA public safety data, MAUDE event records, MDR data files, and MedWatch / eMDR reporting guidance.

## Project Overview
This project is designed to support two related workflows:

1. **Safety Intelligence Assistant**
   - answer grounded questions about device event patterns, problem types, trends, severity, device categories, and postmarket safety concepts

2. **Reporting Copilot**
   - help users interpret FDA reporting concepts, MedWatch / MDR workflows, field expectations, and identify missing or inconsistent draft information before reporting

## Why This Project Matters
Medical device safety work often requires both analytics and reporting discipline. FDA public data supports trend analysis, event review, historical benchmarking, and understanding of device safety reporting structures. This project is intended to turn those public resources into a practical assistant and analytics platform.

## MVP Scope
The first version will focus on:
- MAUDE / MDR public event data
- reporting and safety guidance from FDA public materials
- MedWatch / MDR workflow support
- structured analytics for device event and problem trends

## Planned Core Modules
- data ingestion and schema standardization
- analytical tables for device events, safety summaries, and trend outputs
- hybrid assistant for structured questions and reporting guidance
- reporting field / workflow dictionary and source-mapping support
- benchmark forecasting layer for aggregate trend modeling

## Initial Questions the Platform Should Answer
- Which device problem types have increased or decreased over time?
- How do reported device events vary by manufacturer, device category, or year?
- Which event types are linked to more serious outcomes?
- What does a specific reporting field or reporting concept mean?
- What source information is likely needed for a specific report section?
- What obvious gaps or inconsistencies appear in a draft reporting workflow?

## What This Project Is Not
- not an autonomous filing/submission tool
- not a device-level causal adjudication engine
- not a replacement for regulatory or legal review

## Repository Structure
- `src/` for ingestion, transformation, analytics, assistant, and reporting logic
- `data/` for raw, interim, and processed datasets
- `docs/` for schema notes, field dictionaries, and source-mapping guides
- `app/` for future interface components
- `tests/` for validation and smoke tests
- `reports/` for generated summaries and outputs

## Current Status
- Step 1 setup and repository scaffolding. 
- Step 2 add FDA source inventory and schema planning artifacts. 

## Author
Marzieh Eini

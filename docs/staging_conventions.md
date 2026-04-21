# Staging Conventions

## Purpose
This file defines the intermediate staging conventions used before canonical tables are built.

## Raw vs Interim vs Processed
- `data/raw/` stores original downloaded or extracted source files.
- `data/interim/` stores minimally cleaned or standardized source-specific outputs.
- `data/processed/` stores canonical tables and modeling-ready data products.

## Interim Naming Convention
Use the format:

`<source_group>__<domain_scope>__<time_scope>__<object_name>.csv`

Examples:
- `event_data__medical_devices__2015_present__raw_event_records.csv`
- `reporting__medical_devices__current__field_dictionary_seed.csv`

## Column Naming Convention
- lowercase only
- words separated by underscores
- no spaces
- no punctuation
- normalize all raw column names before downstream logic

## Metadata to Track
Every interim table should have:
- source_name
- extract_date
- source_file_name
- schema_version_note
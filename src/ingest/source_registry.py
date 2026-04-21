from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class SourceRecord:
    source_name: str
    source_group: str
    source_type: str
    page_name: str
    domain_scope: str
    time_scope: str
    update_frequency: str
    planned_use: str
    priority: str
    notes: str


def get_sources() -> List[SourceRecord]:
    return [
        SourceRecord(
            source_name="maude_database",
            source_group="event_data",
            source_type="data_page",
            page_name="FDA MAUDE database",
            domain_scope="Medical Devices",
            time_scope="recent searchable window plus historical context",
            update_frequency="periodic",
            planned_use="device-event analytics and trend exploration",
            priority="high",
            notes="Core public adverse-event source for medical devices",
        ),
        SourceRecord(
            source_name="mdr_data_files",
            source_group="event_data",
            source_type="data_files",
            page_name="FDA MDR data files",
            domain_scope="Medical Devices",
            time_scope="historical downloadable data",
            update_frequency="periodic",
            planned_use="structured offline event analysis",
            priority="high",
            notes="Primary downloadable reporting-data source",
        ),
        SourceRecord(
            source_name="medwatch_forms_and_instructions",
            source_group="reporting",
            source_type="forms_page",
            page_name="FDA MedWatch forms and instructions",
            domain_scope="Medical Devices",
            time_scope="current forms and instructions",
            update_frequency="as updated",
            planned_use="reporting copilot guidance and field interpretation",
            priority="high",
            notes="Core reporting forms source",
        ),
        SourceRecord(
            source_name="emdr_guidance",
            source_group="reporting",
            source_type="guidance_page",
            page_name="FDA eMDR electronic reporting guidance",
            domain_scope="Medical Devices",
            time_scope="current workflow guidance",
            update_frequency="as updated",
            planned_use="electronic reporting workflow support",
            priority="high",
            notes="Important for manufacturer and importer electronic workflows",
        ),
    ]
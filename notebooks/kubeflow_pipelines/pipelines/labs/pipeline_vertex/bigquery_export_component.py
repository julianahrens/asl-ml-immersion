from typing import NamedTuple

from google_cloud_pipeline_components.types.artifact_types import BQTable
from kfp.v2.dsl import Artifact, Input, component


# pylint: disable=unused-argument
@component(
    base_image="python:3.8",
    output_component_file="bigquery_export_component.yaml",
    packages_to_install=["google-cloud-bigquery"],
)
def bigquery_export(
    table: Input[Artifact],
    destination_uri: str,
    location: str = "US",
):
    # pylint: disable=import-outside-toplevel
    from google.cloud import bigquery

    client = bigquery.Client()
    dataset_ref = bigquery.DatasetReference(
        table.metadata["projectId"], table.metadata["datasetId"]
    )
    table_ref = dataset_ref.table(table.metadata["tableId"])

    extract_job = client.extract_table(
        table_ref,
        destination_uri,
        # Location must match that of the source table.
        location=location,
    )  # API request
    extract_job.result()

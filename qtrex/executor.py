"""Implementation for the base and concrete query executors."""


from typing import Protocol

from google.api_core.exceptions import BadRequest, GoogleAPICallError
from google.cloud import bigquery
from pandas import DataFrame

from qtrex.models import QueryRef, QueryResult
from qtrex.errors import ExecutionError


def get_df_from_bigquery_job(job: bigquery.QueryJob) -> DataFrame:
    """Extract pandas dataframe from bigquery job.

    Args:
        job (google.cloud.bigquery.QueryJob): Job

    Returns:
        pandas.DataFrame
    """
    return job.to_dataframe()


class Executor(Protocol):  # pragma: no-cover
    """Protocol for execution query templates against database engines."""

    def execute(self, query: QueryRef, dry_run: bool = False) -> QueryResult:
        """Execute a query reference.

        Args:
            query (qtrex.models.QueryRef): Query reference
            dry_run (bool): Dry run the query

        Returns:
            qtrex.models.QueryResult

        Raises:
            qtrex.errors.ExecutionError
        """


class BigQueryExecutor:
    """Implements the Executor protocol for BigQuery client."""

    def __init__(self) -> None:
        """Instantiate BigQueryExecutor.

        Args:
            location (str): GCP Location
        """
        self.__bq = bigquery.Client()

    def execute(self, query: QueryRef, dry_run: bool = False) -> QueryResult:
        """Execute a query against BigQuery.

        Args:
            query (qtrex.models.QueryRef): Rendered query template to execute.
            dry_run (bool): Dry run query

        Returns:
            qtrex.models.QueryResult

        Raises:
            qtrex.errors.ExecutionError
        """
        job_config = bigquery.QueryJobConfig(
            dry_run=dry_run,
        )

        try:
            job = self.__bq.query(query.template, job_config=job_config)

            if not dry_run:
                job.result()

            return QueryResult(
                query_ref=query,
                df=get_df_from_bigquery_job(job) if not dry_run else None,
            )
        except (GoogleAPICallError, BadRequest) as err:
            return QueryResult(
                query_ref=query,
                error=ExecutionError(
                    caused_by=err, message=f"failed to execute query {query.name}"
                ),
            )

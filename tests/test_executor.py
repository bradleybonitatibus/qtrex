"""Test code for executors."""
from pytest import fixture

from qtrex.errors import ExecutionError
from qtrex.executor import BigQueryExecutor
from qtrex.models import QueryRef


@fixture
def valid_bq_query_ref() -> QueryRef:
    return QueryRef(
        "/tmp/1/valid_query.sql",
        "SELECT SUM(x) AS value FROM UNNEST([1,2,3,4,5]) AS x",
        "valid_query.sql",
    )


@fixture
def invalid_query_ref() -> QueryRef:
    return QueryRef("/tmp/bad.sql", "SELECT ALL THE ROWS FROM MY TABLE", "bad.sql")


def test_bigquery_executor_can_dry(valid_bq_query_ref):
    ex = BigQueryExecutor()

    res = ex.execute(valid_bq_query_ref, dry_run=True)
    assert res.df is None
    assert res.error is None


def test_bigquery_executor_can_execute_succesfully(valid_bq_query_ref):
    ex = BigQueryExecutor()
    res = ex.execute(valid_bq_query_ref, dry_run=False)
    assert res.df is not None
    assert len(res.df) > 0
    assert res.error is None


def test_bigquery_executor_returns_error_in_result_with_invalid_query(
    invalid_query_ref,
) -> None:
    ex = BigQueryExecutor()
    res = ex.execute(invalid_query_ref)
    assert res.error is not None
    assert isinstance(res.error, ExecutionError)

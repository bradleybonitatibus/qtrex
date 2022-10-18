"""Module to test the data qtrex datamodels."""
import pytest

from dataclasses import FrozenInstanceError

from qtrex.models import QueryRef, QueryResult


def test_query_ref_is_immutable() -> None:
    ref = QueryRef("myfile.sql", "SELECT NOW()", "myfile.sql")
    with pytest.raises(FrozenInstanceError):
        ref.filename = "test for exception"


def test_query_result_is_immutable() -> None:
    ref = QueryRef("myfile.sql", "SELECT NOW()", "myfile.sql")
    res = QueryResult(ref)

    with pytest.raises(FrozenInstanceError):
        res.error = "test for exception"

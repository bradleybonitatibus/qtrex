"""Error module tests."""

from qtrex.errors import BaseQtrexException


def test_qtrex_error_surfaces_wrapped_error() -> None:
    s = ValueError("some bad value")

    q_error = BaseQtrexException(caused_by=s)

    assert q_error.caused_by == s

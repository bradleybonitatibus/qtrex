"""Data models for qtrex."""
from typing import Optional
from dataclasses import dataclass

import pandas


@dataclass(frozen=True)
class QueryRef:
    """QueryRef represents a reference to a query template and it's contents.

    The name of a query_ref is associated with the file name without the fully
    qualified path.
    For example, /tmp/proj/my_query.sql will be have the `name` of
    `my_query.sql`, `filename` of `/tmp/proj/my_query.sql` and `contents`
    will contain the file contents.
    """

    filename: str
    template: str
    name: str


@dataclass(frozen=True, slots=True)
class QueryResult:
    """QueryResult is returned from the execution engine that runs the query.

    It will contain the `query_ref`, a `df` if results are returned from
    the query, and an exception if one is returned.
    """

    query_ref: QueryRef
    df: Optional[pandas.DataFrame] = None
    error: Optional[Exception] = None

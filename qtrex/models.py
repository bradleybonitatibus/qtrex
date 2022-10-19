# Copyright 2022 Bradley Bonitatibus

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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


@dataclass(frozen=True)
class QueryResult:
    """QueryResult is returned from the execution engine that runs the query.

    It will contain the `query_ref`, a `df` if results are returned from
    the query, and an exception if one is returned.
    """

    query_ref: QueryRef
    df: Optional[pandas.DataFrame] = None
    error: Optional[Exception] = None

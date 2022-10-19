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

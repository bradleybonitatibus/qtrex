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

"""Shared test fixtures."""
from typing import TextIO, Sequence
from unittest import mock

from pytest import fixture

from qtrex.models import QueryRef
from qtrex.store import Store
from qtrex.config import BaseConfig, YAMLConfig


@fixture
def mock_yaml_fixture() -> TextIO:
    """mock_yaml_fixture builds and returns a TextIO interface with sample YAML data."""
    with mock.patch(
        "{0}.open".format(__name__),
        create=True,
        new_callable=mock.mock_open(
            read_data="""
            params:
                -   key: my_key
                    value: [1, 2, 3]
            """
        ),
    ) as f:
        return f


@fixture
def invalid_top_level_config_fixture() -> TextIO:
    """Invalid top level config for YAML format."""
    with mock.patch(
        "{0}.open".format(__name__),
        create=True,
        new_callable=mock.mock_open(
            read_data="""
            template_me:
                -   key: my_key
                    value: [1, 2, 3]
            """
        ),
    ) as f:
        return f


@fixture
def invalid_key_valid_pair_yaml_fixture() -> TextIO:
    """Invalid key value params for YAML format."""
    with mock.patch(
        "{0}.open".format(__name__),
        create=True,
        new_callable=mock.mock_open(
            read_data="""
            params:
                -   job: teacher
            """
        ),
    ) as f:
        return f


@fixture
def mock_empty_yaml_fixture() -> TextIO:
    """Empty template params for YAML format."""
    with mock.patch(
        "{0}.open".format(__name__),
        create=True,
        new_callable=mock.mock_open(
            read_data="""
            params: []
            """
        ),
    ) as f:
        return f


@fixture
def mock_query_ref() -> QueryRef:
    """Fixture for QueryRef."""
    return QueryRef(
        "/mnt/test1.sql",
        "SELECT * FROM UNNEST({{ params.test_array_key }})",
        "test1.sql",
    )


@fixture
def mock_query_store(mock_query_ref) -> Store:
    store = Store()
    store[mock_query_ref.name] = mock_query_ref
    store["test2.sql"] = QueryRef(
        "/tmp/qtrex/test.sql", "SELECT {{ params.test_string_key }}", "test2.sql"
    )

    return store


@fixture
def mock_config_fixture() -> BaseConfig:
    with mock.patch(
        "{0}.open".format(__name__),
        create=True,
        new_callable=mock.mock_open(
            read_data="""
            params:
                - key: test_string_key
                  value: "string_value"
                - key: test_array_key
                  value: [1,2,3]
                - key: test_dict_key
                  value:
                    first: 1
                    two: 2
                    three: 3
            """
        ),
    ) as f:
        return YAMLConfig(f)


@fixture
def mock_query_file() -> TextIO:
    with mock.patch(
        "{0}.open".format(__name__),
        create=True,
        new_callable=mock.mock_open(
            read_data="""
            SELECT {{ params.test_string_key }}, {{ params.test_dict_key.first }}
            FROM UNNEST({{ params.test_array }})
            """
        ),
    ) as f:
        return f

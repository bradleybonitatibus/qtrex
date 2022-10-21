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
import os

from qtrex.models import QueryRef
from qtrex.store import Store


def test_store_supports_index_accessor_methods(mock_query_ref: QueryRef) -> None:
    store = Store()
    store[mock_query_ref.name] = mock_query_ref
    assert store[mock_query_ref.name] == mock_query_ref


def test_store_can_iterate_through_all_query_ref(mock_query_store: Store) -> None:
    assert len(mock_query_store) != 0
    for r in mock_query_store:
        assert r.filename is not None


def test_store_can_get_put_and_delete(mock_query_store: Store) -> None:
    store = mock_query_store
    assert store.get("some_random_key") is None

    store.put(QueryRef("/mnt/query.sql", "SELECT * FROM my_table", "query.sql"))
    assert store.get("query.sql") is not None
    store.delete("query.sql")
    assert store.get("query.sql") is None


def test_store_can_load_from_path(mock_config_fixture) -> None:
    root = os.path.join(os.path.dirname(__file__), "testdata")
    store = Store.from_path(mock_config_fixture, root)
    assert len(store) == 2
    store = Store.from_path(mock_config_fixture, root, ext=".j2")
    assert len(store) == 1

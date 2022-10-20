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

"""Store is responsible for storing in-memory representation for query templates."""

from typing import Dict, Generator, Optional

from qtrex.models import QueryRef


class Store:
    """Container class to efficently store QueryRef entities."""

    def __init__(self) -> None:
        """Instantiate an empty store."""
        self.__data: Dict[str, QueryRef] = {}

    def __setitem__(self, key: str, value: QueryRef) -> None:
        """Set or overwrite a QueryRef key.

        Args:
            key (str): QueryRef key
            value (QueryRef): Query reference
        """
        self.__data[key] = value

    def __getitem__(self, key: str) -> QueryRef:
        """Get a QueryRef by it's key.

        Args:
            key (str): QueryRef key

        Returns:
            QueryRef

        Raises:
            KeyError
                when key does not exist
        """
        return self.__data[key]

    def __iter__(self) -> Generator[QueryRef, None, None]:
        """Implementa iterator behaviour to iterate through all QueryRef.

        Yields:
            QueryRef
        """
        for _, query_ref in self.__data.items():
            yield query_ref

    def __len__(self) -> int:
        """Return the number of elements in the store.

        Returns:
            int
        """
        return len(self.__data)

    def put(self, query: QueryRef) -> None:
        """Put query into container.

        By default, the key to lookup the QueryRef later will be the query.name.

        Args:
            query (QueryRef): Query reference
        """
        self.__data[query.name] = query

    def get(self, query_name: str) -> Optional[QueryRef]:
        """Get a QueryRef by it's name, or None if does not exist.

        Args:
            query_name (str): Name of query to retrieve.

        Returns:
            Optional[QueryRef]
        """
        return self.__data.get(query_name)

    def delete(self, query_name: str) -> None:
        """Deletes a query from the Store.

        Args:
            query_name (str): QueryRef name
        """
        del self.__data[query_name]

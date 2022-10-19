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

"""Config loads template configuration and provides the interface for implementing custom config."""
from typing import Dict, Any, TextIO
from abc import ABC, abstractmethod

import yaml

from qtrex.errors import InvalidConfig

REQUIRED_KEYS = {"params"}


def has_all_required_config_keys(data: dict) -> bool:
    """Verifies configuration data has all required keys.

    Args:
        data (dict): configuration data

    Returns:
        bool
            True when all keys are present
    """
    return all(k in data for k in REQUIRED_KEYS)


class BaseConfig(ABC):
    """BaseConfig is the abstract base class that defines the parameterization of queries."""

    @property
    @abstractmethod
    def params(self) -> Dict[str, Any]:
        """Get the query template parameters.

        Returns:
            typing.Dict[str, typing.Any]
        """
        raise NotImplementedError


class YAMLConfig(BaseConfig):
    """YAMLConfig loads reads a YAML file and parses the contents into the BaseConfig abstract class."""

    def __init__(self, file_handle: TextIO) -> None:
        """Load and read YAML parameter.

        Args:
            file_handle (typing.TextIO): File handle
        """
        data = yaml.safe_load(file_handle)
        if not has_all_required_config_keys(data):
            raise InvalidConfig(message="config contains invalid top level keys")

        self.__params = {}

        if len(data["params"]) < 1:
            return

        peek: dict = data["params"][0]
        if "key" not in peek and "value" not in peek:
            raise InvalidConfig(
                message="params do not contain key: value pair semantics"
            )
        self.__params = {x["key"]: x["value"] for x in data["params"]}

    @property
    def params(self) -> Dict[str, Any]:
        """Get the query template parameters.

        Returns:
            typing.Dict[str, typing.Any]
        """
        return self.__params

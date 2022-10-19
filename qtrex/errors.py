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

"""Custom exceptions for qtrex."""
from typing import List, Dict, Any, Optional


class BaseQtrexException(Exception):
    """Base exception class for `qtrex` error handling."""

    def __init__(
        self,
        *args: Optional[List[Any]],
        caused_by: Optional[Exception] = None,
        message: Optional[str] = None,
        **kwargs: Optional[Dict[str, Any]],
    ) -> None:
        """Wrap an exception with additional metadata.

        Args:
            caused_by (Optional[Exception]): Any exception raised external to this codebase.
            message (Optional[str]): Error message
        """
        self.caused_by = caused_by
        self.message = message
        super().__init__(*args, **kwargs)


class InvalidConfig(BaseQtrexException):
    """InvalidConfig is an exception for when a config is malformed."""

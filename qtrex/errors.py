"""Custom exceptions for qtrex."""
from typing import List, Dict, Any, Optional


class BaseQtrexException(Exception):
    """Base exception class for `qtrex` error handling."""

    def __init__(
        self,
        caused_by: Optional[Exception] = None,
        message: Optional[str] = None,
        *args: Optional[List[Any]],
        **kwargs: Optional[Dict[str, Any]],
    ) -> None:
        """Wrap an exception with additional metadata.

        Args:
            caused_by (Optional[Exception]): Any exception raised external to this codebase.

        """
        self.caused_by = caused_by
        self.message = message
        super().__init__(*args, **kwargs)


class InvalidConfig(BaseQtrexException):
    """InvalidConfig is an exception for when a config is malformed."""

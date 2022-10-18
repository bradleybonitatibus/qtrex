"""Custom exceptions for qtrex."""
from typing import List, Dict, Any, Optional


class BaseQtrexException(Exception):
    """Base exception class for `qtrex` error handling."""

    def __init__(
        self,
        caused_by: Exception,
        *args: Optional[List[Any]],
        **kwargs: Optional[Dict[str, Any]]
    ) -> None:
        """Wrap an exception with additional metadata.

        Args:
            caused_by (Exception): Any exception raised external to this codebase.

        """
        self.caused_by = caused_by
        super().__init__(*args, **kwargs)

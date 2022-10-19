"""Shared test fixtures."""
from typing import TextIO
from unittest import mock

from pytest import fixture


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

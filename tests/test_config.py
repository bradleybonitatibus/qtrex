"""Config tests."""
from typing import TextIO

import pytest

from qtrex.errors import InvalidConfig
from qtrex.config import YAMLConfig, has_all_required_config_keys


@pytest.mark.parametrize(
    "data,expected",
    [
        ({"params": {"key": "mykey", "value": "myvalue"}}, True),
        (
            {"invalid_key": "test"},
            False,
        ),
    ],
)
def test_has_all_valid_keys(data: dict, expected: bool) -> None:
    assert has_all_required_config_keys(data) == expected


def test_yaml_config_loads_params(mock_yaml_fixture: TextIO) -> None:
    cfg = YAMLConfig(mock_yaml_fixture)

    assert "my_key" in cfg.params
    assert cfg.params.get("my_key") == [1, 2, 3]


def test_yaml_config_with_empty_params(mock_empty_yaml_fixture: TextIO) -> None:
    cfg = YAMLConfig(mock_empty_yaml_fixture)
    assert cfg.params == {}


def test_yaml_config_raise_invalid_config_for_top_level_params(
    invalid_top_level_config_fixture: TextIO,
) -> None:
    with pytest.raises(InvalidConfig):
        YAMLConfig(invalid_top_level_config_fixture)


def test_yaml_config_raise_invalid_config_for_key_value_pairs(
    invalid_key_valid_pair_yaml_fixture: TextIO,
) -> None:
    with pytest.raises(InvalidConfig):
        YAMLConfig(invalid_key_valid_pair_yaml_fixture)

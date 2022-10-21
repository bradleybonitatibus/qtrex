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

"""Renderer module contains the implementation for rendering query templates."""
import sys
from typing import TextIO, Sequence, List

from jinja2 import Template as __template

from qtrex.config import BaseConfig
from qtrex.models import QueryRef


class TemplateRenderer:
    """Renders templates from a user provided configuration."""

    def __init__(self, config: BaseConfig, templates: Sequence[TextIO]) -> None:
        """Instantiate TemplateRenderer.

        Args:
            config (qtrex.config.Config): Query parameter configs
            templates (typing.Sequence[typing.TextIO]): Sequence of file handles
        """
        self.__cfg = config
        self.__templates = templates

    def render(self) -> Sequence[QueryRef]:
        """Render tempaltes using instance configs.

        Returns:
            typing.List[qtrex.models.QueryRef]
        """
        out: List[QueryRef] = []
        sep = "/" if sys.platform != "win32" else "\\"
        for file_handle in self.__templates:
            f_name = file_handle.name
            out.append(
                QueryRef(
                    name=f_name.split(sep)[-1],
                    template=self.inject_params(file_handle.read()),
                    filename=f_name,
                )
            )

        return out

    def inject_params(self, contents: str) -> str:
        """Injects params into query template and returns fully rendered string.

        Args:
            contents (str): Template file contents

        In future versions, we may want to add support for common
        template macros (i.e. Airflow's {{ ds }} or {{ ds_nodash }} macros).

        Returns:
            str
        """
        return __template(contents).render(params=self.__cfg.params)

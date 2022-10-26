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

from qtrex.executor import BigQueryExecutor
from qtrex.store import Store
from qtrex.config import YAMLConfig


def main():
    with open("./example.yaml", "r") as f:
        cfg = YAMLConfig(f)

    store = Store.from_path(cfg, "./testdata")
    ex = BigQueryExecutor()
    for query_ref in store:
        print(f"{query_ref.name}: {query_ref.template}\n")
        res = ex.execute(query_ref, dry_run=True)
        print(f"results: {res}")


if __name__ == "__main__":
    main()

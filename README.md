# qtrex
[![CI](https://github.com/bradleybonitatibus/qtrex/actions/workflows/ci.yml/badge.svg)](https://github.com/bradleybonitatibus/qtrex/actions/workflows/ci.yml)

[![PyPI version](https://badge.fury.io/py/qtrex.svg)](https://badge.fury.io/py/qtrex)

Query template rendering and execution library written in Python.

The goal of `qtrex` is to provide a simple API that supports loading `.sql`
files that can be templated with `jinja`, and provide extensible configuration
options to either compile the files, and execute the rendered templates against
various databases.

## Getting Started

`qtrex` is installable at https://pypi.org/project/qtrex/ via `pip` using:

We currently only support `bigquery`, but plan on adding other DB support as
optional dependencies.

```
pip install 'qtrex[bigquery]==0.0.5'
```

## Examples

Here is a brief example usage of `qtrex`. 

Assuming you have query templates in a directory on a local filesystem, using
our test suite as an example:

```text
|tests
    |--test_*.py
    |--testdata
        |--mytemplate.sql
        |--ingest
            |--another_file_ext.j2
            |--another_query.sql
```

Where `./tests/testdata/mytemplate.sql` has the following contents:
```sql
SELECT SUM(x)
FROM UNNEST({{ params.test_array }}) AS x
```
and `./tests/testdata/ingest/another_query.sql` has:

```sql
SELECT
    *
FROM
    `{{ params.my_project_id }}.{{ params.my_dataset }}.{{ params.my_table }}`
```
and lastly, `./tests/testdata/nested_params.sql` has:
```sql
SELECT
    {{ params.test_dict_key.one }} + {{ params.test_dict_key.two }}
```

Next, we want to have our `.yaml` config (or extend `qtrex.config.BaseConfig`)
to implement your own config mechanism.

Our `./tests/example.yaml` will look like:
```yaml
params:
  - key: test_string_key
    value: "string_value"
  - key: test_array_key
    value: [1, 2, 3]
  - key: test_dict_key
    value:
      one: 1
      two: 2
      three: 3
```

We can now run the following script (`./tests/example.py`) after changing
into the `./tests` directory
```python
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

```

When we run this script:
```shell
cd ./tests
python example.py
```
we should see the following in `stdout`

```text
mytemplate.sql: SELECT SUM(x)
FROM UNNEST([1, 2, 3]) AS x

results: QueryResult(query_ref=QueryRef(filename='./testdata\\mytemplate.sql', template='SELECT SUM(x)\nFROM UNNEST([1, 2, 3]) AS x', name='mytemplate.sql'), df=None, error=None)
nested_params.sql: SELECT
    1 + 2

results: QueryResult(query_ref=QueryRef(filename='./testdata\\nested_params.sql', template='SELECT\n    1 + 2', name='nested_params.sql'), df=None, error=None)

```
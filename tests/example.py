from qtrex.store import Store
from qtrex.config import YAMLConfig


def main():
    with open("./example.yaml", "r") as f:
        cfg = YAMLConfig(f)

    store = Store.from_path(cfg, "./testdata")

    for query_ref in store:
        print(f"{query_ref.name}: {query_ref.template}\n")


if __name__ == "__main__":
    main()

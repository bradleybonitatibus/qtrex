from qtrex.store import Store
from qtrex.config import YAMLConfig


def main():
    with open("./example.yaml", "r") as f:
        cfg = YAMLConfig(f)

    store = Store.from_path(cfg, "./testdata")

    for query_ref in store:
        print(query_ref.template)


if __name__ == "__main__":
    main()

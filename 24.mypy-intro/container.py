from typing import Generic, TypeVar

T = TypeVar("T")


class Container(Generic[T]):
    def __init__(self, data: T) -> None:
        self.data = data


def main() -> None:
    data_str = Container("qwerty")
    print(data_str.data)
    data_int = Container(1234)
    print(data_int.data)

    data_int_or_str = Container[str | int](234)
    print(data_int_or_str.data)
    data_int_or_str.data = "qwe"
    print(data_int_or_str.data)


if __name__ == "__main__":
    main()

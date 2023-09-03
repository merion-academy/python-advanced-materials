from typing import TypeVar, Any

AddParam = TypeVar("AddParam", float, str, list[Any])
T = TypeVar("T")


def hello(name: str) -> str:
    # return "a" + name
    line = f"Hi, {name}!"
    return line


def add(a: AddParam, b: AddParam) -> AddParam:
    return a + b


def repeat_item(item: T, n: int) -> list[T]:
    return [item] * n


def main() -> None:
    print(hello("Suren"))
    # print(hello(123456))
    # print(hello(b"qwert"))

    print(add(1, 2))
    print(add(4.5, 5.5))
    print(add("qwe", "abc"))
    print(add(["qwerty"], ["abc"]))

    items = repeat_item("abc", 3)
    print(items)
    items.append("qwe")
    # items.append(12345)
    print(items)


if __name__ == "__main__":
    main()

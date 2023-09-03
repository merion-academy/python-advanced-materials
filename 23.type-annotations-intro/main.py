from typing import Union, TypeVar, Iterable, Generator

NumInt = TypeVar("NumInt", bound=int)
# NumInt = TypeVar("NumInt", int, float)


def get_char(num: NumInt) -> tuple[str, NumInt]:
    return chr(num), num


def hello(name: str) -> str:
    line = f"Hi, {name}!"
    # print(line)
    return line


# AddType = Union[float, str]
AddType = float | str | list
T = TypeVar("T")


def add(a: T, b: T) -> T:
    return a + b


def repeat_item(item: T, n: int) -> list[T]:
    return [item] * n


def concat(a: str, b: str) -> str:
    return a + b


def powers(*numbers: int, power=2) -> Iterable[int]:
    for num in numbers:
        yield num**power


# def add_nums() -> Generator[yield_type, send_type, return_type]


def add_nums() -> Generator[int, NumInt, tuple[int, list[NumInt]]]:
    all_inputs: list[NumInt] = []
    total = 0
    while True:
        num: NumInt = yield len(all_inputs)
        if num is None:
            return total, all_inputs
        all_inputs.append(num)
        total += num


def process_nums(numbers: tuple[int, ...]):
    g = add_nums()
    print("init", next(g))
    g.send(2)
    g.send(2.5)
    print("got", g.send(1))

    for num in numbers:
        g.send(num)

    result = yield from g
    total, items = result
    yield total



def main():
    assert float | str == Union[float, str]
    print(hello("Suren"))
    print(hello(123))
    print(add(1, 2))
    print(add(3.1, 4.2))
    print(add("foo", "bar"))
    print(concat("foo", "bar"))
    print(add(["foo", "spam"], ["bar", "eggs"]))
    print(add([1, 1, ""], ["bar", "eggs"]))

    repeated_str = repeat_item("1", 2)
    print(repeated_str)
    repeated_str.append("4")
    repeated_str.append(4)
    print(repeated_str)
    repeated_list = repeat_item(("1",), 3)
    print(repeated_list)
    repeated_list.append(("1",))

    a = 3
    print(a)
    names: list[str] = []
    print(names)
    names.append("John")
    names.append(123)
    print(names)

    # a: int = 3

    data: dict[str, int] = {}
    print(data)
    data["foo"] = 123
    data["bar"] = "123"
    print(data)

    res = get_char(60)
    print(res)
    res = get_char(True)
    print(res)

    for i in powers(1, 2, 3, power=2):
        print(i)

    for res in process_nums(
        tuple(i for i in range(10) if i % 2)
    ):
        print("result", res)


if __name__ == "__main__":
    main()

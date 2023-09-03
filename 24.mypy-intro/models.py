from typing import TypeVar, Type, Self, Any


class BaseModel:
    ModelType = TypeVar("ModelType", bound="BaseModel")

    def __init__(self, foo: Any, bar: Any) -> None:
        self.foo = foo
        self.bar = bar

    @classmethod
    def create(cls: Type[ModelType], foo: str | float) -> ModelType:
        bar = foo * 3
        obj = cls(foo=foo, bar=bar)
        return obj

    def update(self) -> Self:
        return self

    def __enter__(self) -> Self:
        return self


class User(BaseModel):
    pass


def main() -> None:
    model = BaseModel(foo="foo", bar="bar")
    print(model)
    model_2 = BaseModel.create(foo="fizz")
    print(model_2)

    user = User(foo="u", bar="ser")
    print(user)
    user_2 = User.create(foo="spam")
    print(user_2)

    u = user_2.update()
    print(u)


if __name__ == "__main__":
    main()

import pytest

from models.user import User


@pytest.fixture()
def user():
    return User("username", "pwd")


@pytest.fixture()
def user_w_username(request, user):
    username = request.param
    # return User(username, "pwd")
    user.username = username
    return user


@pytest.fixture(
    params=[
        pytest.param(("nick", "pwd-n"), id="nick"),
        pytest.param(("john", "pwd"), id="j"),
        pytest.param(("Sam", "pwd2"), id="sam"),
    ],
)
def user_u(request):
    # username = request.param
    username, pwd = request.param
    return User(username, pwd)
    # user.username = username
    # return user

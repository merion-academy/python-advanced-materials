from dataclasses import dataclass, field

import pytest


@dataclass
class Author:
    name: str
    posts: list["Post"] = field(default_factory=list)


@dataclass
class Post:
    title: str
    author: Author
    comments: list["Comment"] = field(default_factory=list)


@dataclass
class Comment:
    text: str
    post: Post
    author: Author


@pytest.fixture()
def author_john():
    author = Author(name="john")
    return author


@pytest.fixture(scope="class")
def author_sam():
    author = Author(name="sam")
    yield author
    print("delete (teardown)", author)


@pytest.fixture()
def post_1_by_john(author_john: Author):
    post = Post(title="Title 1 by John", author=author_john)
    author_john.posts.append(post)
    return post


@pytest.fixture()
def post_2_by_john(author_john: Author):
    post = Post(title="Title 2", author=author_john)
    author_john.posts.append(post)
    return post


def create_post_for_author(title: str, author: Author):
    post = Post(title=title, author=author)
    author.posts.append(post)
    return post


@pytest.fixture()
def create_post_for_john(author_john: Author):
    # author_john.name = ""
    def create_post(title: str):
        post = Post(title=title, author=author_john)
        author_john.posts.append(post)
        return post

    return create_post


@pytest.fixture(autouse=True)
def post_by_sam(author_sam: Author):
    post = Post(title="Some title by Sam", author=author_sam)
    author_sam.posts.append(post)
    return post


@pytest.fixture()
def comment_for_post_1_by_sam(
    post_1_by_john: Post,
    author_sam: Author,
):
    comment = Comment(
        text="Nice post!",
        post=post_1_by_john,
        author=author_sam,
    )
    post_1_by_john.comments.append(comment)
    return comment


def test_fixtures(
    author_john: Author,
    comment_for_post_1_by_sam: Comment,
    # post_by_sam: Post,
):
    assert comment_for_post_1_by_sam.post.author is author_john
    # print(comment_for_post_1_by_sam.author.posts)
    assert comment_for_post_1_by_sam.author.posts
    # print(comment_for_post_1_by_sam.author)
    # print(comment_for_post_1_by_sam.author.posts)


def test_john_posts(
    author_john,
    create_post_for_john,
):
    post_1 = create_post_for_john("Title 1")
    post_2 = create_post_for_john("Title 2")
    assert isinstance(post_1, Post)
    assert isinstance(post_2, Post)
    assert post_1.author is author_john
    assert post_2.author is author_john

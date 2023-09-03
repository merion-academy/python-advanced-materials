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


@pytest.fixture()
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
    post_by_sam: Post,
):
    assert comment_for_post_1_by_sam.post.author is author_john
    # print(comment_for_post_1_by_sam.author.posts)
    assert comment_for_post_1_by_sam.author.posts[0] is post_by_sam

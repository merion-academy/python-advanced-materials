CREATE TABLE users
(
    id       INTEGER     NOT NULL,
    username VARCHAR(30) NOT NULL,
    email    VARCHAR     NOT NULL,
    motto    VARCHAR,
    PRIMARY KEY (id),
    UNIQUE (username)
);

CREATE TABLE posts
(
    title     VARCHAR(100)    NOT NULL,
    body      TEXT DEFAULT '' NOT NULL,
    author_id INTEGER         NOT NULL,
    id        INTEGER         NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES users (id)
);


SELECT posts.title,
       posts.body,
       posts.author_id,
       posts.id,
       users_1.username,
       users_1.email,
       users_1.motto,
       users_1.id AS id_1
FROM posts
         LEFT OUTER JOIN users AS users_1
                         ON users_1.id = posts.author_id
ORDER BY posts.id;


SELECT users.username,
       users.email,
       users.motto,
       users.id,
       posts_1.title,
       posts_1.body,
       posts_1.author_id,
       posts_1.id AS id_1
FROM users
         LEFT OUTER JOIN posts AS posts_1 ON users.id = posts_1.author_id
ORDER BY users.id;

SELECT users.username, users.email, users.motto, users.id
FROM users
ORDER BY users.id;
SELECT posts.author_id AS posts_author_id,
       posts.title     AS posts_title,
       posts.body      AS posts_body,
       posts.id        AS posts_id
FROM posts
WHERE posts.author_id IN (1, 2, 3);
CREATE DATABASE social_network_db;
USE social_network_db;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_posts_users
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);

CREATE TABLE likes (
    like_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_likes_users
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_likes_posts
        FOREIGN KEY (post_id)
        REFERENCES posts(post_id)
        ON DELETE CASCADE
);

CREATE TABLE comments (
    comment_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    comment_text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_comments_users
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_comments_posts
        FOREIGN KEY (post_id)
        REFERENCES posts(post_id)
        ON DELETE CASCADE
);

CREATE TABLE friends (
    friend_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    friend_user_id INT NOT NULL,
    status ENUM('pending', 'accepted', 'blocked') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_friends_user1
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_friends_user2
        FOREIGN KEY (friend_user_id)
        REFERENCES users(user_id)
        ON DELETE CASCADE
);

CREATE INDEX idx_posts_created_at
ON posts(created_at);

CREATE VIEW view_user_info AS
SELECT
    user_id,
    username,
    email,
    created_at
FROM users;

CREATE VIEW view_post_statistics AS
SELECT
    p.post_id,
    p.content,
    u.username,

    COUNT(DISTINCT l.like_id) AS total_likes,
    COUNT(DISTINCT c.comment_id) AS total_comments

FROM posts p

JOIN users u
    ON p.user_id = u.user_id

LEFT JOIN likes l
    ON p.post_id = l.post_id

LEFT JOIN comments c
    ON p.post_id = c.post_id

GROUP BY
    p.post_id,
    p.content,
    u.username;

DELIMITER $$

CREATE PROCEDURE sp_add_user(
    IN p_username VARCHAR(50),
    IN p_password VARCHAR(255),
    IN p_email VARCHAR(100)
)
BEGIN

    DECLARE v_count INT;

    SELECT COUNT(*)
    INTO v_count
    FROM users
    WHERE email = p_email;

    IF v_count > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Email đã được sử dụng';

    ELSE

        INSERT INTO users(username, password, email)
        VALUES(p_username, p_password, p_email);

    END IF;

END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE sp_create_post(
    IN p_user_id INT,
    IN p_content TEXT,
    OUT p_new_post_id INT
)
BEGIN

    INSERT INTO posts(user_id, content)
    VALUES(p_user_id, p_content);

    SET p_new_post_id = LAST_INSERT_ID();

END $$

DELIMITER ;

DELIMITER $$

CREATE PROCEDURE sp_get_friends(
    IN p_user_id INT,
    IN p_limit INT,
    IN p_offset INT
)
BEGIN

    SELECT
        u.user_id,
        u.username,
        u.email,
        f.status

    FROM friends f

    JOIN users u
        ON f.friend_user_id = u.user_id

    WHERE f.user_id = p_user_id
        AND f.status = 'accepted'

    LIMIT p_limit OFFSET p_offset;

END $$

DELIMITER ;

INSERT INTO users(username, password, email)
VALUES
('thach', '123456', 'thach@gmail.com'),
('an', '123456', 'an@gmail.com'),
('binh', '123456', 'binh@gmail.com');

INSERT INTO posts(user_id, content)
VALUES
(1, 'Xin chào mọi người'),
(2, 'Hôm nay trời đẹp'),
(3, 'Đang học SQL');

INSERT INTO likes(user_id, post_id)
VALUES
(2, 1),
(3, 1),
(1, 2);

INSERT INTO comments(user_id, post_id, comment_text)
VALUES
(2, 1, 'Bài viết hay'),
(3, 1, 'Chào bạn'),
(1, 3, 'Cố gắng học tốt');

INSERT INTO friends(user_id, friend_user_id, status)
VALUES
(1, 2, 'accepted'),
(1, 3, 'accepted'),
(2, 3, 'pending');

CALL sp_add_user(
    'khoa',
    '123456',
    'khoa@gmail.com'
);

SET @new_post_id = 0;

CALL sp_create_post(
    1,
    'Bài viết mới từ procedure',
    @new_post_id
);

SELECT @new_post_id;

CALL sp_get_friends(
    1,
    10,
    0
);

SELECT * FROM view_user_info;

SELECT * FROM view_post_statistics;
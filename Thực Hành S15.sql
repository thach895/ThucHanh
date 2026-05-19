CREATE DATABASE mini_social_network;
USE mini_social_network;

-- =========================
-- 1. TẠO BẢNG
-- =========================

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE posts (
    post_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    content TEXT NOT NULL,
    like_count INT DEFAULT 0,
    comment_count INT DEFAULT 0,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES users(user_id)
);

CREATE TABLE comments (
    comment_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES users(user_id),

    FOREIGN KEY (post_id)
    REFERENCES posts(post_id)
);

CREATE TABLE likes (
    like_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES users(user_id),

    FOREIGN KEY (post_id)
    REFERENCES posts(post_id),

    UNIQUE(user_id, post_id)
);

CREATE TABLE friends (
    friend_relation_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    friend_id INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_id)
    REFERENCES users(user_id),

    FOREIGN KEY (friend_id)
    REFERENCES users(user_id)
);

-- =========================
-- FULLTEXT INDEX
-- =========================

ALTER TABLE posts
ADD FULLTEXT(content);

-- =========================
-- AUDIT LOG TABLE
-- =========================

CREATE TABLE post_logs (
    log_id INT PRIMARY KEY AUTO_INCREMENT,
    post_id INT,
    post_content TEXT,
    deleted_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- 2. MOCK DATA
-- =========================

INSERT INTO users(username, password, email)
VALUES
('thach', '123456', 'thach@gmail.com'),
('an', '123456', 'an@gmail.com'),
('binh', '123456', 'binh@gmail.com');

INSERT INTO posts(user_id, content)
VALUES
(1, 'Hello everyone'),
(2, 'My first post'),
(3, 'Learning MySQL');

INSERT INTO likes(user_id, post_id)
VALUES
(1, 2),
(2, 1),
(3, 1);

INSERT INTO comments(user_id, post_id, content)
VALUES
(1, 1, 'Nice post'),
(2, 1, 'Great'),
(3, 2, 'Interesting');

INSERT INTO friends(user_id, friend_id)
VALUES
(1, 2),
(2, 3);

-- =========================
-- 3. VIEW
-- =========================

CREATE VIEW view_user_info AS
SELECT
    user_id,
    username,
    email,
    created_at
FROM users;

-- =========================
-- 4. STORED PROCEDURE
-- =========================

DELIMITER $$

CREATE PROCEDURE sp_add_user(
    IN p_username VARCHAR(100),
    IN p_password VARCHAR(255),
    IN p_email VARCHAR(255)
)
BEGIN

    IF EXISTS (
        SELECT 1
        FROM users
        WHERE username = p_username
    ) THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Username already exists';

    ELSEIF EXISTS (
        SELECT 1
        FROM users
        WHERE email = p_email
    ) THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Email already exists';

    ELSE

        INSERT INTO users(username, password, email)
        VALUES(p_username, p_password, p_email);

    END IF;

END$$

DELIMITER ;

-- =========================
-- 5. TRIGGER LIKE
-- =========================

DELIMITER $$

CREATE TRIGGER tg_after_like_insert
AFTER INSERT
ON likes
FOR EACH ROW
BEGIN

    UPDATE posts
    SET like_count = like_count + 1
    WHERE post_id = NEW.post_id;

END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER tg_after_like_delete
AFTER DELETE
ON likes
FOR EACH ROW
BEGIN

    UPDATE posts
    SET like_count =
        CASE
            WHEN like_count > 0 THEN like_count - 1
            ELSE 0
        END
    WHERE post_id = OLD.post_id;

END$$

DELIMITER ;

-- =========================
-- 6. TRIGGER COMMENT
-- =========================

DELIMITER $$

CREATE TRIGGER tg_after_comment_insert
AFTER INSERT
ON comments
FOR EACH ROW
BEGIN

    UPDATE posts
    SET comment_count = comment_count + 1
    WHERE post_id = NEW.post_id;

END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER tg_after_comment_delete
AFTER DELETE
ON comments
FOR EACH ROW
BEGIN

    UPDATE posts
    SET comment_count =
        CASE
            WHEN comment_count > 0 THEN comment_count - 1
            ELSE 0
        END
    WHERE post_id = OLD.post_id;

END$$

DELIMITER ;

-- =========================
-- 7. THỐNG KÊ HOẠT ĐỘNG
-- =========================

DELIMITER $$

CREATE PROCEDURE sp_user_activity_report()
BEGIN

    SELECT
        u.user_id,
        u.username,

        COUNT(DISTINCT p.post_id) AS total_posts,
        COUNT(DISTINCT l.like_id) AS total_likes,
        COUNT(DISTINCT c.comment_id) AS total_comments

    FROM users u

    LEFT JOIN posts p
        ON u.user_id = p.user_id

    LEFT JOIN likes l
        ON u.user_id = l.user_id

    LEFT JOIN comments c
        ON u.user_id = c.user_id

    GROUP BY
        u.user_id,
        u.username;

END$$

DELIMITER ;

-- =========================
-- 8. DELETE USER TRANSACTION
-- =========================

DELIMITER $$

CREATE PROCEDURE sp_delete_user(
    IN p_user_id INT
)
BEGIN

    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
    END;

    START TRANSACTION;

    DELETE FROM likes
    WHERE user_id = p_user_id
       OR post_id IN (
            SELECT post_id
            FROM posts
            WHERE user_id = p_user_id
       );

    DELETE FROM comments
    WHERE user_id = p_user_id
       OR post_id IN (
            SELECT post_id
            FROM posts
            WHERE user_id = p_user_id
       );

    DELETE FROM friends
    WHERE user_id = p_user_id
       OR friend_id = p_user_id;

    DELETE FROM posts
    WHERE user_id = p_user_id;

    DELETE FROM users
    WHERE user_id = p_user_id;

    COMMIT;

END$$

DELIMITER ;

-- =========================
-- 9. KIỂM SOÁT KẾT BẠN
-- =========================

DELIMITER $$

CREATE TRIGGER tg_before_friend_insert
BEFORE INSERT
ON friends
FOR EACH ROW
BEGIN

    -- tự kết bạn
    IF NEW.user_id = NEW.friend_id THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Cannot add yourself as friend';

    END IF;

    -- trùng dữ liệu
    IF EXISTS (
        SELECT 1
        FROM friends
        WHERE user_id = NEW.user_id
          AND friend_id = NEW.friend_id
    ) THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Friend relation already exists';

    END IF;

    -- lời mời đảo chiều
    IF EXISTS (
        SELECT 1
        FROM friends
        WHERE user_id = NEW.friend_id
          AND friend_id = NEW.user_id
    ) THEN

        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Reverse friend request already exists';

    END IF;

END$$

DELIMITER ;

-- =========================
-- 10. AUDIT LOG TRIGGER
-- =========================

DELIMITER $$

CREATE TRIGGER tg_after_post_delete
AFTER DELETE
ON posts
FOR EACH ROW
BEGIN

    INSERT INTO post_logs(
        post_id,
        post_content
    )
    VALUES(
        OLD.post_id,
        OLD.content
    );

END$$

DELIMITER ;

-- =========================
-- TEST
-- =========================

CALL sp_add_user(
    'new_user',
    '123456',
    'new@gmail.com'
);

CALL sp_user_activity_report();

CALL sp_delete_user(1);

SELECT * FROM view_user_info;

SELECT * FROM post_logs;
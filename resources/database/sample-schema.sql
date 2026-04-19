-- =============================================================================
-- Student IT Handbook – Sample Database Schema
-- Dùng cho học tập và thực hành SQL.
-- Chay: psql -U dev -d internhub -f sample-schema.sql
-- Hoặc tự động chạy khi dùng Docker (xem postgres-compose.yml)
-- =============================================================================

-- Xoá bảng cũ nếu có (thứ tự ngược vì foreign key)
DROP TABLE IF EXISTS post_tags CASCADE;
DROP TABLE IF EXISTS tags CASCADE;
DROP TABLE IF EXISTS comments CASCADE;
DROP TABLE IF EXISTS posts CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- =============================================================================
-- Bảng USERS
-- =============================================================================
CREATE TABLE users (
    id          SERIAL PRIMARY KEY,
    name        VARCHAR(100) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    password    VARCHAR(255) NOT NULL DEFAULT '$2b$12$placeholder', -- bcrypt hash
    role        VARCHAR(50) NOT NULL DEFAULT 'intern',
    is_active   BOOLEAN NOT NULL DEFAULT true,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Index
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_role ON users(role);

-- =============================================================================
-- Bảng POSTS
-- =============================================================================
CREATE TABLE posts (
    id          SERIAL PRIMARY KEY,
    user_id     INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    title       VARCHAR(255) NOT NULL,
    content     TEXT,
    published   BOOLEAN NOT NULL DEFAULT false,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_posts_user_id ON posts(user_id);
CREATE INDEX idx_posts_published ON posts(published);

-- =============================================================================
-- Bảng COMMENTS
-- =============================================================================
CREATE TABLE comments (
    id          SERIAL PRIMARY KEY,
    post_id     INT NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    user_id     INT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    content     TEXT NOT NULL,
    created_at  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_comments_post_id ON comments(post_id);

-- =============================================================================
-- Bảng TAGS
-- =============================================================================
CREATE TABLE tags (
    id      SERIAL PRIMARY KEY,
    name    VARCHAR(50) UNIQUE NOT NULL
);

-- Bảng trung gian POSTS ↔ TAGS (many-to-many)
CREATE TABLE post_tags (
    post_id INT NOT NULL REFERENCES posts(id) ON DELETE CASCADE,
    tag_id  INT NOT NULL REFERENCES tags(id) ON DELETE CASCADE,
    PRIMARY KEY (post_id, tag_id)
);

-- =============================================================================
-- Dữ liệu mẫu
-- =============================================================================

-- Users
INSERT INTO users (name, email, role) VALUES
('Nguyễn Văn A',  'a.nguyen@example.com',  'intern'),
('Trần Thị B',    'b.tran@example.com',    'developer'),
('Lê Văn C',      'c.le@example.com',      'lead'),
('Phạm Thị D',    'd.pham@example.com',    'intern'),
('Hoàng Văn E',   'e.hoang@example.com',   'developer');

-- Posts
INSERT INTO posts (user_id, title, content, published) VALUES
(1, 'Getting Started with Git',     'Git là công cụ quản lý mã nguồn phổ biến nhất...', true),
(2, 'Docker cho người mới bắt đầu', 'Docker giúp đóng gói ứng dụng...', true),
(3, 'CI/CD Pipeline Guide',          'Continuous Integration giúp...',  true),
(1, 'SQL Tips and Tricks',           'Một số tips khi viết SQL...',     false),
(4, 'My First Day as Intern',        'Ngày đầu tiên đi thực tập...',   true),
(2, 'REST API Design Patterns',      'Thiết kế API chuẩn REST...',     true);

-- Tags
INSERT INTO tags (name) VALUES
('git'), ('docker'), ('cicd'), ('sql'), ('career'), ('api'), ('backend');

-- Post-Tags
INSERT INTO post_tags (post_id, tag_id) VALUES
(1, 1),  -- Git post → git tag
(2, 2),  -- Docker post → docker tag
(3, 3),  -- CI/CD post → cicd tag
(4, 4),  -- SQL post → sql tag
(5, 5),  -- Intern post → career tag
(6, 6),  -- REST API → api tag
(6, 7);  -- REST API → backend tag

-- Comments
INSERT INTO comments (post_id, user_id, content) VALUES
(1, 2, 'Bài viết rất hữu ích, cảm ơn bạn!'),
(1, 4, 'Mình đã áp dụng được, thanks!'),
(2, 1, 'Docker compose phần tiếp theo nhé!'),
(5, 3, 'Chào mừng em vào team!');

-- =============================================================================
-- Query mẫu để test
-- =============================================================================

-- Lấy tất cả posts đã published kèm tên tác giả
-- SELECT u.name, p.title, p.created_at
-- FROM users u
-- INNER JOIN posts p ON u.id = p.user_id
-- WHERE p.published = true
-- ORDER BY p.created_at DESC;

-- Đếm số post mỗi user (kể cả user chưa có post)
-- SELECT u.name, COUNT(p.id) as post_count
-- FROM users u
-- LEFT JOIN posts p ON u.id = p.user_id
-- GROUP BY u.name
-- ORDER BY post_count DESC;

-- Lấy posts kèm tags
-- SELECT p.title, STRING_AGG(t.name, ', ') as tags
-- FROM posts p
-- JOIN post_tags pt ON p.id = pt.post_id
-- JOIN tags t ON pt.tag_id = t.id
-- GROUP BY p.title;

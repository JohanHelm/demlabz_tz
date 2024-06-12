-- CREATE USER users_admin WITH PASSWORD 'users_pass';

-- CREATE DATABASE marketplace OWNER users_admin;

-- \c marketplace

CREATE TABLE IF NOT EXISTS user_data (
    id bigserial PRIMARY KEY,
    nickname TEXT NOT NULL UNIQUE,
    pass_hash TEXT NOT NULL,
    email TEXT,
    telegram_name TEXT,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
); 

GRANT USAGE ON SCHEMA public TO users_admin;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO users_admin;

CREATE UNIQUE INDEX nickname ON auth_data (id);


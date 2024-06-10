
CREATE TABLE IF NOT EXISTS auth_data (
    id bigserial PRIMARY KEY,
    nickname TEXT NOT NULL,
    pass_hash TEXT NOT NULL,
    email TEXT,
    telegram_name TEXT,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
); 

CREATE UNIQUE INDEX users_id_idx ON auth_data (id);


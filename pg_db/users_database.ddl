
CREATE TABLE IF NOT EXISTS auth_data (
    id bigserial PRIMARY KEY,
    nickname TEXT NOT NULL,
    password TEXT NOT NULL,
    created_at timestamp with time zone,
); 

CREATE UNIQUE INDEX users_id_idx ON auth_data (id);


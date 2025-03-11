CREATE TABLE IF NOT EXISTS views_data (
    id SERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    title TEXT,
    datetime TIMESTAMP,
    views INT
);
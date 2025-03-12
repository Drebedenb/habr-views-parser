CREATE TABLE IF NOT EXISTS views_data (
    url VARCHAR(100) PRIMARY KEY,  
    title VARCHAR(1000),
    datetime TIMESTAMP,
    views INT
);
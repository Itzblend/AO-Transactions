CREATE TABLE IF NOT EXISTS users (
    id SERIAL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    balance DOUBLE PRECISION,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (name, email)
);

INSERT INTO users (name, email, balance) VALUES ('John Doe', 'john.doe@mail.com', 100.00);
INSERT INTO users (name, email, balance) VALUES ('Jane Doe', 'jane.doe@mail.com', 200.00);
INSERT INTO users (name, email, balance) VALUES ('John Smith', 'john.smith@mail.com', 300.00);
INSERT INTO users (name, email, balance) VALUES ('Jane Smith', 'jane.smith@mail.com', 400.00);

CREATE USER grafanauser WITH PASSWORD 'grafanapassword';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO grafanauser;
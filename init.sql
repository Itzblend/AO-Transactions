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


CREATE TABLE IF NOT EXISTS reservations (
    id SERIAL,
    room_id VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    start_time TIME NOT NULL,
    end_time TIME NOT NULL,
    reserved BOOLEAN DEFAULT FALSE,
    reserved_by VARCHAR(255),
    PRIMARY KEY(room_id, date, start_time, end_time)
);

INSERT INTO reservations (room_id, date, start_time, end_time)
VALUES ('room1', '2020-01-01', '10:00:00', '11:00:00');

INSERT INTO reservations (room_id, date, start_time, end_time)
VALUES ('room1', '2020-01-01', '11:00:00', '12:00:00');

INSERT INTO reservations (room_id, date, start_time, end_time)
VALUES ('room1', '2020-01-01', '12:00:00', '13:00:00');

INSERT INTO reservations (room_id, date, start_time, end_time)
VALUES ('room1', '2020-01-01', '13:00:00', '14:00:00');

INSERT INTO reservations (room_id, date, start_time, end_time)
VALUES ('room1', '2020-01-01', '14:00:00', '15:00:00');

INSERT INTO reservations (room_id, date, start_time, end_time)
VALUES ('room1', '2020-01-01', '15:00:00', '16:00:00');


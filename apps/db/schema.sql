CREATE TABLE users (
	user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	username varchar(20) UNIQUE,
	password varchar(10),
	email varchar(50) UNIQUE,
	created_at datetime
);

CREATE INDEX uindex ON users (username);
CREATE INDEX eindex ON users (email);
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    firstname VARCHAR(255),
    lastname VARCHAR(255),
 	  role VARCHAR(50),
    active boolean default true
);

CREATE TABLE password_resets (
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE UNIQUE,
    token TEXT UNIQUE NOT NULL,
	active boolean default true,
    created_at TIMESTAMP DEFAULT NOW()
);

create table organizations(
	id SERIAL PRIMARY KEY,	
	user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
	name VARCHAR(255),
	active boolean default true
);
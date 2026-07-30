-- This is DDL (Data Definition Languange)
-- Basically same with definiting in C/C++.

CREATE TABLE users (
    id SERIAL NOT NULL PRIMARY KEY,
	nama VARCHAR(100) NOT NULL DEFAULT 'Anonymous Person',
	usia INT NOT NULL DEFAULT 20,
	kota VARCHAR(50)
);

-- Alter table adding column
ALTER TABLE users ADD COLUMN isMarried BOOL DEFAULT FALSE;

-- Insert Data
INSERT INTO users (nama, usia, kota) VALUES ('Gilang', 18, 'Jakarta');
INSERT INTO users (nama, usia, kota) VALUES ('Budi', 28, 'Purwakarta') RETURNING

-- DML (Data Manipulation Language)
-- With select
SELECT * from users;

SELECT nama, usia from users;

SELECT * FROM users WHERE kota = 'Jakoarta';

SELECT * FROM users WHERE usia < 28;
SELECT * FROM users WHERE usia > 28 AND kota = 'Jakarta';
SELECT * FROM users WHERE usia > 28 OR kota = 'Jakarta';

SELECT * FROM users LIMIT 3;
SELECT * FROM users LIMIT 3 OFFSET;

SELECT * FROM users ORDER BY id;
SELECT * FROM users ORDER BY id ASC;
SELECT * FROM users ORDER BY id DESC;





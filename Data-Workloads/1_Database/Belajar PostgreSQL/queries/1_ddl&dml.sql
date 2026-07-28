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



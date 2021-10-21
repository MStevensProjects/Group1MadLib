CREATE TABLE Adjectives (
	adj_id INT NOT NULL,
    adj_word VARCHAR(255) NOT NULL,
    PRIMARY KEY (adj_id)
);
CREATE TABLE FirstNames (
	fName_id INT NOT NULL,
    fName_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (fName_id)
);
CREATE TABLE Verbs (
	verb_id INT NOT NULL,
    verb_word VARCHAR(255) NOT NULL,
    PRIMARY KEY (verb_id)
);
CREATE TABLE Birds (
    bird_id INT NOT NULL,
    bird_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (bird_id)
);
CREATE TABLE Rooms (
    room_id INT NOT NULL,
    room_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (room_id)
);
CREATE TABLE Liquids (
    liquid_id INT NOT NULL,
    liquid_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (liquid_id)
);
CREATE TABLE BodyParts (
    bPart_id INT NOT NULL,
    bPart_name VARCHAR(255) NOT NULL,
    PRIMARY KEY (bPart_id)
);
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

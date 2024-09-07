USE ezenplo;

CREATE TABLE ezenplo.city (
    id INT(10) NOT NULL AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    nickname VARCHAR(50) DEFAULT NULL,
    postal_code VARCHAR(9) DEFAULT NULL,
    state_code VARCHAR(2) DEFAULT NULL,
    PRIMARY KEY (id)
);
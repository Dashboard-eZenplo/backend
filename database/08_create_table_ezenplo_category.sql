USE ezenplo;

CREATE TABLE ezenplo.category (
    id INT(10) NOT NULL AUTO_INCREMENT,
    name VARCHAR(70) NOT NULL,
    icon VARCHAR(50) DEFAULT NULL,
    family VARCHAR(50) DEFAULT NULL,
    PRIMARY KEY (id)
);
USE ages;

CREATE TABLE ages.user (
    id INT(10) NOT NULL AUTO_INCREMENT,
    name VARCHAR(70) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    password VARCHAR(255) NOT NULL,
    cnpj VARCHAR(255) NOT NULL,
    admin BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (id),
    UNIQUE KEY (email)
);

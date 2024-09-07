USE ezenplo;

CREATE TABLE ezenplo.address (
    id INT(10) NOT NULL AUTO_INCREMENT,
    city_id INT(10) NOT NULL,
    state_id INT(10) NOT NULL,
    neighborhood VARCHAR(100) DEFAULT NULL,
    street VARCHAR(100) DEFAULT NULL,
    number VARCHAR(100) DEFAULT NULL,
    complement VARCHAR(100) DEFAULT NULL,
    PRIMARY KEY (id),
    INDEX city_id_idx (city_id),
    INDEX state_id_idx (state_id),
    CONSTRAINT fk_city_address FOREIGN KEY (city_id)
    REFERENCES city (id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_state_address FOREIGN KEY (state_id)
    REFERENCES state (id) ON UPDATE CASCADE ON DELETE CASCADE
);
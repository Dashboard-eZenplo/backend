USE ezenplo;

CREATE TABLE ezenplo.activity (
    id INT(10) NOT NULL AUTO_INCREMENT,
    location_id INT(10) NOT NULL,
    category_id INT(10) NOT NULL,
    name VARCHAR(70) NOT NULL,
    PRIMARY KEY (id),
    INDEX location_id_idx (location_id),
    INDEX category_id_idx (category_id),
    CONSTRAINT fk_location_activity FOREIGN KEY (location_id)
    REFERENCES location (id) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_category_activity FOREIGN KEY (category_id)
    REFERENCES category (id) ON UPDATE CASCADE ON DELETE CASCADE
)
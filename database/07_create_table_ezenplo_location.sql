CREATE TABLE ezenplo.location (
    id INT(10) NOT NULL AUTO_INCREMENT,
    app_user_id INT(10) NOT NULL,
    name VARCHAR(70) NOT NULL,
    latitude DECIMAL(10, 7) DEFAULT NULL,
    longitude DECIMAL(10, 7) DEFAULT NULL,
    icon VARCHAR(50) DEFAULT NULL,
    family VARCHAR(50) DEFAULT NULL,
    created_at DATETIME DEFAULT NULL,
    updated_at DATETIME DEFAULT NULL,
    address VARCHAR(255) DEFAULT NULL,
    status CHAR(1) DEFAULT '1',
    last_activity_at DATETIME DEFAULT NULL,
    keep_time INT(11) DEFAULT NULL,
    PRIMARY KEY (id),
    INDEX app_user_id_idx (app_user_id),
    CONSTRAINT fk_app_user_location FOREIGN KEY (app_user_id)
    REFERENCES app_user (id) ON UPDATE CASCADE ON DELETE CASCADE
);
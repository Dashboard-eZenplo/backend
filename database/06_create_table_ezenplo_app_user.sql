USE ezenplo;

CREATE TABLE ezenplo.app_user (
    id INT(10) NOT NULL AUTO_INCREMENT,
    name VARCHAR(70) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    avatar_id TINYINT(4) DEFAULT NULL,
    created_at DATETIME DEFAULT NULL,
    updated_at DATETIME DEFAULT NULL,
    active CHAR(1) DEFAULT '1',
    admin CHAR(1) DEFAULT '0',
    remember_token VARCHAR(100) DEFAULT NULL,
    notification_time TIME DEFAULT NULL,
    PRIMARY KEY (id)
);
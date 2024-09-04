CREATE TABLE ezenplo.activity_time (
    activity_id INT(10) NOT NULL,
    timekeeper INT(11) DEFAULT NULL,
    registration_date DATE DEFAULT NULL,
    satisfaction INT(11) DEFAULT NULL,
    importance INT(11) DEFAULT NULL,
    rating DECIMAL(14, 1) DEFAULT NULL,
    PRIMARY KEY (activity_id),
    CONSTRAINT fk_activity_time_activity FOREIGN KEY (activity_id)
    REFERENCES activity (id) ON UPDATE CASCADE ON DELETE CASCADE
);
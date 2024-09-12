USE ages;

INSERT INTO ages.user (name, email, phone, password, cnpj, admin) VALUES
('Joao Silva', 'joao.silva@ezenplo.com', '11987654321', '$2b$12$vh4nguv8CnvghuvtV6Hi.OM3pWZF281WyaoTFNuroN99pdFMTKgc6', '12345678000195', TRUE),
('Maria Oliveira', 'maria.oliveira@ezenplo.com', '21987654321', '2b$12$30lOQkEjdrx41B.uFBLdoezGP0c8/NKcnfU/7haY6pfdzj2W7NxxO', '12345678000195', TRUE),
('Jose Souza', 'jose.souza@ezenplo.com', '31987654321', '$2b$12$HUPSVtukphnMpUiUzfpGm.dq6BbXDX9YgWw2Wekkgy00Rpxc6q/PS', '12345678000195', FALSE),
('Ana Santos', 'ana.santos@ezenplo.com', '41987654321', '$2b$12$7JIICh20yqciF6ODb/HPXOZnc1UB9iqcdc.zQTrcsdu.xmVDslKd2', '12345678000195', FALSE);

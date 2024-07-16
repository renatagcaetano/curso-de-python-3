ALTER TABLE empresas MODIFY cnpj VARCHAR(14);

INSERT INTO empresas (nome, cnpj) VALUES
('Bradesco', 00000000000000),
('Vale', 00000000000000),
('Cielo', 00000000000000);

INSERT INTO empresas_unidades (empresa_id, cidade_id, sede) VALUES
(1, 1, 1),
(1, 2, 0),
(2, 1, 0),
(2, 2, 1);
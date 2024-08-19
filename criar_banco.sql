CREATE DATABASE aprovacao_credito;

CREATE TABLE IF NOT EXISTS historico_credito (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    nome TEXT NOT NULL,
    historico TEXT NOT NULL
);

USE aprovacao_credito;  -- Certifique-se de usar o banco de dados correto

INSERT INTO historico_credito (nome, historico) VALUES
    ('João', 'bom'),
    ('Maria', 'regular'),
    ('Pedro', 'ruim'),
    ('Ana', 'bom'),
    ('Carlos', 'regular'),
    ('Fernanda', 'bom'),
    ('Lucas', 'ruim'),
    ('Julia', 'bom'),
    ('Gustavo', 'regular'),
    ('Mariana', 'bom'),
    ('Rafael', 'ruim'),
    ('Isabella', 'bom'),
    ('Diego', 'regular'),
    ('Camila', 'bom'),
    ('Bruno', 'ruim'),
    ('Gabriela', 'bom'),
    ('Eduardo', 'regular'),
    ('Larissa', 'bom'),
    ('Henrique', 'ruim'),
    ('Amanda', 'bom');
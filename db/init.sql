-- Cria a tabela de filmes e alguns registros de exemplo.
-- Na imagem do MySQL, tudo que está em /docker-entrypoint-initdb.d roda só na primeira vez que o volume é criado.
USE loja;

CREATE TABLE IF NOT EXISTS filmes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(120) NOT NULL,
    ano INT NOT NULL
);

INSERT INTO filmes (titulo, ano) VALUES
    ('Matrix', 1999),
    ('Interestelar', 2014),
    ('Blade Runner 2049', 2017),
    ('Ex Machina', 2015);

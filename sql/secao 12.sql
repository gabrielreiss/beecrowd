create schema sqlcurso;

use sqlcurso;

/* cria tabela */
create table tabela(
	coluna1 varchar(30),
    coluna2 varchar(30),
    coluna3 varchar(30)
);

/* adiciona primary key, não tem o autoincremento */
alter table tabela
add primary key(coluna1);

/* adicionando coluna */
alter table tabela
add coluna4 varchar(30);

alter table tabela
add coluna100 varchar(30);


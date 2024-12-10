rentalcliente--- URI Online Judge SQL
--- By Edivânia Pontes
--- Problem 2988

use uri;

create table teams(
  id INTEGER PRIMARY KEY,
  name VARCHAR (50)
);

create table matches(
  id INTEGER PRIMARY KEY,
  team_1 INTEGER REFERENCES teams (id),
  team_2 INTEGER REFERENCES teams (id),
  team_1_goals INTEGER,
  team_2_goals INTEGER
);

INSERT INTO teams(id, name)
VALUES 
       (1, 'CEARA'),
       (2, 'FORTALEZA'),
       (3, 'GUARANY DE SOBRAL'),
       (4, 'FLORESTA');

INSERT INTO matches(id, team_1, team_2, team_1_goals, team_2_goals)
VALUES 
       (1, 4, 1, 0, 4),
       (2, 3, 2, 0, 1),
       (3, 1, 3, 3, 0),
       (4, 3, 4, 0, 1),
       (5, 1, 2, 0, 0),
       (6, 2, 4, 2, 1);

  /*  Execute this query to drop the tables */
  -- DROP TABLE teams, matches; --

/* tabela joinada */
SELECT *
FROM teams as t
INNER JOIN matches as m
ON t.id = m.team_2 OR t.id = m.team_1;


/* uri */
SELECT t.id,
		t.name, 
		COUNT(m.team_1) AS matches2
FROM teams as t
INNER JOIN matches as m
ON t.id = m.team_2 OR t.id = m.team_1
GROUP BY t.name;


/* Vitorias */

(SELECT 	m.team_1 as team,
		COUNT(m.team_1) as count
FROM matches as m
WHERE m.team_1_goals > m.team_2_goals
GROUP BY m.team_1)
union all
(SELECT 	m.team_2 as team,
		COUNT(m.team_2) as count
FROM matches as m
WHERE m.team_2_goals > m.team_1_goals
GROUP BY m.team_2);


/* */
SELECT 
	(SELECT t.name
	FROM teams as t
    WHERE t.id = team.id 
    ) AS name,
    
    (
    SELECT count(team_1)
    FROM matches
    WHERE team_1 = team.id
    )
    +(
    SELECT count(team_2) 
    FROM matches WHERE 
    team_2 = team.id
	) as matches,

	(
    (SELECT count(team_1)
    FROM matches as m
    WHERE team_1 = team.id
    AND m.team_1_goals > m.team_2_goals)
    +
    (SELECT count(team_2)
    FROM matches as m
    WHERE team_2 = team.id
    AND m.team_1_goals < m.team_2_goals
    )
    ) as victories,
    
    (
		(SELECT count(team_1)
        FROM matches as m
        WHERE team_1 = team.id
        AND m.team_1_goals < m.team_2_goals)
        +
        (SELECT count(team_2)
        FROM matches as m
        WHERE team_2 = team.id
        AND m.team_1_goals > m.team_2_goals
        )
    ) as defeats,
    
    (
		(SELECT count(team_1)
        FROM matches as m
        WHERE team_1 = team.id
        AND m.team_1_goals = m.team_2_goals
        ) +
        (SELECT count(team_2)
        FROM matches as m
        WHERE team_2 = team.id
        AND m.team_1_goals = m.team_2_goals) 
    ) AS draws,
    
    ( SELECT 	victories * 3 +
				draws 
    ) AS score
    
FROM teams team
ORDER BY score DESC;
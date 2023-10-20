-- lists all genres from hbtn_0d_tvshows
-- and displays number of rows linked to each one

SELECT tg.name AS "genre", COUNT(ts.id) AS "number_of_shows"
       FROM tv_genres tg
INNER JOIN tv_show_genres sg
      ON tg.id = sg.genre_id
INNER JOIN tv_shows ts
      ON ts.id = sg.show_id
GROUP BY tg.name
ORDER BY COUNT(ts.id) DESC;

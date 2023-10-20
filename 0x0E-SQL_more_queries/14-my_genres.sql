-- lists all genres from hbtn_0d_tvshows
-- and displays number of rows linked to each one

SELECT tg.name
       FROM tv_genres tg
INNER JOIN tv_show_genres sg
      ON tg.id = sg.genre_id
INNER JOIN tv_shows ts
      ON ts.id = sg.show_id
WHERE ts.title = "Dexter"
ORDER BY tg.name;

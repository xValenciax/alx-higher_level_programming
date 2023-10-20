-- lists all shows contained in hbtn_0d_tvshow

SELECT ts.title, tg.id AS "genre_id"
       FROM tv_shows ts
LEFT JOIN tv_show_genres sg
     ON ts.id = sg.show_id
LEFT JOIN tv_genres tg
     ON tg.id = sg.genre_id
ORDER BY ts.title, tg.id;

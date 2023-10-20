-- lists all shows
-- and all genres linked to that show

SELECT ts.title, tg.name
       FROM tv_shows ts
LEFT JOIN tv_show_genres sg
     ON ts.id = sg.show_id
LEFT JOIN tv_genres tg
     ON tg.id = sg.genre_id
ORDER BY ts.title, tg.name;

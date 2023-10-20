-- lists all shows in hbtn_0d_tvshows

SELECT s.title, g.id as "genre_id"
       FROM tv_shows s
INNER JOIN tv_show_genres sg
      ON s.id = sg.show_id
INNER JOIN tv_genres g
      ON sg.genre_id = g.id
ORDER BY s.title, g.id;

-- a script that lists all genres from hbtn_0d_tvshows
SELECT tv_show_genres.name AS 'genre', COUNT(*) AS 'number_of_shows'
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id=tv_show.id
ORDER BY COUNT(*) DESC;

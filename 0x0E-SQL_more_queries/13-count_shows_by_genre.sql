-- a script that lists all genres from hbtn_0d_tvshows
SELECT tv_genres.name AS 'genre', COUNT(*) AS 'number_of_shows'
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id=tv_show.genre_id
ORDER BY 'number_of_shows' DESC;

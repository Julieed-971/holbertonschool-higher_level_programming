-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of_shows 
FROM tv_show_genres
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show_genres.genre_id IS NOT NULL
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
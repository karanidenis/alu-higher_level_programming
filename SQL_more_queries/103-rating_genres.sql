-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(tv_genres_rating.rate) AS rating
FROM tv_genres
JOIN tv_genres_rating ON tv_genres_rating.genre_id = tv_genres.id
GROUP BY tv_genres
ORDER BY rating DESC;
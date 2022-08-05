-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(tv_genre_ratings.rate) AS rating
FROM tv_genres
JOIN tv_genre_ratings ON tv_genre_ratings.genre_id = tv_genres.id
GROUP BY tv_genres
ORDER BY rating DESC;
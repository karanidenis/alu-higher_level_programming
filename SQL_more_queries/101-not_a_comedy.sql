-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT DISTINCT tv_shows.title
FROM tv_genres
LEFT JOIN
(SELECT tv_shows.title
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
WHERE tv_genres.name = "Comedy"
ORDER BY tv_shows.title)
comedy_shows ON comedy_shows.title = tv_shows.title
WHERE tv_shows.title IS NULL
ORDER BY tv_shows.title;
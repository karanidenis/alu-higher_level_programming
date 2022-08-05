-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title
FROM tv_genres
JOIN tv_genres
    ON tv_genres.genre_id = tv_genres.id
JOIN tv_shows
    ON tv_genres.show_id = tv_shows.id
WHERE tv_genres.name =  "Comedy"
ORDER BY tv_shows.title;
-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tvshows
INNER JOIN title
ON tv_shows.title = tv_show_genres.genre_id
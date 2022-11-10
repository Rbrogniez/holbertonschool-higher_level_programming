-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
SELECT tv_show.titles, tv_show._genre_id
FROM tv_show INNER JOIN tv_show.genres
ON tv_show.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;

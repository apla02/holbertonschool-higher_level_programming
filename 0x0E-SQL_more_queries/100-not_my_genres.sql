-- lists all genres not linked to the show Dexter from  hbtn_0d_tvshows database

SELECT tv_genres.name
FROM  tv_genres 
WHERE tv_genres.name NOT IN
(SELECT  tv_genres.name
FROM tv_genres
LEFT OUTER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
LEFT OUTER JOIN tv_shows 
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter')
GROUP BY tv_genres.name;

SELECT * FROM (SELECT movie_id,info_type_id,info,kind_id FROM imdb.movie_info inner join imdb.title on imdb.movie_info.movie_id = imdb.title.id) AS T where (T.info_type_id = 16 and T.info like '%2000%' and T.info like '%USA%' and T.kind_id = 1);
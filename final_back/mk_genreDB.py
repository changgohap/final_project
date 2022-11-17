#  창근 페이지 건들거리지마시오
from django.shortcuts import render
import pandas
# from .models import Movie
import requests
import csv

# tmdb top_rated API 1페이지 ~ 5페이지까지
# for i in range(1, 5):
    # res=requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key=47deac5349c200ea6a8315d1f742e31d&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={i}&with_watch_monetization_types=flatrate3')
    # data=res.json()
# 
# 받은 json 데이터의 필요한 항목만 가져오기
    # for i in data['results']:
        # check.append(i)
        # movie_data.append({'id_num': i['id'], 'genre':['genre_ids']})
        # movie id 가져오기    
        # movie_id.append(i['id'])

# genre table 생성
res_genre = requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key=47deac5349c200ea6a8315d1f742e31d&language=en-US')
genre_data=res_genre.json()
genre_data_list = []
for i in genre_data['genres']:
    genre_data_list.append({ 'name': i['name'], 'genre_id': i['id']})

# df_movie = pandas.DataFrame(genre_data_list)
# df_movie.to_csv('genre_data.csv' ,encoding='utf-8-sig')
print(type(genre_data_list[0]['name']))
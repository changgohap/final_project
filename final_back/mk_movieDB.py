#  창근 페이지 건들거리지마시오
from django.shortcuts import render
import pandas
# from .models import Movie
import requests
import csv

movie_data = []
movie_id = []

# tmdb top_rated API 1페이지 ~ 5페이지까지
for i in range(1, 5):
    res=requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key=47deac5349c200ea6a8315d1f742e31d&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={i}&with_watch_monetization_types=flatrate3')
    data=res.json()

# 받은 json 데이터의 필요한 항목만 가져오기
    for i in data['results']:
        # check.append(i)
        movie_data.append({'id_num': i['id'], 'title':i['title'], 'release_date': i['release_date'], 'poster_path': i['poster_path'], 'overview': i['overview'], 'vote_average': i['vote_average'], 'original_title': i['original_title'], 'original_language': i['original_language'], 'backdrop_path': i['backdrop_path'], 'popularity': i['popularity']})
        # movie id 가져오기    
        movie_id.append(i['id'])

# print(movie_id)
for i in movie_id:
    movie_detail_res = requests.get(f'https://api.themoviedb.org/3/movie/{i}?api_key=47deac5349c200ea6a8315d1f742e31d&language=en-US')
    movie_detail_data = movie_detail_res.json()
    for movie in movie_data:
        if movie['id_num'] == i:
            # movie = ({'hompage' : movie_detail_data['homepage'], 'revenue' : movie_detail_data['revenue'], 'runtime' : movie_detail_data['runtime'], 'budget' : movie_detail_data['budget']})
            movie['homepage'] = movie_detail_data['homepage']
            movie['revenue'] = movie_detail_data['revenue'] 
            movie['runtime'] = movie_detail_data['runtime']
            movie['budget'] = movie_detail_data['budget']
        
df_movie = pandas.DataFrame(movie_data)
df_movie.to_csv('movie_data.csv' ,encoding='utf-8-sig')

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

movie_genre_list = []

for i in data['results']:
    # check.append(i)
    movie_genre_list.append({'movie_id': i['id'], 'genre_id': i['genre_ids'] })
    # movie id 가져오기    
    # movie_id.append(i['id'])
# # for k in range(len(movie_genre_list)):
#     print(movie_genre_list[0]['genre_id'][2])

movie_genre_data = []
for j in range(len(movie_genre_list)):
    for k in range(len(movie_genre_list[j]['genre_id'])):
        movie_genre_data.append({'movie_id': movie_genre_list[j]['movie_id'], 'genre_id': movie_genre_list[j]['genre_id'][k]})

df_movie = pandas.DataFrame(movie_genre_data)
df_movie.to_csv('movie_genre.csv' ,encoding='utf-8-sig')


# with open('movie_genre.csv', 'w', newline='',encoding='utf-8') as csvfile:
#     fieldnames = ['movie_id', 'genre_id']     # 데이터 컬럼 이름
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)     # 컬럼 이름들 작성
# # 
#     writer.writeheader()    # csv 파일에 컬럼이름 반영  
#     for obj in movie_genre_data:       # 위의 장르들 하나하나의 obj에 대해 반복문 돌면서
#         writer.writerow(obj)        # 작성을 해줌

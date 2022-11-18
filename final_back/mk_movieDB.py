#  창근 페이지 건들거리지마시오
from django.shortcuts import render
# from .models import Movie
import requests
import csv

movie_data = []
movie_id = []

# tmdb top_rated API 1페이지 ~ 5페이지까지
for i in range(1,2):
    res=requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key=47deac5349c200ea6a8315d1f742e31d&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={i}&with_watch_monetization_types=flatrate3')
    data=res.json()

# 받은 json 데이터의 필요한 항목만 가져오기
for i in data['results']:
    # check.append(i)
    movie_data.append({'id': i['id'], 'title':i['title'], 'release_date': i['release_date'], 'poster_path': i['poster_path'], 'overview': i['overview'], 'vote_average': i['vote_average'], 'original_title': i['original_title'], 'original_language': i['original_language'], 'backdrop_path': i['backdrop_path'], 'popularity': i['popularity']})
    # movie id 가져오기    
    movie_id.append(i['id'])

for i in movie_id:
    movie_detail_res = requests.get(f'https://api.themoviedb.org/3/movie/{i}?api_key=47deac5349c200ea6a8315d1f742e31d&language=en-US')
    movie_video_res = requests.get(f'https://api.themoviedb.org/3/movie/{i}/videos?api_key=47deac5349c200ea6a8315d1f742e31d&language=en-US')
    movie_detail_data = movie_detail_res.json()
    movie_video_data = movie_video_res.json()

    if len(movie_video_data['results']) == 0:
        movie_video_data['results'].append({'key': ''})

    for movie in movie_data:
        if movie['id'] == i:
            movie['homepage'] = movie_detail_data['homepage']
            movie['revenue'] = movie_detail_data['revenue'] 
            movie['runtime'] = movie_detail_data['runtime']
            movie['budget'] = movie_detail_data['budget']
            movie['youtube_key'] = movie_video_data['results'][0]['key']
            break
    # print(movie_video_data)

# print(movie_data[0])
# # print(movie_video_data['results'][0])




with open('movie.csv', 'w', newline='',encoding='utf-8') as csvfile:
    fieldnames = ['id', 'title', 'release_date', 'poster_path', 'overview', 'vote_average', 'original_title', 'original_language', 'backdrop_path', 'popularity', 'homepage', 'revenue', 'runtime', 'budget', 'youtube_key']    # 데이터 컬럼 이름
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)     # 컬럼 이름들 작성

    writer.writeheader()    # csv 파일에 컬럼이름 반영  
    for obj in movie_data:       # 위의 장르들 하나하나의 obj에 대해 반복문 돌면서
        writer.writerow(obj)        # 작성을 해줌



# print(movie_data)
# print(movie_id)
# print(movie_data)



        
# df_movie = pandas.DataFrame(movie_data)
# df_movie.to_csv('movie_data.csv' ,encoding='utf-8-sig')

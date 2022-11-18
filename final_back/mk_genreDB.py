# #  창근 페이지 건들거리지마시오
import requests
import csv

# from django.shortcuts import render
# import pandas
# # from .models import Movie
# import requests
# import csv

# # tmdb top_rated API 1페이지 ~ 5페이지까지
# # for i in range(1, 5):
#     # res=requests.get(f'https://api.themoviedb.org/3/discover/movie?api_key=47deac5349c200ea6a8315d1f742e31d&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page={i}&with_watch_monetization_types=flatrate3')
#     # data=res.json()
# # 
# # 받은 json 데이터의 필요한 항목만 가져오기
#     # for i in data['results']:
#         # check.append(i)
#         # movie_data.append({'id_num': i['id'], 'genre':['genre_ids']})
#         # movie id 가져오기    
#         # movie_id.append(i['id'])

# # genre table 생성
res_genre = requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key=47deac5349c200ea6a8315d1f742e31d&language=en-US')
genre_data=res_genre.json()
genre_data_list = genre_data['genres']

genre = [{'id':28, 'name': '액션'}, {'id':12, 'name': '모험'}, {'id':16,'name':'애니메이션'}, {'id':35,'name': '코미디'},
    {'id':80, 'name': '범죄'}, {'id':99, 'name': '다큐멘터리'}, {'id':18, 'name': '드라마'}, {'id':10751, 'name': '가족'}, {'id':14, 'name': '판타지'},
    {'id':36, 'name': '역사'}, {'id':27, 'name': '공포'}, {'id':10402, 'name':'음악'}, {'id':9648, 'name':'미스터리'}, {'id':10749, 'name':'로맨스'},
    {'id':878, 'name': 'SF'}, {'id':10770, 'name':'TV 영화'}, {'id':53, 'name': '스릴러'}, {'id':10752, 'name': '전쟁'}, {'id':37, 'name':'서부'}]


# open으로 genre.csv라는 파일을 만들어서 그 안에 작성하는 방식으로 열고 utf-8은 한글떄문에 넣은거
with open('genre.csv', 'w', newline='',encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name']     # 데이터 컬럼 이름
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)     # 컬럼 이름들 작성

    writer.writeheader()    # csv 파일에 컬럼이름 반영  
    for obj in genre_data_list:       # 위의 장르들 하나하나의 obj에 대해 반복문 돌면서
        writer.writerow(obj)        # 작성을 해줌




# for i in genre_data['genres']:
#     genre_data_list.append({ 'name': i['name'], 'genre_id': i['id']})

# # df_movie = pandas.DataFrame(genre_data_list)
# # df_movie.to_csv('genre_data.csv' ,encoding='utf-8-sig')
# print(type(genre_data_list[0]['name']))
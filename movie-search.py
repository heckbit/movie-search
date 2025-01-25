import imdb
import os

file_path = "D:\\Movies"
imdbpy = imdb.IMDb()

files = os.listdir(file_path)

# movie = imdbpy.get_movie('0372784')
# print(movie)

for file in files:
  movie_name = file.split(".")[0]
  extension = file.split(".")[1]
  
  movie_result = imdbpy.search_movie(movie_name)
  imdb_id = movie_result[0].getID()
  movie = imdbpy.get_movie(imdb_id)

  new_name = f"{movie.get('title')} ({movie.get('year')}) \u007bimdb-tt{imdb_id}\u007d.{extension}"

  print(new_name)

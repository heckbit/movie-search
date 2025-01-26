import imdb
import os

file_path = "D:\\Movies"
imdbpy = imdb.IMDb()

files = os.listdir(file_path)

for file in files:
  if file.find("imdb") == -1:
    movie_name = file.split(".")[0]
    extension = file.split(".")[1]

    movie_result = imdbpy.search_movie(movie_name)
    imdb_id = movie_result[0].getID()
    movie = imdbpy.get_movie(imdb_id)

    new_name = f"{movie.get('title')} ({movie.get('year')}) \u007bimdb-tt{imdb_id}\u007d.{extension}"
    new_name = new_name.replace(":","")
    new_name = new_name.replace("?","")

    print(f"Current: {file}")
    print(f"New: {new_name}")

    old_path = file_path + "\\" + file
    new_path = file_path + "\\" + new_name

    os.rename(old_path, new_path)


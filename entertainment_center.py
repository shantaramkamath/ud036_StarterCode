import fresh_tomatoes
from media import Movie

#Creating different Movie objects
pyaasa = Movie("Pyaasa",
               "The film tells the story of Vijay, a struggling poet trying to make his works known in post-independence India",
               "https://upload.wikimedia.org/wikipedia/en/9/9a/Pyaasa_1957_film_poster.jpg",
               "https://www.youtube.com/watch?v=pBZYJAzz5ys")

three_idiots = Movie("3 idiots",
                     "The film follows the friendship of three students at an Indian engineering college and is a satire about the social pressures under an Indian education system.",
                     "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
                     "https://www.youtube.com/watch?v=xvszmNXdM4w")

pk = Movie("pk",
           "The film questions religious dogmas and superstitions",
           "https://upload.wikimedia.org/wikipedia/en/c/c3/PK_poster.jpg",
           "https://www.youtube.com/watch?v=ZVmfNNVMcp0")

tzp = Movie("Taare Zameen Par",
            "The film is about a 8 year old dyslexic child and his teacher who helps him to overcome his disability.",
            "https://upload.wikimedia.org/wikipedia/en/b/b4/Taare_Zameen_Par_Like_Stars_on_Earth_poster.png",
            "https://www.youtube.com/watch?v=tn_2Ie_jtX8")

aaa = Movie("Andaaz Apna Apna",
               "The film has achieved a cult classic status among Hindi audiences",
               "https://upload.wikimedia.org/wikipedia/en/1/15/Andaz_Apna_Apna.jpg",
               "https://www.youtube.com/watch?v=fd_w7Qw8biU")

andhadhun = Movie("Andhadhun",
                  "The film tells the story of a piano player who unwillingly becomes embroiled in the murder of a former film actor.",
                  "https://upload.wikimedia.org/wikipedia/en/4/4a/Andhadhun_Movie_Poster.jpg",
                  "https://www.youtube.com/watch?v=2iVYI99VGaw")

#creating list of movies
movies = [pyaasa, three_idiots, pk, tzp, aaa, andhadhun]
#passing the list of movies as a parameter to fresh_tomatoes.open_movies_page() function
fresh_tomatoes.open_movies_page(movies)


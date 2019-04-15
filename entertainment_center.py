import fresh_tomatoes
from media import Movie

# Creating different Movie objects
pyaasa = Movie("Pyaasa",
               "The film tells the story a struggling poet trying to make his works known in post-independence India",  # NOQA
               "http://bit.ly/2UOpUeL",
               "https://www.youtube.com/watch?v=pBZYJAzz5ys"  # NOQA
               )

three_idiots = Movie("3 idiots",
                     "The film is a satire about the social pressures under an Indian education system.",   # NOQA
                     "http://bit.ly/2IyEgZZ",
                     "https://www.youtube.com/watch?v=xvszmNXdM4w"  # NOQA
                     )

pk = Movie("pk",
           "The film questions religious dogmas and superstitions",
           "http://bit.ly/2VHOI57",
           "https://www.youtube.com/watch?v=ZVmfNNVMcp0"  # NOQA
           )

tzp = Movie("Taare Zameen Par",
            "The film is about a 8 year old dyslexic child and his teacher who helps him to overcome his disability.",  # NOQA
            "http://bit.ly/2X3VmD0",
            "https://www.youtube.com/watch?v=tn_2Ie_jtX8"  # NOQA
            )

aaa = Movie("Andaaz Apna Apna",
               "The film has achieved a cult classic status among Hindi audiences",   # NOQA
               "http://bit.ly/2DfeOFk",
               "https://www.youtube.com/watch?v=fd_w7Qw8biU"  # NOQA
            )

andhadhun = Movie("Andhadhun",
                  "The film tells the story of a piano player who unwillingly becomes embroiled in the murder of a former film actor.",   # NOQA
                  "http://bit.ly/2KwM1Ci",
                  "https://www.youtube.com/watch?v=2iVYI99VGaw"   # NOQA
                  )

# creating list of movies
movies = [pyaasa, three_idiots, pk, tzp, aaa, andhadhun]
# passing the list of movies as a parameter to fresh_tomatoes.open_movies_page() function     # NOQA
fresh_tomatoes.open_movies_page(movies)

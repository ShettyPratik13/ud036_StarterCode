import media
import fresh_tomatoes

# Creating instance toy_story
toy_story = media.Movie("Toy Story", \
                        "A story of a boy and his toys that come to life", \
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", \
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

# Creating instance avatar
avatar = media.Movie("Avatar", \
                     "A marine on an alien planet", \
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", \
                     "https://www.youtube.com/watch?v=uZNHIU3uHT4")


# Creating instance dark_knight
dark_knight = media.Movie("The Dark Knight", \
                          "A vile young criminal calling himself the Joker throws the town into chaos", \
                          "http://filmisub.com/uploads/movies/155/1hRoyzDtpgMU7Dz4JF22RANzQO7.jpg", \
                          "https://www.youtube.com/watch?v=AcpW_cvkEnk")


# Creating instance ratatouille
ratatouille = media.Movie("Ratatouille", \
                          "He's dying to become a chef!", \
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", \
                          "https://www.youtube.com/watch?v=uVeNEbh3A4U")


# Creating instance black_panther
black_panther = media.Movie("Black Panther", \
                            "T'Challa returns home to the African nation of Wakanda to take his rightful place as king.", \
                            "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg", \
                            "https://www.youtube.com/watch?v=T7R7gn6_M7k")


# Creating instance pursuit_happyness
pursuit_happyness = media.Movie("The Pursuit of Happyness", \
                            "Chris refuses to give in to despair as he struggles to create a better life for himself and his son.", \
                            "https://upload.wikimedia.org/wikipedia/en/8/81/Poster-pursuithappyness.jpg", \
                            "https://www.youtube.com/watch?v=00uTFVnWJMw")



movies = [toy_story, avatar, dark_knight, ratatouille, black_panther, pursuit_happyness]

# Passing list of movies to open_movies_page function
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.VALID_RATINGS)



import webbrowser

class Movie():
    """ This class is a blueprint of a movie.

    This class defines the structure and attributes of a movie.
    It also contains a method to show the movie's trailer.

    Attributes:
        title: Movie title.
        storyline: The movie's storyline.
        poster_image_url: The url to the movie's poster.
        trailer_youtube_url: The url to the movie's trailer on youtube.
    """
    
    VALID_RATINGS = ["G","PG","PG-13","R"]
    def __init__(self, movie_title, movie_storyline, poster_image, \
                 trailer_youtube):
        """Initializes Movie instance"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Method to show movie trailer"""
        webbrowser.open(self.trailer_youtube_url)

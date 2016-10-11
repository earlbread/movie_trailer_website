class Movie:
    """This is Movie class for static site generation.

    Attributes:
        title (str) : Movie's title.
        poster_image_url (str) : Box art image url.
        trailer_youtube_url (str) : Movie trailer video url.

    """
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

import media
import fresh_tomatoes

movies = []

# Toy story
movie = (
    "Toy story",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc",
)
movies.append(media.Movie(*movie))

# Avatar
movie = (
    "Avatar",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=cRdxXPV9GNQ",
)
movies.append(media.Movie(*movie))

# School of rock
movie = (
    "School of rock",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc",
)
movies.append(media.Movie(*movie))

# Ratatouille
movie = (
    "Ratatouille",
    "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
    "https://www.youtube.com/watch?v=c3sBBRxDAqk",
)
movies.append(media.Movie(*movie))

# Midnight in Paris
movie = (
    "Midnight in Paris",
    "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=BYRWfS2s2v4",
)
movies.append(media.Movie(*movie))

# Hunger games
movie = (
    "Hunger games",
    "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg",  # NOQA
    "https://www.youtube.com/watch?v=4S9a5V9ODuY",
)
movies.append(media.Movie(*movie))

fresh_tomatoes.open_movies_page(movies)

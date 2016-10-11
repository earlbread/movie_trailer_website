import media
import fresh_tomatoes

# Toy story
title = "Toy story"
poster_image_url = "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
trailer_youtube_url = "https://www.youtube.com/watch?v=KYz2wyBy3kc"
toy_story = media.Movie(title, poster_image_url, trailer_youtube_url)

# Avatar
title = "Avatar"
poster_image_url = "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg"
trailer_youtube_url = "https://www.youtube.com/watch?v=cRdxXPV9GNQ"
avatar = media.Movie(title, poster_image_url, trailer_youtube_url)

# School of rock
title = "School of rock"
poster_image_url = "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg"
trailer_youtube_url = "https://www.youtube.com/watch?v=XCwy6lW5Ixc"
school_of_rock = media.Movie(title, poster_image_url, trailer_youtube_url)

# Ratatouille
title = "Ratatouille"
poster_image_url = "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg"
trailer_youtube_url = "https://www.youtube.com/watch?v=c3sBBRxDAqk"
ratatouille = media.Movie(title, poster_image_url, trailer_youtube_url)

# Midnight in Paris
title = "Midnight in Paris"
poster_image_url = "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg"
trailer_youtube_url = "https://www.youtube.com/watch?v=BYRWfS2s2v4"
midnight_in_paris = media.Movie(title, poster_image_url, trailer_youtube_url)

# Hunger games
title = "Hunger games"
poster_image_url = "https://upload.wikimedia.org/wikipedia/en/3/39/The_Hunger_Games_cover.jpg"
trailer_youtube_url = "https://www.youtube.com/watch?v=4S9a5V9ODuY"
hunger_games = media.Movie(title, poster_image_url, trailer_youtube_url)

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]
fresh_tomatoes.open_movies_page(movies)

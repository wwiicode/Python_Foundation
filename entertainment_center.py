import media 
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
						"A story of a boy and his toy that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
					 "Marine in alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=6ziBFh3V1aM")

#print(toy_story.movie_storyline)
#print(toy_story.trailer_youtube_url)

#toy_story.show_trailer()

school_of_rock = media.Movie("Schol of Rock", "Using rock music to learn",
							 "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
							 "https://www.youtube.com/watch?v=5afGGGsxvEA")

ratarouille = media.Movie("Ratatouille", "A rat is a chef in Paris",
					      "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
					      "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet arthors",
								"https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
								"https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games", "Storyline",
					"http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
					"https://www.youtube.com/watch?v=PbA63a7H0bo")


movies = [toy_story, avatar, school_of_rock, ratarouille, midnight_in_paris, hunger_games]

#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.valid_ratings)
print(media.Movie.__doc__)
print(media.Movie.__name__)
print(media.Movie.__name__)
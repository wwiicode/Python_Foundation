import webbrowser

class Movie():
	"""This class provides a way to store movie related information"""
	

	
	VALID_RATINGS = ["G", "PG", "PG-13", "R"]
	def __init__(self, movie_title,movie_storyline, movie_poster_image_url,
				trailer_youtube_url):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = movie_poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)

class Album():
	def __init__(self, title, artist, genre, id = None):
		self.title = title
		self.artist = artist
		self.genre = genre
		self.id = id
		
	def __repr__(self):
		return f"Album: ID_{self.id} {self.title} by {self.artist.name} ({self.genre}))"
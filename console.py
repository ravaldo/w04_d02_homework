import pdb 
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

##################################################################

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Prodigy")
artist_2 = Artist("Daft Punk")
artist_repository.save(artist_1)
artist_repository.save(artist_2)

artist_1.name = "The Prodigy"
artist_repository.update(artist_1)

artist_repository.delete(artist_2.id)

result = artist_repository.select_all()

for artist in result:
    print(artist.__dict__)

##################################################################

assert(artist_1.id is not None)
album_1 = Album("The Fat of the Land", artist_1, "Electronic")
album_repository.save(album_1)

album_2 = Album("Always Outnumbered, Never Outgunned", artist_1, "Electronic")
album_repository.save(album_2)

album_3 = Album("Invaders Must Die", artist_1, "Electronic")
album_repository.save(album_3)

albums = album_repository.find_albums_by_artist(artist_1)
assert(len(albums) == 3)

album_repository.delete(album_3.id)
albums = album_repository.find_albums_by_artist(artist_1)
assert(len(albums) == 2)

album_2.genre = "Electro Punk"
album_repository.update(album_2)

result = album_repository.select_all()

for album in result:
	print(album.__dict__)

##################################################################

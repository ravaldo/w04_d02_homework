from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album
import repositories.artist_repository as artist_repository

def select_all():
	albums = []
	cmd = "SELECT * FROM albums"
	results = run_sql(cmd)
	
	for row in results:
		artist = artist_repository.select(row['artist_id'])
		album = Album(
			row['title'],
			artist,
			row['genre'],
			row['id']
			)
		albums.append(album)
	return albums


def select(id):
	album = None
	
	cmd = "SELECT * FROM albums WHERE id = %s"
	values = [id]
	results = run_sql(cmd, values)
	
	if result is not None:
		artist = artist_rep.select(row['artist_id'])
		album = Album(
			row['title'],
			artist,
			row['genre'],
			row['id']
			)
	return album

def save(album):
	cmd = "INSERT INTO albums (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
	values = [album.title, album.artist.id, album.genre]
	
	results = run_sql(cmd, values)
	id = results[0]['id']
	album.id = id
	return album # is this necessary?
	
def delete_all():
	cmd = "DELETE FROM albums"
	run_sql(cmd)

def delete(id):
	cmd = "DELETE FROM albums WHERE id = %s"
	values = [id]
	run_sql(cmd, values)

def update(album):
	cmd = "UPDATE albums SET (title, artist_id, genre) = (%s, %s, %s) WHERE id = %s"
	values = [album.title, album.artist.id, album.genre, album.id]
	results = run_sql(cmd, values)
	
	
def find_albums_by_artist(artist):
	albums = []
	cmd = "SELECT * FROM albums where artist_id = %s"
	values = [artist.id]
	
	result = run_sql(cmd, values)
	
	for row in result:
		artist = artist_repository.select(row['artist_id'])
		album = Album(
			row['title'],
			artist,
			row['genre'],
			row['id']
			)
		albums.append(album)
	return albums
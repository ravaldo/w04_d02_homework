from db.run_sql import run_sql
from models.artist import Artist


def select_all():
	artists = []
	cmd = "SELECT * FROM artists"
	results = run_sql(cmd)
	
	for row in results:
		artist = Artist(row['name'], row['id'])
		artists.append(artist)
	return artists


def select(id):
	artist = None
	
	cmd = "SELECT * FROM artists WHERE id = %s"
	values = [id]
	result = run_sql(cmd, values)[0]
	
	if result is not None:
		artist = Artist(result['name'], result['id'])  # remember to grab the id
	return artist

def save(artist):
	cmd = "INSERT INTO artists (name) VALUES (%s) RETURNING *" # need the RETURNING to get the generated id
	values = [artist.name]
	
	results = run_sql(cmd, values)
	id = results[0]['id']
	artist.id = id
	return artist # is this necessary?
	
def delete_all():
	cmd = "DELETE FROM artists"
	run_sql(cmd)

def delete(id):
	cmd = "DELETE FROM artists WHERE id = %s"
	values = [id]
	run_sql(cmd, values)

def update(artist):
	cmd = "UPDATE artists SET name = %s WHERE id = %s"	# no parenthesis when setting a single column
	values = [artist.name, artist.id]
	results = run_sql(cmd, values)
	
 

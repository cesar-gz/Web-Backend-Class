import requests
print("................................. running all REST API calls\n")

r = requests.get('http://localhost:8000/api/tables/artists/rows?_limit=10&_search=Red%20Hot%20Chili%20Peppers')
r = r.json()
ArtistId = r['data']
ArtistId = ArtistId[0]['ArtistId']

url = "http://localhost:8000/api/tables/albums/rows?_schema=Title%2CArtistId&_filters=ArtistId%3A{}".format(ArtistId)
r = requests.get(url)
r = r.json()
print("1) Albums by the Red Hot Chili Peppers:")
Albums = r['data']
for a in Albums:
  print(a['Title'])

r = requests.get("http://localhost:8000/api/tables/artists/rows?_search=U2")
r = r.json()
ArtistId = r['data']
ArtistId = ArtistId[0]['ArtistId']

url = "http://localhost:8000/api/tables/albums/rows?_schema=AlbumId%2CTitle%2CArtistId&_filters=ArtistId%3A{}".format(ArtistId)
r = requests.get(url)
r = r.json()
AlbumId = r['data']
print("\n2) Genres associated with the artist U2:")
for a in AlbumId:
  id = str(a)
  id = id[12:15]

  url = "http://localhost:8000/api/tables/tracks/rows?_schema=AlbumId%2CGenreId&_extend=GenreId&_filters=AlbumId%3A{}".format(id)
  r = requests.get(url)
  r = r.json()
  Tracks = r['data']
  print("Genre: " + str(Tracks[0]['GenreId_data']['Name']))
  print("For the Album: " + str(a['Title']) + "\n" )

print("3) Names of tracks on the playlist “Grunge” and their associated artists and albums:\n")

r = requests.get('http://localhost:8000/api/tables/playlists/rows?_filters=name%3AGrunge')
r = r.json()
PlaylistId = r['data']
PlaylistId = PlaylistId[0]['PlaylistId']

url = "http://localhost:8000/api/tables/playlist_track/rows?_extend=TrackId&_limit=20&_filters=PlaylistId%3A{}".format(PlaylistId)
r = requests.get(url)
r = r.json()
Playlist = r['data']

for song in Playlist:
  name = song['TrackId_data']['Name']
  artist = song['TrackId_data']['Composer']
  album = song['TrackId_data']['AlbumId']
  print("Track name: " + str(name))
  print("Artist name: " + str(artist))
  print("Related Album id: " + str(album) + "\n")

url = "http://localhost:4000/graphql"
print("\n........................................ running all GraphQL calls")

query = """
  query{
    artist(where:{Name : "Red Hot Chili Peppers"}){
      artistId
      albums{
        title
      }
    }
  }
"""
payload = { 'query' : query }
r = requests.post(url, json=payload)
r = r.json()

albums = r['data']['artist']['albums']
print("\nAlbums by the Red Hot Chili Peppers:")
for a in albums:
  print(a['title'])

query = """
  query {
    artists(where: { Name: "U2" }) {
      artistId
      albums {
        albumId
        tracks {
          genreId
          genre {
            name
          }
        }
      }
    }
  }
"""
payload = { 'query' : query }
r = requests.post(url, json=payload)
r = r.json()

genre1 = r['data']['artists'][0]['albums'][0]['tracks'][0]['genre']['name']
genre2 = r['data']['artists'][0]['albums'][9]['tracks'][0]['genre']['name']
print("\nGenres associated with the artist U2:")
print(genre1 + " and " + genre2)

query = """
  query {
    playlists( where:{ Name:"Grunge" }) {
      playlistId
      tracks {
        name,
        composer,
        albumId
        album {
          title,
          artistId
          artist {
            name
          }
        }
      }
    }
  }
"""
payload = { 'query' : query }
r = requests.post(url, json=payload)
r = r.json()

tracks = r['data']['playlists'][0]['tracks']

print("\nNames of tracks on the playlist “Grunge” and their associated artists and albums:")
for t in tracks:
  print("\nTrack Name: " + t['name'])
  if t['composer']:
    print("Composer: " + t['composer'])
  else:
    print("Composer: None")
  print("Album title: " + t['album']['title'])
  print("Artist: " + t['album']['artist']['name'])

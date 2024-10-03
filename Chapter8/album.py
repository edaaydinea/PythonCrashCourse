def make_album(artist, title, num_songs=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

# Create three albums
album1 = make_album('Pink Floyd', 'The Dark Side of the Moon')
album2 = make_album('The Beatles', 'Abbey Road')
album3 = make_album('Led Zeppelin', 'Led Zeppelin IV', num_songs=8)

# Print each album
print(album1)
print(album2)
print(album3)

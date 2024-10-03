def make_album(artist, title, num_songs=None):
    """Build a dictionary describing a music album."""
    album = {'artist': artist, 'title': title}
    if num_songs:
        album['num_songs'] = num_songs
    return album

# Start a loop to collect user input for albums
while True:
    print("\nEnter the album information (or 'quit' to exit):")

    artist = input("Artist: ")
    if artist == 'quit':
        break

    title = input("Album Title: ")
    if title == 'quit':
        break

    album = make_album(artist, title)
    print(f"\nAlbum created: {album}")

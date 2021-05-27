class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album not in self.albums:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'
        return f'Band {self.name} already has {album.name} in their library.'

    def remove_album(self, album_name):
        albums = [album for album in self.albums if album.name == album_name]
        if not albums:
            return f'Album {album_name} is not found.'
        album = albums[0]
        if album.published:
            return f'Album has been published. It cannot be removed.'
        self.albums.remove(album)
        return f'Album {album_name} has been removed.'

    def details(self):
        res = f'Band {self.name}\n'
        for album in self.albums:
            res += album.details() + '\n'
        return res
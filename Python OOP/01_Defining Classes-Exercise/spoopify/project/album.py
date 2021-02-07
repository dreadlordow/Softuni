class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False
        for song in songs:
            self.add_song(song)

    def add_song(self, song):
        if song.name in map(lambda s: s.name, self.songs):
            return f'Song is already in the album.'
        elif self.published:
            return 'Cannot add songs. Album is published.'
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        self.songs.append(song)
        return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        songs_list = [s for s in self.songs if s.name == song_name]
        if self.published:
            return f'Cannot remove songs. Album is published.'
        elif not songs_list:
            return 'Song is not in the album.'

        self.songs.remove(songs_list[0])
        return f'Removed song {song_name} from album {self.name}.'

    def publish(self):
        if not self.published:
            self.published = True
            return f'Album {self.name} has been published.'
        return f'Album {self.name} is already published'

    def details(self):
        result = ''
        result += f'Album {self.name}\n'
        for song in self.songs:
            result += f'== {song.get_info()}\n'
        return result

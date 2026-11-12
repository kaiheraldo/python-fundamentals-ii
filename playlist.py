"""A very simple playlist."""


class SongNotFoundError(Exception):
    """The requested song is not in the playlist."""


songs = {
    "Bohemian Rhapsody": 354,
    "Despacito": 229,
}


def add_song(title, seconds):
    songs[title] = seconds


def find(title):
    if title not in songs:
        raise SongNotFoundError(f'"{title}" is not in the playlist')
    return songs[title]


def total_duration(*titles):
    return sum(find(title) for title in titles)

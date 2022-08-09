class Video:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    def like(self):
        self._likes += 1

    @property
    def likes(self):
        return self._likes

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    def __str__(self):
        return (f'{self._name} '
                f'- {self.year} '
                f'- {self.likes} \u2764 ')


class Movie(Video):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return (f'{self._name} '
                f'- {self.year} '
                f'- {self.duration} minutes '
                f'- {self.likes} \u2764 ')


class Series(Video):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return (f'{self._name} '
                f'- {self.year} '
                f'- {self.seasons} seasons '
                f'- {self.likes} \u2764 ')


class Playlist(list):
    def __init__(self, name, content):
        self.name = name
        self._content = content

    def __getitem__(self, item):
        return self._content[item]

    @property
    def listing(self):
        return self._content

    def __len__(self):
        return len(self._content)


avengers_3_movie = Movie('avengers - Infinity Wars', 2018, 160)
atlanta_series = Series('atlanta', 2018, 2)
the_godfather_1_movie = Movie('The Godfather', 1972, 155)
arcane_series = Series('Arcane', 2021, 1)

atlanta_series.like()
arcane_series.like()
arcane_series.like()

playlist1 = [avengers_3_movie, atlanta_series, the_godfather_1_movie, arcane_series]

weekend_playlist = Playlist("Weekend", playlist1)

print(f'Playlist size: {len(weekend_playlist)} items')

for i in weekend_playlist:
    print(i)

print(f'Is it on? {arcane_series in weekend_playlist}')

print(len(weekend_playlist))

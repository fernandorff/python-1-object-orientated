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


class Movie(Video):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration


class Series(Video):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


avenvers_3_movie = Movie('avengers - Infinity Wars', 2018, 160)
print(f'{avenvers_3_movie.name}\n'
      f'- Ano: {avenvers_3_movie.year}\n'
      f'- Duration: {avenvers_3_movie.duration}\n'
      f'- Likes: {avenvers_3_movie.likes}\n')

atlanta_series = Series('atlanta', 2018, 2)
print(f'{atlanta_series.name}\n'
      f'- Ano: {atlanta_series.year}\n'
      f'- Seasons: {atlanta_series.seasons}\n'
      f'- Likes: {atlanta_series.likes}\n')

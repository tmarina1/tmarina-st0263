from mrjob.job import MRJob

class peliculas7(MRJob):
    def mapper(self, _, line):
        User,Movie,Rating,Genre,Date = line.split(',')
        yield Genre, (int(Rating), int(Movie))

    def reducer(self, Genre, MovieRating):
        listaMovieRating = list(MovieRating)
        valores = [min(listaMovieRating), max(listaMovieRating)]
        yield Genre, valores

if __name__ == '__main__':
    peliculas7.run()

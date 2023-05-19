from mrjob.job import MRJob

class peliculas2(MRJob):
    def mapper(self, _, line):
        User,Movie,Rating,Genre,Date = line.split(',')
        yield Movie, [User, int(Rating)]

    def reducer(self, Movie, UserRating):
        listaUserRate = list(UserRating)
        
        cantidadUsuarios = 0
        ratingPromedio = 0
        for datos in listaUserRate:
            cantidadUsuarios += 1
            ratingPromedio += datos[1]
        ratingPromedio = ratingPromedio/len(listaUserRate)

        respuesta = [ratingPromedio, cantidadUsuarios]

        yield Movie, respuesta

if __name__ == '__main__':
    peliculas2.run()
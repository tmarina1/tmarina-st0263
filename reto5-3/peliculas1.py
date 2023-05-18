from mrjob.job import MRJob

class peliculas1(MRJob):
    def mapper(self, _, line):
        User,Movie,Rating,Genre,Date = line.split(',')
        yield User, int(Rating)

    def reducer(self, user, movieRate):
        listaMoviRate = list(movieRate)
        
        promedio = sum(listaMoviRate)/len(listaMoviRate)
        cantidadDePeliculasVistas = len(listaMoviRate)
        listaResultado = [cantidadDePeliculasVistas, promedio]
        
        yield user, listaResultado

if __name__ == '__main__':
    peliculas1.run()
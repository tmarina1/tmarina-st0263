from mrjob.job import MRJob
from mrjob.step import MRStep

class peliculas6(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                    reducer=self.reducer0),
            MRStep(reducer=self.reducer)
        ]

    def mapper(self, _, line):
        User,Movie,Rating,Genre,Date = line.split(',')
        yield Date, int(Rating)

    def reducer0(self, Date, Rating):
        listaRate = list(Rating)

        promedio = sum(listaRate)/len(listaRate)

        yield None, [promedio, Date]

    def reducer(self, _, val):
        val = list(val)
        valMax = max(val)
        yield valMax

if __name__ == '__main__':
    peliculas6.run()
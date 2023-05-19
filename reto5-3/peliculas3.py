from mrjob.job import MRJob
from mrjob.step import MRStep

class peliculas2(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper,
                    reducer=self.reducer0),
            MRStep(reducer=self.reducer)
        ]

    def mapper(self, _, line):
        User,Movie,Rating,Genre,Date = line.split(',')
        yield Date, 1

    def reducer0(self, Date, val):
        global peliculasPorDia
        val = sum(val)
        yield None, [val, Date]
    
    def reducer(self, _, val):
        val = list(val)
        valMin = min(val)
        yield valMin

if __name__ == '__main__':
    peliculas2.run()
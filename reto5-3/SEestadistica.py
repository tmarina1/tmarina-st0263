from mrjob.job import MRJob

class SEestadistica(MRJob):
    def mapper(self, _, line):
        idemp,sececon,salary,year = line.split(',')
        yield idemp, 1

    def reducer(self, idemp, valores):
        cantidad = sum(valores)
        yield idemp, cantidad

if __name__ == '__main__':
    SEestadistica.run()
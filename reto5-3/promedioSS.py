from mrjob.job import MRJob

class promedioES(MRJob):
    def mapper(self, _, line):
        idemp,sececon,salary,year = line.split(',')
        yield sececon, int(salary)

    def reducer(self, sececon, salary):
        lista = list(salary)
        promedio = sum(lista)/len(lista)
        yield sececon, promedio

if __name__ == '__main__':
    promedioES.run()
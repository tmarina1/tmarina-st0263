from mrjob.job import MRJob

class promedioSE(MRJob):
    def mapper(self, _, line):
        idemp,sececon,salary,year = line.split(',')
        yield idemp, int(salary)

    def reducer(self, idemp, salary):
        lista = list(salary)
        promedio = sum(lista)/len(lista)
        yield idemp, promedio

if __name__ == '__main__':
    promedioSE.run()
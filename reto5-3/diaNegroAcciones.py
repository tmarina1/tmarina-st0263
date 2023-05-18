from mrjob.job import MRJob
from mrjob.step import MRStep

class diaNegroAcciones(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapperr,
                    reducer=self.reducer0),
            MRStep(reducer=self.reducer)
        ]

    def mapperr(self, _, line):
        company,price,date = line.split(',')
        yield date, float(price)

    def reducer0(self, date, price):
        valor = []
        listaPrecio = list(price)
        for precio in listaPrecio:
            valor.append(precio)
        cantidad = sum(valor)
        yield None, (date, cantidad)

    def reducer(self, _, cantidad):
        val = list(cantidad)
        valMin = min(val)
        yield valMin

if __name__ == '__main__':
    diaNegroAcciones.run()
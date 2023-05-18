from mrjob.job import MRJob

class mayormenorAccion(MRJob):
    def mapper(self, _, line):
        company,price,date = line.split(',')
        yield company, (date, float(price))

    def reducer(self, company, datePrice):
        listaFechaPrecio = list(datePrice)
        lista = []
        listaMinimo = []
        listaMaximo = []
        valorMaximo = 0
        valorMinimo = 1000000
        for i in listaFechaPrecio:
            if i[1] < valorMinimo:
                valorMinimo = i[1]
                if not listaMinimo:
                    listaMinimo.append(i[0])
                else:
                    listaMinimo.pop()
                    listaMinimo.append(i[0])
            if i[1] > valorMaximo:
                valorMaximo = i[1]
                if not listaMaximo:
                    listaMaximo.append(i[0])
                else:
                    listaMaximo.pop()
                    listaMaximo.append(i[0])
        yield company, [listaMinimo,listaMaximo]
        
if __name__ == '__main__':
    mayormenorAccion.run()
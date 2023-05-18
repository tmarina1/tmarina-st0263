from mrjob.job import MRJob

class estadoAcciones(MRJob):
    def mapper(self, _, line):
        company,price,date = line.split(',')
        yield company, float(price)

    def reducer(self, company, price):
        listaPrecio = list(price)
        precioactual = 0
    
        for precio in listaPrecio:
          if precio >= precioactual:
            estado = 'Se mantine estable'
            precioactual = precio
          else:
            precioactual = precioactual
            estado = 'No se mantiene estable'
        yield company, estado

if __name__ == '__main__':
    estadoAcciones.run()
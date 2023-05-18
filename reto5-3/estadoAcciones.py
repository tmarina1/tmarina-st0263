from mrjob.job import MRJob

class estadoAcciones(MRJob):
    def mapper(self, _, line):
        company,price,date = line.split(',')
        yield company, float(price)

    def reducer(self, company, price):
        listaPrecio = list(price)
        precioactual = 0
        estado = ''
    
        for precio in listaPrecio:
          if precio > precioactual or precio == precioactual:
            estado = 'Se mantine estable'
            precioactual = precio
          else:
            estado = 'No se mantiene estable'
        if estado == 'Se mantine estable':
          yield company, estado

if __name__ == '__main__':
    estadoAcciones.run()

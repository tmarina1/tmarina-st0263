import os
import grpc
import search_pb2
import search_pb2_grpc
import sys
from concurrent import futures

sys.path.insert(0, 'microServicio')

from MS1 import buscarArchivo, listarArchivos
import configuracion

class MyService(search_pb2_grpc.SearchServiceServicer):
  def Search(self, request, context):
      # Perform the search and return the results
      archivo = []
      peticion = str(request)
      if '-' in peticion:
        nombreArchivo = peticion.split('-', 1)
        nombreArchivo = nombreArchivo[1]
        nombreArchivo = nombreArchivo[:-2]
        archivo = buscarArchivo(nombreArchivo)
      else:
        archivo = listarArchivos()
      return search_pb2.SearchResponse(results=archivo)

def servidor():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  search_pb2_grpc.add_SearchServiceServicer_to_server(MyService(), server)
  server.add_insecure_port(f'[::]:{configuracion.PUERTO}')
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
  servidor()

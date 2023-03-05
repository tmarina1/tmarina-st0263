from fastapi import FastAPI
import sys
sys.path.insert(1, 'MOM')
import consumer
import producer
import grpc
sys.path.insert(1, 'gRPC')
import search_pb2
import search_pb2_grpc

sys.path.insert(0, 'gRPC/microServicio')
import configuracion

from google.protobuf.json_format import MessageToDict

app = FastAPI()
roundRobin = 0

@app.get("/listFiles")
async def root():
  global roundRobin
  request = 'listFiles'
  if roundRobin == 0:
    try:
      conexion = mom(request)
      roundRobin = 1
    except:
      conexion = gRPC(request)
      roundRobin = 1
  elif roundRobin == 1:
    try:
      conexion = gRPC(request)
      roundRobin = 0
    except:
      conexion = mom(request)
      roundRobin = 0

  return {"message": conexion}

@app.get("/searchFile/{archivo}")
async def root(archivo):
  global roundRobin
  request = f'searchFile-{archivo}'
  if roundRobin == 0:
    try:
      conexion = mom(request)
      roundRobin = 1
    except:
      conexion = gRPC(request)
      roundRobin = 1
  elif roundRobin == 1:
    try:
      conexion = gRPC(request)
      roundRobin = 0
    except:
      conexion = mom(request)
      roundRobin = 0
  
  return {"message": conexion}

def gRPC(request):
  channel = grpc.insecure_channel(f'{configuracion.IP}:{configuracion.PUERTO}')
  stub = search_pb2_grpc.SearchServiceStub(channel)
  response = stub.Search(search_pb2.SearchRequest(query=request))
  response  = MessageToDict(response)
  return response 

def mom(request):
  producer.productor(request)
  consumer.consumidor1()
  response = consumer.consumidor2()
  return response

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)

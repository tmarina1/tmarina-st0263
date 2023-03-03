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
  if roundRobin == 0:
    producer.productor('listFiles')
    consumer.consumidor1()
    response = consumer.consumidor2()
    print(response)
    roundRobin = 1
  elif roundRobin == 1:
    print("entro aca")
    request = 'listFiles'
    channel = grpc.insecure_channel(f'{configuracion.IP}:{configuracion.PUERTO}')
    stub = search_pb2_grpc.SearchServiceStub(channel)
    response = stub.Search(search_pb2.SearchRequest(query=request))
    print(response)
    response = MessageToDict(response)
    roundRobin = 0

  return {"message": response}

@app.get("/searchFile/{archivo}")
async def root(archivo):
  global roundRobin
  request = f'searchFile-{archivo}'
  if roundRobin == 0:
     producer.productor(request)
     consumer.consumidor1()
     response = consumer.consumidor2()
     roundRobin = 1
  elif roundRobin == 1:
    channel = grpc.insecure_channel(f'{configuracion.IP}:{configuracion.PUERTO}')
    stub = search_pb2_grpc.SearchServiceStub(channel)
    response = stub.Search(search_pb2.SearchRequest(query=request))
    response = MessageToDict(response)
    roundRobin = 0

  return {"message": response}

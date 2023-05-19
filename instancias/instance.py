import grpc
import messages_pb2
import messages_pb2_grpc
from random import random,choices
from concurrent import futures

uso = 30
estado = 0

class messageService(messages_pb2_grpc.messageServiceServicer):
    def message(self, request, context):
        if request.estado == 'EstaVivo':
            CPU = usoCPU()
            return messages_pb2.messageResponse(respuesta = "estoyVivo", usoCPU = CPU)
        if request.estado == 'Evento':
            reset()
            return messages_pb2.messageResponse(respuesta = "reseteado")

def usoCPU():
    global uso
    global estado
    if estado == 0:
        delta = random()
        print(f'DELTA1 --> {delta}')
        if delta <= 0.5:
            uso -= 1
        else:
            uso +=1
        
        delta2 = random()
        print(f'DELTA2 --> {delta2}')
        if delta2 >= 0.8 and delta2<=0.85:
            estado = 2
        elif delta2 >0.85 and delta2<=0.9:
            estado = 1
        else: 
            estado = 0
    elif estado == 1 and uso <100:
        print(uso)
        uso += 2
    elif estado == 2 and uso > 0:
        print(uso)
        uso -= 2
    
    return uso

def reset():
    global uso
    global estado
    uso = 30
    estado = 0

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    messages_pb2_grpc.add_messageServiceServicer_to_server(messageService(), server)
    server.add_insecure_port(f'[::]:8080')
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

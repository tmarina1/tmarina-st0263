# https://medium.com/better-programming/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
# consumer.py
# Consume RabbitMQ queue
import pika
import os
import producer
import configuracionMOM
val = ''

def consumidor1():
  connection = pika.BlockingConnection(pika.ConnectionParameters(configuracionMOM.IP, configuracionMOM.PUERTO, '/', pika.PlainCredentials("user", "password")))
  channel = connection.channel()
  def callback(ch, method, properties, body):
      body = body.decode('utf-8')
      if '-' in body: #searchFile
        nombreArchivo = body.split('-', 1)
        nombreArchivo = nombreArchivo[1]
        nombreArchivo = nombreArchivo[:-2]
        lista = buscarArchivos(configuracionMOM.DIRECTORIO, nombreArchivo)
        lista = str(lista)
        print(lista)
        producer.productor1(lista)
        print("salio por aca")
        connection.close()
      else: #listFiles
        lista = listarArchivos(configuracionMOM.DIRECTORIO)
        lista = str(lista)
        print(lista)
        producer.productor1(lista)
        print("salio por aca")
        connection.close()
  channel.basic_consume(queue="my_app", on_message_callback=callback, auto_ack=True)
  channel.start_consuming()

def consumidor2():
  connection = pika.BlockingConnection(pika.ConnectionParameters(configuracionMOM.IP, configuracionMOM.PUERTO, '/', pika.PlainCredentials("user", "password")))
  channel = connection.channel()

  def callback(ch, method, properties, body):
      print('consumidor2')
      print(body)
      body = body.decode('utf-8')
      global val
      val = body
      connection.close()
      return val
  print(f'imprimiendo el valor: {val}')
  channel.basic_consume(queue="response", on_message_callback=callback, auto_ack=True)
  channel.start_consuming()
  return val

def listarArchivos(directorio):
    listaDirectorios = os.listdir(directorio)
    return listaDirectorios

def buscarArchivos(directorio, nombreArchivo):
    archivo = []
    for root, dirs, files in os.walk(directorio):
      for file in files:
        if nombreArchivo in file:
          archivo.append(os.path.join(root, file))
    return archivo

import pika
import configuracionMOM

def productor(consulta):
    connection = pika.BlockingConnection(pika.ConnectionParameters(configuracionMOM.IP, configuracionMOM.PUERTO, '/', pika.PlainCredentials('user', 'password')))
    channel = connection.channel()

    print(f'en productor {consulta}')
    channel.basic_publish(exchange='my_exchange', routing_key='test', body=consulta)

    connection.close()

def productor1(consulta):
    connection = pika.BlockingConnection(pika.ConnectionParameters(configuracionMOM.IP, configuracionMOM.PUERTO, '/', pika.PlainCredentials('user', 'password')))
    channel = connection.channel()

    print(f'en productor1 {consulta}')
    channel.basic_publish(exchange='my_exchange', routing_key='test1', body=consulta)

    connection.close()

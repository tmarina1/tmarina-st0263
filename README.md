# ST0263
# Tomas Marin Aristizabal, tmarina@eafit.edu.co
# Edwin Montoya, edwinM@eafit.edu.co

#1

##1.1

Cumpli con todos los componentes debedo a que realice el api gateway, la comunicacion entre el api gateway con el microservicio 1 y con el microservicio 2 
el primero con RPC(gRPC) y el segundo mediente el uso de MOM(RabbitMQ).

##2

Se podria decir que el reto cumple con un patron conocido como CAR

##3

Para el desarrollo de este reto se uso python con la ayuda de algunas librerias como os, sys, grpc, pika.
Ademas se uso fastapi para el desarrollo del api gateway.

para ejecturar el proyecto:

* Se debe iniciar la maquina virtual
* Se hace la conxion con la maquina
* Luego se debe iniciar el contener de docker con el comando "docker start 6472190018f657b0744618ad67ba4db7c7694dd00a9fb6d02cb26cac9f9ec8c7docker start 6472190018f657b0744618ad67ba4db7c7694dd00a9fb6d02cb26cac9f9ec8c7"
* Se debe de dirigir a la ruta "cd st0256/reto2" y correr el comendo para iniciar el fastapi "uvicorn api:app --host 0.0.0.0"

Si se decea modificar algun parametro de las configuraciones se debe acceder a la carpeta MOM o a "cd /gRPC/microServicio" y modificar los respectivos archivos
de conficuraciones


#4

#5

Para el desarrollo del reto se consultaron las siguientes paginas web:
* https://www.rabbitmq.com/tutorials/tutorial-six-python.html
* https://betterprogramming.pub/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
* https://fastapi.tiangolo.com/tutorial/
* https://grpc.io/docs/languages/python/basics/

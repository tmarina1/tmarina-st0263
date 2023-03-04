# Info de la materia: ST0263
# Estudiante: Tomas Marin Aristizabal, tmarina@eafit.edu.co
# Profesor: Edwin Montoya, emontoya@eafit.edu.co
# Reto 2

1

*1.1

Cumpli con todos los componentes debedo a que realice el api gateway, la comunicacion entre el api gateway con el microservicio 1 y con el microservicio 2 
el primero con RPC(gRPC) y el segundo mediente el uso de MOM(RabbitMQ).

2

Se podria decir que el reto cumple con un patron de diseño conocido como BFF, el cual esta diseñado para la implementación de microServicios y considera que el uso de los servicios se da mediante clientes que tienen necesidades y requerimientos especificos, que en nuestro caso seria el requerimeinto o necesidad de listar o buscar archivos.

3

* Para el desarrollo de este reto se uso python con la ayuda de algunas librerias como os, sys, grpc, pika.
* El reto se desplego en AWS, en especifico en una maquina virtual.
* Se uso fastapi para el desarrollo del api gateway.

para ejecturar el proyecto:

* Se debe iniciar la maquina virtual
* Se hace la conxion con la maquina
* Luego se debe iniciar el contener de docker con el comando "docker start 6472190018f657b0744618ad67ba4db7c7694dd00a9fb6d02cb26cac9f9ec8c7"
* Se debe de dirigir a la ruta "cd st0256/reto2" y correr el comendo para iniciar el fastapi "uvicorn api:app --host 0.0.0.0"

* Si se decea modificar algun parametro de las configuraciones se debe acceder a  "cd /MOM" o a "cd /gRPC/microServicio" y modificar los respectivos archivos
de conficuraciones.

* LOs puertos usados son el 8080 para la comunicacion del apiGateWay con el servidor de gRPC, el puerto 5672 para la comunicación del programa con RabbitMQ y el puerto 15672 para poder acceder al administrador de RabbitMQ. 

4

* Los archivos de configuraciones permiten modificar la carpeta en la que se haran las busquedas.
* La IP utilizada para la las conexiones en la 127.0.0.1 osea localhost.
* Para utilizar el reto 2 debe de buscar en el navegador lo siguiente: IPMaquinaVirtual:8000/listFiles para listar los archivos de un directorio o IPMaquinaVirtual:8000/searchFile/nombreArchivo para buscar un archivo en concreto dentro de un directorio.


5

Para el desarrollo del reto se consultaron las siguientes paginas web:
* https://www.rabbitmq.com/tutorials/tutorial-six-python.html
* https://betterprogramming.pub/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
* https://fastapi.tiangolo.com/tutorial/
* https://grpc.io/docs/languages/python/basics/

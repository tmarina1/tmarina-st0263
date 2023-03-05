# Info de la materia: ST0263 - Tópicos de telemática.
# Estudiante: Tomas Marin Aristizabal, tmarina@eafit.edu.co
# Profesor: Edwin Montoya, emontoya@eafit.edu.co
# Reto 2

1.
1.1

Cumpli con todos los componentes debedo a que realice el api gateway, la comunicacion entre el api gateway con el microservicio 1 y con el microservicio 2 
el primero con RPC(gRPC) y el segundo mediente el uso de MOM(RabbitMQ), ademas de implemetar el comportamiento de Round Robin para ir alternando la consultas entre ambos microservicios.

2

Se podría decir que el reto cumple con un patrón de diseño conocido como BFF, el cual esta diseñado para la implementación de microServicios y considera que el uso de los servicios se da mediante clientes que tienen necesidades y requerimientos específicos, que en nuestro caso seria el requerimiento o necesidad de listar o buscar archivos. Además, se debe resaltar que en si las comunicaciones siguen una arquitectura cliente/servidor donde el cliente realiza consultas y el servidor le manda la respuesta encontrada.

3

* Para el desarrollo de este reto se uso python con la ayuda de algunas librerias como os, sys, grpc, pika.
* El reto se desplego en AWS, en especifico en una maquina virtual que corre con linux ubuntu.
* Se uso fastapi para el desarrollo del api gateway.
* El código utiliza un metodo de Round Robin con el fin de utilizar un metodo de conexion diferente en cada consulta, ya sea gRPC o MOM, además de contar con un manejo de errores en el cual si uno de los microservicios no responde se dirigira a preguntarle a el otro microservicio.

para ejecturar el proyecto:

* Se debe iniciar la maquina virtual
* Se hace la conexión con la maquina
* Se debe de dirigir a la ruta "cd st0256/reto2" y correr el comendo para iniciar el fastapi "uvicorn apiGateWay:app --host 0.0.0.0"

* Si se decea modificar algun parametro de las configuraciones se debe acceder a  "cd /MOM" o a "cd /gRPC/microServicio" y modificar los respectivos archivos
de conficuraciones.

* Los puertos usados son el 8080 para la comunicacion del apiGateWay con el servidor de gRPC, el puerto 5672 para la comunicación del programa con RabbitMQ y el puerto 15672 para poder acceder al administrador de RabbitMQ. 

4

* Los archivos de configuraciones permiten modificar la carpeta en la que se haran las busquedas, los puertos de conexión y las IP.
* La IP utilizada para las conexiones en la 127.0.0.1 osea localhost.
* La IP por la que el apiGateWay escucha es la 0.0.0.0 permitienso asi el acceso desde cualquier dirección IP.

* Para utilizar el reto 2 debe de buscar en el navegador lo siguiente: IPMaquinaVirtual:8000/listFiles para listar los archivos de un directorio o IPMaquinaVirtual:8000/searchFile/nombreArchivo para buscar un archivo en concreto dentro de un directorio, ejemplo: http://100.25.102.33:8000/searchFile/MS1.py.

Resultados:

<img width="434" alt="image" src="https://user-images.githubusercontent.com/68928376/222937514-2cbbac1b-2b46-471b-989c-05c3d6dd3cbc.png">
<img width="749" alt="image" src="https://user-images.githubusercontent.com/68928376/222937519-74d50df4-9b4f-42ac-9773-1c22f6e31c02.png">

5

Para el desarrollo del reto se consultaron las siguientes paginas web:
* https://www.rabbitmq.com/tutorials/tutorial-six-python.html
* https://betterprogramming.pub/introduction-to-message-queue-with-rabbitmq-python-639e397cb668
* https://fastapi.tiangolo.com/tutorial/
* https://grpc.io/docs/languages/python/basics/
* https://docs.docker.com/
* https://pika.readthedocs.io/en/stable/modules/channel.html

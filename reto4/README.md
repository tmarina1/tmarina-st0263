
# Info de la materia: ST0263 Tópicos especiales de telemática

# Estudiante(s): Tomas Marin Aristizábal (tmarina@eafit.edu.co), Simón Cárdenas Villada (sicarvi@eafit.edu.co)

# Profesor: Edwin Montoya, emontoya@eafit.edu.co

# Reto # 4

# 1. breve descripción de la actividad

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Se cumplió con todos los requerimientos expuestos por el profesor, mediante la creación de un balanceador de carga encargado de balancear el autoscaling group que tenia las instancias de Moodle, dichas instancias se conectan a una base de datos y a un servidor NFS ambos creados desde GCP.
## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)
Se cumplió con todo lo estipulado por el profesor
# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.
Para este reto se siguió la siguiente arquitectura:
  
![image](https://user-images.githubusercontent.com/68928376/235477905-e403f783-063a-4721-b5f1-aaae670957a5.png)

Como podemos ver en esta arquitectura se tiene en la parte superior un balanceador de carga que tiene la función de gestionar el grupo de instancias que cuentan con la configuración de Moodle, mas abajo se encuentra la base de datos que como se dijo anterior mente se contrata como un servicio de GCP y por ultimo se encuentra el servidor NFS que permite el almacenamiento de archivos estáticos.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerías, paquetes, etc, con sus números de versiones.

## como se compila y ejecuta.
Para la ejecución del reto se tuvieron que crear y usar diferentes servicios de GCP, como por ejemplo el balanceador de carga que se enlazaba con un grupo de instancias que contaban con la capacidad de crecer a medida que se fueran aumentando los requerimientos de la aplicación, una base de datos adquirida desde GCP y un NFS server obtenido desde FileStorage de GCP, cabe resaltar que para el correcto uso del reto se debieron iniciar y mantener prendidas todas las instancias descritas anteriormente.
## detalles del desarrollo
Para el desarrollo del reto primero se creo una maquina virtual donde se hizo la configuración de todos los requerimientos necesarios para correr el Moodle, la base de datos y el servidor NFS, las configuraciones que se realizaron en esta instancia fueron las siguientes:
  
# Configuración para la instancia de Moodle:
  
  ![image](https://user-images.githubusercontent.com/68928376/235477958-0e18fff2-a846-4d52-857b-336857cc4a5c.png)

Configuración conexión con el NFS:

  ![image](https://user-images.githubusercontent.com/68928376/235478006-fc4d17bb-399e-4900-ae26-54385775b63e.png)

Automatización de arranque con mount a el NFS server:

  ![image](https://user-images.githubusercontent.com/68928376/235478070-e0a9d315-0eea-49a6-ae6e-3d452b47b655.png)

# Para la creación de la base de datos se siguió la siguiente configuración:

  ![image](https://user-images.githubusercontent.com/68928376/235478383-ff28318e-3b2d-4837-b691-85c4a55af5a6.png)

Configuración para la creacción de la base de datos:
  
  ![image](https://user-images.githubusercontent.com/68928376/235478463-c059f82e-6881-456b-be79-e9e90007778c.png)
 
Servicio para la base de datos creada:
  
  ![image](https://user-images.githubusercontent.com/68928376/235478541-43454824-2fc9-4982-b79a-c544167b7262.png)

Datos para conexion con la base de datos:
  
  ![image](https://user-images.githubusercontent.com/68928376/235478637-bb54f5ae-de78-484d-b62f-19e2d2f081db.png)

Base de datos creada:
  
  ![image](https://user-images.githubusercontent.com/68928376/235479433-bc8e9c6b-da7c-4288-b4f8-08f671b26760.png)

# Configuración para el desarrollo del servidor NFS:
  
![image](https://user-images.githubusercontent.com/68928376/235479781-51e6045f-0895-4926-baf0-a2f5f290fcbe.png)

Configuración de creaccion del NFS:
  
  ![image](https://user-images.githubusercontent.com/68928376/235479831-5d415540-1f47-4fb2-a6bf-136907b2ec35.png)

NFS creado y punto de acceso:
  
  ![image](https://user-images.githubusercontent.com/68928376/235479900-4292b9e0-bf04-43d0-a5ab-b9bc15fc837f.png)

# Configuración para la creacción de Imagen:
  
  ![image](https://user-images.githubusercontent.com/68928376/235480009-edd4eecc-2093-4a39-b6da-2ad649f68ee2.png)

  ![image](https://user-images.githubusercontent.com/68928376/235480045-fd7ce5cc-9168-4fce-a8a6-485fdf615a25.png)

  ![image](https://user-images.githubusercontent.com/68928376/235480076-99334291-1822-42d3-b52f-de605207e85e.png)
  
# Configuración para el template
  
  ![image](https://user-images.githubusercontent.com/68928376/235480222-86cac82b-a5f2-4867-bd57-dce252af8d8b.png)

Configuración del disco de arranque para el template:
  
  ![image](https://user-images.githubusercontent.com/68928376/235480293-e6c19ac2-2ea0-4fed-af20-0daa369873ca.png)

Template  creado correctamente:
  
  ![image](https://user-images.githubusercontent.com/68928376/235480381-bc9deaba-acb4-4443-b331-1c3e03b29c43.png)

# Configuración del grupo de instancias
 
  ![image](https://user-images.githubusercontent.com/68928376/235480459-4c9bef53-1548-480f-a3d9-0f4a6acd3733.png)

Configuración del autoescaling group:
  
  ![image](https://user-images.githubusercontent.com/68928376/235480526-5bd8efc4-5aec-4f40-ab13-44fee8fa1a4d.png)

Configuración verificador de estado:
  
  ![image](https://user-images.githubusercontent.com/68928376/235480663-0b88dbd5-f425-4af5-a1d3-cb51f5132d45.png)

Grupo de instancias creado:
  
  ![image](https://user-images.githubusercontent.com/68928376/235480704-8c9a8ae4-e937-4f57-b27d-0bde603eb75c.png)
  
  ![image](https://user-images.githubusercontent.com/68928376/235480735-cf0fd272-cc42-4bab-af20-b0ecf4c4ad16.png)

# Configuración para el balanceador de carga:
  
  ![image](https://user-images.githubusercontent.com/68928376/235481036-f65bcf61-821c-45ae-884b-0a3f5055bf94.png)

  ![image](https://user-images.githubusercontent.com/68928376/235481109-01684525-6c92-434c-b026-eb5294a6c5da.png)

Balanceador creado:
  
  ![image](https://user-images.githubusercontent.com/68928376/235481199-3d1283b4-76aa-4321-8194-758cee377da1.png)

Certificado SSL:
  
  ![image](https://user-images.githubusercontent.com/68928376/235481230-6f1b8ef9-7d03-4c5e-89a8-c4796cb61281.png)

# Página funcionando correctamente:
  
  ![image](https://user-images.githubusercontent.com/68928376/235481291-6f073da3-ccf3-4c84-9d4c-8d20ba2e8273.png)
  
  ![image](https://user-images.githubusercontent.com/68928376/235481305-da3f6334-5840-4e1e-91ce-1d85302183cb.png)


# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 

# 5. otra información que considere relevante para esta actividad.

# referencias:

* https://cloud.google.com/filestore/docs/create-instance-console?hl=es-419
* https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-20-04-es
* https://hub.docker.com/r/bitnami/moodle

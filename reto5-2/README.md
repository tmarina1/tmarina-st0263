# Info de la materia: ST0263 Tópicos especiales en telemática
# Estudiante(s): Tomas Marin Aristizabal, tmarina@eafit.edu.co

# Profesor: Edwin Montoya, emontoya@eafit.edu.co

# Reto # 5-2

# 1. Breve descripción de la actividad

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Se cumplió con todos los requerimientos debido a se realizo la creacción de un Bucket s3 con nombre st0263tmarina este con el fin de almacenar los archivos que se manejen en el cluster, ademas se creo el cluster en el cual se descargaron las aplicaciones de Hadoop, Hue, Zeppelin, Jupyther. Como tambien se hizo el manejo de archivos mediante terminal y mediante Hue utilizando el dataset proporcionado por el profesor.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Se cuplio con los lineamientos estipulados para el reto5-2

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## Detalles del desarrollo

### Teniendo el cluster previamente creado y activo, empezamos ingresando a este de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/06d1fd8b-ce39-4666-b9c8-6f5d6a7d54f6)

### Descargamos de manera local la carpeta datasets y la subimos a el cluster de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/6106b5bc-e8f7-4805-8a63-f6efd6a0a649)

### Revisamos que contenido tienen los directorios base y creamos el directorio datasets y datasets/gutenberg-small de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/43a87fc3-15e3-4402-ad5b-6a500bbb35ef)

### Luego empezamos a copiar los archivos locales a el HDFS de la siguiente manera:

Archivos locales FS:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/bb039118-62cb-467e-bd31-698ea09e6a47)

Archivos S3:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/6942f15a-a21d-4226-827c-f85911dad869)
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/3d483a72-fc7a-4c73-833c-a40f0a360f22)

Copia recursiva de datos:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/555ee755-7cdb-4571-8e7c-efe510d1bbb8)

### Listamos los archivos previamente almacenados para verificar su creación de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/ff64b123-0055-4d56-b0f3-88bb0399b52f)

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/faccaa57-4362-417b-94d4-f67316f9e3ae)

### Ahora vamos a copiar los archivos del HDFS hacia el servidor local de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/d4b82cb5-6e12-4900-99e9-f5f8512f50b0)

Cabe resaltar que previamente se debe hacer la creación de la carpeta mis_datasets

### Otros comandos probados:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/053db054-1f81-4f0c-b3d4-d529842aea7e)

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/16ef678f-2f38-49c1-84ed-8501873509e9)

## Manejo de archivos via Hue

### Primero metemos un archivo a la carpeta datasets como ya se hizo anteriormente de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/71f64fc8-ee6e-442a-89c3-2fa08230e833)
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/46337655-5c28-4b79-a775-2f4df2e15fef)

### Verificamos su creación en la interfaz de Hue de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/64ddab8b-934d-42b5-8f15-6de27ec17e2b)
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/c2685d0d-4c77-43ee-8765-1711760925be)

### Ahora creamos un directorio que en este caso lo llame pruebas de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/5c52916e-840a-43e6-beb4-6bae938d7595)

### Guardamos un archivo dentro de esta carpeta de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/3e74e634-c81e-4484-9662-ab71c27015a2)

### Revisamos su contenido de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/dc644a59-d863-4380-aeda-753f4fa1f6b6)

### Por ultimo podemos ver como por consola podemos ver la carpeta y el achivo creado de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/de95d00a-d29b-4faf-82bc-9a1c193b6136)

## Detalles técnicos

Se creo un cluster con las diguientes aplicaciones:
* Hadoop versión: 3.2.1
* Hue versión: 4.9.0
* JupiterHub versión: 1.2.0
* Spark versión: 3.1.1
* Zeppelin versión: 0.9.0
* HCatalog versión: 3.1.2
* Livy versión: 0.7.0
* Sqoop versión: 1.4.7
* JupyterEnterpriseGateway versión: 2.1.0

* Cluster creado con la versión: emr-6.3.1

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## Conexión con cluster

Para la conexión con el cluster ingrese a PowerShell en su computador, ingrese al directorio donde se encuentra la clave .pem y digite el siguiente comando:

ssh -i tma.pem hadoop@ec2-54-165-141-22.compute-1.amazonaws.com

Como se ve en la imagen a continuación:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/ad17dcd4-93e3-42ff-aef1-dbccb1792558)


# 5. otra información que considere relevante para esta actividad.

# referencias:

### https://www.youtube.com/watch?v=MyXSwxN5Zdk&ab_channel=EdwinNelsonMontoya
### https://www.youtube.com/watch?v=3sao-qJG34Y&ab_channel=EdwinNelsonMontoya
### https://github.com/st0263eafit/st0263-231/tree/main/bigdata
### https://www.hostinger.co/tutoriales/comando-scp#:~:text=El%20comando%20SCP%20(Secure%20Copy,Remota%20de%20Berkeley%20Software%20Distribution.

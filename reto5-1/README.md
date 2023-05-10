# Info de la materia: ST0263
# Estudiante(s): Tomas Marin Aristizabal, tmarina@eafit.edu.co

# Profesor: Edwin Montoya, emontoya@eafit.edu.co

# Reto # 5

# 1. Breve descripción de la actividad

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Se cumplió con todos los requerimientos debido a se realizo la creacción de un Bucket s3 con nombre st0263tmarina este con el fin de almacenar los archivos que se manejen en el cluster, ademas se creo el cluster en el cual se descargaron las aplicaciones de Hadoop, Hue, Zeppelin, Jupyther.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Se cuplio con los lineamientos estipulados para el reto5-1

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## Detalles del desarrollo

### Ingrese a AWS y busque EMR

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/eef2f79a-0c78-40b3-ba93-83db2776fb8d)

### Luego dele crear cluster y empiece la configuración de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/e75edc3d-c49a-4010-930b-a459ca43cc99)

### Modifique el tipo de maquina a m4.xlarge de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/1753b136-bf43-4d9f-b668-d5e9f80ceec0)
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/65dbd743-8bad-41e3-b903-341078d583ae)

### Seleccione la VPC y la Subnet que esta por defecto de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/b4082498-8c7c-421d-b3bc-301995b51c37)

### Agrege la este script para el almacenamiento de los cuadernos Jupiter en el bucket de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/dc3f023a-adcb-4697-8d32-f6517bde2fcb)

### Coloque una llave de su preferencia

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/249e48c6-fa22-45c9-aa4e-2d2a2450243b)

### Coloque los roles por default de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/c1dd2476-616d-40dd-b021-e11637915323)

### Agrege los puertos 8888, 9443 y 8899 en la configuración del firewall

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/838d06b7-8969-4259-b18f-ea30f1d86dba)

## Creacción de Bucket

### Dirijase a s3, dele crear bucket y haga la configuración de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/e29a4575-1061-449b-86e1-7823b58b93c5)

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/3bc8cc3f-9bef-4ac5-8333-5c73f604c9de)

### Agrege la configuración para colocar el bucket publico de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/4be51ee7-fd80-45fc-962c-eeeb31e55c0a)


### Pruebe la conexión con el cluster ingresando el comando ssh en la terminal de la siguiente manera:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/c0c90d97-e757-487d-82b5-a551c5e801d6)

### Verifique la conexión con la Hue

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/787c5416-7b05-492f-ba85-20472f351cf7)

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

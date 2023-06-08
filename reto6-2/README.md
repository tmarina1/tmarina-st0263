# Info de la materia: ST0263 Tópicos especiales en telemática
# Estudiante(s): Tomas Marin Aristizabal, tmarina@eafit.edu.co

# Profesor: Edwin Montoya, emontoya@eafit.edu.co

# Reto # 6-2

# 1. Breve descripción de la actividad

## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Se cumplieron con todos los aspectos propuestos por el profesor para el laboratorio 6-2, se utilizo el dataset propuesto con el fin de manejar y utilizar Spark para el manejo de datos.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Se cuplio con los lineamientos estipulados para el reto6-2

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## Detalles del desarrollo en google Colab

# 1.
Para realizar el desarrollo del reto primero se cargo el dataset de casos de positivos de covid en mi google drive personal y en el bucket s3 creado para la materia.

# 2.

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/c7dd7a39-d16a-40c5-8555-fe322ec62fde)

Carga de dataset y visualización de las columnas del dataset:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/b9a49897-910b-4386-8e2b-212b4317ef98)

Visualizacion del tipo de datos de las columnas:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/dee8462a-7004-4e3a-bf50-47ad273c3aa4)

Renombrado de columna:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/0203e3d9-7ba4-45b3-9f07-1f65955dba50)

Creacción de una nueva columna:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/c3b3cfe2-85a6-4c21-ac5d-3f98cd05d056)

Borrado de la columna previamente creada:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/d4474b69-bbf6-48ae-9b63-5b246a6257d8)

Filtrado de datos:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/36f5ac1c-a6b4-43f0-8590-be9b49e209b4)

Función lambda y UDF:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/20551f99-a4f3-4c8d-9d39-006fda52df39)

# 3.

Los 10 departamentos con más casos de covid en Colombia ordenados de mayor a menor:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/964e0135-4a68-4e7b-a0c9-34fba271965d)

Las 10 ciudades con más casos de covid en Colombia ordenados de mayor a menor:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/8fa0f47c-7f9b-40f0-9e99-615007219d34)

Los 10 días con más casos de covid en Colombia ordenados de mayor a menor:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/abbbc2c1-10de-400e-8b97-7331a97e41b3)

Distribución de casos por edades de covid en Colombia

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/92a731d1-b0a1-4d7a-9432-e5c11a223414)

Realice la pregunda de negocio que quiera sobre los datos y respondala con la correspondiente programación en spark:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/4019fd9d-08ec-4f39-8a5d-ddb963283734)


## Detalles del desarrollo en JupyterHub

# 1.
Para realizar el desarrollo del reto primero se cargo el dataset de casos de positivos de covid en mi google drive personal y en el bucket s3 creado para la materia.

# 2.

Carga de dataset, visualización de las columnas y el tipo de datos del dataset:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/8848d4ae-ab62-41df-8ce0-402f6d177fdd)

Renombrado de columna:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/6451512c-ab4f-43ca-8fc7-f4f96c462d80)

Creacción de una nueva columna:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/5d8db294-c9e0-4389-9007-cc2b0f655756)

Borrado de la columna previamente creada:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/0d72722a-14ab-4a92-8d28-ae51fac7464c)

Filtrado de datos:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/55c7a7f3-8e95-4dcf-aef1-2db20777f186)

Función lambda y UDF:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/e66be415-b72e-4b0b-be8f-282b69086d53)

# 3.

Los 10 departamentos con más casos de covid en Colombia ordenados de mayor a menor:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/159e0eee-e814-495b-a17e-817884b14d60)

Las 10 ciudades con más casos de covid en Colombia ordenados de mayor a menor:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/6cf092c6-d856-4f61-9872-85717077e7e2)

Los 10 días con más casos de covid en Colombia ordenados de mayor a menor:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/4dcc8d5a-9831-4f8b-bf90-469e2d117921)

Distribución de casos por edades de covid en Colombia

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/b831ee78-72cf-4729-943a-b852dedd640f)

Realice la pregunda de negocio que quiera sobre los datos y respondala con la correspondiente programación en spark:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/cb801ae3-5ee8-4153-b0de-78dfbfbdb583)

# 4 

Como se puede ver en las imagenes de los codigos anteriores se almaceno el resultado que estos querys arrojaron en un bucket S3

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/e42b9f88-db8b-4cd1-bcef-317a6bfc311b)

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/95b5026a-46c0-4830-98a7-62f59fbb5dd7)

La ruta de acceso al bucket es: "s3://st0263tmarina/resultados.csv/"


# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

La ejecución de este laboratorio se hizo en un cluster en su versión emr-6.3.1 y en google colab, ademas de usar JupyterHub en su versión 1.2.0.

# 5. otra información que considere relevante para esta actividad.

# referencias:

* https://github.com/st0263eafit/st0263-231/tree/main/bigdata
* https://barcelonageeks.com/como-eliminar-columnas-en-el-marco-de-datos-de-pyspark/
* https://www.oreilly.com/library/view/learning-spark-2nd/9781492050032/ch04.html
* https://sparkbyexamples.com/pyspark/pyspark-join-explained-with-examples/


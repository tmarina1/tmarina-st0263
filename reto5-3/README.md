# Info de la materia: ST0263 Tópicos especiales en telemática

# Estudiante(s): Tomas Marin Aristizabal, tmarina@eafit.edu.co

# Profesor: Edwin Montoya, emontoya@eafit.edu.co

# Reto # 5-2

# 1. breve descripción de la actividad
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Funciono todo, debido a que se realizaron todos los códigos requeridos, ademas de probarse los codigos propuestos por el profesor.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

Se utilizo la libreria que permite desarrollar un Map Reduce, con el fin de probar y experimentar con esta herramienta. 

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## como se compila y ejecuta.
Para correr un archivo que contenga un codigo de Map Reduce solo es necesario ejecutar el siguiente código:
```bash
  nombreArchivo.py rutaDataset
```
## detalles del desarrollo.

# Dataset empleados

1.

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/29662edd-a98c-4770-98eb-0480d55470f7)

2.

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/e2a53f2e-e38f-45ee-a4f2-3f4ba20534b3)

3.

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/68498546-2f61-4c56-bdbb-38c5855590e6)

# Dataset acciones

1.
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/7c1a7ae0-1a2d-42b1-8f3f-25fa6ef0b1b0)

2.
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/086f9d68-aa99-45af-b970-6d1c74ed8311)

3.

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/ca854a47-4260-48a0-a5a4-d714a3b38cfb)

# Dataset peliculas
1.
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/e91ce70e-cf4a-45bb-b0af-fb410c53ab3d)

2.

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/6468cd28-78a9-43ed-948e-325b761bf666)

3.

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/381408a1-81ed-438b-84cc-dbce4bd64027)

4.

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/e1aa156d-4b2e-4257-93c6-26b90f15b1bb)

5.

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/875e6ddd-8dc8-4d62-9fd8-8cee309a6c6f)

6.

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/450c2449-10de-4526-9886-ead0ebbcaea9)

7.
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/d4e1a5d5-3c60-49f9-ad83-635e0420260c)


Parte 2

3.
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/1a99c5ff-9063-4983-8a8b-2fff2f4051d4)
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/f3723ac9-db0c-4c6a-a3ef-18544c2b4cc7)
![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/29ed90cb-f88b-475d-a405-45bfc31a3558)

4.
En el codigo se hace una conexión con PySpark, se trae la información de un bucket S3, luego se mira que contenido tiene este archivo y como se organizo, luego de esto se empiezan a hacer segregaciones de datos o en si operaciones con los datos como por ejemplo ´´´ df.select('mobile').distinct().count(´´´ 

# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.



# 5. otra información que considere relevante para esta actividad.

# referencias:
* https://mrjob.readthedocs.io/en/latest/guides/quickstart.html
* https://github.com/st0263eafit/st0263-231/blob/main/bigdata

#### versión README.md -> 1.0 (2022-agosto)

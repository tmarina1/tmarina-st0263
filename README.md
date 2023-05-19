# ST0263-4529
## Integrantes
- Tomas Marín Aristizábal, tmarina@eafit.edu.co. 
- Juan Pablo Yepes, jpyepesg@eafit.edu.co.  
- Simón Cárdenas Villada, scardenasv@eafit.edu.co.
## Docente:
- Edwin Nelson Montoya Munera, emontoya@eafit.brightspace.com

# Proyecto #2
## Descripción del proyecto
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Todo lo planteado en el proyecto fue realizado, debido a que se hizo el programa para hacer el manejo de máquinas virtuales, específicamente haciendo la creación y eliminación de máquinas, además de que se hizo una comunicación grpc con cada instancia creada para validar su estado y de esta manera poder gestionar este grupo de instancias.

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)  

Se cumplio con todo lo planteado por el profesor.

## 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas. 

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/6e39c656-6b49-46f9-acfe-d31c411a0c43)

La arquitectura en la que se basa el proyecto consiste en una instancia que tiene el Monitor S que es el encargado de gestionar el funcionamiento, este tiene la capacidad de comunicarse con las instancias que creo previamente, además de tener la lógica para poder hacer la creación y eliminación de máquinas virtuales dependiendo de cómo se esté comportando de la CPU del pool de instancias, cabe resaltar se creó una imagen con la plantilla base para poder hacer la creación de instancias a partir de una imagen AMI.

## 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

   
## 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.  


## Referencias
* https://hands-on.cloud/boto3-ec2-tutorial/#h-terminating-ec2-instance
* https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationec2.html
* https://repost.aws/questions/QUvkTnk24TRQaO522FONlgvQ/i-am-running-into-an-error-using-boto3

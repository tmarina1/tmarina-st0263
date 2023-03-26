
# Info de la materia: ST0263 Tópicos especiales de telemática

# Estudiante: Tomas Marin Aristizábal, tmarina@eagit.edu.co

# Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Reto 3 

# 1. Breve descripción de la actividad

En este reto se hace el despligue de una arquitectura donde se tienen 2 WordPress, un balanceador de carga, una base de datos y un servidor NFS, se cuentan con dos instancias WordPress para garantizar la disponibilidad de la pagina web, además de contar con un el dominio con certificado SSL para una conexión segura mediante https.

# 1.1 Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor. (Requerimientos funcionales y no funcionales)

Cumplí con todos los requerimientos solicitados por el profesor, creando 5 instancia una para el servidor nginx, que funciona como balanceador de carga y que cuenta con el certificado SSL para el dominio escogido, dos instancias para las paginas WordPress que se conectan a una base de datos remota, una instancia para la base de datos y una instancia el servidor NSF de archivos compartidos.

# 2. Información general de diseño de alto nivel, arquitectura, patrones , mejores practicas utilizadas.

Para el desarrollo del reto se desarrolla e implementa la arquitectura propuesta por el profesor que se ve de la siguiente manera:

**![](https://lh6.googleusercontent.com/3PiHctEkvBymHhlPa3xoGybk357PhwN7NxiOOtu92CF9k58gtpN3MB21QaNstHB6BUkrm8q1Sx4tXNU5fb8AnlwK5ZSrHXLYw6tj9SnycJaeHpd7LNqWqQeu3--_rejCa88ymrfw2Qqi7Mr0OQeYe9A)**

En si es una arquitectura cliente servidor, las instancias del balanceador de carga, WordPress y base de datos están realizadas con contenedores de Docker. Se tiene una maquina para el balanceador de cargas que se encarga de repartir las peticiones entre las dos instancias WordPress, estas dos instancias WordPress cuentan con una base de datos compartida al igual que un servidor NFS.

# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programacion, librerías, paquetes, etc, con sus números de versiones.

## Base de datos:

* Primero se actualiza la instancia y se hace la instalación de Docker:

**![](https://lh3.googleusercontent.com/x8Ij5124qEH3dJDTx5eNjFT1sFXn9YJZEL73k-bcAAjMJ_gctVcX1XAmhyDEUUMiS2K30QbY-xro0qmKIc2WuO8OdfObecxdwuGxEuNQhBSV-Y9v_Vcfw3O7cuxWRuNvdsEHoXZYP9SuET25ctBXLps)**
* Se crear un archivo .yml que contenga la información requerida para correr la base de datos:

**![](https://lh3.googleusercontent.com/ZbOSj1o35ZpTtVB4gKOONprnwrsAAXfv224rw5MwGqr8WZA-nXwzOrn9ivFibCwgtU7dMoWv5rlRhIYRj8NqXGn2zphS3-9vlisFlKcPUCGixqH2H2kFz_SI5m1_5GrPqnnWvyf-czroFkSwTe6yF8A)**

* Por último se corre el siguiente comando para correr Docker con el archivo creado anteriormente:
 “docker-compose -f wordpress-db.yml up”
 
**![](https://lh3.googleusercontent.com/FKo6yhRm-rgzRUynZ2-BC0c-gYkVnDyCXdMz-P06FVkHoMypnVMPoOf3Cm7pYYtTf767OomMIyI7fQutW90oTaxMUy_MpSeuW452zHzCUKIO9b8ll_vqgRK4mArtjeJkjpyjVN16aM3D_uGChz5P5O8)**

# WordPress

* Primero se actualiza la instancia y se hace la instalación de Docker:

**![](https://lh3.googleusercontent.com/x8Ij5124qEH3dJDTx5eNjFT1sFXn9YJZEL73k-bcAAjMJ_gctVcX1XAmhyDEUUMiS2K30QbY-xro0qmKIc2WuO8OdfObecxdwuGxEuNQhBSV-Y9v_Vcfw3O7cuxWRuNvdsEHoXZYP9SuET25ctBXLps)**

* Se crear un archivo .yml que contenga la información requerida para correr WordPress con una base de datos remota y un NFS:

**![](https://lh5.googleusercontent.com/SYmTtcKe8gq1fvhsdEqch4yTZn4FMOJenOKR-8-N6W_p4QuJXhKbVndz24qNhQw0sc6T5oX3LVqESs7B3giaxPE33gbfj6L3rB41PFdho13Ns9yXEUVKv-NzPnGP0d1_Fr1M9cOuwsOO5CjKI-9Zp2A)**
    
-   Se debe de hacer la configuración del NFS cliente de la siguiente manera:

**![](https://lh3.googleusercontent.com/kIha8lq8ifuAGO8dU3__vKIBaD_1MOpCny0SMaYsnVQ-W4gihj7ABDjKP3WfAg0rWxQMZW7fggq8MKmqV02W7jw_Ree5nyDYEw6lDGa8QPZcAM41NgqveRV3j8xKg5-ou8C7V9noFXkRyETHjAWIpOI)**

**![](https://lh3.googleusercontent.com/jPn_Ao4BTBBNcuZXK-97gGO5ODDT1k0WDjpHsoSSZjpt4m85U0LVEdy-epTDXEkyvpUeyTGrgcvWQ4B2KQw3oiB9MGSahGdGRv4yBUurpkULeCbM8RQ09FhsbLxXP6uHNO6YkObJvpNI3-68LYt7wAI)**

* Se corre el comando "docker-compose -f wordpress.yml up" y ya con esto podremos acceder  a Google con la IP de la maquina virtual para hacer la configuración del WordPress:
**![](https://lh3.googleusercontent.com/KLBaMIVBsO6joa8hm-ZSPG_smH627uFjxkmEE5WiubdjqjG2OJSWdDlSEy9oF34he-0g3XGSFzmIn8jZeKeTD9vC4i2TCuKgbjY-DefP5DDYWB8lhnWeaWWxQCeXXBghVcy93sweSPgcwPvEe8t0U5c)**

Cabe resaltar que esta configuración anterior se debe hacer en las dos instancias WordPress requeridas en el reto, para poder contar con dos instancias que contengan la pagina web.

# NFS server

* Se debe hacer la instalación del NFS-server

**![](https://lh6.googleusercontent.com/2duIu3O4xM9fYTgjsxeEsfjY68GGZ-7CGq7Q0D_Nno7rTc0lJddvtzaYGQTcPi-8pT4tHNPocieHA2zWY2X7LVirioBgAGKRY-hVIpX0MCCWbv67grpeE4o0GJC_80Q8aWnHcNUYHNPxhzZnkCea_lY)**

* Se hace la configuración del NFS server:

**![](https://lh4.googleusercontent.com/ZWbLsL6ddCg2Z40tQtUHDY87_ZT-CxMNkdqvW2qjitfga6wZhJDiMbRYIbpuavoEKcTibIgh9-mb088kjD5mz-t1iLBATBgi7_4-EE_l1hfgyB67sIbsJbXAAl1o7M5NLPS0YooNDvRMj-o1PXLQXHc)**

* Se colocan la IP privada que abarca las dos máquinas virtuales WordPress previamente creadas:

**![](https://lh3.googleusercontent.com/qeSg8Pvwto8cePqQQBlckVTduyZqa7onj7ffZI0LsIGjHnD6cl1mp1yndsOCWkH9kWQDO8xC-Axp9-2ri36qf-hSCyRSQTNpmp93fpNYbuHKrOdVjg91Fvh4EoMrcnz9Ul-fp7w2fwVkA05bnJHE_5A)**

* Por ultimo se reinicia el NFS server

**![](https://lh4.googleusercontent.com/Ye28A-spzT0oXfRd8O9yjOKkMbKKN2Au0wlQnFkrq2a_v4JYhtijYBqeY0Hu2XVUfK-xLV4243xddpanGNvBspKuywb7N5iSnfTD1n3CRq4lHnxxxjpuSswj6htIHL7UP8J-KLU_CNVlFKhs1b7v4q8)**

# Balanceador de carga
* Antes de realizar la configuración se debe de verificar que los puertos requeridos por letsencrypt y nginx esten habilitados

* Se actualiza la maquina virtual y luego se instala letsencrypt, cerbot y nginx

**![](https://lh5.googleusercontent.com/7GfggiQdP3TM7nOmJU12222ujoXtE-dPv2Ft-p5_6cmRSq9o7zHpQQ0dwJtyK0AuxaPyLSo-al-LX1ZlQd42HkFJN0AfsVODZYENhx6-jAvS9C4a80c2DzEbfAlcsK_1Dndzr-s5YJQFDV6GpLtkpuM)**

* Modificamos el archivo de nginx

**![](https://lh4.googleusercontent.com/OD8O2xT1xK6LHa8yc4LOkdLAGVGG2eIWjTAYiRbcC61-oLhKavgwZ-7BjJdzgCeYWdQjNqDej7xM_sBk2me51D0h9W9FdQaUnwM3B7Q6uwiRfrqI52I4XKdSE59pJ6K2ILfHzDYWv84X2lLI6d2WZFE)**

* Creamos la carpeta para letsencrypt y se recarga nginx

**![](https://lh5.googleusercontent.com/LN_EI_3LynLI69EyPrJnm0upo72bPnn7uvSKaIY7q5gMjDGNF_7-fRFA9q4c_tHgeTrkR4ox0LYXgEel1D3bEkV7qgE0OnjqWtNOWFnk_3c6A8witviKY__0cC9WWIsb6GcCYvXuf5ueLi_JMVyoMcQ)**

* Para realizar el siguiente paso previamente se debe de haber reservado el nombre de dominio en Freenom o en cualquier otra plataforma de manejo de dominios y se debió haber asignado la IP elástica de la maquina del balanceador de carga de la siguiente manera:

**![](https://lh5.googleusercontent.com/jvOJA8Hr8sd4XCr2CVAOL3lEOYiyMqn-ejUp4GLoldM71LNPZ_laHTQOcDPhD-Mtf4F68ukAoJrGIxVm3KBtEhyYy87WztFySzfjB4I3nME0re8CPSN4OO3Vr5D10BaXKrqUREqSV5l9-RFG9uIk__Q)**
 
* Se pide el certificado SSL para el dominio, en este caso se pidió el certificado SSL para el dominio prodroductosjst.tk

**![](https://lh3.googleusercontent.com/5QPmYWE8rn6z1-emTKj47bHEGTJaF-G2BWxhvMsDf-cLXvrfuXHQV11gA0tTrXLpZcVPmPtVAWkdjtOs_yrCi6k9Xj4ZVI08pVEBW-v6d8p9fj6yqUAPSMViAB7zD1s2Q9NoiN-Fs0AmQPDxl2V4Ngk)**
* Se mueven los archivos de ejecución y configuración generados por letsencrypt para el dominio

**![](https://lh6.googleusercontent.com/7NL3TJvRbfls9gAUCkhdvyYPrQ7hJpQKX58ipuOembBXkpwRQ-WTo7cO5OWzaYklCjkXGQ2LTxqnv7RbfHQGUmwomifvtcCLLmIeBtn3pEhfYvn1u7kfcpS5mXGLB7-qUfIhKnV2TveXbSiUnDeiRxg)**
* Se instala Docker

**![](https://lh5.googleusercontent.com/8GIlMu_VFuHN4g4qZBRsMYkeaXqp6kbms9zLMttMxBxIN1dDa7WYDigkl_ZOAQ_ELgu_sHZEgMkRKj88ySQGv2u6ugOjeuesckS5TVfUIVDWi9Eetez773wFsPp-Hq5Hl2AjKuBRWDb8f0VtbmCf5iE)**
* Se crean y se mueven los archivos de configuración y ejecución

**![](https://lh4.googleusercontent.com/viJFEOOMtPUaAGh4qaGUVBz-cwaaNHTezRPg0uuDOLLBJCT69dB2X-PHFrPuFeHvyWF9-TcZyQdzExVp5kqp7DSVyXk9_qbcB0-Okbk9ivLsp-UZpiAeUqFhPcrjNyljUusopz5mn3MAB24yaN-v8is)**

* Se debe de modificar el archivo de configuración de nginx, agregando el upstream con las IPs con las que hará el balanceo de carga

**![](https://lh6.googleusercontent.com/ghMNbnVo-QURFnecRSEuS1b6UgQWwYkdYdBgs8HtQ18vIG1up4wgmnSYqJJcp1dNY3spTGQ5Stk_QP7xDUjq6XAHgJK7pDmXFJc_bOl7Ty1eZ3ZcO82Cy7I2F0UxXVRCaDqgjIniqcNi5hlt-a0eWkI)**
**![](https://lh3.googleusercontent.com/hyhEmgA10zcbT_6Dh6PH-GnTfmDYK_Gxl7hloQa26YEQTvifYD7xfd7jkqg4Yk9UMKdxieNqDiLRicwBq11fJTM5044hRL8bmFe_Eq2XBZmaDWJW5QqmN74muYQlbED_Us_k6sV1rFZ0a6QdYAQhjNE)**
* Se modigica el archivo docker-compose.yml para usar el contenedor de nginx y se coloca la siguiente información:

 **![](https://lh4.googleusercontent.com/dO_rjj2bhhg1YnaiVb9NbieT-1CM6eka42JH8vF9dYO3yk8gNVacKwyW1FPsFwH5EzWchXBWv8nT0ByyUl6R_Vzcame916DZ_5_CANjrIy9Ej3Ppn953eSUJzPZxMSrv1VyWJY32GqZP51ePn1bX8Y0)**
* Se crea el archivo de configuracion del ssl con la siguiente información:

**![](https://lh6.googleusercontent.com/SreFcOMxPxJNMNTSJ60YkYoVMA5PQ5pcJoHaVE1qLek7zFHeSswBzPTgiWu_RjanMB-R8kMqjn1o8lYdC3EAbtOHAKsZAkqzTKW3g0ZdbHdHG-2YrizlQbzOGSfUEoqbj4Jgpf4hnhVEQm0g3nMcF8k)**

* Se verifica que nginx no este corriendo por defecto

**![](https://lh3.googleusercontent.com/Q0NOihlOfZ0cepJT2MJDJ4IX2MxQjIxA2CjsnBbDNXgX9PW1IBKNwtGsuq_T3nlhYN3y4gJpnFla8cR1KgBoyJaNcO7N2DpewZTCK8FYLyunyHfKCH3RKGyhFSJk-we-IxIrEUTWyJ8e9EGGqDAJ40A)**

* Por último se ingresa a la carpeta que se creo, en este caso con el nombre WordPress y se corre docker-compose

**![](https://lh6.googleusercontent.com/GN_sz7snv8iFwkXpZYnqF_Z7BTKL5NGI88yquqpH9YaFEpbJmDXer5MsTKsuB-NmFQHhXNgXoDPuqM1GUKgLD1eNkp9yfQleQfkpxXcuI9fVuZYfgI5fDzC7fcfqmqje99Ftptg7__O_NoEpFT3Km8g)**
# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerías, paquetes, etc, con sus números de versiones

Para el desarrollo del reto 3 se utilizo la plataforma Google Cloud Platform con la ayuda de instancias de Ubuntu en su versión 20.04, el dominio fue obtenido en freenom utilizando el propio servicio DNS que ofrece freenom.

## Dominio:
* productosjst.tk

## Instancias y sus respectivas IPs
**![](https://lh6.googleusercontent.com/0od9Ay7i48dgoGB24VeMRDbmHE5tAe-r90eUgqlJxUrtQ-of8KbZJDep7jYgpIQsvbhsU35U1ioScHGCNrASC_EssBaLPTAChCsdZYPvgI_nTEJwiwU8gtzTAEbc12kRFhIEDoPiuqMdY680s2Xtbuo)**

## como se lanza el servidor
Para que todo funcione se debe de correr el docker-compose en la maquina virtual del balanceador de carga de la siguiente manera:
* Ingresar a la terminal de esta maquina y digitar el siguiente comando "cd /home/tomimundo24/wordpress"
* Levante el docker-compose con el comando "sudo docker-compose up --build -d"


## una mini guía de como un usuario utilizaría el software o la aplicación
Para utilizarlo por un usuario normal se debe dirigir a la siguiente pagina web en su navegador: 
* https://productosjst.tk/

# 5. Otra información que considere relevante para esta actividad.
## Referencias:
* https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-20-04
* https://www.digitalocean.com/community/tutorials/how-to-run-nginx-in-a-docker-container-on-ubuntu-22-04
* https://github.com/st0263eafit/st0263-231/tree/main/docker-nginx-wordpress-ssl-letsencrypt
* https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-to-setup-an-Nginx-load-balancer-example

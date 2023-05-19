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

Para el desarrollo del Monitor se creo un archivo llamado clases_ec2-py el cual cumple la función del SDK donde se pueden crear y eliminar instancias, este código se implementó de la siguiente manera:

En el siguiente código se hace el constructor de la clase Manager donde se tiene una lista llamada pool donde se almacenara la IP e ID de las máquinas creadas, además de hacer la conexión con AWS.

```python
class Manager:
  def __init__(self) -> None:
    self.pool = []
    self.ec2 = boto3.resource('ec2', 
                              aws_access_key_id =  accesoAWS.aws_access_key_id,
                              aws_secret_access_key = accesoAWS.aws_secret_access_key, 
                              aws_session_token = accesoAWS.aws_session_token, 
                              region_name = 'us-east-1')
```
El siguiente código permite hacer la creación y eliminación de máquinas virtuales:

```python
def crearInstanciaEC2(self, amiImage):
    instancia = self.ec2.create_instances(
      ImageId = amiImage, 
      MinCount = 1, 
      MaxCount = 1,
      InstanceType = 't2.micro', 
      KeyName = "vockey",
      )
    time.sleep(2)
    instancia[0].reload()
    self.pool.append((instancia[0].id, instancia[0].public_ip_address))
    return instancia
  
  def eliminarInstanciaEC2(self, instanceId):
    instancia = self.ec2.Instance(instanceId)
    instancia.terminate()
    return instancia
```

En el archivo monitor.py se realizó el código que hace el manejo de las instancias, todo esto se hace mediante conexiones con las instancias creadas con grpc que permiten recopilar información sobre el estado y uso de la CPU de cada máquina para así poder determinar si es necesario crear o eliminar una instancia.

```python
def monitor():
  global uso

  if not manager.pool:
    for i in range(2):
      try:
        manager.crearInstanciaEC2(accesoAWS.ami_template)
        manager.verPool()
      except:
        conexionInstancia = 'Error en  creacción instancias iniciales'
  else:
    for instancia in manager.pool:
      time.sleep(1)
      try:
        conexionInstancia = gRPC(instancia[1], 'EstaVivo')
        uso.append(conexionInstancia["usoCPU"])
      except:
        conexionInstancia = 'Error en envio de EstaVivo a instancia'   
    if uso:
        #promedioUso = sum(uso)/len(uso)
        valMin = min(uso) 
        valMax = max(uso)
        manager.verPool()
        print(f'Valor minimo{valMin}')
        print(f'Valor maximo{valMax}')
        uso = []

        if valMax >= 70:
          print('creando')
          manager.crearInstanciaEC2(accesoAWS.ami_template)
          manager.verPool()
          for instancia in manager.pool:
            try:
              conexionInstancia = gRPC(instancia[1], 'Evento')
            except:
              conexionInstancia = 'Error en envio de evento crear instancia'
        if valMin < 19:
          if len(manager.pool) == 2:
              for instancia in manager.pool:
                try:
                  conexionInstancia = gRPC(instancia[1], 'Evento')
                except:
                  conexionInstancia = 'Error en envio de evento'
          else:
            print('borrando')
            tupla = random.choice(manager.pool)
            IDinstancia = tupla[0]
            manager.eliminarInstanciaEC2(IDinstancia)
            valTupla = manager.pool.index(tupla)
            manager.pool.pop(valTupla)
            manager.verPool()
            for instancia in manager.pool:
              try:
                conexionInstancia = gRPC(instancia[1], 'Evento')
              except:
                conexionInstancia = 'Error en envio de evento eliminar instancia'
```

El archivo instance.py contiene los métodos que se ejecutarán de forma automática en cada una de las instancias del cluster admnistrado por el Manager. Se define un servicio de mensajes para la comuniación por grpc y un método que simula la carga de trabajo de cada instancia medida en el porcentaje de uso de su CPU, y se simula por medio de unas variables aletatorias que dictan el comportamiento.
```python
class messageService(messages_pb2_grpc.messageServiceServicer):
    def message(self, request, context):
        if request.estado == 'EstaVivo':
            CPU = usoCPU()
            return messages_pb2.messageResponse(respuesta = "estoyVivo", usoCPU = CPU)
        if request.estado == 'Evento':
            reset()
            return messages_pb2.messageResponse(respuesta = "reseteado")
```

```python
def usoCPU():
    global uso
    global estado
    if estado == 0:
        delta = random()
        if delta <= 0.5:
            uso -= 1
        else:
            uso +=1
        
        delta2 = random()
        if delta2 >= 0.8 and delta2<=0.85:
            estado = 2
        elif delta2 >0.85 and delta2<=0.9:
            estado = 1
        else: 
            estado = 0
    elif estado == 1 and uso <100:
        uso += 2
    elif estado == 2 and uso > 0:
        uso -= 2
    
    return uso
```

Para el uso de grpc se diseñó el siguiente archivo .proto:

```
syntax = "proto3";

service messageService {
  rpc message (instructionRequest) returns (messageResponse) {}
}

message instructionRequest {
  string estado = 1;
}

message messageResponse {
  string respuesta = 1;
  int32 usoCPU = 2;
}
```


## 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.  

Para ejecutar el cluster, es necesario crear una imagen AMI que servira de plantilla para la creación de las demás instancias:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/d5879415-c92b-4c1d-b6d4-51637db4595d)

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/81934947-76d9-44bc-af4d-c98845391494)

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/b4bc4bc0-017b-4d66-861b-92de8523a756)


Además es necesario definir un servicio en el systemctl para que se ejecute el servidor de forma automática:

```bash
sudo nano /etc/systemd/system/instancias.service
```

Luego se ingresa la siguiente información en el archivo:

```
[Unit]
Description=My Server
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
ExecStart=/usr/bin/python3 /home/ubuntu/proyecto2TT/instancias/instance.py

User=ubuntu

Restart=always
RestartSec=1

[Install]
WantedBy=multi-user.target
```

Por ultimo se activa el servicio de la siguiente manera:

```bash
sudo systemctl start instancias
```

Una vez hecho esto, se debe configurar el archivo accesoAWS.py con las credenciales respectivas para la conexión del SDK con el AWS:

``` python
ami_template = 'ami-02db252a712b094d8'

aws_access_key_id = 'ASIAQZFGU3EJJPX4HQQ7'
aws_secret_access_key = '97m3iJzEKofT9E9sZR9zAie8l5gkWcBWJ1YMo91m'
aws_session_token = 'FwoGZXIvYXdzEDUaDAsxA9tYcp48XavlJSLFAc57FmUdwNraQ4mcQLIzXrBPsYoGdN15jdzskK6VkNBheBipKtghf8IWJmuB2CJBaT5itrOCkZgndIIOBhHIJyge3lGf6DUfeHDTE96fkw2Xb5wcG3wWa1cbkYSBtCDi4kcjB2begJ+0kgZbMXqly7MP216Mx+wkl1QiFam4pVTofHBkuitb1RPp2TpPhmysDPMGjIgShmNOfYUnzwKNhPOx+kUNFv3lEQdbsto+CXuZubj5eGLCOC2E+P1+R5fSTJ6D4+0fKMPYlKMGMi28MytAZmpsG4IkY8jIrcx6quHbQMWI0kcdWWgcF9nKrQhUAxDNYDoMU/HiXko='
```

Ejecutar monitor.py:

<img width="601" alt="image" src="https://github.com/tmarina1/tmarina-st0263/assets/68928376/d862541d-526c-4320-b361-da66a5829f51">
<img width="800" alt="image" src="https://github.com/tmarina1/tmarina-st0263/assets/68928376/3ae1945c-d16c-4062-92e0-26d2f7d0540b">


Dashboard de AWS en ejecución:

![image](https://github.com/tmarina1/tmarina-st0263/assets/68928376/1af39fd3-3126-42ae-8114-484c85941eff)

## Referencias
* https://github.com/st0263eafit/st0263-231/tree/main
* https://hands-on.cloud/boto3-ec2-tutorial/#h-terminating-ec2-instance
* https://boto3.amazonaws.com/v1/documentation/api/latest/guide/migrationec2.html
* https://repost.aws/questions/QUvkTnk24TRQaO522FONlgvQ/i-am-running-into-an-error-using-boto3

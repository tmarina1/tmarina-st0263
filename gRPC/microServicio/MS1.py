import os

def buscarArchivo(nombreArchivo):
    archivo = []
    for root, dirs, files in os.walk(os.getcwd()):
      for file in files:
        if nombreArchivo in file:
          archivo.append(os.path.join(root, file))
    return archivo

def listarArchivos():
    listaDirectorios = os.listdir(os.getcwd())
    return listaDirectorios

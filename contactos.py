from replit import db

# Método para agregar contactos
def agregar_contacto():
  nombre = input("Nombre del contacto: ")
  tel_num = input("Teléfono de contacto: ")
  if nombre in db:
    print("El contacto ya existe")
  else:
    db[nombre] = tel_num
    print("Contacto agregado")

def listar_contactos():
  print("----------------------------------------")
  print("      Lista de contactos      ")
  print("")
  for i in db:
    print(i, " : ", db[i])
  print("----------------------------------------")

def modificar_num_contacto():
  listar_contactos()
  print("----------------------------------------")
  nombre = input("Nombre del contacto a modificar: ")
  tel_num = input("Teléfono nuevo: ")
  db[nombre]=tel_num
  print("")
  print("Número de contacto modificado satisfactoriamente")
  print("----------------------------------------")

def modificar_nombre_contacto():
  listar_contactos()
  print("----------------------------------------")
  nombre_viejo = input("Nombre del contacto a modificar: ")
  nombre_nuevo = input("Nuevo nombre: ")
  db[nombre_nuevo]= db[nombre_viejo]
  del db[nombre_viejo]
  print("")
  print("Nombre de contacto modificado satisfactoriamente")
  print("----------------------------------------")
  
def eliminar_contacto():
  listar_contactos()
  print("----------------------------------------")
  nombre = input("Nombre del contacto a eliminar: ")
  del db[nombre]
  print("")
  print("Contacto eliminado satisfactoriamente")
  print("----------------------------------------")
  
def eliminar_todo():
  listar_contactos()
  print("----------------------------------------")
  for i in db:
    del db[i]
  print("")
  print("Agenda eliminada")  
  print("----------------------------------------")
  
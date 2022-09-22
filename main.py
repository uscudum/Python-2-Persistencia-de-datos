import contactos

print("----------------------------------------")
print("           AGENDA CONTACTOS         ")
print("")
print("1 - Agregar contacto")
print("2 - Modificar el número de un contacto")
print("3 - Modificar el nombre del contacto")
print("4 - Eliminar un contacto")
print("5 - Eliminar agenda completa")
print("----------------------------------------")


op = int(input("Ingrese la opción deseada: "))

if (op == 1): 
  contactos.agregar_contacto()
elif(op == 2):
  contactos.modificar_num_contacto()
elif(op == 3):
  contactos.modificar_nombre_contacto()
elif(op == 4):
  contactos.eliminar_contacto()
elif(op == 5):
  contactos.eliminar_todo()
else:
  print("Opción no válida")
    



contactos.listar_contactos()





#Almacenar en mi db
#db["Guillermo"] = "098465892"
#print(db["Guillermo"])

#Modificar valor
#db["Guillermo"]="091098159"

#Mostrar Llaves
#print(db.keys())

#Borrar
#del db["Guillermo"]

#print(db.keys())

#a = {}
#a["Juan"] = "091158762"
#print(a["Juan"])
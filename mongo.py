from pymongo import MongoClient
import pymongo

try:
  # Conexión con la base de datos
  client = MongoClient('mongodb://localhost:27017/')
  
  # Seleccionar la base de datos
  db = client['covid19']
  
  # Seleccionar la colección
  collection = db['casos']
  
  print("All done...")
  
  consulta = {"Ciudad de ubicación": "Bogotá D.C."}
  result = collection.find(consulta).limit(1)

  def menu():
    print("Welcome to de menu of mongo db")
    enter = input("Chosee an option: ")
    print("1 | Cuantos casos se registraron en Bogotá")
    
    while True:
      print("Hellow menu")
      break
  menu()

  # Cerrar la conexión
  client.close()
  print("see you...")
  
except pymongo.errors.PyMongoError as e:
  print("Error:", str(e))

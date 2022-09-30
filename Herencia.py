class Vehiculo:
 def _init_ (self, marca, modelo):
  self.marca = marca
  self.modelo = modelo 
  self.acelera = False
 
 def marcas(self):
  self.marca = True
 def modelos(self):
  self.modelo = True
 def acelerar(self):
  self.acelera = True
 def operacion(self):
  print("Marca :", self.marca)
  print("Modelo : ", self.modelo)
  print("Acelerar: ", self.acelera)

import sys 
class Nodo:
	def __init__(self, nombre= None, cedula=None, sig=None):
		self.nombre	= nombre
		self. cedula = cedula
		self.sig =sig

# Devuelve una cadena o cadenas de los objetos que se coloquen
	def __str__(self):
		return "%s %s" %(self.nombre, self.cedula)

class lSimples:
# hacemos un inicializador de una cola
	def __init__(self):
		self.cabeza = None
		self.cola = None	

# Recivimos un objeto de tipo nodo 
	def agregar(self, elemento):
		if self.cabeza == None:
			self.cabeza = elemento

		if self.cola != None:
			self.cola.sig = elemento

		self.cola = elemento
		
	def listar(self):
		aux = self.cabeza
		if aux != None:
			print("\nLa lista de las ordenes es:")
			while aux != None:
# aux contiene  al objeto de dados uno a uno
# como se manda a imprimir se activa la funcion __str__
				print(aux)
				aux = aux.sig
		else:
			print("No tienes datos en la cola")

	def buscar(self, cedula):
		aux = self.cabeza
		while aux != None:
			if int(aux.cedula) == int(cedula):
				return aux
			aux = aux.sig
		return None

	def eliminar(self, cedula):
		if int(self.cabeza.cedula)==int(cedula):
			self.cabeza = self.cabeza.sig
			return True
		else:
			aux = self.cabeza
			anterior = aux
			while aux != None:
				if int(self.cabeza.cedula)==int(cedula):
					anterior.sig = nodo.sig
					return True
				anterior = aux
				aux = aux.sig
		return False

	def modificar(self, cedula, elemento)
		if int(self.cabeza.cedula)==int(cedula):
			elemento.sig = self.cabeza.sig
			self.cabeza = elemento
		else:
			aux = self.cabeza
			anterior = aux	
			while aux != None:
				if int(aux.cedula)==int(cedula):
					elemento.sig = aux.sig
					anterior.sig = elemento
					return True
				anterior = aux
				aux = aux.sig
		return False



if __name__ == "__main__":
	ls =  lSimples() 
	while (True):
		print("-----Menu-----\n"+
			"1. Agregar\n"+
			"2. Listar\n"+
			"3. Buscar\n"+
			"4. Borrar\n"+
			"5. Modificar\n"+
			"6. Salir\n")
		num = input("Ingrese la opcion\n")

		if num == "1":
			nombre = input("Ingrese el nombre\n")
			cedula = input("Ingrese la cedula\n")
			nod = Nodo(nombre, cedula)
			ls.agregar(nod)

		elif num == "2":
			ls.listar()

		elif num == "3":
			cedula = input("Ingrese la cedula")
			result = ls.buscar(cedula)
			if result is not None:
				print(result)
			else:
				print("Registro no encontrado")

		elif num == "4":
			cedula = input("Ingrese la cedula")
			if (ls.eliminar(cedula)):
				print("Registro borrado con exito")
			else:
				print("Se encontraron errores al procesar")
		
		elif num == "5":
			cedulaMod = input("Ingrese la cedula: ")
			nombre	= input("Ingrese el nombre: ")
			cedula = input("Ingrese la cedula: ")
			nod = Nodo(nombre, cedula)
			ls.modificar(cedulaMod, nod)

		elif num == "6":
			sys.exit("Gracias por utilizar la app xD")
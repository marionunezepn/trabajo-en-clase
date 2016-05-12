
import os

	def cargararchivo(self):
		archivo = open("ag","r")
		linea = archivo.readline()
		if linea:
			while linea:
				if linea[-1] == '\n':
					linea = linea[:-1] 
				self.lista.append(linea)
				linea = archivo.readline()
		archivo.close()
		

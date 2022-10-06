from xml.dom.expatbuilder import parseString


class Enigma:
	alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	rotores = {"ROTOR_I": "EKMFLGDQVZNTOWYHXUSPAIBRCJ", 
				"ROTOR_II": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
				"ROTOR_III": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
				"ROTOR_IV": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
				"ROTOR_V": "VZBRGITYUPSDNHLXAWMJQOFECK",
				"REFLECTOR_B": "YRUHQSLDPXNGOKMIEBFZCWVJAT"}

	saltos = {"ROTOR_I": "R", 
				"ROTOR_II": "F",
				"ROTOR_III": "W",
				"ROTOR_IV": "K",
				"ROTOR_V": "A"}
	
	
	

	def __init__(self, r_izquierdo, r_central, r_derecho, reflector, c_izquierdo, c_central, c_derecho, lista_clavijas=[]):

		self.r_izquierdo = (self.rotores[r_izquierdo])
		self.r_central = (self.rotores[r_central])
		self.r_derecho = (self.rotores[r_derecho])

		self.reflector = (self.rotores[reflector])

		self.c_izquierdo = c_izquierdo
		self.c_central = c_central
		self.c_derecho = c_derecho

		self.s_izquierdo = (self.saltos[r_izquierdo])
		self.s_central = (self.saltos[r_central])
		self.s_derecho = (self.saltos[r_derecho])
		
		self.lista_clavijas = lista_clavijas

		pass

	def resto(self, posicion):
		if posicion >= 26:
			realPos = posicion%26
			return realPos 
		return posicion	
	
	def codifica(self, texto):
		texto_codificado = ""
		#TO DO

		posRotDer = self.alfabeto.find(self.c_derecho)
		posRotCen = self.alfabeto.find(self.c_central)
		posRotIzq = self.alfabeto.find(self.c_izquierdo)

		print("El texto a codificar es: " + texto)


		for letra in texto:

			letra = letra.upper()
			# print("Camino Ida")
   
			l = len(self.lista_clavijas)
			i = 0
			j = 0

			while i < l:
				if(letra == self.lista_clavijas[i][0]):
					letra = self.lista_clavijas[i][1]
					break
				if(letra == self.lista_clavijas[i][1]):
					letra = self.lista_clavijas[i][0]
					break
					
				i = i + 1
			# print(letra)
			posicion = self.alfabeto.find(letra)
			posRotDer = posRotDer + 1

			if(self.alfabeto[self.resto(posRotDer)] == self.s_derecho):
				posRotCen = posRotCen + 1
		
			if(self.alfabeto[self.resto(posRotCen) + 1] == self.s_central):
				posRotCen = posRotCen + 1
				posRotIzq = posRotIzq + 1

			rot1 = self.r_derecho[self.resto(posicion + posRotDer)]
			# print(rot1)

			posicion = self.alfabeto.find(rot1) - posRotDer 
			rot2 = self.r_central[self.resto(posicion + posRotCen)]
			# print(rot2)

			posicion = self.alfabeto.find(rot2) - posRotCen
			rot3 = self.r_izquierdo[self.resto(posicion + posRotIzq)]
			# print(rot3)

			posReflector = self.alfabeto.find(rot3) - posRotIzq

			reflect = self.reflector[posReflector]

			# print("Posicion del reflector: " + reflect)
			# print("Camino Vuelta")

			posicion = self.alfabeto.find(reflect)
			aux = self.alfabeto[self.resto(posicion + posRotIzq)]
			rot4 = self.alfabeto[self.r_izquierdo.find(aux)]
			# print(rot4)

			posicion = self.alfabeto.find(rot4) - posRotIzq
			aux = self.alfabeto[self.resto(posicion + posRotCen)]
			rot5 = self.alfabeto[self.r_central.find(aux)]
			# print(rot5)

			posicion = self.alfabeto.find(rot5) - posRotCen
			aux = self.alfabeto[self.resto(posicion + posRotDer)]
			rot6 = self.alfabeto[self.r_derecho.find(aux)]
			# print(rot6)

			posicion = self.alfabeto.find(rot6) - posRotDer
   
			letter = self.alfabeto[posicion]

			# print("Letra obtenida: " + letter)
   
			while j < l:
				if(letter == self.lista_clavijas[j][0]):
					letter = self.lista_clavijas[j][1]
					break
				if(letter == self.lista_clavijas[j][1]):
					letter = self.lista_clavijas[j][0]
					break
				j = j + 1

			texto_codificado = texto_codificado + letter
			# print("El resultado obtenido es: " + texto_codificado)
		return texto_codificado
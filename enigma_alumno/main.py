from codigo.enigma_alumno import Enigma


if __name__ == '__main__':
	enigma = Enigma(r_izquierdo="ROTOR_I", r_central="ROTOR_II", r_derecho="ROTOR_III", reflector="REFLECTOR_B", c_izquierdo="C", c_central="M", c_derecho="A", lista_clavijas=[])
	print("El texto cifrado es", enigma.codifica("holaquetal"))

import time

class Ecomyclass_buscador_personas():

	def ebp_cargartxtcedulas():
		
		
		f = open ('cedulas.txt')
		datis = f.read()
		time.sleep(2)
		cedulas_array = []
		for fila in datis.split("\n"):
			fila_en_pos = fila
			cedulas_array.append(str(fila_en_pos))
		f.close()
		print('')
		time.sleep(.7)
		return cedulas_array









class Ecomyclass_cargar_cedulas():
	def __init__(self):
		print('Iniciando aplicacion en consola...')
		time.sleep(.4)
		print('.')
		print('Cargando archivo de cedulas')
		time.sleep(.4)
		print('..')
		time.sleep(.4)
		print('...')
		arrays = Ecomyclass_buscador_personas.ebp_cargartxtcedulas()
		lineas = []
		personaCompleta = []

		personasCompletas = []

		for i in arrays:
			dato = i.split(",")
			personasCompletas.append(str(dato))
			time.sleep(0.2)


		print('--Test--')
		time.sleep(.4)
		print('.')
		time.sleep(.4)
		print('..')
		time.sleep(.4)
		print('...')
		time.sleep(1)
		self.mostrar_cualquier_array(personasCompletas)


	def mostrar_cualquier_array(self, array):
		todo_el_array = Ecomyclass_buscador_personas.ebp_cargartxtcedulas()

		for i in todo_el_array:
			print (i)
		print('')
		print('Archivo mostrado y variable lista para sea guardar en  base de datos y trabajar con ella a antojo')


startapp = Ecomyclass_cargar_cedulas()

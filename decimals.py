# -*- coding: utf-8 -*-

def do_trunk():
	"""
	Para redondear un numero en pyhton utilizamos la función round:

	El resultado seria 12.0546
	En la expresión {0:.2f}, en el lado del valor del diccionario indicamos el numero de decimales.
	Seguido del metodo format y dentro la cantidad a truncar.
	"""
	return "{0:.4f}".format(12.05464897987)

def do_round():
	"""
	Para redondear un numero en pyhton utilizamos la función round:

	El resultado seria 12.0547
	Ejecutamos el metodo round y este recibe:
	- Cantidad
	- Numero de Decimales a redondear.
	"""
	return round(12.05464897987,0)

def do_short():
	return "{0:.2f}".format(123456789.0777000)


if __name__ == "__main__":
	print(do_trunk())
	print(do_round())
	print(do_short())

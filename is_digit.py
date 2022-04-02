

def start(data):
	for i, x in enumerate(data):
		result = x[0].replace(x[1], "", 1).isdigit()
		print(result)

def get_numbers_from_string():
	"""Using List comprehension + isdigit() +split() 
	"""
	text_string = 'HORAS EXTRAS DOBLES 3:09'
	d = [i for i in text_string.split() if i.replace(":", "", 1).isdigit()]
	return d

data = [
	("124", "."),
	("12.4", "."),
	("12:4", ":"),
	("12,4", ","),
	("12..4", "."),
	("192.168.1.1", ".")
]
if __name__ == "__main__":
	start(data)
	number = get_numbers_from_string()
	print(number)
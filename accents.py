# -*- coding: utf-8 -*-
import unicodedata


def start():
	""" 
	Normalise (normalize) unicode data in Python to remove umlauts, accents etc. 
	"""
	data = u'naïve café'
	normal = unicodedata.normalize('NFKD', data).encode('ASCII', 'ignore')
	return normal


if __name__ == "__main__":
	d = start()
	print(d)
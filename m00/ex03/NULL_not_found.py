import math

def NULL_not_found(object: any) -> int:
	t = type(object)
	if object is None:
		print('Nothing:', object, t)
	elif t == float and math.isnan(object):
		print('Cheese:', object, t)
	elif t == int and object == 0:
		print('Zero:', object, t)
	elif t == str and not object:
		print('Empty:', t)
	elif t == bool and not object:
		print('Fake:', object, t)
	else:
		print('Type not Found')
		return 1
	return 0

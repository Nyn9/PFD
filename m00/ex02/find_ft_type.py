def all_thing_is_obj(object: any) -> int:
	t = type(object)
	if (t == list):
		print("List : ", t)
	elif (t == tuple):
		print("Tuple : ", t)
	elif (t == set):
		print("Set : ", t)
	elif (t == dict):
		print("Dict : ", t)
	elif (t == str):
		print(f"{object} is in the kitchen : ", t)
	else:
		print("Type not found")
	return 42;
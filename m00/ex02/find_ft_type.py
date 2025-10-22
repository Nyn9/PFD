def all_thing_is_obj(object: any) -> int:
    t = type(object)
    if isinstance(object, list):
        print("List :", t)
    elif isinstance(object, tuple):
        print("Tuple :", t)
    elif isinstance(object, set):
        print("Set :", t)
    elif isinstance(object, dict):
        print("Dict :", t)
    elif isinstance(object, str):
        print(f"{object} is in the kitchen :", t)
    else:
        print("Type not found")
    return 42

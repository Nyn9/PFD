def NULL_not_found(object: any) -> int:
    t = type(object)
    if object is None:
        print('Nothing:', object, t)
    elif object != object:
        print('Cheese:', object, t)
    elif object == 0:
        print('Zero:', object, t)
    elif t == str and not object:
        print('Empty:', t)
    elif t == bool and not object:
        print('Fake:', object, t)
    else:
        print('Type not Found')
        return 1
    return 0

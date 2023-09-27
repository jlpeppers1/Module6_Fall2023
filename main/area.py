def area(length, width=''):
    """
    try:
        if width == '':
            width = length
        if length <= 0:
            print("Lenth is less than 0")
            raise ValueError
        if width <= 0:
            print("Lenth is less than 0")
            raise ValueError
        return length * width
    except:
        print("You did not supply integers as arguments")
        raise ValueError
    """
    try:
        if width == '':
            width = length
        length = int(length)
        width = int(width)
    except:
        print("Must supply integers")
        raise ValueError
    if (length < 0) or (width < 0):
        print("length must not be negative")
        raise ValueError
    return length * width

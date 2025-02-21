def string_color(name):
    if len(name) < 2: return None
    
    values = [ord(i) for i in name]
    first = hex(sum(values) % 256).replace("-", "")[2:]
    total = 1
    for i in values:
        total = total * i
    
    second = hex(total % 256).replace("-", "")[2:]
    print("second:", second)
    
    third = hex(values[0] - sum(values[1:])).replace("-", "")[2:]
    print("third", third)
    
    return first.upper()+second.upper()+third.upper()
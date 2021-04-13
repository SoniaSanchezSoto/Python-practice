def num_max (a, b, c):
    if a > b and a > c:
        print (a)
    elif b > a and b > c:
        print (b)
    elif c > a and c > b:
        print (c)
    else:
        print ("Son Iguales")
num_max(1,2,3)
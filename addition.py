def add(a, b):
    "Return the sum of a and b"
    print("Passed a=%s and b=%s, returning a+b=%s" % (a,b,a+b))
    return a+b


if __name__ == '__main__':
    add(1,1)
    add(2,3)
    add(10,-2.1)
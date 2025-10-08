def trace(fn): #fn -> function pointer
    def enhance(n):
        print(f"{fn.__name__}: {n}")
        return fn(n)
    return enhance 

@trace 
def square(n):
    return n**2

@trace 
def cube(n):
    return n**3

@trace 
def quad(n):
    return n**4

# x = trace(quad)(5)
# print(x)

#now using the @notation 
result = cube(5)
print(result)
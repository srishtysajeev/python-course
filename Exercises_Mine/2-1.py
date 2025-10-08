def leapyear(year):
    if year % 400 == 0:
        return True 
    elif year % 100 == 0:
        return False 
    elif year % 4 == 0:
        return True   
    else:
        False 

print(leapyear(2000))
print(leapyear(1900))
print(leapyear(2012))
print(leapyear(2011))

def days_between_years(year1, year2):
    counter = 0
    assert year2 > year1
    for i in range(year2-year1 -1):
        if leapyear(year1) is True: 
            counter += 366
        else:
            counter += 365
    return counter

#days_between_years(2999, 2000)
print(days_between_years(2000, 2999))


"""
Write a program that prints out the square, cubes and fourth power of the first 20 integers.
Use a decorator
"""

def print_decorator(fn): 
    def nice_statement(num): 
        func_name = fn.__name__ 
        print(f"Calculating... {func_name} of {num}:") 
        return fn(num)
    return nice_statement

@print_decorator
def square(x): 
    return x * x
@print_decorator
def cube(x):
    return x * x * x
@print_decorator
def quad(x):
    return x * x * x * x

print(cube(20))


# def fib(num): 
    


"""Write a function that rotates the values of 3 variables.  For example:"""

def rotate_vars(x, y, z):
    store = [x, y, z]
    x = store[1]
    y = store[2]
    z = store[0]

def rotate_array(arr: list):
    #el_1 = arr[0]
    # get rid of first element 
    # add it onto the end 
    # we want some kind of fifo 
    el_1 = arr.pop(0)
    arr.append(el_1)
    return arr 

print(rotate_array([100, 200, 300, 400, 500]))



lookUp = { 
             0: '', 
             1: 'I', 
             2: 'II', 
             3: 'III', 
             4: 'IV', 
             5: 'V',
             6: 'VI', 
             7: 'VII', 
             8: 'VIII', 
             9: 'IX', 
            10: 'X',
            20: 'XX',
            30: 'XXX',
            40: 'XL',
            50: 'L',
            60: 'LX',
            70: 'LXX',
            80: 'LXXX',
            90: 'XC',
           100: 'C',
           200: 'CC',
           300: 'CCC',
           400: 'CD',
           500: 'D',
           600: 'DC',
           700: 'DCC',
           800: 'DCCC',
           900: 'CM',
          1000: 'M',
          2000: 'MM',
          3000: 'MMM',
          4000: 'MMMM'
         }
def roman_num(num): 
    if num in lookUp: 
        print(lookUp[num])
    if num < 100: 
        # need to find the 


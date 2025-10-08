# Notes 

- Website to see the most popular languages: https://www.tiobe.com/tiobe-index/ 
- Interpretter goes line by line to machine code but compiler does the whole thing first 
- Python acts as a compiler and imterpretter = slow 
- anaconda depreciated at diamond because of a paywall now use conda to install python 
- use time.sleep to run pieces of code concurrently 
- id() tells you where the object is in memory 
- l value is what appears on left hand side of equals and r value is what appears on rhs of '='
- print(f"main symbol table: {list(locals().keys())}")
Use above to list aout all symbols 

## Debugger 
- F5 to start debugger from the start 
- Can edit the launch.json in .vscode to customise 
    ```"stopOnEntry": true``` makes sure you start debugger from line 1 
    ```"justMyCode": true``` set to false if you want to go into external libs 



print(", ".join(list)) -> convert list to a string 
## Unicode 
You can use symbols in variable names (see 10.9)

## Logging
- you have to set your level of logging (you will get that level and everything below it)
- glob allows you to use wildcards ! 

## Decorator 
- see memoize for why this is useful 
- @property allows you to call methods without the brackets - this cuts down on time as the attributes are only calculated when needed and not when instantiated (note that usually everything is stored in a dict which can be accessed with object.__dict__)

## OOP 
Diff to functional because you store the state of your object like petrol level in a car. 
In banking you can have locks so that (mutable data) a transaction can only be done by one person 
Threading - allows you to run code concurrently 
'pointer' is a pointer in memory and anything that has a name can be a pointer 
If you add a __str__ then you can print out a desc of your object ! 
use dir() to get all methods of a class 
variables traverses the dictionary from lowest (object) to highest (class) see the oop-revision file you made 

Association - Uses A 
Aggregation - Has A 
Inheritance - Is A 

When inheriting from a base class you can either do BaseClass.__init__() OR super.__init__

## List comprehension 
    list        [ fn(item) for item in sequence ]
    dict        { key:value for item in sequence }
    set         { fn(item) for item in sequence }
    generator   ( fn(item) for item in sequence )

See example to handle exceptions 

```python

def catch(fn):  # fn captures n in the call
    try:
        return f"{fn():.2f}"  # fn = the lambda which takes no parameters
    except Exception as e:
        return e

# create a list containing zero
numbers = [float(n) for n in range(-5, 5)]
print(numbers)

# comprehension will raise an exception for a zero entry
reciprocals = [catch(lambda : 1/n) for n in numbers] # lambda captures n
print(f"{reciprocals}")

```
## Iterators 
Python iterators are defined as classes that support the following methods: __iter__() and __next__().
Amongst other things, Python provides special language support for iterators when used in a for loop.  We will 
be investigating this support below.


## Generators

Python created generators.  Generators are a special type of iterator.  A generator is defined as any function
that uses the "yield" instruction.

Can use g.__next__() or next(g) -> this is the same thing 
(g is generator above)

Iterators don't have to return self while generators do 

Difference between an iterable and iterator is just that iterable has the next() method 
To stop iteration without error: 
```python
except StopIteration as e:
        break
```

## lambda funcs
introduced because they were in C and ppl wanted it in python 

SYNTAX
lambda in:out

filter: 
```python 
sequence = [5, 7, 9, 2, 4, 6]
result = filter (lambda x: x > 4, sequence) 
```

* you can use lambdas to pass into other funcs as parameters because it is technically an expression 

## scope 
The letters in the acronym LEGB stand for Local, Enclosing, Global, and Built-in scopes. 

```python 
sum = 99        # global scope

def outer():
    sum = 88    # enclosing scope
    def inner():
        sum = 77  # local scope
        print(sum)
    inner()

outer()
```

## partial funcs 
these let you add some parameters and then add the rest later . 


## closures
use displayClosures()
you can add an immutable type to local variable using ```nonlocal x``` (see gotcha 6)
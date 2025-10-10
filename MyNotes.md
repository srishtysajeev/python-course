# Notes 

- Website to see the most popular languages: https://www.tiobe.com/tiobe-index/ 
- in functional programming everything is immutable 
- Interpretter goes line by line to machine code but compiler does the whole thing first 
- Python acts as a compiler and imterpretter = slow 
- Use multiple processes if CPU intensive and multiple threads if IO intensive (not sure if that's the right way around )
- anaconda depreciated at diamond because of a paywall now use conda to install python 
- use time.sleep to run pieces of code concurrently 
- when we use something like linux we are actually using virtual rather than real memory - the amount of space in the virtual will be much less than real and it is then saved to disk so both can see the data..
- id() tells you where the object is in memory 
- l value is what appears on left hand side of equals and r value is what appears on rhs of '='
- print(f"main symbol table: {list(locals().keys())}")
- polars is pandas but written in rust and it is meant to be much faster and like a sql database (not good with delimiters)
Use above to list aout all symbols 
- ```with``` python -> context manager. under covers will create a try finally to close the pool (usually used with I/O stasks)
- numpy arange is for an array range 
- To run python on multiple CPUs use Processes.join
- 
- A process is an entire executing program with its own memory space and resources, while a thread is a smaller unit of execution within a process that shares the process's resources
- quicker to do context switch with threads. threads are good if you have similar parts of a program you want to run concurrently. have to use processes if you want completely diff programs to run concurrently. 
coroutine is a two way generator 
- threading is not recommended in python (with the current version)
```Python 


@numba.jit(nopython=True, parallel=False)
def forLoopWithNumba(n):
    _sum = 0
    for i in range(n):
        _sum += float(i)**0.5
    return _sum
```
- Cython is the same as python but you just have to define your types at the top (40 - 50x faster than python ) -> converts to c code under the hood 
### numpy 
- np.array is much faster than normal arrays 
- np.arange is better than range because it can deal with floats 

- with np.linspace you get equal spacing and it includes the last number 

- can use np.reshape to reshape you array eg to a 3D one. 

```python 
# create array
a = np.arange(24); print(a)
# reshape it
b = a.reshape(2,3,4); print(b)
a[13] = 99
print(a)
print(b)
# display some properties held in the view
print(type(b))
print("Shape:", b.shape)
print("Dimensions:", b.ndim)
print("Size:", b.size)
print("Item type:", b.dtype.name)
print("Item size:", b.itemsize)
```
# dot and cross product
a = np.array( [[ 2,4], [3,5]] )
b = np.array( [[ 0,1], [1,0]] )
c = np.dot(a,b); print(c)
c = np.cross(a,b); print(c)
```
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

## Asincio 

Uses Corouties 
The asyncio module uses new style coroutines.  These are defined as a function prepended by the async keyword.
Coroutines are a type of generator and like generators you need to call them to create the actual coroutine.
Level 3/09 AsyncIO/04.tasks.py
```python
async def main(): # wrong (does each sequentially)
    await coroutine1()
    await coroutine2()
    await coroutine3()

async def main2(): # right way (does in parallel )
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())
    task3 = asyncio.create_task(coroutine3())
    await task1
    await task2
    await task3
```

So you have input output bound tasks where you give a program an input and you are waiting for an out put for example connecting to a website and then you have CPU intensive tasks which is are tasks that take a lot of processing power. 


## type hints 
types languages like C are much faster! 

Use mypy to check that your type hints work and that therea re no errors 

## matplotlib 
use tightlayout to prevent slots from overlapping 

## HDF5 
Basically a concept where you divide a file into it's own subdirectory and so you only load the bit you need into memory - not clogging up the whole file system. 

## Other 
Can run linux commands  using subprocess: 
```python 
import subprocess
try:
    subprocess.run("module load dawn; dawn")
except:
    print("you must be on a Diamond machine to run 'dawn'")
```

quick way to write a func 
```python
def f1(self): print("this is f1()")
```
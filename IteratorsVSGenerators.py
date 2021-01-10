hello_str = 'hello'
hello_iterator = iter(hello_str)
next(hello_iterator)
print(next(hello_iterator))
# iteralbe(such as (string,list) ____iter()____ iterator (could next())

def my_for(iterable,func):
    iterator = iter(iterable)
    while True:
        try:
            thing = (next(iterator))
        except StopIteration:
            break
        else:
            func(thing)

def square(x):
    print(x *x)
my_for([1,2,3,4,5,6,7],square)

class Counter:
    def __init__(self,low,high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration

for x in Counter(1,10):
    print(x)

# function   use return | only return once | when using  return value
# generatorfuc use yield| return many times| when using  return generator
def count_up_to(max):
    count = 1
    while count <=max:
        yield count
        count +=1
count = count_up_to(5) #this is a generator
print(next(count))
print(next(count))
for num in count:
    print(num)

def Yes_or_No():
    current = 1
    while True:
        current +=1
        if current%2 ==0:
            yield "yes"
        else:
            yield "no"

def yes_or_no():
    answer = "yes"
    while True:
        yield answer
        answer = "no" if answer == "yes" else "yes"

def get_multiples(number,count):
    current = number
    for num in range(0,count):
        yield current
        current += number

my_gen = get_multiples(1,10)
print(next(my_gen))
print(next(my_gen))

# Generator expression ()
# list comprehension []

sum(num for num in range(1,10))
sum([num for num in range(1,10)]) #this way cost more memory than generator expression

#example: generator function to generator expression:
def nums():
    for num in range(1,10):
        yield num
# ==
new_gen = (num for num in range(1,10))


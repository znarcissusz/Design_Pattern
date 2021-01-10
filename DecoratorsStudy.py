from functools import wraps
from time import time
def be_polite(fn):   #通俗理解 装饰器 有赋予被装饰greet超级能力,能力增强，或者限制其能力,限制必须输入什么以及顺序
    def wrapper():
        print('what a pleasure to meet you!')
        fn()
        print('have a greet day!')
    return wrapper

def greet():
    print('My name is Thomas.')

greet = be_polite(greet) #= @be_polite
#greet()
@be_polite
def rage():
    print('I HATE YOU!')
#polite_rage = be_polite(rage)
rage()


def shout(fn):
    def wrapper(*args,**kwargs):
        return fn(*args).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi,I'm{name}"

@shout
def order(main,side):
    return f"Hi, i'd like the {main},with a side of {side}"

print(greet("todd"))
print(order("burger","fires"))


def log_funtion_data(fn):
    @wraps(fn) #不加此行结果会不同
    def wrapper(*args,**kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}.")
        print(f"here's the documentation:{fn.__doc__}")
    return wrapper

@log_funtion_data
def add(x,y):
    """ADD TWO NUMBER TOGETHER"""
    return x+y
print(add.__doc__)
print(add.__name__)


def speed_test(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        start_time = time()
        result = fn(*args,**kwargs)
        end_time = time()
        print(f"Executing {fn.__name__}")
        print(f"Time Elapsed:{end_time -start_time}")
        return result
    return wrapper

@speed_test
def sum_num_gen():
    return sum(x for x in range(9000000))

@speed_test
def sum_num_list():
    return sum([x for x in range(9000000)])

sum_num_gen()
sum_num_list()


def ensure_no_kwargs(fn):
    @wraps(fn)
    def wrapper(*args,**kwargs):
        if kwargs:
            raise ValueError("No Kwargs allowed!")
        return fn(*args,**kwargs)
    return wrapper
@ensure_no_kwargs
def greet(name):
    return f"hi,I'm{name}"

print(greet("thomas"))

# @decorator
# def func(*args,**kwargs):
    # pass
# func = docorator(func)
####################################
# @decorator(arg)
# def func(*args,**kwargs):
    # pass
# func = decorator(arg)(func)
def ensure_first_arg_is(val):
    def inner(fn):
        @wraps(fn)
        def wrapper(*args,**kwargs):
            if args and args[0] != val:
                return f"First arg needs to be {val}"
            return fn(*args,**kwargs)
        return wrapper
    return inner

@ensure_first_arg_is("burrito")
def fav_food(*foods):
    print(foods)

print(fav_food("pizza","burrito"))

@ensure_first_arg_is(10)
def add_to_ten(num1,num2):
    return num1 + num2
#输入的第一个参数必须是10

def enforce(*types):
    def decorator(f):
        def new_func(*args,**kwargs):
            new_args = []
            for (a,t) in zip(args,types):
                new_args.append(t(a))
            return f(*new_args,**kwargs)
        return new_func
    return decorator

@enforce(str,int)
def repeat_message(msg,times):
    for time in range(times):
        print(msg)

repeat_message('hello',3)

@enforce(float,float)
def divide(a,b):
    print(a/b)
divide(5,5,10)


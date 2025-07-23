import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #do somthing
        function()
        function()
        # do somthing
    return wrapper_function

@delay_decorator
def say_hello():
    print("Delay because of decorator")

@delay_decorator
def say_Bye():
    print("Delay because of decorator")

def say_Greeting():
    print("Delay because of decorator")


say_hello()
say_Bye()

decorated_function = delay_decorator(say_Greeting)
decorated_function()
from datetime import datetime

def logger(func):
    def wrapper():
        print("Function Name:", func.__name__)
        print("Called At:", datetime.now())
        return func()
    return wrapper


@logger
def greet():
    print("Hello, Welcome!")


greet()
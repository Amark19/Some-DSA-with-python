'''
helps to modify function
why do we need to modfiy function?

- lets suppose you have 1000 functions and you want to add some print statement in one of function before running function then instead of searching you can use decorators to modify it
'''

# def some_fun(func):
#     def wrapper():
#         print("this is before fun")
#         func()
#         print("this is after fun")
#     return wrapper

# @some_fun
# def add():
#     print("in fun")

# add()

import os

def decor(fx):
    def wrapper(*args):
        output = fx(*args)
        print(output)
        
    return wrapper

@decor
def func(path):
    if os.path.exists(path):
        return os.path.getsize(path)
    else:
        return "file not exist"

func("A://calcont-users.csv") # decor(func)("somePath")

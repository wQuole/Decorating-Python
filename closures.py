__author__ = 'William Kvaale'
# C L O S U R E S 
'''
"(wikipedia)... is a record storing a function together with an environment: 
a mapping associating each free variable of the function with the value or 
storage location to which the name was bound when the closure was created."
---
A closure is an inner function that remembers and has access to variables in the local scope in which is was created,
even after the outer function finished executing.
'''


def outer_func(msg):
    def inner_func():
        print(msg)

    return inner_func

__author__ = 'William Kvaale'

import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))
    return log_func

def add(x, y):
    return x + y

def sub(x, y):
    return x - y



def main():
    # --- Basics
    # hi_func = outer_func('hi')
    # bye_func = outer_func('bye')
    # hi_func()
    # bye_func()
    # --- Logger below 
    add_logger = logger(add)
    sub_logger = logger(sub)

    add_logger(3,3)
    add_logger(4,5)

    sub_logger(70,1)
    sub_logger(1339,2) 


if __name__ == '__main__':
    main()
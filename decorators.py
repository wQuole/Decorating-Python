__author__ = 'William Kvaale'
# D E C O R A T O R S


# Class decorator, basically same functionality as decorator_func
'''
class decorator_class(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print('The call method executed this before {} ...'.format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)
'''

def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print('Wrapper function executed this before {} ...'.format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func


@decorator_func
def display():
    print('Display function executed ... \n')


@decorator_func
def display_info(name, age):
    print('Display_info ran with arguments ({}, {})'.format(name, age))


def main():
    display()
    display_info("Bobby Binders", 29)

if __name__ == '__main__':
    main()


''' C O M M E N T:
 def display():
    print('Display function executed ... \n')

decorated_display = decorator_func(display)
decorated_display()

 ... is EQUIVALENT with ...

@decorator_func # This is where the magic happens
 def display():
     print('Display function executed ... \n')
'''
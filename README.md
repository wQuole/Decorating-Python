# Decorating-Python
Getting started with using decorators in Python 3.7 using this [quick guide](https://www.youtube.com/watch?v=kr0mpwqttM0&index=1&list=PLzTAO9z9xIreYGpvZpQqmE_z12ijDqFun)

Got inspired at [itDAGENE 2018](https://itdagene.no) when [Equinor](https://www.equinor.com/no.html) held a short course on how to use Decorators in Python. 

### Some keynotes:
```python
 def display():
    print('Display function executed ... \n')

decorated_display = decorator_func(display)
decorated_display()

# ... is EQUIVALENT with ...

@decorator_func # This is where the magic happens
 def display():
     print('Display function executed ... \n')
```
### and ...

```python
@my_logger
@my_timer
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


# ... is EQUIVALENT with ...

def display_info(name, age):
   print('display_info ran with arguments ({}, {})'.format(name, age))

display_info = my_logger(my_timer(display_info))
```

__author__ = 'William Kvaale'
# F I R S T  C L A S S  F U N C T I O N S


def cube(x):
    return x * x * x


def square(x):
    return x*x


def my_map(func, arg_list):
    result = []
    print("Preprosessed numbers:\n ",arg_list)
    print("\nNew numbers: ")
    for i in arg_list:
        result.append(func(i))
    return result


def logger(msg):
    def log_message():
        print("Log:", msg)
    return log_message


def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text


def main():
    # --- Basic
    #f = square
    #print(square) # Prints <function square at 0x01C70810 >
    #print(f(5)) # Prints 5*5 = 25
    
    #squares = my_map(square, [1,2,3,4,5])
    #print(squares)

    #log_hi = logger("Hi!")
    #log_hi()

    # html 
    # print_h1 = html_tag('h1')
    # print_h1('Test Headline!')
    # print_h1('Another Headline!')
    # print_p = html_tag('p')
    # print_p('Test paragraph')


if __name__ == '__main__':
    main()  

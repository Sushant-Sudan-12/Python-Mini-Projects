
def add(*args):
    sum = 0
    for n in args:          #args is  a tuple
        sum += n
    print(sum)

add(2,3,4)


def calculate(n, **kwargs):
    #kwargs is a dictionary
    n += kwargs["add"]               # Necessary Argument
    n -= kwargs["sub"]               # Necessary Argument
    if kwargs.get("mul")!=None:      # Optional argument
        n *= kwargs.get("mul")       # Optional argument
    if kwargs.get("div")!=None:      # Optional argument
        n /= kwargs.get("div")       # Optional argument
    print(n)

calculate(4,sub = 3,mul = 10 , div = 2 , add = 6)
calculate(4,add = 6,sub = 3,mul = 10) #THIS GIVES ERROR SO WE USE get METHOD IN OUR FUNCTION
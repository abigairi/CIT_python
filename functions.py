#ans 1
def fun1(name, age=20):
    print(name, age)
fun1('Emma', 25)

#ans 2
def fun1(*data):
    for i in data:
      print(i)
      print("Done!")
fun1(25, 75, 55)
fun1(10, 20)

#ans 3
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d

    return inner_fun(a, b)
    return a

result = outer_fun(5, 10)
print(result)

#ans 4


#qn 5
def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)

#qn 6

def display(**kwargs):
    for i in kwargs:
        print(i)

display(emp="Kelly", salary=9000)

#qn 7
def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)

# qn 8
def add(a, b):
    return a+5, b+5

result = add(3, 2)
print(result)

#qn 9

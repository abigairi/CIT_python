a = 22
b =25
if a > b:
            print("a is greator than b")
else:
            print("a is not greator than b")

            #comparison operator
val =  b > a
print(val)

val1 = b < a
print(val1)

val2 = b == a
print(val2)


#logical operator



#functions gives ouput when it is called 

def fun ():
            print("Welcome to CIT Uganda course for python")
fun()

# example 2 (passing parameter )

def add(num1: int, num2: int) -> int:
	"""Add two numbers"""
	num3 = num1 + num2

	return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f" {num1} and {num2} results {ans}.")




#mo examples of functions
def my_name(fname,lname):
            print(fname, lname)
            
my_name(fname='Abigail',lname='Mnzava')
my_name(fname='love to learn every day',lname='GOD lead me to achive better than yesterday.')
            


#more examples
def func (*kids):
            print("The youngest child is " + kids[2])

func=("asha","joe","loe")




#maswali

x = 10.0
y = (x < 100.0) and isinstance(x, float)
print(y)


# maswali 01

n = 1 + 2 ** 3 * 4
print(n)

#maswali 2

x = 100
x *= 5
print(x)

#maswali 3

print(-18 // 4)

# maswali 4
a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)

#maswali 5
x = 100
y = 50
print(x and y)

#maswali 6
print(2%6)

#maswali 7
print(2 ** 3 ** 2)
x = 6
y = 2
print(x ** y)
print(x // y)

#maswali 8
a = 4
b = 11
print(a | b)
print(a >> 2)

#maswali 9
print(10 - 4 * 2)

#maswali 10
print(2 * 3 ** 3 * 4)

#maswali 11
y = 10
y += 2
print(y)

#maswali 12
x = 10
y = 50
if x ** 2 > 100 and y < 100:
    print(x, y)
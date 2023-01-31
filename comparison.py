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






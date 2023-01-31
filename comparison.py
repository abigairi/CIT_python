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



# some more functions
def is_prime(n):
	if n in [2, 3]:
		return True
	if (n == 1) or (n % 2 == 0):
		return False
	r = 3
	while r * r <= n:
		if n % r == 0:
			return False
		r += 2
	return True
print(is_prime(78), is_prime(79))



#1
strOne = str("pynative")
strTwo = "pynative"
print(strOne == strTwo)
print(strOne is strTwo)

#2
str = "My salary is 7000"
print(str.isalnum())

#3
str1 = "My salary is 7000"
str2 = "7000"

print(str1.isdigit())
print(str2.isdigit())

#4
print("John" > "Jhon")
print("Emma" < "Emm")

#5
myString = "pynative"
stringList = ["abc", "pynative", "xyz"]

print(stringList[1] == myString)
print(stringList[1] is myString)

#6
str1 = "PYnative"
print(str1[1:4], str1[:5], str1[4:], str1[0:-1], str1[:-1])

#7
str = "my name is James bond"
print (str.capitalize())

#8
str1 = "my isname isisis jameis isis bond"
sub = "is"
print(str1.count(sub, 4))

#9
str1 = 'Welcome'
print(str1*2)

#10
str1 = 'Welcome'
print (str1[:6] + ' PYnative')

#11

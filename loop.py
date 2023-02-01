for num in range(2,-5,-1):
    print(num, end=", ")

# answer 2
for num in range(10, 14):
   for i in range(2, num):
       if num%i == 1:
          print(num)
          break

#answer 3
for num in range(-2,-5,-1):
    print(num, end=", ")

#answewr 4
    x = 0
while (x < 100):
  x+=2
print(x)

#answer 5
x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)

#answer 6
for l in 'Jhon':
   if l == 'o':
      pass
   print(l, end=", ")

#answewr 7
a, b = 12, 5
if a + b:
    print('True')
else:
  print('False')

#answewr 8
x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

#answer 9
var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)

#answe 10
x = 0
a = 0
b = -5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

#answer 11
numbers = [10, 20]
items = ["Chair", "Table"]

for x in numbers:
  for y in items:
    print(x, y)

#answer 12

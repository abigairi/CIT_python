f = open("test.txt", "r")
print(f.readline(3))
f.close()

#2
x = float('NaN')
print('%f, %e, %F, %E' % (x, x, x, x))

#3

print('[%c]' % 65)

#4
#print('Tanzania ', end='//')
#print(' is for ', end='//')
#print(' forever in my heart', end='//')

#5
print('Ben', 25, 'California',sep='--')

#6
print('%x, %X' % (15, 15))
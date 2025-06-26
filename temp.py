"""
n = 123400
rev = 0
while n>0:
    d = n % 10
    rev = (rev * 10) + d
    n = n // 10
print(rev)

num = 54451

s = str(num)
if s == s[::-1]:
    print("True")
else:
    print("False")

a , b = 20, 15
while a > 0 and b > 0:
    if a > b:
        a = a % b
    else:
        b = b % a
    
    if a == 0:
        print(b)
    elif b == 0:
        print(a)

n = 3710
temp = n
cnt = len(str(n))
total = 0
while n > 0:
    rem = n % 10
    total += rem ** cnt
    n = n // 10

if total == temp:
    print("Yes")
else:
    print("No")
    

l = [2,2,3,4,4,2]
d= dict()
for i in l:
    d[i] = d.get(i, 0) + 1

max_key = max(d, key=d.get)
max_val = d[max_key]
print(max_key)
min_key = min(d, key=d.get)
print(min_key)
print(d)
"""

l = [1,2,3,4,9,3,4,56,11,789]

largest = -1
second_largest = -1

for i in l:
    if i > largest:
        second_largest, largest = largest, i

l = [1,2,4,5,6,7,8,9]
calcualted_sum = int(9*10/2)
actual_sum = sum(l)
print(calcualted_sum - actual_sum)

xor = 0
for i in l:
    xor = xor ^ i
print(xor)

def test(num):
    if int(num) % 2 != 0:
        return num
    for i in range(len(num)-1, -1, -1):
        if int(num[i]) % 2 != 0:
            return num[0:i]
    
    return ""

print(test("1234567"))

    
file = open("Notes.txt", "r")
data = file.read()
print(data)
file.close()

#print(file.read())  # Bug 1: Trying to read after closing the file


"""
Note questions
"""
l = [1,2]
m = l
print(id(l))
print(id(m))
m.append(3)
print(id(l))
print(id(m))
print(l, m)

s1 = "test"
s2 = "test"
print(id(s1))
print(id(s2))
s2 += " pass"
print(s1,s2)
print(id(s1))
print(id(s2))


def test():
    try:
        return 1
    finally:
        return 2

print(test())

def square(n):
    return n*n

def sum(x):
    tot = 0
    for n in range(1,x):
        tot +=square(n)
    return tot

print(sum(10))

friends = ['Jack', 'Rose', 'Stark']
for x in friends:
    print("Hello", x)

values = [20, 34, 45, 66]
total = 0
length = 0
for a in values:
    total += a
    length += 1
print("Total sum ", str(total))
print("Average ", str(total/length))

def factorial(n):
    result =1
    for i in range(1, n+1):
        result= result*i
    return result
print(factorial(4))

def to_Celcius(x):
    return (x-32)*5/9
    for b in range(0, 101, 10):
        print(x, to_Celcius(x))

print(to_Celcius(23))
x = 0
while x<5:
    print("Not yet there, x=", str(x))
    x = x+1
print("x=" +str(x))


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")


attempts(4)

def count_down(current):
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)
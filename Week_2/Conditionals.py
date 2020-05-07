print("cat" > "Cat")

def hint_username(username):
    if len(username)<3:
        print("Username must be atleast 3 characters long")

hint_username("se")

def is_positive(number):
  if number > 0:
    return True

print(is_positive(1))

def is_pos(num):
    if num >0:
        return True
    else:
        return False
print(is_pos(0))

def hint_username(username):
    if len(username)<3:
        print("Username must be atleast 3 characters long")
    elif len(username)>15:
        print("Username must be atmost 15 characters long")
    else:
        print("Valid Username")
hint_username("Striker")

def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:
    return "Zero"
  else:
    return "Negative"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative
print("mountains".upper())

answer = "YES"
if answer.lower() == "yes":
    print("User said yes")

x = " YES "
print(x.strip())
print(x.lstrip())
print(x.rstrip())

def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0]
    return "".join(result).upper()

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
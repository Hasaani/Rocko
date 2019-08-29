import math

print("hello world")

# primitive data types
int = 15
string = "hassan"
float = 5.22
boolean = True

# python array
course = "python programming"
print(len(course))
print(course[0])
print(course[0:-5])

# escape character "/"
print("hello \\ world")
print("hello \n world")
print("hello \" world")
print("hello \' world")

# concatination  and formatted string method
firstName = "hassan"
lastName = "eman"
fullName = firstName + " " + lastName  # concatination
print(fullName)

firstName = "hassan"
lastName = "eman"
fullName = f"{firstName} {lastName}"  # formatted string
print(fullName)

# string functions or methods
course = "    programming language"
print(course.upper())
print(course.title())
print(course.strip())  # l or r
print(course.find("lan"))
print(course.replace("m", "b"))
print("khan" in course)
print("hazz" not in course)

# working with numbers

#    import math
# check math module sheet
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
print(2 // 2)  # no float
print(2 % 2)   # remainder
print(2 ** 2)  # exponent

print(round(2.6))
print(abs(-2.6))

print(math.ceil(2.1))
#   math.sin    use that

# input function
x = input("x: ")
y = x + 1
print(f"x: {x} , y: {y}")

# condition statements

temperature = 200
if temperature >= 25:
    print("it's hot")
elif temperature >= 20:
    print("it's warm")
    print("drink water")
else:
    print("it's cold")
print("done")

# ternary operator
age = 25
message = "wuu codaynaya" if age > 15 else "ma codaynayo"
print(message)

# chaining comparison operators
age = 32
if age >= 20 and age < 50:
    # if 20 <= age < 50:
    print("Good")
else:
    print("not good")

# for loops
for number in range(1, 11):
    print("hassan", number, number * ".")

# ----------------------------

successful = False
for x in range(3):
    print("attempt")
    if successful:
        print("successful")
        break
else:
    print("attempted 3 times and failed")

# nested loops (coordinates)
for x in range(5):
    for y in range(3):
        print(f"({x},{y}) ")

# iterables
for x in range(5):
    print(x)
    # for x in [1, 2, 3, 4, 5]:
    # for x in ("hassan"):

# while loop
number = 100
while number > 0:
    print(number)
    number //= 2

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

while True:
    command = input(">")
    print("qortay", command)
    if command.lower() == "quit":
        break

# exercise
count = 0
number = 2
while number < 10:
    count += 1
    print(number)
    number += 2
print(f"we have {count} even numbers")

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")

# functions  creating one


def great():
    print("hi there")
    print("welcome")


great()


def greating(first_name, last_name):  # perameter
    print(f"Hi {first_name} {last_name} ")
    print("welcome aboard")


greating("hassan", "eman")  # arguments
greating("hussein", "eman")


def salan(name):
    print(f"Hi {name}")


def get_greating(name):
    return f"hi {name}"  # will not print something


message = get_greating("hassan")  # this is the return value
print(message)


def salaan(name):
    print(f"Hi {name}")
  #  return "....."


print(salaan("hassan"))


def increment(number, by):
    return number + by


print(increment(2, by=1))  # by is keyword argument


def increments(number, by=1):  # defualt perameter and its optional
    return number + by


print(increments(2, 6))


def multiply(*numbers):  # one astrik is Tuples
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(5, 5, 4, 5))


def save_user(**user):  # double astrik is Dictionary
    print(user["name"])


save_user(id=1, name="hassan", age=22)


# =====================================

# FIZZBUZZ Algorithm

def fizz_buzz(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "fizzBuzz"
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(3))

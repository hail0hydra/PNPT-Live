##!/usr/bin/python3

# Print string
print("Hello, World!") #double quotes

print('Hello, world!') #single quotes

print("""This string runs multiple 
        lines""") # triple quotes for multiple lines


print("This string is "+"awesome!")

print("\n") # new line



# MATH

print(50+50) #add
print(50-50) #subtract
print(50 *50) #multiply
print(50/50) #divide
print(50+50 - 50*50 /  50) #BODMAS
print(50**2) #exponents
print(50%6) # modulo - remainder
print(50/6)
print(50//6) #Quotient - division with no leftovers


 # Variables and methods
quote = "All is fair in love and war"
print(quote)

# A method is a functions avialable for given object. we are talking about bbuilt-ins

print(quote.upper())
print(quote.lower())
print(quote.title())
print(len(quote))


name = "regx" #string
age = 1337 #int
gpa = 3.7 # float

print(int(age))
print(int(30.1))
print(int(30.9))

print("My name is "+name+" and I am "+str(age)+" years old.")

age+=1

print(age)

birthday = 1
age+= birthday

# print(age)



# Functions

print('\n')

print("Here is an example function")

def whoami():  # this is a function
    name = "regx"
    age = "1337"
    print("My name is "+ name + " and I am "+str(age)+" years old.")

whoami()

# adding parameters

def add_one_hundred(num):
    print(num+100)

add_one_hundred(100)


# multiple parameters
def add(x,y):
    print(x+y)

add(7,7)

def multiply(x,y):
    return x*y

print(multiply(7,7))


def square_root(x):
    print(x ** 0.5)

square_root(64)


def nl():
    print("\n")

nl()



# BOOLEAN EXPRESSIONS (True or False)

print("Boolean Expressions:")


bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1, bool2, bool3 , bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

nl()


# RELATIONAL AND BOOLEAN OPERATORS
greater_than = 7 > 5

less_than = 5<7
greater_or_equal_to = 7>=7
less_than_or_equal_to = 7<=7

nl()

test_and = (7 > 5) and (5 < 7) # True
test_and2 = (7 > 5) and (5 > 7) #False
test_or = (7 > 5) or (5 < 7) # True
test_or2 = (7 > 5) or (5 > 7) # False


test_not = not True # False
nl()


#CONDITIONAL STATEMENTS

def drink(money):
    if money >= 2:
        return "You've got yourself a drink"
    else:
        return "No drink for you!"

print(drink(3))
print(drink(1))

def alcohol(age, money):
    if (age >= 21) and (money >= 5):
        return "We're getting a drink!"
    elif (age >= 21) and (money < 5):
        return "Comeback with more money."
    elif (age < 21) and (money >=5):
        return "Nice try, kid!"
    else:
        return "You're too poor and too young!"

print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))

'''print("         /|")
print("        / |")
print("       /  |")
print("      /   |")
print("     /    |")
print("    /     |")
print("   /      |")
print("  /       |")
print(" /________|")

#Using variables
name=Charles
age= 20
print("There was once a man named ") print(name)
print("He is") print(age) print("years old")
print("he relly likes the name ") print(name)
print("But he does not like being") print(age)

#Getting two numbers from the user to perform a math operation
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")
result = float(number1) + float(number2)
print("Your answer is" (result))

#creating a madlip
name = input("Enter your name: ")
school = input("Enter your school: ")
age = input("Enter your age: ")
print("My name is " +name)
print("I school at " +school)
print("I am " +age+ " years old")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
result = float(num1) + float(num2)
print(f"Your answer is {result}")


#Using lists
friends = ["Franscisca", "John", "Rhymes", "Desmond", "Frank"]
print(friends[1:])


#Functions
def say_hi(name, feelings):
    print("Hello " +name+ " This is how i feel about you: " +feelings)


say_hi("Franscisca,","I love you")

#return statement
def add(number1, number2):
    return number1+number2

result = add(3,4)
print(result)

#using if/else comparisons with boolaen values
is_married = False
is_single = False

if is_married:
    print("You are not single")
elif is_single:
    print("You are not married")
elif not(is_married) and not(is_single):
    print("You are not ready for commitment")


#Building a simple calculator
num1 = float(input("Enter the first number: "))
op = input("Enter a mathematical operator: ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1+num2)
elif op == "-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    print(num1/num2)
else:
    print("Invalid operator")



#using dictionaries

week_conversions = {
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thurs": "Thursday",
    "fri": "Friday",
    "sat": "Saturday",
    "sun": "Sunday",
}


print(week_conversions.get("hun","Invalid keyword"))

#Building a guessing game
secret_word = "franscisca"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess = input("Guess the secret word: ")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE!")
else:
    print("You win!")




#Building my own game

print("I am a country that has USA in the middle.")
print("What am I?")
print("NB: You only have three tries")

answer = "Jerusalem"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != answer and not(out_of_guesses):
    if guess_count<guess_limit:
        guess = input("What is the answer: ")
        guess_count = guess_count + 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of tries, Better luck next time")
else:
    print("HOORAY! You did it")




#for loops
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for days in week_days:
    if days == "Monday":
        print("This is the first day of the week")
    else:
        print("Not the first day of the week")

#Building exponential functions using for loops
def raise_to_the_power(base_num, power_num):
        answer = 1
        for index in range(power_num):
            answer = answer * base_num
        return answer


print(raise_to_the_power(2,5))

#2D Lists and Nested Loops
list_of_numbers = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10]
]

for row in list_of_numbers:
    for col in row:
        print(col)


#Building a simple Translator using pig latin

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter .isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation           

print(translate(input("Enter a word: ")))


#Try excepts

try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)

except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invalid Input")
    


#Reading files
Class_group_work_members = open("index2.html", "w")
Class_group_work_members.write("<p>This is HTML</p>")


Class_group_work_members.close()



#Using modules and pips
import Functions

print(Functions.add(3,4))'''



#Using classes and objects
class halls_of_residence:

    def __init__(self, name, color_of_shirt, location, identifier, quality_of_hall):
            self.name = name
            self.color_of_shirt = color_of_shirt
            self.location = location
            self.identifier = identifier
            self.quality_of_hall = quality_of_hall


    def whether_a_good_place(self):
        if self.quality_of_hall >= 3.5:
            print("A great place to stay for the semester")
        else:
            print("a place to manage till the semester ends")

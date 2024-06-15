age = 20
price = 19.95
first_name = 'shogo'
is_online = True
print(age)

name = input('What is your name?　')
print("Hello" + name)

birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)
print(age)

First = float(input('First: '))
Second = float(input('Second: '))
sum = First + Second
Str = str(sum)
print("Sum: " + Str)

course = 'Python for Beginners'

# print(course.find('Python'))
print('Python' in course)

print( 10 ** 3)
X = 10
X = X + 3
X += 3

x = 10 + 3 * 2
print(x)

x = 3 != 2
print(x)

price = 25
print(price > 10 or price > 30)

temperature = 25
if temperature > 30:
    print('Hot day')
    print('Drink plenty of water')
elif temperature > 20:
    print('Nice day')
elif temperature > 10:
    print('Bit cold')
else:
    print('Cold')
print('Done')

weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))

i = 1
while i <= 1_000:
    print(i)
    i = i + 1

names = ["John", "Bob", "Mosh", "Sam", "Mary"]
print(names[0:3])

numbers = [1,2,3,4,5]
print(len(numbers))

numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

numbers = range(5, 10, 2)
for number in range(5):
    print(number)

numbers = (1,2,3)
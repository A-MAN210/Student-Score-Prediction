print("Hello, AI & ML Internship - Day 2")
# Input Function,Varaibales,DataTypes
name = input("Enter your name: ")
print("Hello, " + name)
# If-else statements.
age = int(input("Enter your age: "))
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")
is_Intern = input("Are you an intern?: ")

# Arithmetic Operations
a = int(input("Enter first number: "))
b=int(input("Enter second number: "))
sum = a + b
print("The sum of", a, "and", b, "is:", sum)
diff = a - b
print("The difference of", a, "and", b, "is:", diff)
cross = a * b
print("The product of", a, "and", b, "is:", cross)
divide = a / b
print("The division of", a, "and", b, "is:", divide)
modulo = a % b
print("The modulo of", a, "and", b, "is:", modulo)

# Print number from 1 to 10.
# While loop
count =1
while count <=10:
    print(count)
    count += 1

# For loop Print Number from 5 to 0.
for i in range(5,-1,-1):
    print(i)
    i -= 1

list_subjects = ["Maths", "Science", "English", "History", "Geography"]
for subject in list_subjects:
    print(subject)
    subject += 1

# Person Daily Study Hour by Use of Functtions.
study_hours = int(input("Enter your daily study hours: "))
def calculate_study_hours(study_hours):
    if study_hours >= 5:
        print("Great Effort!")
    else:
        print("Try to study more!")

calculate_study_hours(study_hours)




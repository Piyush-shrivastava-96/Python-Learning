print("1. If-Else use;")

student_marks = int(input("Aapke class 12th me kitne marks hai:"))
sports_quota = input("kya apke pass sports quata hai (yes/no):")

q = sports_quota
print(sports_quota.lower())

print("\nAdmission prosses: start now")

if student_marks < 250:
    print("Admission prosses Denied!")
    print("Because your marks are very low so i am really very sorry")

elif sports_quota == "yes":
    print("Status: I feel that you might get admitted now. ")
    print("Because having a sports quota will admission quickly.")
    
else:
    print("Status: Admission Granted!")
    print("Checking your scholarship eligibilty and admissio selection prosses.")
    int(input("Please,Write your 12th marks on computer screen ;"))
    print("Okay you are selected because your marks are very high so you will come to collage tommarow.")

print("\n2. If-Else use;")

num = 19 
num = int(input("Enter your number:"))
if (num < 0):
    print("your number is negative")
elif (num == 0):
    print("your number is zero")
else :
    print("your num is positive")

print("\n3. If-Else use;")
typing_speed = 35 
typing_speed = int(input("Enter your typing speed:"))

if (typing_speed < 30):
    print("Sorry your typing speed is very slow!")

elif (typing_speed > 30 and typing_speed < 35):
    print("Okay! Your typing speed is pretty good.")
elif (typing_speed >=35 and typing_speed <=45):
    if (typing_speed == 35):
        print("Okay! Your typing speed is normal.")
    
    else:
        print("Brilliant! Your typing is very fast.")
else :
    print("exlent your typing is realy very fast you are a top boy/girl typing master")
        
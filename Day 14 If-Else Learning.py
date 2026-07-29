print("1. If-Else Program use;")

student_marks = int(input("Aapke class 12th me kitne marks hai:"))
if student_marks > 500:
    print("Error")
    exit()
elif student_marks <= 0:
    print("Error")
    exit()

sports_quota = input("kya apke pass sports quata hai (yes/no):")

q = sports_quota
print(sports_quota.lower())
if sports_quota == "yes":
     print("Status: I feel that you might get admitted now. ")
     print("Because having a sports quota will admission quickly. Thankyou!")
     exit()


print("\nAdmission prosses: start now")

if student_marks < 250:
    print("Admission prosses Denied!")
    print("Because your marks are very low so i am really very sorry, We will not give you admission. Thankyou!")


elif student_marks > 250 and student_marks <= 350:
    print("Umm Okay! your marks are average.")
    print("But sorry I can not give you admission because your marks are average. Thankyou!")

elif student_marks >350 and student_marks <= 450:
    print("Your marks are better than other students, But if the college list drops to this score, We will give you admission. Thankyou!")


else:
    print("Status: Admission Granted!")
    print("\nChecking your scholarship eligibilty and admissio selection prosses.")

    re_enter_marks = int(input("\nPlease, Re-enter your 12th marks on computer screen, that you wrote above;"))

    if re_enter_marks == student_marks:
        print("\nOkay you are selected because your marks are very high so you will come to the collage tommarow.")

    else : 
        print("\nError! Please enter the same marks you entered previously. Thankyou!")

        re_enter_again = int(input("\nPlease, Re-enter tha same marks on the computer screen;"))
        if re_enter_again == student_marks:
            print("\nOkay you are selected because your marks are very high so you will come to the collage tommarow.")
        else:
            print("\nYou have entered the wrong marks again, Admission Cancelled!")

print("\n2. If-Else use;")

num = 19 
num = int(input("Enter your fav. number:"))
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
        
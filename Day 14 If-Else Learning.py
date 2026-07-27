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
    print("Checking your scholarship eligibilty")

     
import time

hour = int(time.strftime('%H'))

if 3 <= hour < 12:
    print("Good Morning sir")

elif 12 <= hour < 17:
    print("\nGood Afternoon sir")

elif 17 <= hour < 20:
    print("\nGood Evening sir")

else:
    print("\nGood Night sir")

print("\nNow time is:", time.strftime('%I:%M %p'))


import time 

hour = int(time.strftime('%I'))

am_pm = time.strftime('%p')

if am_pm == 'AM' and 4 <= hour < 12:
    print("\nGood morning sir, Have a nice day!")

elif am_pm == 'PM' and (hour == 12 or hour < 5):
    print("\nGood Afternoon sir, Can I Help you .")

elif am_pm == 'PM' and 5 <= hour < 7:
    print("\nGood Evening Sir, Can I Help you.")

else: 
    print("\nGood Night Sir, You can eating food and sleep.")

print("\nSir, Would you like to know that current time;")
q = str(input("Please, give me answer (yes/no);"))

if q == 'yes':
    print("okay, The time is -", time.strftime('%I:%M %p'))
    print("Thank you Sir!🙏")

elif q == "no":
    print("Okay Sir no problem,have a nice day.")
    print("Thank you Sir!🙏")

else:
    print("Error: Invalid input! Please enter only 'yes' or 'no'.")
    re_enter = str(input("Please enter only 'yes' or 'no'"))
    if re_enter == "yes":
        print("okay, The time is -", time.strftime('%I:%M %p'))
        print("Thank you Sir🙏")
    else:
        print("Error: Invalid input! Please Re-Start Now. Thank you.")




                                    

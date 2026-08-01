q = "SmartBite: AI Restaurant System"
print(q.center(100))

a = "🫡  second project use in python😁"
print(a.center(100))


print("\n\n{Real life of example for loop in python}:\n")

import time
hour = int(time.strftime("%I"))

ampm = (time.strftime("%p"))

if ampm == "AM" and 4 <= hour < 12:
    print("\nGood morning sir, Have a nice day! 🌞")

elif ampm == "PM" and hour ==12 or 1 <= hour < 5:
    print("\nGood afternoon sir, Have a nice day! 🌞")

elif ampm == "PM" and 5 <= hour < 7:
    print("\nGood evening sir, Have a nice day! 🌙")

else:
    print("\nGood night sir, I hope you had a good day, Today!")
print("\nNow time is;", time.strftime("%I:%M:%S %p"))

print("\n------------------Welcome to PS Restaurant-------------------, \nSir, Please tell me, how can I help you ?")

q = str(input("Sir, Our Restaurant food is very delicious, Would you like to see the menu? (yes/no):"))
match q:
    case "yes":
        print("\n Okay Sir, Here is our menu:")
        food = {'chai': 20, 'coffee': 50, 'juice': 80, 'samosa': 30, 'pizza': 150, }
        for k, v in food.items():
            print("The price of the", k, "is:", v, "₹")

            total_bill = 0
        order = str(input("\nPlease tell me sir, what would you like to order from our menu:").lower())
        match order:
            case "chai" | 'coffee' | 'juice' | 'samosa' | 'pizza':
                print("\nSure sir, Your order for " + order + " is placed successfully! It will be ready in 5 minutes. Thank you for ordering from PS Restaurant.🙏")
                total_bill += food[order]
            case _:
                print("\nSorry sir, Invalid input! ")  
                exit("Please Re-Start Now. Thank you")     
        second_order = str(input("\nSir, Would you like to order another item from menu? (yes/no):")) 

        if second_order == "yes":
             next_order = str(input("\nPlease tell me sir, what else would you like to bring from menu:").lower()) 

             match next_order:
                  case "chai" | 'coffee':
                       print("\nOkay sir, Hot chai is coming right up!")
                  
                  case "juice":
                       print("\nOkay sir, Fresh juice is coming right up!")
                  
                  case "pizza" | 'samosa':
                       print("\nOkay sir, Delicious pizza is coming right up!")
                       total_bill += food[next_order]
                  case _:
                       print("\nSorry sir, " + next_order + " is currently not available. Thank you")

             print("\nSir, Your order will be ready in 5 minutes. Thank you for first ordering from PS Restaurant, Please wait a moment!🙏")

        if total_bill > 0:
            print("\nSir, you have finished your dish, I hope enjoyed it!")

            print("\n========================Your Total bill is: ", total_bill, "₹========================")

            print("\n=========================================================================================")

        feedback = str(input("\n Sir, how was the food? Do you like it? (yes/no):"))
        
        if feedback == "yes":
             print("\nThank you so much sir for your wonderful feedback! Please visit us again! 🙏✨")

        else:
             print("\nSir, we are very sorry for your bad experience! We will try to improve our food quality.😒 ")
        
        
                                                                                
    case "no":
            print("\nOkay sir, no problem. Thank you for visiting PS Restaurant. Have a nice day!🙏")
    case _:
            print("\nError: Invalid input! Please enter only 'yes' or 'no'.")


                                    
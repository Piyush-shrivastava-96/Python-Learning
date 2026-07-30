# x = int(input("Aapko in numbers me se konsa number pasnad hai;- '1,2,3,4,5,6,7'"))

# match x:
#     case 1:
#         print("Achha apko 1 number pasand hai ")
#     case 2:
#         print("Achha apko 2 number pasand hai ")
#     case 3:
#         print("Achha apko 3 number pasand hai ")
#     case 4: 
#         print("Achha apko 4 number pasand hai ")
#     case 5:
#         print("Achha apko 5 number pasand hai ")
#     case 6:
#         print("Achha apko 6 number pasand hai ")
#     case 7:
#         print("Achha apko 7 number pasand hai ")
#     case _:
#         print("Koi baat nhi! sir/madam agr aapko ek bhi number pasand nhi hai, Thankyou")
while True:
    print("' \n🤖Aapka swagat hai is smart calculater 🧮 bot me'")
    n1 = int(input("Enter your fav. first number;"))
    n2 = int(input("Enter your fav. second number;"))

    check = input("Aapko inme se kya krna hai; {'+','-','*','**','//','/', 'check', 'kuchh bhi nhi'}-:")

    match check:
        case "+":
            print("\nYour Result -;",n1+n2)
        case '-':
            print("\nYour Result -;",n1-n2)
        case '*':
            print("\nYour Result -;",n1*n2)
        case '**':
            print("\nYour Result -;",n1**n2)
        case '//' if n2 != 0:
            print("\nYour Result -;",n1//n2)
        case '//' if n2 == 0:
            print("\n❌Error; Aap kisi bhi sankhya ka 0 se bhaag nhi de sakte hai.")
        case '/'  if n2 != 0:
            print("\nYour Result -;",n1/n2)
        case '/'  if n2 == 0:
            print("\n❌Error; Aap kisi bhi sankhya ka 0 se bhaag nhi de sakte hai,\nThank you.🙏")
        case 'check' if n1 < n2:
            print("\nAapka pehla number chhota hai or dusra badha hai,\nThank you.🙏")
        case 'check' if n1 > n2:
            print("\nAapka pehla number badha hai or dusra chhota hai,\nThank you.🙏")
        case 'check' if n1 == n2:
            print("\nAapka pehla number or dusra number dono brabar(=) hai,\nThank you.🙏")
        case 'kuchh bhi nhi':
            print("\n👍Koi baat nhi sir agar apko kuchh bhi pasnd nhi hai to, Thank you.🙏")
        case _:
            print("\n❌Error! Invalid input Thank you.🙏")
x = 10
while x > 0:
    print(x)
    x = x -1

q = 5
while q > 0:
    print(q)
    q = q - 1


s = 9
while s > 0:
    print(s)
    s = s - 2
else:
    print("Loop is over!")

print("\n")

print("Aapka SBI ATM me swagt hai ")
while True:
    q = int(input("Aapko kitne pese nikalne hai 'Amount Dale';"))
    a = int(input("Please enter your pin ya passaward 4 digits ;"))
    if a == 9889:
        print("Aap pese nikal skte hai, Thank you!")
        break
    else:
        print("Wrong passward! Sorry Please Re-Start Now.")

print("Flight 101 me swagt hai.")
for i in range(1, 11):
    if i == 4:
        print(f"Seat num. {i} VIP hai direct andar ane do ")
        continue
    print(f"Seat num. {i} Tumhari checking ho gai Tum thoda wait kro jldi hi andar jane dege. ")


    if i == 7:
        print("saari seete full ho gai get band kro jldi.")
        break

print("Welcome to Instagram")

for a in range(1, 12):
    if a == 3:
        print("reels", a, "Boring AD skip now.")
        
        continue
    print(f"acchi reels hai num. {a}")

    if a == 7:
        print("Mummy aa gai band kro phone so jao jldi se.")
        break


for s in range(12):
    
    if s+1 == 5:
        print("This is so easy you can try it.")
        continue
    print("3 X", s+1, "=", 3 *(s+1) )
    if s+1 == 10:
        print("stop bhai itna hi sunana tha okay 👍")
        break


i = 0
while True:
    print(i)
    i = i+1
    if (i%100 == 10):
        print("over the loop.")
        break
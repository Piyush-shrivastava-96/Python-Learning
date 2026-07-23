name = "piyush" 
print(len(name))
he = len("piyush")
print(he)

the_word = "Rohan bhai"
print("\n ---1. POSITIVE SLICING---")
print(len(the_word))
print(the_word[0:7])
print(the_word[4:8])
print(the_word[:9])
print(the_word[3:])

print("\n ---2. NEGATIVE SLICING---")
print(the_word[-5:-1])
print(the_word[-10:-1])
print(the_word[-7:-4])
print(the_word[-8:-3])

print("\n ---3. LEN() WITH NEGATIVE SLICING---")
print(the_word[len(the_word)-5:len(the_word)-1])
print(the_word[len(the_word)-9:len(the_word)-8])
print(the_word[len(the_word)-10:len(the_word)-7])

print("\n ---4. EMPATY OUTPUTS---")
print(the_word[9:2])
print(the_word[-7:-8])
print(the_word[9:2])

print(the_word[4:8:2])
print(the_word[3:9:-2])
print(the_word[3:9:-1])


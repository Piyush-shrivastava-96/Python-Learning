#    "Strings are immutable"

N = "piyush shrivastava"
print(N.upper())  #Sabko CAPITAL letters me badalta hai.
print(N.lower())  #Sabko small letters me badalta hai.

a = "      piyush bhai     "
print(a.strip())   #Shuruat aur aakhiri ke faltu spaces ko hata deta hai.

q = "Rohan??????????????????????"
print(q.rstrip("?"))  #Sirf aakhiri ke (right side ke) characters ya spaces hatata hai.

w = "Hey, kapil bhai"
print(w.replace("kapil", "Ram").replace("bhai", "bhaiya"))
print(w.replace("bhai", "bhai, how are you?"))   #Purane shabd ko naye shabd se badalta hai.

r = "Hello, Ram bhai kese ho?"
print(r.split(" "))   #Kisi character (jaise space) se string ko todkar List bana deta hai.

t = "syAM BHai"
print(t.capitalize())   #Sirf pehle letter ko Capital karta hai, baki sabko small.

y = "Ramu Don"
print(y.center(50))   #String ko beech me laata hai aur di gayi width ke hisab se spaces bharta hai.

u = "Hey, I am a good boy and i need urgent some money."
print(u.count("e"))   #Koi character ya word kitni baar aaya hai, ginta hai.

i = " I want to become a very rich man."
print(i.find("rich"))
print(i.find("hello"))   #Kisi shabd ki position (index) dhoodta hai. Na milne par -1 deta hai.

o = " Hello, i am ram shrivastava and you ? "
print(o.index('you'))   #find() jaisa hai, par shabd na milne par program me Error de deta hai.

p = "Python is my favorite subject"
print(p.startswith("Python"))  #Check karta hai kya string isse shuru ho rahi hai (True/False).

e = "Python is my best friend"
print(e.endswith("nd"))  # Check karta hai kya string isse khatam ho rahi hai (True/False).

s = "Javascript7"
print(s.isalnum())  #Agar string me sirf letters (A-Z) aur numbers (0-9) hain, to True. Space hone par False.

d = "Printoutput"
print(d.isalpha())  #Agar string me sirf alphabets (letters) hain, to True. Number ya space par False

f = " haniya amir"
print(f.islower())  #Agar saare letters small hain, to True.

g = "SALMAN KHAN"
print(g.isupper())  #Agar saare letters Capital hain, to True.

h = "bhopal is the best city of colleges."
print(h.isprintable())  #Agar saare characters screen par dikhte hain, to True. \n (new line) hone par False.

j = "     "
print(j.isspace()) #Agar string me sirf aur sirf khali jagah (spaces) hain, to True.

k = "Hello Python"
print(k.istitle())  #Agar har word ka pehla letter Capital hai, to True.

l = "i aM rOHan yaDAv"
print(l.swapcase())  #Small ko Capital aur Capital ko Small me ulat-palat kar deta hai.

z = "welcome to my code & \ni will be greatful to you."
print(z.title())     #Poori string ke har shabd ka pehla letter Capital kar deta hai.
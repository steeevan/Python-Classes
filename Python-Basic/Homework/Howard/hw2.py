#q1
h = "Today there are many things in life, that require things to do in the thing world"
print("there are",h.count("thing"),"thing in this sentence")
print("there are",h.count(","),"comma in this sentence")
print("there are",h.count(" "),"spaces in this sentence")

#q2
a = "I am eating our food in the kitchen under our roof"
print(a.replace("a","e"))
print(a.replace("e","i"))
print(a.replace("i","o"))
print(a.replace("o","u"))
#bonus------------------------------------------------------------------------------------
print(a.replace("u","q"))

#q3
ohio = "ohio people be like, I can spell ohio:OJUO"
ohiopeople = ohio.split()
print(ohiopeople)
ohio2 = []
for i in ohiopeople:
  (i.capitalize())
  ohio2.append(i.capitalize())
print(ohio2)
#bonus------------------------------------------------------------------------------------
#I will make it into one sentence not a list
print(" ".join(ohio2))

#q4
h = "ABCDEFG"
j = h.lower()
print(j)
#bonus------------------------------------------------------------------------------------
#to prove that h did not change
print(h)
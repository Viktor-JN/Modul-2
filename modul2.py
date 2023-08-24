#Miniräknare
print("""Multiplikationsräknare
Mata in 2 tal
""")
tal1 = int(input("Tal 1:\n")) #Tal 1
tal2 = int(input("Tal 2\n")) #Tal 2
print(tal1, "*", tal2, "=")
print(tal1*tal2) #Resultatet
#Bmi kalkylator
print("""Bmi kalkylator
Mata in vikt och längd
""")
weight=float(input("Hur mycket väger du i kg?\n"))
height=float(input("Hur lång är du i cm?\n"))
height=height/100*2
bmi=weight/height
print("Du har", "%.1f" %bmi, "i bmi\n")
if bmi < 18.5:
    print("Du är underviktig, ät mer\n")
elif 18.5<=bmi<=24.9:
    print("Du är normalvikt\n")
elif 25<=bmi<=29.9:
    print("Du är övervikt, kanske borde äta lite mindre donken\n")
elif bmi>30:
    print("Du är fetma, borde kanske delta i ramadan eller nått\n")

#KG till LBS omvandlare
print("Omvandla KG TILL LBS")
kg=float(input("Hur många kilo vill du konvertera?\n"))
lbs=kg*2.2046
print(kg, "kg", "i lbs är", lbs)
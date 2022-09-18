import math
import random



kapott = random.randint(1,2)
valasz = str(input("Fej vagy irás? "))

if valasz == "Fej" or "fej":
    valasz = int(1)
if valasz == "Iras" or "iras":
    valasz= int(2)


if kapott == 1:
     print("Fej")
else:
     print("Irás")

if valasz == kapott:
     print("Gratulálok eltaláltad")
else:
    print("Hát sajnos ez most nem jött össze! :(")


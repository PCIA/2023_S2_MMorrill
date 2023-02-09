Menu = ("Spicy Soup, Raw Steak, or Bread")
print("Welcome to restaurant blue! We have", Menu)
Served_Item = input("What would you like to eat? ")
Served_Item = Served_Item.upper()
if Served_Item == "SPICY SOUP" or "RAW STEAK":
    print("You have contracted food poisioning!")
else: print("You are full.")
text=input("How many melons do you want? ")
try:
    melons=int(text)
    total=melons*15000
except ValueError:
    print("Please enter a whole number")


else:
    print(f"Total: {total} soum")
    print("Thank you!")
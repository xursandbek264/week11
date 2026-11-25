while True:
    text=input("How many portions? ") 
    try:

        number_portions=int(text)
        if number_portions>=1:
            break
        else:
            print("Please order at least 1 portion.")
    except ValueError:
        print("Please enter a whole number.")
price=25000
total=number_portions*price
print(f"{number_portions} portions of shivit oshi: {total} soum")
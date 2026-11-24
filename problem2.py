text=input("Hours on the road: ")
try:
    hours=float(text)
    speed=30/hours
except ValueError:
    print("Please enter a number")
except ZeroDivisionError:
    print("Time cannot be zero!")

print(f"Average speed: {speed} km/h")




#Part a
'''def valid_numbers(records):
    numbers=[]
    for record in records:
        try:
            numbers.append(int(record))
        except ValueError:
            pass
    return numbers
records = ["120", "95", "abc", "110", " 130 ", "", "8O"]
print(valid_numbers(records))'''



#Part b

records = ["120", "95", "abc", "110", " 130 ", "", "8O"]
day=0
for record in records:
    day=day+1
    try:
        kg=int(record)
        print(f"Day {day}: {kg} kg")
    except ValueError:
        print("Invvalid number")   




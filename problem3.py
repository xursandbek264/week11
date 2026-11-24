def ticket_price(tickets):
    if tickets>1 or tickets>4:
        raise ValueError("you can buy tickets from 1 to 4")
    return tickets*20000
print(ticket_price(tickets))

assert ticket_price(1)==20000
assert ticket_price(4)==80000

tickets=int(input("Number of tickets: "))

































'''def ticket_price(tickets):
    if not (1 <= tickets <= 4):
        raise ValueError("Error: you can buy from 1 to 4 tickets")
    return f"price: {tickets*20000} soum"
try:
    ticket=int(input("Number of tickets:  "))
    print(ticket_price(ticket))
except ValueError:
    print("Error: you can buy from 1 to 4 tickets")'''
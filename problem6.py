#Part A

rates = {"USD": 12000, "EUR": 14000, "RUB": 150}
def convert(amount, currency, rates):
    if amount<=0:
        raise ValueError("amount must be positive")
    else:
        rate=rates[currency]
        return amount*rate
assert convert(10, "USD", rates) == 120000
assert convert(1, "RUB", rates) == 150






#Part B


requests = ["100 USD", "50 EUR", "2000 RUB", "30 GBP", "abc USD", "-20 EUR", "0 USD"]
total=0
for r in requests:
    parts=r.split(" ")
    print(parts)
    currency=parts[1]
    try:
        amount=int(parts[0])
        soum=convert(amount, currency, rates)
        print(f"{amount} {currency} = {soum} soum")
        total+=soum
    except ValueError:
        print(f"{r}:wrong amount")
    except KeyError:
        print(f"{r}:unknown currency")

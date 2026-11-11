cash = 100000
price = 250
shares = 0
print("PAPER TRADING ONLY")
while True:
    print("Cash:", cash, "Shares:", shares)
    action = input("buy/sell/quit: ").lower()
    if action == "quit": break
    if action not in ("buy", "sell"): continue
    try:
        qty = int(input("Quantity: "))
        if qty <= 0: raise ValueError
    except ValueError:
        print("Invalid quantity")
        continue
    if action == "buy" and cash >= qty * price:
        cash -= qty * price
        shares += qty
    elif action == "sell" and shares >= qty:
        cash += qty * price
        shares -= qty
    else:
        print("Insufficient funds or shares")

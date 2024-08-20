print("-----Currency Converter-----")
print("1. IDR to USD")
print("2. USD to IDR")

user_choice = int(input("Enter your choice(1 or 2):"))

if user_choice == 1:
    amount = float(input("Enter your IDR amount:"))
    amount_in_usd = amount * 0.000065
    print(f"IDR Rp.{amount} is USD ${amount_in_usd}")

elif user_choice == 2:
    amount = float(input("Enter your USD amount:"))
    amount_in_idr = amount * 15.457,60
    print(f"USD ${amount} is IDR Rp.{amount_in_idr}")

else:
    print("Invalid Choice!")

    
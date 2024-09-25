current = input("""Enter the from currency (eg: USD, INR, EUR,etc.): """).upper()
cu_cur = int(input("Enter the amount"))
conv = input("Enter the to currency (eg: USD, IRN, EUR,etc.): ").upper()
dic = {}
f = open('currency rates', 'r')

for i in f:
    key, value = i.rstrip('\n').split(',')
    dic[key] = float(value)


def conversion(amount, cur, conv):
    if cur in dic and conv in dic:
        in_usd = amount * dic[cur]
        convert = in_usd / dic[conv]
        print(f"You converted currency is: {convert}, PS: This is not based on current exchange rate")
    else:
        print("""Invalid Currency, or not in our database
        if you are admin you can add the currency""")
        admin = input("admin: ")
        if admin == 'Jacob':
            r = open('currency rates', 'a')
            print("These are the currency in data")
            for i in dic:
                print(i)
            sign = input("Enter the currency code: ").upper()
            rate = float(input("Enter currency rate in usd: "))
            r.write(sign + ',' + str(rate) + '\n')
        else:
            print("Only admins can change the value")


conversion(cu_cur, current, conv)

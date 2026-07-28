from itertools import permutations
letters = "SENDMORY"
for p in permutations("0123456789", len(letters)):
    d = dict(zip(letters, p))
    # First letters cannot be zero
    if d['S'] == '0' or d['M'] == '0':
        continue
    send = int(d['S'] + d['E'] + d['N'] + d['D'])
    more = int(d['M'] + d['O'] + d['R'] + d['E'])
    money = int(d['M'] + d['O'] + d['N'] + d['E'] + d['Y'])
    if send + more == money:
        print("SEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        break

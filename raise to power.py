base = float(input("Enter base: "))
exp = int(input("Enter exponent (whole numbers only): "))

i = 1
while i < exp:
    i = i + 1
    base = base * base
print(base)
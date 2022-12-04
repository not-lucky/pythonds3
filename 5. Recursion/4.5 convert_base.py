from string import digits, ascii_uppercase


def convert(n, base):
    strng = digits + ascii_uppercase
    if n // base == 0:
        return strng[n]
    return convert(n // base, base) + strng[n % base] 


a = 1453
print(convert(a, 16))
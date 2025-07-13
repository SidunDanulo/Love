def difference(*args):
    if not args:
        return 0
    return round(max(args) - min(args), 2)
print(difference(1, 2, 3))
print(difference(10.5, 4.2, 8.8))
print(difference())
print(difference(3.14159, 2.71828))

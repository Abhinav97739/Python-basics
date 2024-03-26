integers=range(1,51)
for n in integers:
    if n%3 and n%5:
        print("FIZZBUZZ")
    elif n%3:
        print("FIZZ")
    elif n%5:
        print("BUZZ")
    else:
        print(n)
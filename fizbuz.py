batas = int(input("\nMasukan Batas Angka (1-100): "))

print("\n=== FizzBuzz ===")
for i in range(1, batas + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

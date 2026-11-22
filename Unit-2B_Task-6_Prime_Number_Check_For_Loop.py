num = int(input("Enter a number (1 to 100): "))
count = 0

if num <= 1:
    print("Not a Prime Number")
else:
    for i in range(2, num):
        if num % i == 0:
            count = 1
            break

    if count == 0:
        print("Prime Number")
    else:
        print("Not a Prime Number")
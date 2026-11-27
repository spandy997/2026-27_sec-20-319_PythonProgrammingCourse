try:
    num = int(input("Enter a number: "))

except ValueError:
    print("Error: Please enter a valid integer")

else:
    print("Square:", num * num)

finally:
    print("Program finished")
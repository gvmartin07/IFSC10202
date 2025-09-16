# Find special numbers in a range
# A special number is equal to the sum of its digits each raised to the power of the number of digits

startrange = int(input("Enter start of range: "))
endrange = int(input("Enter end of range: "))

for num in range(startrange, endrange + 1):
    # Step 1: Count number of digits
    temp = num
    digits = 0
    while temp > 0:
        temp = temp // 10
        digits += 1

    # Step 2: Calculate sum of each digit raised to the power of number of digits
    temp = num
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp = temp // 10

    # Step 3: Check if it's a special number
    if total == num:
        print(num)

#find special numbers in range
#special number is the sum of its own digits each raised to the power of the number of digits.
#determine number of digits with while loop & reminder division by 10
#special num 153 = 1^3 + 5^3 + 3^3
startrange = int(input("Enter start of range: "))
endrange = int(input("Enter end of range: "))
for i in range(startrange, endrange+1):
    #finding number of digits in value
    number = i
    digits = 0
    while number > 0:
        number = number//10
        digits += 1
    number = i
    sum = 0
    while number > 0:
        value = number%10
        sum += value**digits
    if sum == i:
    #finding if value is special number
        print(i)
#find special numbers in range
#special number is the sum of its own digits each raised to the power of the number of digits.
#determine number of digits with while loop & reminder division by 10
#special num 153 = 1^3 + 5^3 + 3^3
startrange = int(input("Enter start of range: "))
endrange = int(input("Enter end of range: "))
endrange += 1
for i in range(startrange, endrange):
    #finding number of digits in value
    number = i
    digits = 0
    while number > 0:
        number = number//10
        digits += 1
    #finding value of ones, tens, etc
    while i != 0:
        ones = i % 10
        tens = i // 10
        hundreds = i // 100
        thousands = i // 1000
        #finding if value is special number
        if ones**digits + tens**digits + hundreds**digits + thousands**digits == i:
            print(i)
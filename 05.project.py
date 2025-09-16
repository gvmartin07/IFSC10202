#find special numbers in range
#special number is the sum of its own digits each raised to the power of the number of digits.
#determine number of digits with while loop & reminder division by 10
#special num 153 = 1^3 + 5^3 + 3^3
startrange = int(input("Enter start of range: "))
endrange = int(input("Enter end of range: "))
for num in range(startrange, endrange+1):
    #finding how many digits in number
    temp = num
    digits = 0
    while temp > 0:
        temp = temp//10
        digits += 1
    
    #adding up each ones digit after * to digit count and shortening number
    temp = num
    total = 0
    while temp > 0:
        value = temp%10
        total += value**digits
        temp = temp // 10
    
    #finding if its special number
    if total == num:
        print(num)
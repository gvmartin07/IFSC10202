#find special numbers in range
#special number is the sum of its own digits each raised to the power of the number of digits.
#determine number of digits with while loop & reminder division by 10
#special num 153 = 1^3 + 5^3 + 3^3
startrange = int(input("Enter start of range: "))
endrange = int(input("Enter end of range: "))
for num in range(startrange, endrange+1):
    temp = num
    digits = 0
    while temp > 0:
        temp = temp//10
        digits += 1
    
    
    
    num = temp
    sum = 0
    while temp > 0:
        value = temp%10
        sum += value**digits
        temp = temp // 10
    if sum == num:
        print(num)
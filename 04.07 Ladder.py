#print ladder of N steps
#loop till sum = N
#sum = 1, print sum +=1 every loop
N = int(input("Enter a Number: "))
for i in range(1, N+1):
    print("*"*i)
for down in range (N-1, 0, -1):
    print("*"*down)
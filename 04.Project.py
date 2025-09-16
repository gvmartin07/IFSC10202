#make a ascending and descending steps of "*"
N = int(input("Enter a Number: "))
for up in range(1, N+1):
    #going up
    print("*"*up)
for down in range (N-1, 0, -1):
    #going down
    print("*"*down)
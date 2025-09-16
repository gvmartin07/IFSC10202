#make a ascending and descending steps of "*"
N = int(input("Enter maximum height: "))
for up in range(1, N+1):
    #going up
    print("*"*up)
for down in range (N-1, 0, -1):
    #going down
    print("*"*down)
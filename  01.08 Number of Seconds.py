#Asking for minutes & seconds
minutes = input("Enter Minutes: ")
seconds = input("Enter Seconds: ")
#Converting strings to integars
minutes = int(minutes)
seconds = int(seconds)
totalseconds = (minutes * 60 + seconds)
print(totalseconds)
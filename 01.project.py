initialseconds = input("Enter amount of time in seconds: ")
#converting intitialseconds to an integar
initialseconds = int(initialseconds)
#finding amount of years
years = initialseconds // 31536000
#finding remaining seconds
remainingseconds = initialseconds - years*31536000
#finding the amount of days in remaining seconds
days = remainingseconds // 86400
#removing seconds for amount of days
remainingseconds = remainingseconds - days*86400
#finding the hours in the left over seconds
hours = remainingseconds // 3600
#taking away hours from remainingseconds
remainingseconds = remainingseconds - hours*3600
#finding amount of minutes in remaining seconds
minutes = remainingseconds // 60
#finding leftover seconds
remainingseconds = remainingseconds - minutes*60
#printing out the time
print("Years: ")
print(years)
print("Days: ")
print("Hours: ")
print("Minutes: ")
print("Seconds: ")
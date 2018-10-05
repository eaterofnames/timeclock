import datetime

#Intro menu: Display the options

print("Welcome to Clocker.\n")
menu = ["1: Clock in", "2: Clock out", "3: Weekly report",
"4: Export data", "5: Exit"]

#Set up some variables so they exist outside functions

clockInTime = datetime.datetime.now()
clockOutTime = datetime.datetime.now()


def Clockin():
    clockInTime = datetime.datetime.now()
    print ("You clocked in at " + clockInTime.strftime("%H:%M:%S"))

def Clockout():
    clockOutTime = datetime.datetime.now()
    print("You clocked out at " + clockOutTime.strftime("%H:%M:%S"))
    timeworked = clockOutTime - clockInTime
    secondsWorked=divmod(timeworked.days * 86400 + timeworked.seconds, 60)
    print(secondsWorked)


while True:
        print(*menu, sep="\n")

        selection=input("Please Select:  ")
        if selection =='1':
            print("Clock in")
            Clockin()
        elif selection =='2':
            print("Clock out")
            Clockout()
        elif selection =='3':
            print("Weekly report")
            WeeklyReport()
        elif selection =='4':
            print("Export Raw Data")
            ExportData()
        elif selection =='5':
            break
        else:
            print("Unknown option selected!")
#Get the user's option, print it to the screen.

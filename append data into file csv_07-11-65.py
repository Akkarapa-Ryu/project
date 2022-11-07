import csv

def openA(sid,fn,ln,date,leave):
    with open('editstudents.csv','a',newline='') as cf:
        cfw = csv.writer(cf)
        cfw.writerow([sid,fn,ln,date,leave])
    print("data successfully saved")
    return
open = openA(int(input("StudenID: ")),input("Firstname: "),input("Lastname: "),input("Date: "),input("Leave: "))
print(open)

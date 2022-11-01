import pandas as pd
import datetime

#การ appand เข้าไปในไฟล์
#ID = int(input())
def openFile():
    dfile = pd.read_csv('editstudents.csv')
    print(dfile)

x = int(input('OPTION:  ' ))
while True:
    if x == 1:
        openFile()  
        break
    else:

        SID = []
        SID.append(int(input("StudentID: ")))

        data = {
        'id': SID,
        'fname': [input("Firstname: ")],
        'lname': [input("Lastname: ")],
        'date': [input("Date: ")],
        'leave': [input("Leave (S=Sick/B=Business/T=Travel/O=Other): ")]
        }
        df = pd.DataFrame(data)
 
# append data frame to CSV file
        df.to_csv('editstudents.csv', mode='a',index=False,header=False)

# print message
        print("Data appended successfully.")
        break



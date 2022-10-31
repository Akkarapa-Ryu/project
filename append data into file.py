import pandas as pd
import utf8
#การ appand เข้าไปในไฟล์
data = {
    'id': [int(input())],
    'fname': [input()],
    'lname': [input()],
    'date': [input()],
    'leave': [input()]
}
df = pd.DataFrame(data)
 
# append data frame to CSV file
df.to_csv('editstudents.csv', mode='a',index=False,header=False)

# print message
print("Data appended successfully.")

dfile = pd.read_csv(r'H:\DST\Python\Project\editstudents.csv')
print(dfile)

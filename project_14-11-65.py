from doctest import script_from_examples
#import pandas as pd
import csv
import datetime

def Submite():
    while True:
        print()
        Submit = input("Submit?(Yes/No): ")
        if Submit == "Yes":
            Stop = 'Submit'
            print("Submit Data")
            break
        elif Submit == "No":
            print ("Ok reset data")
            Stop = 0
            break
        else:
            print ("Please Input Yes or No")
    return Stop

#append data into csvfile =================
def openA(sid,fn,ln,date,leave): #append data into file
    with open('editstudents.csv','a',newline='') as cf:
        cfw = csv.writer(cf)
        cfw.writerow([sid,fn,ln,date,leave])
    print("data successfully saved")

#function is check student ID in students.csv
def check(id_:str) -> tuple : 
    with open ('students.csv','r',newline='') as f :
        list_student = csv.DictReader(f)
        student_in = False
        finame = ''
        lname = ''
        for data in list_student :
            if data['id'] == id_ :
                finame = data['fname']
                lname = data['lname']
                student_in = True
    return (finame,lname,student_in) #รีเทินเป็นtuple

def d():
    pass


while True: #จะให้รับเรื่อยๆจรกว่าจะปิดโปรแกรม
    print ("MUICT Student Leave System")
    print (" 1. Print a list of student")
    print (" 2. Submit a leave request")
    print (" 3. Check leave with class data")
    print (" 4. Check leave with student ID")
    print (" 5. Check leave with student First name")
    print (" 6. print leave summary")
    print (" 0. exit")


    menu = input('Option: ')
    print()
    if menu == '0':#เมนูปิดโปรแกรม
        print ("ShutDown Programme")
        break

#========================================
    
    elif menu == '1': #เมนูแสดงรายชื่อ
        #names_students = pd.read_csv('students.csv')
        #print(names_students)

        with open('students.csv','r') as rs :
            r_n = csv.DictReader(rs)
            for i in r_n:
                print(i['id'],i['fname'],i['lname'])

         #print('-'*40)
         #print()

#========================================

    elif menu == '2': #ส่งคำร้องลาเรียน
     while True:
        Stop = 0
        date = ''
        while True:
          id_ = input('ID :')
          found_student = check(id_)
          if found_student[2] :
              Stop = Submite()
              if Stop == "Submit":
                    break
          
#ลาด้วยเหตุผลอะไร
        if found_student[2] :
            while True:
                print()
                Leave = input("Leave (S=Sick/B=Business/T=Travel/O=Other): ")
                Stop = 0
                if Leave == "S":
                    Stop += 1
                    L = 'Leave Sick'
                elif Leave == "B":
                    Stop += 1
                    L = 'Leave Business'
                elif Leave == "T":
                    Stop += 1 
                    L = "Leave Travel"
                elif Leave == "O":
                    Stop += 1
                    L = 'Leave Other'
                if Stop == 1:
                    Stop = Submite()
                if Stop == "Submit":
                    break
                print ("Plase Input Leave (S=Sick/B=Business/T=Travel/O=Other)")
                print ()
        
         

#เช็คว่าวันที่กรอกมีอยู่จริงไหม
        DD = 0
        MM = 0
        YYYY = 0
        if found_student[2] :
            while True:
                date_pass = False
                print()
                print ("Class data DD-MM-YYYY")
                date = input('data DD-MM-YYYY :')
                date_lis = date.split('-')
                DD = date_lis[0]
                MM = date_lis[1]
                YYYY = date_lis[2]
                print(DD,MM,YYYY)

#เช็คเดือนที่ลงท้ายด้วยคม
    
                if MM == '01' or MM == '03' or MM == '05' or MM == '07' or MM ==  '08' or MM == '10' or MM == '12' and int(DD) >= 1 and int(DD) <= 31 and len(YYYY) == 4 and int(YYYY) >= 2022:
                  date_pass = True
          
#เช็คเดือนที่ลงท้ายด้วยยน
        
                elif MM == '04' or MM == '06' or MM == '09' or MM == '11' and int(DD) >= 1 and int(DD) <= 30 and len(YYYY) == 4 and int(YYYY) >= 2022:
                  date_pass = True

#เช็คเดือนกุมภาพันธ์
        
                elif MM == '02' and int(DD) >= 1 and (int(DD) <= 28 or ((int(YYYY))%4 == 0 and int(DD) <= 29)) and len(YYYY) == 4 and int(YYYY) >= 2022:
                  date_pass = True
                
                else :
                  print ("Class data Erorr Please Input DD-MM-YYYY")
                if date_pass :
                    Stop = Submite()
                    if Stop == "Submit":
                        break
                    
            Stop = input("Submit All Data?(Yes/No): ")
            if Stop == 'Yes':
                Stop = 'Submit'
                break
            print("Ok resset All data")
     if Stop == "Submit":
            openA(id_,check(id_)[0],check(id_)[1],date,L) # used function openA to writed new data on editstudents.csv
          
    



#======================================
  
    elif menu == '3': #ตรวจวันลาจากวันที่
      date = input('Date DD-MM-YYYY :')
      try :
          datetime.datetime.strptime(date,'%d-%m-%Y') #chech date
          with open('editstudents.csv','r',newline='') as f : # find from editstudents.csv
              student_leave = csv.DictReader(f)
              counter = 0
              list_print = []
              for data in student_leave :
                  if data['date'] == date :
                      list_print.append(data['id']+' '+data['fname']+' '+data['lname']+' '+data['leave'])
                      counter += 1 # count students leave
              print("There are "+ str(counter)+ " students leave on "+date)
              for printLine in list_print :
                  print(printLine)

      except :
          print("Class data Erorr Please Input DD-MM-YYYY")

      print()

#=====================================
    
    elif menu == '4': #ตรวจวันลาจากรหัส
        id = input('ID :')
        with open('editstudents.csv','r',newline='') as i :
            student_id = csv.DictReader(i)
            s = False
            for data in student_id :
                if id in data['id']:
                    print(data['id']+' '+data['fname']+' '+data['lname']+' '+data['leave'])
                    s = True
            if not s : #ถ้าหาไม่พบเลยสักตัวจะ print('Not Found')
                print('Not Found')
        print()

#=====================================
    
    elif menu == '5': #ตรวจวันลาจากขื่อ
      s_name = input('Frist name: ')
      with open('editstudents.csv','r',newline='') as f : # find from editstudents.csv
              student_leave = csv.DictReader(f)
              s = False
              for data in student_leave :
                  if s_name in data['fname']: #s_name เป็นส่วนหนึ่งของ data['fname'] หรือไม่
                      print(data['id']+' '+data['fname']+' '+data['lname']+' '+data['leave'])
                      s = True
              if not s : #ถ้าหาไม่พบเลยสักตัวจะ print('Not Found')
                  print('Not Found')
      print()

#=====================================
    
    elif menu == '6': #สรุปวันลาทั้งหมด 
        ls = 'Leave Sick'
        lb = 'Leave Business'
        lt = 'Leave Travel'
        lo = 'Leave Other'
        with open('editstudents.csv','r',newline='') as le :
            leave_s = csv.DictReader(le)

            
            ltlist = []
            lslist = []
            lblist = []
            lolist = []
            cs = []
            cb = []
            ct = []
            co = []
            for data in leave_s:
                if lt == data['leave']:
                    ltlist.append(data['id']+' '+data['fname']+' '+data['lname']+' '+data['leave'])
                    ct.append(1)
                if ls == data['leave']:
                    lslist.append(data['id']+' '+data['fname']+' '+data['lname']+' '+data['leave'])
                    cs.append(1)
                if lb == data['leave']:
                    lblist.append(data['id']+' '+data['fname']+' '+data['lname']+' '+data['leave'])
                    cb.append(1)
                if lo == data['leave']:
                    lolist.append(data['id']+' '+data['fname']+' '+data['lname']+' '+data['leave'])
                    co.append(1)
            

            if len(lslist) > 0:
                print('Student '+ls+' '+str(len(cs)))
                for data in lslist:
                    print(data)
            else:
                print('Student '+ls)
                print('Not Found')

            print()

            if len(lblist) > 0:
                print('Student '+lb+' '+str(len(cb)))
                for data in lblist:
                    print(data)
            else:
                print('Student '+lb)
                print('Not Found')

            print()

            if len(ltlist) > 0:
                print('Student '+lt+' '+str(len(ct)))
                for data in ltlist:
                    print(data)
            else:
                print('Student '+lt)
                print('Not Found')

            print()

            if len(lolist) > 0:
                print('Student '+lo+' '+str(len(co)))
                for data in lolist:
                    print(data)
            else:
                print('Student '+lo)
                print('Not Found')
                
            print()
        print()

#=====================================

    else:
      print("Please enter a number in the range 0-6 to access the menu")
      print ()
      print ("==================")
      print ()

#=====================================
#ไม่เอา
"""x
    if menu ==  '7' :
        print(check(input()))
"""
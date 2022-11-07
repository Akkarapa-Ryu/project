import pandas as pd
import csv
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
def openA(sid,fn,ln,date,leave):
    with open('editstudents.csv','a',newline='') as cf:
        cfw = csv.writer(cf)
        cfw.writerow([sid,fn,ln,date,leave])
    print("data successfully saved")
    return

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
      names_students = pd.read_csv('students.csv')
      print(names_students)

#========================================

  elif menu == '2': #ส่งคำร้องลาเรียน
    while True:
      while True: 
        print()
        StudentID = input("ID ICT/DST: ")
        Stop = 0
#เช็ครหัส
        if len(StudentID) == 7:
          Stop += 1
          if StudentID[0] == '6':
            Stop += 1
            if StudentID[1] == '5':
              Stop += 1
              if StudentID[2] == '8':
                Stop += 1
          
#ยืนยันบันทึก
        if Stop == 4:
          Stop = Submite()
        if Stop == "Submit":
            break
        print ("Please Input ID Student ICT or DST")
        print ()
#ลาด้วยเหตุผลอะไร

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
    
      while True:
        print()
        print ("Class data DD-MM-YYYY")
        DD = input("DD: ")
        MM = input("MM: ")
        YYYY = input("YYYY: ")
        Stop = 0

#เช็คเดือนที่ลงท้ายด้วยคม
    
        if MM == '01' or MM == '03' or MM == '05' or MM == '07' or MM ==  '08' or MM == '10' or MM == '12' and int(DD) >= 1 and int(DD) <= 31 and len(YYYY) == 4 and int(YYYY) >= 2022:
          Stop += 1
          
#เช็คเดือนที่ลงท้ายด้วยยน
        
        elif MM == '04' or MM == '06' or MM == '09' or MM == '11' and int(DD) >= 1 and int(DD) <= 30 and len(YYYY) == 4 and int(YYYY) >= 2022:
          Stop +=1

#เช็คเดือนกุมภาพันธ์
        
        elif MM == '02' and int(DD) >= 1 and (int(DD) <= 28 or ((int(YYYY))%4 == 0 and int(DD) <= 29)) and len(YYYY) == 4 and int(YYYY) >= 2022:
          Stop += 1

          
        if Stop == 1:
          Stop = Submite()
        if Stop == "Submit":
          break

        print ("Class data Erorr Please Input DD-MM-YYYY")
      
      print ()
      print (StudentID)
      print (L)
      print (f"{DD}-{MM}-{YYYY}")
      while True:
        print()
        Submit = input("Submit AllData?(Yes/No): ")
        if Submit == "Yes":
          Stop = 'Submit'
          print("Submit All Data")
          break
        elif Submit == "No":
          print ("'Reset All Data'")
          Stop = 0
          break
        else:
          print ("Please Input Yes or No")
        
      if Stop == "Submit":
        break

#======================================
  
    open = openA(StudentID,input("Firstname: "),input("Lastname: "),(DD,MM,YYYY),L)
    print(open)

#======================================
  
  elif menu == '3': #ตรวจวันลาจากวันที่
    print()

#=====================================
    
  elif menu == '4': #ตรวจวันลาจากรหัส
    print()

#=====================================
    
  elif menu == '5': #ตรวจวันลาจากขื่อ
    print()

#=====================================
    
  elif menu == '6': #สรุปวันลาทั้งหมด 
    print()

#=====================================

  else:
    print("Please enter a number in the range 0-6 to access the menu")
  print ()
  print ("==================")
  print ()

#=====================================
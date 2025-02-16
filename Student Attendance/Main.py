#This is the Main file This is the file From which we'll start our program
from config import get_db_connection
from importing import importing_Data,exporting_Data
import os
from slogin import student_login,teacherslogin
import pyfiglet
conn,cur=get_db_connection()
subjects = {1: "java", 2: "python", 3: "dsc", 4: "asp"}
if conn is not None and cur is not None:
    try:
        def showOneAttendance(roll):
            sel_sub = int(input("Enter the subject \n 1. Java\n2. Python\n3.DSC\n4. ASP.net\n> "))

            subjects = {1: "java", 2: "python", 3: "dsc", 4: "asp"}
            sel_sub = subjects.get(sel_sub)

            if sel_sub is None:
                print("Error: Wrong input")
                input("Press Enter to continue...")
                return

            # Construct query dynamically for table name
            show_script = f"SELECT status FROM {sel_sub} WHERE roll_no = %s"

            try:
                cur.execute(show_script,(roll,))
                total_lec=0
                attended_lec=0
                for data in cur.fetchall():
                    if data:
                        total_lec+=1
                        if data[0] == 'P':
                            attended_lec += 1
                print(f"Subject: {sel_sub}")
                print(f"Total Lectures: {total_lec}")
                print(f"Attended Lectures: {attended_lec}")
                print("Attendance %: ", (attended_lec / total_lec) * 100)
                input("Press Enter to continue...")
            except Exception as e:
                print(f"Error retrieving attendance: {e}")
        def showdetailedattend(roll):
            for i in subjects:
                Query=f'''SELECT * FROM {subjects.get(i)} WHERE roll_no=%s'''
                print(f"Subject:    {subjects.get(i)}")
                try:
                    cur.execute(Query,(roll,))
                    for data in cur.fetchall():
                        if data: print(data[1],"\t",data[2])
                        else: print("No Attendance Found")

                except Exception as e:
                    print(f"Error: {e}")
        def showAllAttendance(roll):
            for i in subjects:
                sub_query=f'''SELECT status FROM {subjects.get(i)} where roll_no=%s'''
                try:
                    cur.execute(sub_query,(roll,))
                    total_lec=0
                    attended_lec=0
                    for data in cur.fetchall():
                        if data:
                            total_lec+=1
                            if data[0]=='P':
                                attended_lec+=1
                    print(f"Subject:            {subjects.get(i)}")
                    print(f"Total Lectures:     {total_lec}")
                    print(f"Attended Lecture:   {attended_lec}")
                    print(f"Attendance %:       {(attended_lec/total_lec)*100}")
                except Exception as e:
                    print(f"Error retrieving attendace: {e}")

        loop=False
        while not loop:
            os.system('cls')
            banner = pyfiglet.figlet_format("Student Attendance System",width=100)
            print(banner)
            print("Enter your Role")
            print("1. Student")
            print("2. Teacher")
            print("3. Exit")
            opt=int(input(">"))
            if opt == 1:
                roll,name=student_login()
                if roll is not None and name is not None:
                    while True:
                        os.system('cls')
                        print(f"Welcome {name}")
                        print("Enter the option")
                        print("1. Show attendance of all subjects")
                        print("2. Show attendance of specific subject")
                        print("3. Logout")
                        opt=int(input(">"))
                        if opt==1:
                            showAllAttendance(roll)
                            input("Press Enter to continue...")
                        elif opt==2:
                            showOneAttendance(roll)
                        else:
                            break
                else:
                    print("Thanks For Visiting....!")
            elif opt==2:
                id,name=teacherslogin()
                if id is not None and name is not None:
                    os.system('cls')
                    print(f"Welcome {name}")
                    print("Enter your Option")
                    opt=int(input("1. Show all Students Attendance\n2. Show Specify Student Attendance\n3. Import Attendance form Excel Sheet\n4. Export data To Excel Sheet\n5. Exit\n"))
                    if opt==1:
                        try:
                            Query=''' SELECT roll_no,name FROM studentinfo order by roll_no'''
                            cur.execute(Query)
                            for data in cur.fetchall():
                                print(f"Student Name: {data[1]}")
                                showAllAttendance(data[0])
                            input("Press Enter to Continue...")

                        except Exception as e:
                            print(f"Error While retriving data {e}")
                    elif opt==2:
                        rollno=int(input("Enter Student Roll No: "))
                        showdetailedattend(rollno)
                        input("Press Enter to Continue....")
                    elif opt==3:
                        importing_Data()
                    elif opt==4:
                        exporting_Data()
                    elif opt==5:
                        break
                    else:
                        print("Sorry! Wrong Input...")
                        input("Please Enter to Continue....")
            elif opt==3:
                break
            else:
                print("Sorry! Wrong Input...")
                input("Please Enter to Continue....")
    except Exception as error:
        print(f"Error occured: {error}")
    finally:
        cur.close()
        conn.close()
else:
    print("Unable to connect to the data base")
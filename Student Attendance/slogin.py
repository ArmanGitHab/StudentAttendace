import os
from config import get_db_connection

conn, cur = get_db_connection()
#Function To Login Student or Register Himself
def student_login():
    if conn is not None and cur is not None:
        try:
            while True:
                os.system("cls")
                print("Enter the option")
                print("1. Login")
                print("2. Register")
                print("3. Exit")
                con = int(input(">"))
                if con == 1:
                    try:
                        log = "SELECT roll_no,name, password FROM studentinfo WHERE roll_no = %s AND password = %s"
                        roll = int(input("Enter your Roll No: "))
                        passwd = input("Enter your Password: ")
                        cur.execute(log, (roll, passwd))
                        data = cur.fetchone()

                        if data:
                            rolldb,name, passdb = data
                            if roll == rolldb and passwd == passdb:
                                print("Login successful!")
                                return roll,name
                            else:
                                print("Wrong student credentials.")
                                input("Press Enter to continue...")
                        else:
                            print("No matching student found.")
                            input("Press Enter to continue...")
                    except Exception as error:
                        print(f"Something went wrong while logging in: {error}")
                        input("Press Enter to continue...")

                elif con == 2:
                    try:
                        os.system("cls")
                        reg_roll = int(input("Enter your Roll No: "))
                        reg_pass = input("Enter your Password: ")
                        get_stu = '''SELECT roll_no, password FROM studentinfo WHERE roll_no = %s'''
                        cur.execute(get_stu, (reg_roll,))
                        data = cur.fetchone()

                        if data:
                            stored_roll_no, stored_password = data
                            if reg_pass == stored_password:
                                print("This password is already registered.")
                                input("Press Enter to continue...")
                            else:
                                update_pass = '''UPDATE studentinfo SET password = %s WHERE roll_no = %s'''
                                cur.execute(update_pass, (reg_pass, reg_roll))
                                conn.commit()
                                print("Password updated successfully!")
                                input("Press Enter to continue...")
                        else:
                            print("Student not found.")
                            input("Press Enter to continue...")
                    except Exception as e:
                        print(f"Error occurred while registering: {e}")
                        input("Press Enter to continue...")

                elif con == 3:
                    return None,None
                else:
                    print("Error: You entered something wrong.")
                    input("Press Enter to continue...")

        except Exception as err:
            print(f"Error occurred: {err}")
            input("Press Enter to continue...")

        finally:
            cur.close()
            conn.close()
    else:
        print("Failed to connect to the database")

def teacherslogin():
    if conn is not None and cur is not None:
        try:
            while True:
                os.system('cls')
                opt=int(input("1. Login\n2. Register\n3. Exit\n"))
                if opt==1:
                    ID=int(input("Enter your ID"))
                    Pass=input("Enter your Password")
                    log_query='''SELECT Id,name FROM teachersinfo WHERE Id=%s AND pass=%s'''
                    cur.execute(log_query,(ID,Pass))
                    data=cur.fetchone()
                    if data:
                        return data[0],data[1]
                    else:
                        print("No Data Found Or You are not Registered")
                elif opt==2:
                    ID=int(input("Enter your ID: "))
                    Name=input("Enter Your Name: ")
                    Pass=input("Enter Your Password: ")
                    CheckPass=input("Re-enter Your Password: ")
                    if Pass==CheckPass:
                        Reg_query='''INSERT INTO teachersinfo(Id,name,pass) VALUES (%s,%s,%s)'''
                        cur.execute(Reg_query,(ID,Name,Pass))
                        conn.commit()
                    else:
                        print("Password Does not Match")
                        input("Press Enter To continue")
                elif opt==3:
                    return None,None
                else:
                    print("Worng Input")

        except Exception as e:
            print(f"Error While connecting to the database: {e}")
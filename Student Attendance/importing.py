from openpyxl import load_workbook
import pandas as pd
from config import get_pd_file
from config import get_db_connection
import os
from datetime import datetime
import numpy as np

conn, cur = get_db_connection()
subjects = {1: "java", 2: "python", 3: "dsc", 4: "asp"}
def importing_Data():
    df = get_pd_file()
    if df is not None and conn is not None and cur is not None:
        while True:
            print("Select Your Option")
            opt = int(input("1. To Import Attendance to the Database\n2. To display the given Excel File\n3. Exit\n"))

            if opt == 1:
                sub=int(input("Enter your subject\n1. Java\n2. Python\n3. Data Structure Using C\n4. ASP .net\n"))
                try:
                    get_roll='''SELECT roll_no FROM studentinfo'''
                    cur.execute(get_roll)
                    roll_numbers=cur.fetchall()
                    for search_value in roll_numbers:
                        if search_value[0] in df['ID'].values:
                            row = df[df['ID'] == search_value[0]]
                            da=row['ID']
                            try:
                                for key, val in row.iloc[0].items():
                                    if isinstance(key, datetime):  # If key is datetime
                                        #this query stops duplicate attendance to be inserted
                                        insert_query = f'''
                                            INSERT INTO {subjects.get(sub)}(roll_no, dates, status)
                                            VALUES (%s, %s, %s)
                                            ON CONFLICT (roll_no, dates) DO NOTHING;
                                        '''
                                        cur.execute(insert_query, (search_value[0], key, val))
                                        conn.commit()
                                print(f"Inserted Attendance Successfully Of student {search_value[0]}")
                            except Exception as e:
                                print(f"Error While Importing Attendance")

                        else:
                            print(f"No rows found with roll number {search_value[0]}")
                except Exception as e:
                    print(f"Error : {e}")
            elif opt == 2:
                os.system('cls')
                print(df.head(6))

            elif opt == 3:
                return

            else:
                print("Sorry, You have Entered Something Wrong...!")
def get_unique_filename(base_name="attendance"):
    count = 0
    while True:
        fname = f"{base_name}{count}.xlsx"
        if not os.path.exists(fname):  # Check if file exists
            return fname  # Return the first available unique name
        count += 1


def exporting_Data():
    subjects = {1: "java", 2: "python", 3: "dsc", 4: "asp"}  # Table names for each subject
    File_Name = get_unique_filename()  # Generate a unique filename

    with pd.ExcelWriter(File_Name, engine="openpyxl") as writer:
        for subject_id, table_name in subjects.items():
            print(f"Processing subject: {table_name}")

            # Step 1: Get all unique roll numbers
            cur.execute(f'''SELECT DISTINCT roll_no FROM {table_name} ORDER BY roll_no''')
            roll_numbers = [row[0] for row in cur.fetchall()]

            # Step 2: Get all unique dates
            cur.execute(f'''SELECT DISTINCT dates FROM {table_name} ORDER BY dates''')
            dates = [row[0] for row in cur.fetchall()]

            # Step 3: Create DataFrame structure
            columns = ["ID", "Name"] + dates  # First two columns: ID, Name
            df = pd.DataFrame(columns=columns)

            # Step 4: Fill DataFrame with attendance data
            rows_list = []  # Using list to store rows before creating DataFrame

            for roll_no in roll_numbers:
                # Get student name from studentinfo table
                cur.execute(f'''SELECT name FROM studentinfo WHERE roll_no = {roll_no}''')
                student_name = cur.fetchone()
                student_name = student_name[0] if student_name else "Unknown"

                # Initialize row with ID and Name
                row_data = {col: None for col in columns}
                row_data["ID"] = roll_no
                row_data["Name"] = student_name

                # Get attendance status for each date
                cur.execute(f'''SELECT dates, status FROM {table_name} WHERE roll_no = {roll_no}''')
                attendance_records = cur.fetchall()

                for date, status in attendance_records:
                    row_data[date] = status  # Fill attendance data (P/A)

                rows_list.append(row_data)  # Add row to list

            # Convert list to DataFrame and append
            if rows_list:
                df = pd.concat([df, pd.DataFrame(rows_list)], ignore_index=True)

            # Only save the sheet if it has data
            if not df.empty:
                df.to_excel(writer, sheet_name=table_name, index=False)

    print(f"✅ Data exported successfully to {File_Name}")

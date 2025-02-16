import os

import psycopg2
import psycopg2.extras
import pandas as pd
FILE_NAME="booo.xlsx"
DB_CONFIG={
    "user":"postgres",
    "password":"Arman",
    "host":"localhost",
    "port":5433,
    "dbname":"Student"
}
#For connection for Database
def get_db_connection():
    try:
        conn=psycopg2.connect(**DB_CONFIG)
        cur=conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return conn,cur
    except Exception as e:
        print(f"Error connecting  to the database: {e}")
        return None,None
#For Connection of Exel From using Pandas
def get_pd_file():
    try:
        print("Enter the option")
        opt=int(input("1. Show all Excel files in the folder\n2. Enter Your File Name\n3. Exit\n"))
        if opt==1:
            files=os.listdir(".")
            for f in files:
                if f.endswith(".xlsx") : print(f)
            FILE_NAME = input("Enter your File name(Excel)")
            df = pd.read_excel(FILE_NAME)
            return df
        elif opt==2:
            FILE_NAME=input("Enter your File name(Excel)")
            df = pd.read_excel(FILE_NAME)
            return df
        elif opt==3:
            return None
        # df=pd.read_excel(FILE_NAME)
        # return df
    except FileExistsError as e:
        print(f"Error fetching file: {e}")
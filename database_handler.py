import sqlite3
from datetime import datetime

def open_db(): #create a function to open database
    global conn
    conn = sqlite3.connect('accounts.db') #create database with file name(accounts)

    global c
    c = conn.cursor() #.cursor - communicate with the MySQL database

def close_db(): #create a function to close database
    c.close()
    conn.close()

def create_table(): # create a table in mysql
    open_db()
    #create a table if accounts(file name) does not exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS accounts( 
            first_name TEXT,
            last_name TEXT,
            username TEXT,
            password TEXT,
            date_registered TEXT
        )
    ''')

    close_db()

def delete(username,password):
    open_db()
            
    c.execute('''
        DELETE FROM accounts 
        WHERE username = (?)
        AND password = (?)
    ''', (username, password))
    
    conn.commit()
    close_db()

def register(first,last,username,password,date):
    open_db()

    c.execute('''
        INSERT INTO accounts VALUES (?,?,?,?,?) 
    ''', (first, last, username, password, date))

    conn.commit()
    close_db()   

def login(username, password):
    open_db()

    c.execute('''
        SELECT * FROM accounts
        WHERE username = (?)
        AND password = (?)    
    ''', (username, password)) 

    data = c.fetchone()
    if data:
        close_db()
        return True
    else:
        close_db()
        return False
  
def get_acc_info(username, password):
    open_db()

    c.execute('''
        SELECT * FROM accounts
        WHERE username = (?)
        AND password = (?)    
    ''', (username, password)) 

    data = c.fetchone()
    close_db()
    return data    

def update_first_name(username, password, new_first):
    open_db()

    c.execute('''
        UPDATE accounts
        SET first_name = (?)
        WHERE username = (?) AND password = (?)
    ''', (new_first, username, password))

    conn.commit()
    close_db()

def update_last_name(username, password, new_last):
    open_db()

    c.execute('''
        UPDATE accounts
        SET last_name = (?)
        WHERE username = (?) AND password = (?)
    ''', (new_last, username, password))

    conn.commit()
    close_db() 

def update_username(username, password, new_user):
    open_db()

    c.execute('''
        UPDATE accounts
        SET username = (?)
        WHERE username = (?) AND password = (?)
    ''', (new_user, username, password))

    conn.commit()
    close_db()

def update_password(username, password, new_pass):
    open_db()

    c.execute('''
        UPDATE accounts
        SET password = (?)
        WHERE username = (?) AND password = (?)
    ''', (new_pass, username, password))

    conn.commit()
    close_db()


#def current_date():
    
#dateNow = datetime.now()
#dateStr = datetime.strftime(dateNow, '%m/%d/%Y')


create_table()
#register("Nacky", "Loz", "nackyloz", "123me", dateStr)
#update_first_name("nackyloz", "123me", "Nance")

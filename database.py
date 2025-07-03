import pymysql
from tkinter import messagebox

def connect_database():
    global cur, con
    try:
        con=pymysql.connect(host='localhost',user='root',password='@dakka')
        cur=con.cursor()
    except:
        messagebox.showerror('ERROR','Something went wrong. Please open mysql app before running again')
        return

    cur.execute('CREATE DATABASE IF NOT EXISTS employee_data')
    cur.execute('USE employee_data')
    cur.execute('CREATE TABLE IF NOT EXISTS data(Id VARCHAR(10), Name VARCHAR(20), Phone VARCHAR(15), Role VARCHAR(30), Gender VARCHAR(10), Salary DECIMAL(10,2))')


def id_exists(id):
    cur.execute('SELECT COUNT(*) FROM data WHERE id=%s',id)
    res=cur.fetchone()
    return res[0]>0


def insert(id,name,phone,role,gender,salary):
    cur.execute('INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)',(id,name,phone,role,gender,salary))
    con.commit()


def fetch_employees():
    cur.execute('SELECT * FROM data')
    res=cur.fetchall()
    return res


def update(id,name,phone,role,gender,salary):
    cur.execute('UPDATE data SET name=%s, phone=%s, role=%s, gender=%s, salary=%s WHERE id=%s',(name,phone,role,gender,salary,id))
    con.commit()


def delete(id):
    cur.execute('DELETE FROM data WHERE id=%s',(id))
    con.commit()


def search(option,value):
    cur.execute('SELECT * FROM data WHERE {}=%s'.format(option),value)
    res=cur.fetchall()
    return res


def deleteall():
    cur.execute('TRUNCATE TABLE data')
    con.commit()


connect_database()
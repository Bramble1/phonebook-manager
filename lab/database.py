import sys
import pyodbc

 

connection_string=(
        'DRIVER=MariaDB Unicode;'
        'SERVER=localhost;'
        'PORT=3306;'
        'DATABASE=testDB;'
        'UID=username;'
        'PWD=password;'
        )
 

def create_table(con,cursor):
    cursor.execute('drop table if exists People;')
    cursor.execute('create table if not exists People(ID INT AUTO_INCREMENT PRIMARY KEY,LastName varchar(255) not null,FirstName varchar(255) not null);');

con=pyodbc.connect(connection_string)
cursor = con.cursor()


def populate_table(con,cursor):
    cursor.execute('Insert into People(LastName,FirstName) values(\'Joy\',\'July\')')
    cursor.execute('Insert into People(LastName,FirstName) values(\'Smith\',\'Robert\')')
    cursor.execute('Insert into People(LastName,FirstName) values(\'Dhillon\',\'Sam\')')



def print_table(cusor):
    for row in cursor.execute('select * from People'):
        print(row)

#MAIN

con=pyodbc.connect(connection_string)
cursor=con.cursor()

#con.commit()

create_table(con,cursor)

populate_table(con,cursor)

con.commit()


print_table(cursor)



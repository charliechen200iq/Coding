import sqlite3
import os
os.system('clear')
connection = sqlite3.connect("customer.db")
cursor = connection.cursor()

#Create a table named customer

command1 = """ CREATE TABLE IF NOT EXISTS 
customer (first_name text, last_name text, email text)"""

cursor.execute(command1)



cursor.execute("INSERT INTO customer VALUES ('James', 'Toptun', 'jamestoptun@macleans.school.nz')")
cursor.execute("INSERT INTO customer VALUES ('charlie', 'Chen', 'charrliechen@macleans.school.nz')")
cursor.execute("INSERT INTO customer VALUES ('Eric', 'Wang', 'ericwang@macleans.school.nz')")
print("Records added to the table")

print("----------------------------------------- \n Customer Table")
connection.commit()
cursor.execute("SELECT * FROM customer")
results = cursor.fetchall()
print(results)


print("=============================================================")
print("Name" + " " + "Surname" + " " + "Email")
for item in results:
    print(item[0] + " " + item[1] + " " + item[2])
    print("\n")


connection.close()




connection = sqlite3.connect("customer.db")
cursor = connection.cursor()
cursor.execute("INSERT INTO customer VALUES ('joshua', 'Toptun', 'jamestoptun@macleans.school.nz')")
cursor.execute("INSERT INTO customer VALUES ('whats up', 'Chen', 'charrliechen@macleans.school.nz')")
connection.commit()
print("hi")
connection.close()
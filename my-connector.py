import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='priya1510',
    port='3306',
    database='ease_my_trip'
)

mycursor = mydb.cursor()

mycursor.execute('SELECT * FROM user')

user = mycursor.fetchall()

for user in user:
    print(user)
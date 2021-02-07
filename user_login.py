import main
import students
import mysql.connector
from getpass import getpass
connection = mysql.connector.connect(user='root',password='Mithaimate@28',host='localhost',database='project2')
mycursor = connection.cursor()

n = input('Enter the choice(a/b):\n a->User\n b->student\n')
if n == 'a':
    while True:
        user = input('Enter the username: ')
        password = input('Enter the password: ')

        mycursor.execute("select * from user where username = '%s' ;" % user)
        temp = mycursor.fetchall()

        if not temp:
            mycursor.execute("insert into user values ('%s','%s') ;" % (user,password ))
            connection.commit()
            mycursor.execute("select * from user where username = '%s' ;" % user)
            temp = mycursor.fetchall()
            temp = list(temp)

        if temp is None:
            print('Invalid username')

        elif temp[0][1] == password:
            main.main()
            break
        else:
            print('Wrong password')
    connection.commit()
else:
    connection.commit()
    print('For Students'.center(32, '*'))
    students.main()
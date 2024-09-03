import mysql.connector as connector

class DBHelper:
    def __init__(self):
        self.con=  connector.connect(host='localhost',
                                    port= '3306',
                                    user= 'root',
                                    password='root',
                                    database= 'pythontest')
        query= 'craete table if not exists user(userId int primary key, userName varchar(200), phone varchar(12))'
        cur= self.con.curser()
        cur.execute(query)
        print("created")


#main coding


helper= DBHelper()
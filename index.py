import crypt;
import mysql.connector;

import urllib;

mydb = mysql.connector.connect(user="root",password="root",host="localhost",port="3306",database="test");
if mydb.is_connected():
    mycursor = mydb.cursor();
    mycursor.execute("select * from sample_users");
    data = mycursor.fetchall(); # get all the records in the cursor
    for col in data:
        print(col);

mycursor.execute("insert into sample_users values ('xx224', 'xxxt1')")
## database commit required for the data to go inthe system.....
mydb.commit();

#conn = pymssql.connect("server", "user", "password", "db");
#cursor = conn.cursor();
#cursor.execute("statement");
#cursor.fetchone(); # cursor.fetchall();





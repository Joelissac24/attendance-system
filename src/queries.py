import db_connector as db

def adding(names):
    db.mycursor.execute("insert into student_details(student_name,student_age) values(%(name)s,%(age)s)",name)
    db.mydb.commit()

def list_details():
    operation = "select * FROM student_details "
    a=dc.mycursor.execute (operation, multi=True)
    for result in a : 
        print(result.fetchall())
import db_connector as dc

class Student:
    
    def add(self,values:list):
        val=values
        for names in val:
            dc.mycursor.execute("insert into student_details(student_name,student_age) values(%(name)s,%(age)s)",names)
            dc.mydb.commit()
       
    def edit(self,data:int,val2:dict):
        val2["id"] = data
        query=( "UPDATE student_details set student_name=%(name)s,student_age=%(age)s where id=(%(id)s)"
        )
        dc.mycursor.execute(query,val2)
        dc.mydb.commit()

    def list_details(self):
        operation = "select * FROM student_details "
        query2=dc.mycursor.execute (operation, multi=True)
        return query2

    def show(self,id:int):
        dc.mycursor.execute("select * FROM student_details where id=%s",(id,))
        row=dc.mycursor.fetchone()
        return row

    def delete(self,id:int):
        dc.mycursor.execute("DELETE  FROM student_details where id=%s",(id,))
        dc.mydb.commit()
    
stud=Student()
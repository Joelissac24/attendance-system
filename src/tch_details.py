import db_connector as dc

class Teacher:

    def add(self,values:list):
        for names in values:
            dc.mycursor.execute("insert into teacher_details(teacher_id,teacher_name)values(%(id)s,%(name)s)",names)
            dc.mydb.commit()
        
    def edit(self,data:int,val2:dict):
        val2["id"] = data
        query=(
           "UPDATE teacher_details set teacher_name=%(name)s where teacher_id=(%(id)s)" 
        )
        dc.mycursor.execute(query,val2)
        dc.mydb.commit()

    def list_details(self):
        operation="select * FROM teacher_details"
        query2=dc.mycursor.execute(operation,multi=True)
        return query2

    def show(self,id:int):
        dc.mycursor.execute("select * FROM teacher_details where teacher_id =%s",(id,))
        row=dc.mycursor.fetchone()
        return row

    def delete(self,id:int):
        dc.mycursor.execute("DELETE FROM teacher_details where teacher_id=%s",(id,))
        dc.mydb.commit()

tch=Teacher()



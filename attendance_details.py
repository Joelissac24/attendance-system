import db_connector as dc

class Attendance:
    def add(self,values:list):
        for data in values:
            dc.mycursor.execute("insert into records (student_id,attendance) values(%(id)s,%(attendance)s)",data)
        dc.mydb.commit()
    
    def edit(self,val:dict,data:int):
        val["id"]= data
        quer=(
            "UPDATE records set attendance=%(attendance)s where student_id =%(id)s"
            )
        dc.mycursor.execute(quer,val)
        # dc.mycursor.execute("UPDATE records set attendance=%(attendance)s where student_id =%(id)s",val)
        dc.mydb.commit()

    def list_details(self):
        operation="select records.student_id,student_details.student_name,records.attendance FROM records join student_details ON records.student_id=student_details.id;"
        query=dc.mycursor.execute(operation,multi=True)
        return query

    def show(self,id:int):
        dc.mycursor.execute("select records.student_id,student_details.student_name,records.attendance FROM records join student_details ON records.student_id=student_details.id where student_details.id=%s",(id,))
        row=dc.mycursor.fetchone()
        return row

    def delete(self,id:int):
        dc.mycursor.execute("delete from records where student_id= %s",(id,))
        dc.mydb.commit()
        

at=Attendance()
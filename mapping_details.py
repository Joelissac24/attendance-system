import db_connector as dc

class Mapping():
    def add(self,values:list):
        for data in values:
            dc.mycursor.execute("insert into class(t_id,s_id) values(%(t_id)s,%(s_id)s)",data)
            dc.mydb.commit()

    def edit(self,val2:list,data:int):  
        dc.mycursor.execute=("UPDATE class set t_id=%(t_id)s , s_id=%(s_id)s where t_id=%s",(val2,data))
        dc.mydb.commit()

    def list_details(self):
        operation="select teacher_details.teacher_name,student_details.student_name from class inner join teacher_details ON class.t_id=teacher_details.teacher_id inner join student_details ON class.s_id=student_details.id"
        query=dc.mycursor.execute(operation,multi=True)
        return query

    def show(self,id:int):
        dc.mycursor.execute("select teacher_details.teacher_name,student_details.student_name from class inner join teacher_details ON class.t_id=teacher_details.teacher_id inner join student_details ON class.s_id=student_details.id where class.t_id=%s",(id,))
        row=dc.mycursor.fetchall()
        return row

    def delete(self,id:int):
        dc.mycursor.execute("delete from class where t_id=%s",(id,))
        dc.mydb.commit()

mp=Mapping()
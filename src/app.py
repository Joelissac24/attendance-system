import click
import parsing as pg
import tch_details as td 
import stud_details as sd
import mapping_details as md
import attendance_details as ad

@click.group()
def cli():
    pass
@click.command()
@click.option('--action',required=True)
@click.option('--filename')
@click.option('--data')
def student(action,filename,data):  
    if action == "add":
        values = pg.obj1.convert(filename)
        sd.stud.add(values)
        print("Student_details Added Successfully")

    if action == "edit":
        val2 = pg.obj1.covert(filename)
        sd.stud.edit(data,val2)
        print("Updated Successfully")

    if action == "list_details":
        z = sd.stud.list_details()
        for result in z : 
            a=result.fetchall()
            for data in a:
                print(data)
        
    if action == "show":
        row = sd.stud.show(data)  
        print(row)      
        
    if action == "delete":
        sd.stud.delete(data)
        print("Deleted Successfully")
        

@click.command()
@click.option('--action',required=True)
@click.option('--filename')
@click.option('--data')
def teacher(action,filename,data):
    if action == "add":
        values = pg.obj1.convert(filename)
        td.tch.add(values)
        print("Teacher_details Added successfully")

    if action == "edit":
        val2=pg.obj1.covert(filename)
        td.tch.edit(data, val2)
        print("Updated Successfully")

    if action == "list_details":
        a=td.tch.list_details()
        for data in a:
            a=data.fetchall()
            for row in a:
                print(row)
             
    if action == "show":
        row = td.tch.show(data)
        print(row)

    if action == "delete":
        td.tch.delete(data)
        print("Deleted Successfully")
    
@click.command()
@click.option('--action',required=True)
@click.option('--filename')
@click.option('--data')
def mapping(action,filename,data):
    if action == "add":
        values=pg.obj1.convert(filename)
        md.mp.add(values)
        print("Mapped Successfully")

    if action == "edit":
        values=pg.obl1.convert(filename)
        md.mp.edit(values,data)
        print("Updated Successfully")

    if action == "list_details":
        a=md.mp.list_details()
        for data in a:
            a=data.fetchall()
            for row in a:
                print(row)

    if action == "show":
        row = md.mp.show(data)
        for data in row:
            print(data)

    if action == "delete":
        md.mp.delete(data)
        print("Deleted Successfully")


@click.command()
@click.option('--action',required=True)
@click.option('--filename')
@click.option('--data')
def attendance(action,filename,data):
    if action == "add":
        values=pg.obj1.convert(filename)
        ad.at.add(values)
        print("Added Successfully")
    if action == "edit":
        values=pg.obj1.convert(filename)
        ad.at.edit(values, data)
        print("Updated Successfully")

    if action == "list_details":
        a=ad.at.list_details()
        for data in a:
            a=data.fetchall()
            for row in a:
                print(row)

    if action == "show":
        row=ad.at.show(data)
        print(row)
    
    if action == "delete":
        ad.at.delete(data)
        print("Deleted Successfully")

cli.add_command(teacher)
cli.add_command(student)
cli.add_command(mapping)
cli.add_command(attendance)
cli()

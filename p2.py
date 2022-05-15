from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
from tkinter.scrolledtext import * 


def f1():
	mw.withdraw()
	aw.deiconify()

def f2():
	aw.withdraw()
	mw.deiconify()

def f3():
	mw.withdraw()
	vw.deiconify()
	vw_st_data.delete(1.0,END)
	info = ""
	con = None
	try:

		con =connect("kc.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			info =info +"rno ="+str(d[0])+"name ="+str(d[1])+"\n"
		vw_st_data.insert(INSERT,info)
	except Exception as e:
		showerror("Mistake",e)
	finally:
		if con is not None:
			con.close()
def f4():
	vw.withdraw() 
	mw.deiconify()
def f5():
	rno = int(aw_ent_rno.get())
	name = aw_ent_name.get()
	con = None
	try:
		con = connect("kc.db")
		cursor = con.cursor()
		sql= "insert into student values('%d','%s')"
		cursor.execute(sql%(rno,name))
		con.commit()
		showinfo("Success", "record saved")
		aw_ent_rno.delete(0, END)
		aw_ent_name.delete(0,END)
		aw_ent_rno.focus()
	except Execution as e:
		showerror("Mistake",e)
	finally:
		if con is not none:
			con.close()
mw =Tk()
mw.title("S.M.S")
mw.geometry("700x600+200+200")

f =("Times New Roman",24,"bold")
mw_btn_add =Button(mw,text ="Add",font=f,width =6,command=f1)
mw_btn_view =Button(mw,text ="View",font =f,width=6,command=f3)


y=20
mw_btn_add.pack(pady=y)
mw_btn_view.pack(pady=y)

aw = Toplevel(mw)
aw.title("Add Student")
aw.geometry("700x600+200+200")

aw_lab_rno = Label(aw, text="enter rno:", font=f)
aw_ent_rno=Entry(aw,font=f,bd=3)
aw_lab_name=Label(aw,text="enter name: ", font=f)
aw_ent_name=Entry(aw,font=f,bd=3)
aw_btn_save=Button(aw,text="Save",font=f,command=f5)
aw_btn_back=Button(aw,text="Back",font=f, command=f2)
aw_lab_rno.pack(pady=y)
aw_ent_rno.pack(pady=y)
aw_lab_name.pack(pady=y)
aw_ent_name.pack(pady=y)
aw_btn_save.pack(pady=y)
aw_btn_back.pack(pady=y)
	
aw.withdraw()
vw= Toplevel(mw)
vw.title("View Student")
vw.geometry("700x600+200+200")

vw_st_data =ScrolledText(vw,width =30,height=10,font=f)
vw_btn_back=Button(vw,text="Back",font=f,command=f4)


vw_st_data.pack(pady=y)
vw_btn_back.pack(pady=y)
vw.withdraw()

mw.mainloop()	


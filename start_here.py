import tkinter.ttk as ttk
import mysql.connector as sql
import smtplib
import os
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

#Environment variables
email_user = os.environ.get('mailus')
email_pass = os.environ.get('mailpa')
sql_pass = os.environ.get('mysqlpa')

#global variables
global city_list
global mainscrn
global usern
global passw
global logid
global reg_edit
reg_edit = False
logid = ''

#defining functions
def mainpage():
	global mainscrn
	global usern
	global passw
	global logid
	mainscrn = Tk()
	mainscrn.geometry("640x360")
	mainscrn.resizable(0, 0)
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	frm1 = LabelFrame(mainscrn,text="Please login/register to continue.")
	lbl1 = Label(mainscrn,text="Welcome to Hacking Electronics Workshop",font=("Arial Bold",10))
	lbl2 = Label(mainscrn,text="OR")
	lbl3 = Label(frm1,text="UserID/Email:")
	lbl4 = Label(frm1,text="Password:")
	but1 = Button(mainscrn,text="Login",command=login)
	but2 = Button(mainscrn,text="Register",command=register)
	usern = Entry(frm1,width=35)
	passw = Entry(frm1,show='*',width=35)
	bg_topl = ImageTk.PhotoImage(Image.open("images/top_bg.jpg"))
	bg_botl = ImageTk.PhotoImage(Image.open("images/bottom_bg.jpg"))
	bg_leftl = ImageTk.PhotoImage(Image.open("images/left_bg.jpg"))
	bg_rightl = ImageTk.PhotoImage(Image.open("images/right_bg.jpg"))
	lbl5 = Label(image=bg_topl)
	lbl6 = Label(image=bg_botl)
	lbl7 = Label(image=bg_leftl)
	lbl8 = Label(image=bg_rightl)

	frm1.grid(row=2,column=1,columnspan=3)
	lbl1.grid(row=1,column=1,columnspan=3)
	lbl2.grid(row=3,column=2)
	lbl3.grid(row=0,column=0,sticky=E)
	lbl4.grid(row=1,column=0,sticky=E)
	but1.grid(row=3,column=1)
	but2.grid(row=3,column=3)
	usern.grid(row=0,column=1)
	passw.grid(row=1,column=1)
	lbl5.grid(row=0,column=1,columnspan=3)
	lbl6.grid(row=4,column=1,columnspan=3)
	lbl7.grid(row=0,column=0,rowspan=5)
	lbl8.grid(row=0,column=4,rowspan=5)
	mainscrn.mainloop()

def register():
	global regscrn
	global logid
	global reg_edit
	mainscrn.destroy()
	regscrn = Tk()
	width = 382
	height = 320
	screen_width = regscrn.winfo_screenwidth()
	screen_height = regscrn.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2)
	regscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
	regscrn.resizable(0, 0)
	regscrn.title("Register to Hacking Electronics Shop")
	regscrn.iconbitmap('images/icon.ico')
	
	frm2 = LabelFrame(regscrn)
	lbl7 = Label(regscrn,text="Please enter your details",font=("Arial Bold",10))
	lbl8 = Label(frm2,text="User ID:")
	lbl9 = Label(frm2,text="Email Add.:")
	lbl10 = Label(frm2,text="Password:")
	lbl11 = Label(frm2,text="Retype:")
	lbl12 = Label(frm2,text="First Name:")
	lbl13 = Label(frm2,text="Last Name:")
	lbl14 = Label(frm2,text="Mobile:")
	lbl15 = Label(frm2,text="Address:")
	lbl16 = Label(frm2,text="City:")
	lbl17 = Label(frm2,text="State:")
	lbl18 = Label(frm2,text="Pincode:")
	frm2.grid(row=1,column=0,columnspan=3,padx=4)
	lbl7.grid(row=0,column=0,columnspan=3)
	lbl8.grid(row=0,column=0,sticky=E)
	lbl9.grid(row=1,column=0,sticky=E)
	lbl10.grid(row=2,column=0,sticky=E)
	lbl11.grid(row=3,column=0,sticky=E)
	lbl12.grid(row=4,column=0,sticky=E)
	lbl13.grid(row=5,column=0,sticky=E)
	lbl14.grid(row=6,column=0,sticky=E)
	lbl15.grid(row=7,column=0,sticky=E)
	lbl16.grid(row=9,column=0,sticky=E)
	lbl17.grid(row=10,column=0,sticky=E)
	lbl18.grid(row=11,column=0,sticky=E)

	global userr
	global emair
	global passr
	global agair
	global fnamr
	global lnamr
	global mobir
	global add1r
	global add2r
	global cityr
	global pincr
	global state
	
	userr = Entry(frm2,width=50)
	emair = Entry(frm2,width=50)
	passr = Entry(frm2,show='*',width=50)
	agair = Entry(frm2,show='*',width=50)
	fnamr = Entry(frm2,width=50)
	lnamr = Entry(frm2,width=50)
	mobir = Entry(frm2,width=50)
	add1r = Entry(frm2,width=50)
	add2r = Entry(frm2,width=50)
	cityr = Entry(frm2,width=50)
	pincr = Entry(frm2,width=50)

	if reg_edit:
		sql_query = "SELECT * FROM he_users WHERE user_id = '{}'".format(logid)
		he_cursor.execute(sql_query)
		result = he_cursor.fetchall()

		userr.insert(0,result[0][0])
		emair.insert(0,result[0][1])
		passr.insert(0,result[0][2])
		fnamr.insert(0,result[0][3])
		lnamr.insert(0,result[0][4])
		mobir.insert(0,result[0][5])
		add1r.insert(0,result[0][6])
		add2r.insert(0,result[0][7])
		cityr.insert(0,result[0][8])
		pincr.insert(0,result[0][10])
		state = StringVar()
		state.set(result[0][9])

	else:
		state = StringVar()
		state.set("Select State")

	states = ["Andaman & Nicobar","Andhra Pradesh","Arunachal Pradesh",
	"Assam","Bihar","Chandigarh","Chhattisgarh","Dadra & Nagar Haveli",
	"Daman & Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh",
	"Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep",
	"Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram",
	"Nagaland","Orissa","Pondicherry","Punjab","Rajasthan","Sikkim",
	"Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttaranchal","West Bengal"]

	sttdw = OptionMenu(frm2,state,*states)
	
	userr.grid(row=0,column=1)
	emair.grid(row=1,column=1)
	passr.grid(row=2,column=1)
	agair.grid(row=3,column=1)
	fnamr.grid(row=4,column=1)
	lnamr.grid(row=5,column=1)
	mobir.grid(row=6,column=1)
	add1r.grid(row=7,column=1)
	add2r.grid(row=8,column=1)
	cityr.grid(row=9,column=1)
	sttdw.grid(row=10,column=1,sticky=W)
	pincr.grid(row=11,column=1)

	but5 = Button(regscrn,text="Clear",command=reg_clr)
	but6 = Button(regscrn,text="Cancel",command=reg_can)
	but7 = Button(regscrn,text="Register",command=reg_add)
	but5.grid(row=2,column=0)
	but6.grid(row=2,column=1)
	but7.grid(row=2,column=2)

	regscrn.mainloop()

def reg_clr():
	userr.delete(0,END)
	emair.delete(0,END)
	passr.delete(0,END)
	agair.delete(0,END)
	fnamr.delete(0,END)
	lnamr.delete(0,END)
	mobir.delete(0,END)
	add1r.delete(0,END)
	add2r.delete(0,END)
	pincr.delete(0,END)
	cityr.delete(0,END)
	state.set("Select State")

def reg_can():
	regscrn.destroy()
	mainpage()

def reg_add():
	global logid
	global reg_edit
	global msg
	incom = 12
	if len(userr.get()) != 0:
		incom -= 1
	if len(emair.get()) != 0:
		incom -= 1
	if len(passr.get()) != 0:
		incom -= 1
	if len(agair.get()) != 0:
		incom -= 1
	if len(fnamr.get()) != 0:
		incom -= 1
	if len(lnamr.get()) != 0:
		incom -= 1
	if len(mobir.get()) != 0:
		incom -= 1
	if len(add1r.get()) != 0:
		incom -= 1
	if len(add2r.get()) != 0:
		incom -= 1
	if len(pincr.get()) != 0:
		incom -= 1
	if len(cityr.get()) != 0:
		incom -= 1
	if state.get() != "Select State":
		incom -= 1

	if incom >= 1:
		messagebox.showerror("Registration Failed!","One or more fields is empty please fill it in.")
	else:
		if passr.get() != agair.get():
			messagebox.showerror("Registration Failed!","Passwords do not match.")
		elif len(pincr.get()) != 6:
			messagebox.showerror("Registration Failed!","Pincode is not of 6 digits.")
		elif len(mobir.get()) != 10:
			messagebox.showerror("Registration Failed!","Mobile number is not of 10 digits.")
		else:
			if len(emair.get()) < 7:
				messagebox.showerror("Registration Failed!","Email is invalid. Please correct the email address.")
			else:
				at = 0
				for ch in emair.get():
					if ch == "@":
						at += 1
				em_chk = ""
				for chno in range(-1,-5,-1):
					em_chk += emair.get()[chno]
				if em_chk == "moc." and at == 1:
					sql_query = "SELECT user_id FROM he_users"
					he_cursor.execute(sql_query)
					result = he_cursor.fetchall()
					if len(result) == 0:
						inv_em = False
						inv_id = False
						inv_mo = False
					else:
						for qur_res in result:
							if qur_res[0] == userr.get() and not reg_edit:
								inv_id = True
								break
							else:
								inv_id = False
						sql_query = "SELECT email FROM he_users"
						he_cursor.execute(sql_query)
						result = he_cursor.fetchall()
						for qur_res in result:
							if qur_res[0] == emair.get() and not reg_edit:
								inv_em = True
								break
							else:
								inv_em = False
						sql_query = "SELECT mob FROM he_users"
						he_cursor.execute(sql_query)
						result = he_cursor.fetchall()
						for qur_res in result:
							if qur_res[0] == mobir.get() and not reg_edit:
								inv_mo = True
								break
							else:
								inv_mo = False
					if inv_id:
						messagebox.showerror("Registration Failed!","User ID taken. Please try something else.")
					elif inv_em:
						messagebox.showerror("Registration Failed!","Email Registered. Please try something else.")
					elif inv_mo:
						messagebox.showerror("Registration Failed!","Mobile Number Registered. Please try something else.")
					else:
						try:
							int(mobir.get())
							int(pincr.get())
						except:
							messagebox.showerror("Registration Failed.","Mobile Number/Pincode is not a Number.")
						else:
							if reg_edit:
								sql_query = "DELETE FROM he_users where user_id = '{}'".format(logid)
								he_cursor.execute(sql_query)
								reg_edit = False
								logid = ""
							sql_query = "INSERT INTO he_users (user_id, email, pass, f_name, l_name, mob, add1, add2, city, state, pin, doj) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',NOW())".format(userr.get(),emair.get(),passr.get(),fnamr.get(),lnamr.get(),mobir.get(),add1r.get(),add2r.get(),cityr.get(),state.get(),pincr.get())
							he_cursor.execute(sql_query)
							he_db.commit()
							msg = EmailMessage()
							msg['Subject'] = "Final Step: Reply to activate account."
							msg['From'] = email_user
							msg['To'] = emair.get()
							msg.set_content("""
								Hi {}!
								    You received this email because it was submitted for registration to Hacking Electronics Shop.

								    If you would like to Register please reply:
								        Yes, Please activate my account.

								    Or else if you would like not to register please reply:
								        No, do not activate account.
								""".format(fnamr.get()))
							#send_email()
							messagebox.showinfo("Registration Complete","Registration Successful. Please activate account by replying to email sent to your email address and wait for admin approval.")
							regscrn.destroy()
							mainpage()
				else:
					messagebox.showerror("Registration Failed!","Email is invalid. Please correct the email address.")

def send_email():
	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(email_user,email_pass)
		smtp.send_message(msg)

def login():
	global logid
	global reg_edit
	if usern.get() == "" and passw.get() == "":
		messagebox.showerror("Login Failed!","Please enter User ID and Password.")
	elif usern.get() == "":
		messagebox.showerror("Login Failed!","Please enter User ID.")
	elif passw.get() == "":
		messagebox.showerror("Login Failed!","Please enter Password.")
	else:
		sql_query = "SELECT user_id FROM he_users"
		he_cursor.execute(sql_query)
		result = he_cursor.fetchall()
		for qur_res in result:
			if usern.get() == qur_res[0]:
				log_id_chk = True
				break
			else:
				log_id_chk = False
		if log_id_chk == False:
			sql_query = "SELECT email FROM he_users"
			he_cursor.execute(sql_query)
			result = he_cursor.fetchall()
			for qur_res in result:
				if usern.get() == qur_res[0]:
					log_em_chk = True
					break
				else:
					log_em_chk = False
		if log_id_chk == False and log_em_chk == False:
			reg_yesno = messagebox.askyesno("Login Failed!","User not registered. Would you like to register?")
			if reg_yesno == 1:
				register()
		elif log_id_chk:
			sql_query = "SELECT pass,approved FROM he_users WHERE user_id = '{}'".format(usern.get())
			he_cursor.execute(sql_query)
			result = he_cursor.fetchall()
			if passw.get() != result[0][0]:
				messagebox.showerror("Login Failed!","Password incorrect!")
			elif 'n' == result[0][1]:
				messagebox.showerror("Login Failed!","Registration not verified by admin. Please wait for sometime.")
			elif 'r' == result[0][1]:
				messagebox.showerror("Login Failed!","Please make necessary changes in registration as soon as possible in the next window or the registration will be rejected and deleted.")
				reg_edit = True
				logid = usern.get()
				register()
			else:
				messagebox.showinfo("Login Success","Login Successful. Please enjoy shopping with us.")
				logid = usern.get()
				user_home()
		else:
			sql_query = "SELECT pass,approved FROM he_users WHERE email = '{}'".format(usern.get())
			he_cursor.execute(sql_query)
			result = he_cursor.fetchall()
			if passw.get() != result[0][0]:
				messagebox.showerror("Login Failed!","Password incorrect!")
			elif 'n' == result[0][1]:
				messagebox.showerror("Login Failed!","Registration not verified by admin. Please wait for sometime.")
			elif 'r' == result[0][1]:
				messagebox.showerror("Login Failed!","Please make necessary changes in registration as soon as possible in the next window or the registration will be rejected and deleted.")
				reg_edit = True
				logid = usern.get()
				register()
			else:
				messagebox.showinfo("Login Success","Login Successful. Please enjoy shopping with us.")
				logid = usern.get()
				user_home()

def user_home():
	global mainscrn
	global userscrn
	mainscrn.destroy()
	userscrn = Tk()
	userscrn.title("Hacking Electronics Shop")
	userscrn.iconbitmap('images/icon.ico')
	but1 = Button(userscrn,text="Logout",command=user_logout)
	but1.pack()
	userscrn.mainloop()

def user_logout():
	logid = ''
	userscrn.destroy()
	mainpage()

#Check if db and tables are present and continue
try:
	he_db = sql.connect(host="localhost",user="root",passwd=sql_pass,database="hack_ele")
	he_cursor = he_db.cursor(buffered=True)
except:
	messagebox.showerror("Application failed","Application failed to load. Error Code: no_db")
else:
	sql_query = "SHOW TABLES"
	he_cursor.execute(sql_query)
	query_result = he_cursor.fetchall()
	for qur in query_result:
		if qur[0] == "he_users":
			noprob1 = True
			break
		else:
			noprob1 = False
	for qur in query_result:
		if qur[0] == "he_products":
			noprob2 = True
			break
		else:
			noprob2 = False
	for qur in query_result:
		if qur[0] == "he_orders":
			noprob3 = True
			break
		else:
			noprob3 = False
	if noprob1 and noprob2 and noprob3:
		#Main window:
		mainpage()
	else:
		messagebox.showerror("Application failed","Application failed to load. Error Code: no_tbl")
import mysql.connector as sql
import tkinter.ttk as ttk
import smtplib
import atexit
import os
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from email.message import EmailMessage

#Environment variables
email_user = os.environ.get('mailus')
email_pass = os.environ.get('mailpa')
sql_pass = os.environ.get('mysqlpa')

online = True # Set this to True for using app online or False for offline

#defining functions
def onExit():
    he_db.close()

def mainpage():
	global mainscrn
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	width = 640
	height = 360
	screen_width = mainscrn.winfo_screenwidth()
	screen_height = mainscrn.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2) - (height/12)
	mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
	mainscrn.resizable(0, 0)
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')

	frm1 = LabelFrame(mainscrn,text="Please login/register to continue.")
	lbl1 = Label(mainscrn,text="Welcome to Hacking Electronics Workshop",font=("Arial Bold",10))
	lbl2 = Label(mainscrn,text="OR")
	lbl3 = Label(frm1,text="UserID/Email:")
	lbl4 = Label(frm1,text="Password:")
	but1 = Button(mainscrn,text="Login",command=lambda:login(usern.get(),passw.get()))
	but2 = Button(mainscrn,text="Register",command=lambda:register(False,""))
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

def register(reg_edit,username):
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	width = 382
	height = 320
	screen_width = mainscrn.winfo_screenwidth()
	screen_height = mainscrn.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2) - (height/12)
	mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
	mainscrn.resizable(0, 0)
	mainscrn.title("Register to Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	mainscrn.grab_set()
	mainscrn.focus()
	
	frm2 = LabelFrame(mainscrn)
	lbl7 = Label(mainscrn,text="Please enter your details",font=("Arial Bold",10))
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
		sql_query = "SELECT * FROM he_users WHERE user_id = '{}'".format(username)
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

	but5 = Button(mainscrn,text="Clear",command=reg_clr)
	but6 = Button(mainscrn,text="Cancel",command=reg_can)
	but7 = Button(mainscrn,text="Register",command=lambda:reg_add(reg_edit,username))
	but5.grid(row=2,column=0)
	but6.grid(row=2,column=1)
	but7.grid(row=2,column=2)

	mainscrn.mainloop()

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
	mainscrn.destroy()
	mainpage()

def reg_add(reg_edit,username):
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
								sql_query = "DELETE FROM he_users where user_id = '{}'".format(username)
								he_cursor.execute(sql_query)
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
							#send_email(msg)
							messagebox.showinfo("Registration Complete","Registration Successful. Please activate account by replying to email sent to your email address and wait for admin approval.")
							mainscrn.destroy()
							mainpage()
				else:
					messagebox.showerror("Registration Failed!","Email is invalid. Please correct the email address.")

def send_email(msg):
	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(email_user,email_pass)
		smtp.send_message(msg)

def login(username,password):
	global mainscrn
	if username == "" and password == "":
		messagebox.showerror("Login Failed!","Please enter User ID and Password.")
	elif username == "":
		messagebox.showerror("Login Failed!","Please enter User ID.")
	elif password == "":
		messagebox.showerror("Login Failed!","Please enter Password.")
	else:
		sql_query = "SELECT user_id FROM he_users"
		he_cursor.execute(sql_query)
		result = he_cursor.fetchall()
		if len(result) == 0:
			messagebox.showerror("Login Failed","No user registered yet.")
			return
		for qur_res in result:
			if username == qur_res[0]:
				log_id_chk = True
				break
			else:
				log_id_chk = False
		if log_id_chk == False:
			sql_query = "SELECT email FROM he_users"
			he_cursor.execute(sql_query)
			result = he_cursor.fetchall()
			for qur_res in result:
				if username == qur_res[0]:
					log_em_chk = True
					break
				else:
					log_em_chk = False
		if log_id_chk == False and log_em_chk == False:
			reg_yesno = messagebox.askyesno("Login Failed!","User not registered. Would you like to register?")
			if reg_yesno == 1:
				register(False,"")
		elif log_id_chk:
			sql_query = "SELECT pass,approved FROM he_users WHERE user_id = '{}'".format(username)
			he_cursor.execute(sql_query)
			result = he_cursor.fetchall()
			if password != result[0][0]:
				messagebox.showerror("Login Failed!","Password incorrect!")
			elif 'n' == result[0][1]:
				messagebox.showerror("Login Failed!","Registration not verified by admin. Please wait for sometime.")
			elif 'r' == result[0][1]:
				messagebox.showerror("Login Failed!","Please make necessary changes in registration as soon as possible in the next window or the registration will be rejected and deleted.")
				register(True,username)
			else:
				messagebox.showinfo("Login Success","Login Successful. Please enjoy shopping with us.")
				user_qur("Top Deals",username)
		else:
			sql_query = "SELECT pass,approved FROM he_users WHERE email = '{}'".format(username)
			he_cursor.execute(sql_query)
			result = he_cursor.fetchall()
			if password != result[0][0]:
				messagebox.showerror("Login Failed!","Password incorrect!")
			elif 'n' == result[0][1]:
				messagebox.showerror("Login Failed!","Registration not verified by admin. Please wait for sometime.")
			elif 'r' == result[0][1]:
				messagebox.showerror("Login Failed!","Please make necessary changes in registration as soon as possible in the next window or the registration will be rejected and deleted.")
				register(True,username)
			else:
				messagebox.showinfo("Login Success","Login Successful. Please enjoy shopping with us.")
				user_qur("Top Deals",username)

def user_qur(cate_chk,username):
	if cate_chk == "Top Deals":
		sql_query = "SELECT * FROM he_products ORDER BY prod_dis DESC"
	elif cate_chk == "New Arrivals":
		sql_query = "SELECT * FROM he_products ORDER BY doa DESC"
	else:
		sql_query = "SELECT * FROM he_products WHERE prod_categ = '{}' ORDER BY doa DESC".format(cate_chk)
	he_cursor.execute(sql_query)
	qur_list = he_cursor.fetchall()
	user_shop(cate_chk,username,qur_list)

def user_shop(cate_chk,username,qur_list):
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	mainscrn.configure(bg='#282923')
	width = 1120
	height = 680
	screen_width = mainscrn.winfo_screenwidth()
	screen_height = mainscrn.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2) - (height/18)
	mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
	mainscrn.resizable(0, 0)

	navfrm = LabelFrame(mainscrn,pady=8,background="#202020")
	if cate_chk == "Top Deals":
		nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=1,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Top Deals",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/best_deals.png"))
	else:
		nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),relief=FLAT,bg="#202020",fg="white").grid(row=1,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "New Arrivals":
		nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=2,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="New Arrivals",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/new_arr.png"))
	else:
		nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),relief=FLAT,bg="#202020",fg="white").grid(row=2,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Learning and Robotics":
		nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=3,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Learning and Robotics",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/lar.png"))
	else:
		nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),relief=FLAT,bg="#202020",fg="white").grid(row=3,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Drones and Parts":
		nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=4,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Drones and Parts",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/drone.png"))
	else:
		nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=4,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "E-Bikes and Parts":
		nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=5,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="E-Bikes and Parts",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/ebike.png"))
	else:
		nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=5,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "3D Printers and Parts":
		nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=6,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="3D Printers and Parts",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/3d.png"))
	else:
		nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=6,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Batteries":
		nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=7,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Batteries",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/bat.png"))
	else:
		nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),relief=FLAT,bg="#202020",fg="white").grid(row=7,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Motors, Drivers, Actuators":
		nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=8,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Motors, Drivers, Act...",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/mot_act.png"))
	else:
		nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),relief=FLAT,bg="#202020",fg="white").grid(row=8,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Development Boards":
		nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=9,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Development Boards",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/dev_board.png"))
	else:
		nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),relief=FLAT,bg="#202020",fg="white").grid(row=9,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Arduino":
		nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=10,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Arduino",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/ard.png"))
	else:
		nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),relief=FLAT,bg="#202020",fg="white").grid(row=10,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Raspberry Pi":
		nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=11,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Raspberry Pi",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/rpi.png"))
	else:
		nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),relief=FLAT,bg="#202020",fg="white").grid(row=11,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Sensors":
		nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=12,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Sensors",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/sen.png"))
	else:
		nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),relief=FLAT,bg="#202020",fg="white").grid(row=12,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "IoT and Wireless":
		nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=13,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="IoT and Wireless",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/iot.png"))
	else:
		nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),relief=FLAT,bg="#202020",fg="white").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Displays":
		nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=14,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Displays",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/dis.png"))
	else:
		nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="white").grid(row=14,column=0,padx=5,pady=0,sticky=W)

	if cate_chk == "Power Supply":
		nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=15,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Power Supply",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/ps.png"))
	else:
		nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="white").grid(row=15,column=0,padx=5,pady=0,sticky=W)

	if cate_chk == "Electronic Modules":
		nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=16,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Electronic Modules",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/e_mod.png"))
	else:
		nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="white").grid(row=16,column=0,padx=5,pady=0,sticky=W)

	if cate_chk == "Electronic Components":
		nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=17,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Electronic Components",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/e_com.png"))
	else:
		nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="white").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Wires and Cables":
		nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=18,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Wires and Cables",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/wire.png"))
	else:
		nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="white").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Instruments and Tools":
		nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=19,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Instruments and Tools",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/tools.png"))
	else:
		nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="white").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Mechanical Parts":
		nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),state=DISABLED,relief=FLAT,bg="#202020",fg="white").grid(row=20,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Mechanical Parts",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/mech.png"))
	else:
		nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	frm_tree = Frame(mainscrn,background="#909090")
	style = ttk.Style(frm_tree)
	style.theme_use("clam")
	style.configure("Treeview.Heading",background="#202020",fieldbackground="#202020",foreground="white",borderwidth=0)
	style.configure("Treeview",borderwidth=0,rowheight=56)
	scrollbary = Scrollbar(frm_tree,orient = VERTICAL)
	tree = ttk.Treeview(frm_tree,columns = ("PID","Product Name","Price","Discount","GST","Total","Availablity"),height = 9,selectmode = "extended",yscrollcommand = scrollbary.set)
	scrollbary.config(command = tree.yview)
	scrollbary.pack(side = RIGHT,fill = Y)
	tree.heading('#0',text = "Image",anchor = W)
	tree.heading('PID',text = 'PID',anchor = W)
	tree.heading('Product Name',text = 'Product Name',anchor = W)
	tree.heading('Price',text = 'Price',anchor = W)
	tree.heading('Discount',text = 'Discount',anchor = W)
	tree.heading('GST',text = 'GST',anchor = W)
	tree.heading('Total',text = 'Total',anchor = W)
	tree.heading('Availablity',text = 'Availablity',anchor = W)
	tree.column('#0',stretch = NO,minwidth = 10,width = 114)
	tree.column('#1',stretch = NO,minwidth = 10,width = 96)
	tree.column('#2',stretch = NO,minwidth = 10,width = 250)
	tree.column('#3',stretch = NO,minwidth = 10,width = 95)
	tree.column('#4',stretch = NO,minwidth = 10,width = 95)
	tree.column('#5',stretch = NO,minwidth = 10,width = 95)
	tree.column('#6',stretch = NO,minwidth = 10,width = 100)
	tree.column('#7',stretch = NO,minwidth = 10,width = 95)
	tree.pack()
	frm_tree.pack(pady=30,anchor=E,side=BOTTOM)

	if len(qur_list) != 0:
		imgs_prod = []
		for app_res in qur_list:
			imgs_prod.append(ImageTk.PhotoImage(Image.open(app_res[8])))
		a=0
		for app_res in qur_list:
			total = '₹'+str(round(app_res[3]*((app_res[4]+100)/100)*((app_res[5]+100)/100),2))
			img = ImageTk.PhotoImage(Image.open(app_res[8]))
			tree.insert('','end',image=imgs_prod[a],values=(app_res[0],app_res[1],'₹'+str(app_res[3]),str(app_res[4])+'%',str(app_res[5])+'%',total,app_res[6]))
			a+=1

	shartlb = Label(mainscrn,image=shopart,background="#909090")
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),bg="#202020",fg="white")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),bg="#202020",fg="white")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),bg="#202020",fg="white")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),bg="#202020",fg="white")
	sh_ent = Entry(mainscrn,bg="#202020",fg="white",width=30)
	sort_opt = StringVar()
	sort_opt.set("Discount")
	sh_ddon = OptionMenu(shartlb,sort_opt,"Relevance","Discount","Newest","Oldest","Price L to H","Price H to L","A to Z","Z to A")
	sh_ddon.config(bg="#202020",fg="white")
	sh_ddon["highlightthickness"]=0
	sh_ddon["menu"].config(bg="#202020")
	sh_ddon["menu"].config(fg="white")
	if cate_chk == "Top Deals" or cate_chk == "New Arrivals":
		stext = "Search the Store"
	else:
		stext = "Search " + cate_chk
	sh_ser = Button(mainscrn,text=stext,bg="#202020",fg="white",command=lambda:user_search(username,cate_chk,sh_ent.get(),sort_opt.get()))

	ad_crt = LabelFrame(mainscrn,background="#202020")
	ad_lb1 = Label(ad_crt,text="Select item, ",background="#202020",foreground="white").grid(row=0,column=0,padx=40)
	ad_des = Button(ad_crt,text="More Details",bg="#202020",fg="white").grid(row=0,column=1,padx=40,pady=2)
	ad_wli = Button(ad_crt,text="Add to Wishlist",bg="#202020",fg="white").grid(row=0,column=2,padx=50)
	ad_lb2 = Label(ad_crt,text="               --OR--                         Specify Quantity:  ",bg="#202020",fg="white").grid(row=0,column=3)
	ad_spn = Spinbox(ad_crt,from_=1,to=999,width=3,bg="#202020",fg="white",buttonbackground="#202020").grid(row=0,column=4)
	ad_crb = Button(ad_crt,text="Add to Cart",bg="#202020",fg="white").grid(row=0,column=5,padx=60)

	shartlb.place(x=-2,y=-2)
	navfrm.place(x=-2,y=118)
	sh_but1.place(x=819,y=10)
	sh_but2.place(x=900,y=10)
	sh_but3.place(x=975,y=10)
	sh_but4.place(x=1060,y=10)
	sh_ent.place(x=488,y=90)
	sh_ddon.place(x=755,y=86)
	sh_ser.place(x=865,y=86)
	ad_crt.place(x=158,y=648)
	mainscrn.mainloop()

def user_search(username,cate_chk,serkey,sort_by):
	if sort_by == "Relevance":
		if len(serkey) == 0:
			return
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT *,MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') as score FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY score DESC".format(serkey,serkey)
		else:
			sql_query = "SELECT *,MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') as score FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY score DESC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Discount":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			return
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			user_qur("Top Deals",username)
			return
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY prod_dis DESC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY prod_dis DESC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Newest":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY doa DESC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY doa DESC"
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY doa DESC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY doa DESC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Oldest":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY doa ASC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY doa ASC"
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY doa ASC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY doa ASC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Price L to H":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_price ASC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_price ASC"
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY prod_price ASC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY prod_price ASC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Price H to L":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_price DESC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_price DESC"
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY prod_price DESC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY prod_price DESC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "A to Z":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_name ASC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_name ASC"
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY prod_name ASC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY prod_name ASC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Z to A":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_name DESC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_name DESC"
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY prod_name DESC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY prod_name DESC".format(serkey,serkey,cate_chk)
	he_cursor.execute(sql_query)
	qur_list = he_cursor.fetchall()
	user_shop(cate_chk,username,qur_list)

def user_wl(username):
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	mainscrn.configure(bg='#282923')
	width = 1120
	height = 680
	screen_width = mainscrn.winfo_screenwidth()
	screen_height = mainscrn.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2) - (height/18)
	mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
	mainscrn.resizable(0, 0)

	navfrm = LabelFrame(mainscrn,pady=8,background="#202020")
	nav_lbl = Label(navfrm,text="My Wishlist",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
	nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),relief=FLAT,bg="#202020",fg="white").grid(row=1,column=0,padx=5,pady=0,sticky=W)
	nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),relief=FLAT,bg="#202020",fg="white").grid(row=2,column=0,padx=5,pady=0,sticky=W)
	nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),relief=FLAT,bg="#202020",fg="white").grid(row=3,column=0,padx=5,pady=0,sticky=W)
	nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=4,column=0,padx=5,pady=0,sticky=W)
	nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=5,column=0,padx=5,pady=0,sticky=W)
	nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=6,column=0,padx=5,pady=0,sticky=W)
	nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),relief=FLAT,bg="#202020",fg="white").grid(row=7,column=0,padx=5,pady=0,sticky=W)
	nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),relief=FLAT,bg="#202020",fg="white").grid(row=8,column=0,padx=5,pady=0,sticky=W)
	nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),relief=FLAT,bg="#202020",fg="white").grid(row=9,column=0,padx=5,pady=0,sticky=W)
	nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),relief=FLAT,bg="#202020",fg="white").grid(row=10,column=0,padx=5,pady=0,sticky=W)
	nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),relief=FLAT,bg="#202020",fg="white").grid(row=11,column=0,padx=5,pady=0,sticky=W)
	nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),relief=FLAT,bg="#202020",fg="white").grid(row=12,column=0,padx=5,pady=0,sticky=W)
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless"),relief=FLAT,bg="#202020",fg="white").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="white").grid(row=14,column=0,padx=5,pady=0,sticky=W)
	nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="white").grid(row=15,column=0,padx=5,pady=0,sticky=W)
	nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="white").grid(row=16,column=0,padx=5,pady=0,sticky=W)
	nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="white").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="white").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="white").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	shopart = ImageTk.PhotoImage(Image.open("images/shop_art/my_wl.png"))
	shartlb = Label(mainscrn,image=shopart,background="#909090")
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),state=DISABLED,bg="#202020",fg="white")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),bg="#202020",fg="white")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),bg="#202020",fg="white")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),bg="#202020",fg="white")

	ad_crt = LabelFrame(mainscrn,background="#202020")
	ad_lb1 = Label(ad_crt,text="Select item, ",background="#202020",foreground="white").grid(row=0,column=0,padx=40)
	ad_des = Button(ad_crt,text="More Details",bg="#202020",fg="white").grid(row=0,column=1,padx=40,pady=2)
	ad_wli = Button(ad_crt,text="Delete",bg="#202020",fg="white").grid(row=0,column=2,padx=70)
	ad_lb2 = Label(ad_crt,text="               --OR--                         Specify Quantity:  ",bg="#202020",fg="white").grid(row=0,column=3)
	ad_spn = Spinbox(ad_crt,from_=1,to=999,width=3,bg="#202020",fg="white",buttonbackground="#202020").grid(row=0,column=4)
	ad_crb = Button(ad_crt,text="Add to Cart",bg="#202020",fg="white").grid(row=0,column=5,padx=60)

	shartlb.place(x=-4,y=-4)
	navfrm.place(x=0,y=118)
	sh_but1.place(x=819,y=10)
	sh_but2.place(x=900,y=10)
	sh_but3.place(x=975,y=10)
	sh_but4.place(x=1060,y=10)
	ad_crt.place(x=160,y=648)
	mainscrn.mainloop()

def user_ord(username):
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	mainscrn.configure(bg='#282923')
	width = 1120
	height = 680
	screen_width = mainscrn.winfo_screenwidth()
	screen_height = mainscrn.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2) - (height/18)
	mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
	mainscrn.resizable(0, 0)

	navfrm = LabelFrame(mainscrn,pady=8,background="#202020")
	nav_lbl = Label(navfrm,text="My Orders",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
	nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),relief=FLAT,bg="#202020",fg="white").grid(row=1,column=0,padx=5,pady=0,sticky=W)
	nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),relief=FLAT,bg="#202020",fg="white").grid(row=2,column=0,padx=5,pady=0,sticky=W)
	nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),relief=FLAT,bg="#202020",fg="white").grid(row=3,column=0,padx=5,pady=0,sticky=W)
	nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=4,column=0,padx=5,pady=0,sticky=W)
	nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=5,column=0,padx=5,pady=0,sticky=W)
	nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=6,column=0,padx=5,pady=0,sticky=W)
	nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),relief=FLAT,bg="#202020",fg="white").grid(row=7,column=0,padx=5,pady=0,sticky=W)
	nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),relief=FLAT,bg="#202020",fg="white").grid(row=8,column=0,padx=5,pady=0,sticky=W)
	nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),relief=FLAT,bg="#202020",fg="white").grid(row=9,column=0,padx=5,pady=0,sticky=W)
	nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),relief=FLAT,bg="#202020",fg="white").grid(row=10,column=0,padx=5,pady=0,sticky=W)
	nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),relief=FLAT,bg="#202020",fg="white").grid(row=11,column=0,padx=5,pady=0,sticky=W)
	nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),relief=FLAT,bg="#202020",fg="white").grid(row=12,column=0,padx=5,pady=0,sticky=W)
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless"),relief=FLAT,bg="#202020",fg="white").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="white").grid(row=14,column=0,padx=5,pady=0,sticky=W)
	nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="white").grid(row=15,column=0,padx=5,pady=0,sticky=W)
	nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="white").grid(row=16,column=0,padx=5,pady=0,sticky=W)
	nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="white").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="white").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="white").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	shopart = ImageTk.PhotoImage(Image.open("images/shop_art/my_ord.png"))
	shartlb = Label(mainscrn,image=shopart,background="#909090")
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),bg="#202020",fg="white")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),state=DISABLED,bg="#202020",fg="white")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),bg="#202020",fg="white")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),bg="#202020",fg="white")

	ad_crt = LabelFrame(mainscrn,background="#202020")
	ad_lb1 = Label(ad_crt,text="Select item, ",background="#202020",foreground="white",padx=40).grid(row=0,column=0)
	ad_des = Button(ad_crt,text="More Details",bg="#202020",fg="white").grid(row=0,column=1,padx=40,pady=2)
	ad_wli = Button(ad_crt,text="Add to Wishlist",bg="#202020",fg="white").grid(row=0,column=2,padx=50)
	ad_lb2 = Label(ad_crt,text="               --OR--                         Specify Quantity:  ",bg="#202020",fg="white").grid(row=0,column=3)
	ad_spn = Spinbox(ad_crt,from_=1,to=999,width=3,bg="#202020",fg="white",buttonbackground="#202020").grid(row=0,column=4)
	ad_crb = Button(ad_crt,text="Add to Cart",bg="#202020",fg="white").grid(row=0,column=5,padx=60)

	shartlb.place(x=-2,y=-2)
	navfrm.place(x=0,y=119)
	sh_but1.place(x=819,y=10)
	sh_but2.place(x=900,y=10)
	sh_but3.place(x=975,y=10)
	sh_but4.place(x=1060,y=10)
	ad_crt.place(x=160,y=648)
	mainscrn.mainloop()

def user_acc(username):
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	mainscrn.configure(bg='#282923')
	width = 1120
	height = 680
	screen_width = mainscrn.winfo_screenwidth()
	screen_height = mainscrn.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2) - (height/18)
	mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
	mainscrn.resizable(0, 0)

	navfrm = LabelFrame(mainscrn,pady=8,background="#202020")
	nav_lbl = Label(navfrm,text="My Account",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
	nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),relief=FLAT,bg="#202020",fg="white").grid(row=1,column=0,padx=5,pady=0,sticky=W)
	nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),relief=FLAT,bg="#202020",fg="white").grid(row=2,column=0,padx=5,pady=0,sticky=W)
	nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),relief=FLAT,bg="#202020",fg="white").grid(row=3,column=0,padx=5,pady=0,sticky=W)
	nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=4,column=0,padx=5,pady=0,sticky=W)
	nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=5,column=0,padx=5,pady=0,sticky=W)
	nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=6,column=0,padx=5,pady=0,sticky=W)
	nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),relief=FLAT,bg="#202020",fg="white").grid(row=7,column=0,padx=5,pady=0,sticky=W)
	nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),relief=FLAT,bg="#202020",fg="white").grid(row=8,column=0,padx=5,pady=0,sticky=W)
	nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),relief=FLAT,bg="#202020",fg="white").grid(row=9,column=0,padx=5,pady=0,sticky=W)
	nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),relief=FLAT,bg="#202020",fg="white").grid(row=10,column=0,padx=5,pady=0,sticky=W)
	nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),relief=FLAT,bg="#202020",fg="white").grid(row=11,column=0,padx=5,pady=0,sticky=W)
	nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),relief=FLAT,bg="#202020",fg="white").grid(row=12,column=0,padx=5,pady=0,sticky=W)
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless"),relief=FLAT,bg="#202020",fg="white").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="white").grid(row=14,column=0,padx=5,pady=0,sticky=W)
	nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="white").grid(row=15,column=0,padx=5,pady=0,sticky=W)
	nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="white").grid(row=16,column=0,padx=5,pady=0,sticky=W)
	nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="white").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="white").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="white").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	shopart = ImageTk.PhotoImage(Image.open("images/shop_art/my_acc.png"))
	shartlb = Label(mainscrn,image=shopart,background="#909090")
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),bg="#202020",fg="white")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),bg="#202020",fg="white")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),state=DISABLED,bg="#202020",fg="white")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),bg="#202020",fg="white")

	shartlb.place(x=-2,y=-2)
	navfrm.place(x=0,y=119)
	sh_but1.place(x=819,y=10)
	sh_but2.place(x=900,y=10)
	sh_but3.place(x=975,y=10)
	sh_but4.place(x=1060,y=10)
	mainscrn.mainloop()

def user_cart(username):
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	mainscrn.configure(bg='#282923')
	width = 1120
	height = 680
	screen_width = mainscrn.winfo_screenwidth()
	screen_height = mainscrn.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2) - (height/18)
	mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
	mainscrn.resizable(0, 0)

	navfrm = LabelFrame(mainscrn,pady=8,background="#202020")
	nav_lbl = Label(navfrm,text="Mechanical Parts",font=("Arial Bold",10),background="#202020",foreground="white").grid(row=0,column=0,padx=4,pady=1,sticky=W)
	nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),relief=FLAT,bg="#202020",fg="white").grid(row=1,column=0,padx=5,pady=0,sticky=W)
	nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),relief=FLAT,bg="#202020",fg="white").grid(row=2,column=0,padx=5,pady=0,sticky=W)
	nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),relief=FLAT,bg="#202020",fg="white").grid(row=3,column=0,padx=5,pady=0,sticky=W)
	nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=4,column=0,padx=5,pady=0,sticky=W)
	nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=5,column=0,padx=5,pady=0,sticky=W)
	nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=6,column=0,padx=5,pady=0,sticky=W)
	nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),relief=FLAT,bg="#202020",fg="white").grid(row=7,column=0,padx=5,pady=0,sticky=W)
	nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),relief=FLAT,bg="#202020",fg="white").grid(row=8,column=0,padx=5,pady=0,sticky=W)
	nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),relief=FLAT,bg="#202020",fg="white").grid(row=9,column=0,padx=5,pady=0,sticky=W)
	nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),relief=FLAT,bg="#202020",fg="white").grid(row=10,column=0,padx=5,pady=0,sticky=W)
	nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),relief=FLAT,bg="#202020",fg="white").grid(row=11,column=0,padx=5,pady=0,sticky=W)
	nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),relief=FLAT,bg="#202020",fg="white").grid(row=12,column=0,padx=5,pady=0,sticky=W)
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless"),relief=FLAT,bg="#202020",fg="white").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="white").grid(row=14,column=0,padx=5,pady=0,sticky=W)
	nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="white").grid(row=15,column=0,padx=5,pady=0,sticky=W)
	nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="white").grid(row=16,column=0,padx=5,pady=0,sticky=W)
	nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="white").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="white").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="white").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	shopart = ImageTk.PhotoImage(Image.open("images/shop_art/my_cart.png"))
	shartlb = Label(mainscrn,image=shopart,background="#909090")
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),bg="#202020",fg="white")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),bg="#202020",fg="white")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),bg="#202020",fg="white")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),state=DISABLED,bg="#202020",fg="white")

	ad_crt = LabelFrame(mainscrn,background="#202020")
	ad_lb1 = Label(ad_crt,text="Select item, ",background="#202020",foreground="white").grid(row=0,column=0,padx=60)
	ad_wli = Button(ad_crt,text="Delete",bg="#202020",fg="white").grid(row=0,column=1,padx=70,pady=2)
	ad_lb2 = Label(ad_crt,text="                  --OR--                                          Continue to ",bg="#202020",fg="white").grid(row=0,column=2,padx=20)
	ad_crb = Button(ad_crt,text="Checkout",bg="#202020",fg="white").grid(row=0,column=4,padx=100)

	shartlb.place(x=-2,y=-2)
	navfrm.place(x=0,y=118)
	sh_but1.place(x=819,y=10)
	sh_but2.place(x=900,y=10)
	sh_but3.place(x=975,y=10)
	sh_but4.place(x=1060,y=10)
	ad_crt.place(x=160,y=648)
	mainscrn.mainloop()

def user_logout():
	messagebox.showinfo("Logout successful","You have been logged out. Thank you for shopping with us. Come back soon!")
	logid = ''
	mainscrn.destroy()
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
		mainpage()
	else:
		messagebox.showerror("Application failed","Application failed to load. Error Code: no_tbl")
		
atexit.register(onExit)

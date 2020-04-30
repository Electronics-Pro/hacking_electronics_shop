import mysql.connector as sql
import tkinter.ttk as ttk
import webbrowser
import pdf_gen
import atexit
import time
import os
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from reportlab.pdfgen import canvas

mainscrn = Tk()
mainscrn.grab_set()
mainscrn.focus_force()
width = 420
height = 60
screen_width = mainscrn.winfo_screenwidth()
screen_height = mainscrn.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2) - (height/12)
mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
mainscrn.resizable(0, 0)
mainscrn.title("Hacking Electronics Shop")
mainscrn.iconbitmap('images/icon.ico')
lblprogress = Label(mainscrn,text="Loading Hacking Electronics Shop... Please Wait.",bg='white')
progress = ttk.Progressbar(mainscrn, orient = HORIZONTAL,length = 400, mode = 'determinate')
lblprogress.pack(pady=5)
progress.pack()
progress['value'] = 0
mainscrn.update_idletasks()

#Environment variables
sql_pass = os.environ.get('mysqlpa')

#Classes
class header:
	def __init__(self,CustomerName,CustomerContact):
		self.InvoiceNumber = time.time()
		self.CustomerName = CustomerName
		self.CustomerContact = CustomerContact
		timedate = time.asctime()
		self.date = timedate[4:8] + timedate[8:10] + ", " + timedate[20:24] + "."
		self.time = " " + timedate[11:20]

class product:
	def __init__(self,name,quantity,rate,tax,discount):
		self.name = name
		self.quantity = quantity
		self.rate = rate
		self.tax = tax
		self.total = (quantity * rate) - discount
		self.discount = discount

#defining functions
def onExit():
	try:
		he_db.close()
	except:
		pass

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
	add_prob = False
	if len(userr.get()) == 0 or len(userr.get()) > 255:
		messagebox.showerror("Registration Failed!","Username not entered or is longer than 255 characters.")
		add_prob = True
	if len(emair.get()) == 0 or len(emair.get()) > 255:
		messagebox.showerror("Registration Failed!","Email not entered or is longer than 255 characters.")
		add_prob = True
	if len(passr.get()) == 0 or len(passr.get()) > 255:
		messagebox.showerror("Registration Failed!","Password not entered or is longer than 255 characters.")
		add_prob = True
	if len(agair.get()) == 0 or len(agair.get()) > 255:
		messagebox.showerror("Registration Failed!","Password again not entered.")
		add_prob = True
	if len(fnamr.get()) == 0 or len(fnamr.get()) > 255:
		messagebox.showerror("Registration Failed!","First Name not entered or is longer than 255 characters.")
		add_prob = True
	if len(lnamr.get()) == 0 or len(lnamr.get()) > 255:
		messagebox.showerror("Registration Failed!","Last Name not entered or is longer than 255 characters.")
		add_prob = True
	if len(mobir.get()) == 0:
		messagebox.showerror("Registration Failed!","Mobile Number not entered.")
		add_prob = True
	if len(add1r.get()) == 0 or len(add1r.get()) > 255:
		messagebox.showerror("Registration Failed!","Address 1 not entered or is longer than 255 characters.")
		add_prob = True
	if len(add2r.get()) == 0 or len(add2r.get()) > 255:
		messagebox.showerror("Registration Failed!","Address 2 not entered or is longer than 255 characters.")
		add_prob = True
	if len(pincr.get()) == 0:
		messagebox.showerror("Registration Failed!","Pincode not entered.")
		add_prob = True
	if len(cityr.get()) == 0 or len(cityr.get()) > 255:
		messagebox.showerror("Registration Failed!","City not entered or is longer than 255 characters.")
		add_prob = True
	if state.get() == "Select State":
		messagebox.showerror("Registration Failed!","Please enter your State.")
		add_prob = True

	if add_prob:
		return
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
							messagebox.showerror("Registration Failed!","Mobile Number/Pincode is not a Number.")
						else:
							if reg_edit:
								sql_query = "DELETE FROM he_users where user_id = '{}'".format(username)
								he_cursor.execute(sql_query)
							sql_query = "INSERT INTO he_users (user_id, email, pass, f_name, l_name, mob, add1, add2, city, state, pin, doj) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',NOW())".format(userr.get(),emair.get(),passr.get(),fnamr.get(),lnamr.get(),mobir.get(),add1r.get(),add2r.get(),cityr.get(),state.get(),pincr.get())
							he_cursor.execute(sql_query)
							he_db.commit()
							messagebox.showinfo("Registration Complete!","Registration Successful. Please activate account by replying to email sent to your email address and wait for admin approval.")
							mainscrn.destroy()
							mainpage()
				else:
					messagebox.showerror("Registration Failed!","Email is invalid. Please correct the email address.")

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
				messagebox.showinfo("Login Success!","Login Successful. Please enjoy shopping with us.")
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
				messagebox.showinfo("Login Success!","Login Successful. Please enjoy shopping with us.")
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
	mainscrn.configure(bg='#202020')
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
	style.configure("Treeview.Heading",background="#202020",foreground="white",borderwidth=0)
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
			price = '₹'+str(app_res[3])
			total = '₹'+str(round(app_res[3]*((100-app_res[4])/100)*((app_res[5]+100)/100),2))
			tree.insert('','end',image=imgs_prod[a],values=(app_res[0],app_res[1],price,str(app_res[4])+'%',str(app_res[5])+'%',total,app_res[6]))
			a+=1

	shartlb = Label(mainscrn,image=shopart,background="#909090")
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),bg="#202020",fg="white")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),bg="#202020",fg="white")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),bg="#202020",fg="white")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),bg="#202020",fg="white")
	sh_ent = Entry(mainscrn,bg="#202020",fg="white",width=30)
	sort_opt = StringVar()
	sort_opt.set("Relevance")
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
	ad_des = Button(ad_crt,text="More Details",bg="#202020",fg="white",command=lambda:user_proddet(tree)).grid(row=0,column=1,padx=40,pady=2)
	ad_wli = Button(ad_crt,text="Add to Wishlist",bg="#202020",fg="white",command=lambda:user_addwl(username,tree)).grid(row=0,column=2,padx=50)
	ad_lb2 = Label(ad_crt,text="               OR                           Specify Quantity:  ",bg="#202020",fg="white").grid(row=0,column=3)
	ad_spn = Spinbox(ad_crt,from_=1,to=999,width=3,bg="#202020",fg="white",buttonbackground="#202020")
	ad_crb = Button(ad_crt,text="Add to Cart",bg="#202020",fg="white",command=lambda:user_addcart(username,ad_spn.get(),tree))
	ad_spn.grid(row=0,column=4)
	ad_crb.grid(row=0,column=5,padx=60)

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
		elif len(serkey) == 0:
			sql_query = "SELECT * FROM he_products WHERE prod_categ = '{}' ORDER BY prod_dis DESC".format(cate_chk)
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY prod_dis DESC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY prod_dis DESC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Newest":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY doa DESC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY doa DESC"
		elif len(serkey) == 0:
			sql_query = "SELECT * FROM he_products WHERE prod_categ = '{}' ORDER BY doa DESC".format(cate_chk)
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY doa DESC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY doa DESC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Oldest":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY doa ASC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY doa ASC"
		elif len(serkey) == 0:
			sql_query = "SELECT * FROM he_products WHERE prod_categ = '{}' ORDER BY doa ASC".format(cate_chk)
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY doa ASC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY doa ASC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Price L to H":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_price ASC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_price ASC"
		elif len(serkey) == 0:
			sql_query = "SELECT * FROM he_products WHERE prod_categ = '{}' ORDER BY prod_price ASC".format(cate_chk)
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY prod_price ASC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY prod_price ASC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Price H to L":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_price DESC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_price DESC"
		elif len(serkey) == 0:
			sql_query = "SELECT * FROM he_products WHERE prod_categ = '{}' ORDER BY prod_price DESC".format(cate_chk)
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY prod_price DESC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY prod_price DESC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "A to Z":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_nm ASC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_nm ASC"
		elif len(serkey) == 0:
			sql_query = "SELECT * FROM he_products WHERE prod_categ = '{}' ORDER BY prod_nm ASC".format(cate_chk)
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY prod_nm ASC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY prod_nm ASC".format(serkey,serkey,cate_chk)
	
	elif sort_by == "Z to A":
		if len(serkey) == 0 and cate_chk == "Top Deals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_nm DESC"
		elif len(serkey) == 0 and cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products ORDER BY prod_nm DESC"
		elif len(serkey) == 0:
			sql_query = "SELECT * FROM he_products WHERE prod_categ = '{}' ORDER BY prod_nm DESC".format(cate_chk)
		elif cate_chk == "Top Deals" or cate_chk == "New Arrivals":
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 ORDER BY prod_nm DESC".format(serkey,serkey)
		else:
			sql_query = "SELECT * FROM he_products WHERE MATCH (prod_nm, prod_categ, prod_desc) AGAINST ('{}') > 0 && prod_categ = '{}' ORDER BY prod_nm DESC".format(serkey,serkey,cate_chk)
	he_cursor.execute(sql_query)
	qur_list = he_cursor.fetchall()
	user_shop(cate_chk,username,qur_list)

def user_proddet(tree):
	try:
		prod_id = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Show Product Failed!","Please select a order first.")
	else:
		proddet = Toplevel()
		proddet.grab_set()
		proddet.focus_force()
		proddet.title("Hacking Electronics Shop")
		proddet.iconbitmap('images/icon.ico')
		proddet.configure(bg='#282923')
		width = 810
		height = 680
		screen_width = proddet.winfo_screenwidth()
		screen_height = proddet.winfo_screenheight()
		x = (screen_width/2) - (width/2)
		y = (screen_height/2) - (height/2) - (height/18)
		proddet.geometry("%dx%d+%d+%d" % (width, height,x,y))
		proddet.resizable(0, 0)

		frame = Frame(proddet,width=800,height=680)
		frame.pack()
		canvas = Canvas(frame,width=800,height=680,bg="white")
		canvas.config(scrollregion=(-400,300,5000,5000))
		vbar = Scrollbar(frame,orient=VERTICAL)
		vbar.pack(side=RIGHT,fill=Y)
		vbar.config(command=canvas.yview)
		canvas.config(yscrollcommand=vbar.set)
		canvas.pack()

		sql_query = "SELECT prod_img1,prod_img2,prod_img3,prod_desc FROM he_products WHERE prod_id = {}".format(prod_id)
		he_cursor.execute(sql_query)
		qur_res = he_cursor.fetchall()
		img1 = ImageTk.PhotoImage(Image.open(qur_res[0][0]))
		img2 = ImageTk.PhotoImage(Image.open(qur_res[0][1]))
		img3 = ImageTk.PhotoImage(Image.open(qur_res[0][2]))
		prd_des = Label(canvas,text=qur_res[0][3])
		canvas.create_image(400,600,image=img1)
		canvas.create_image(400,1200,image=img2)
		canvas.create_image(400,1800,image=img3)
		canvas.create_window((400,2400),window=prd_des)

		proddet.mainloop()

def user_addwl(username,tree):
	try:
		prod_id = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Add to Wishlist Failed!","Please select a product first.")
	else:
		sql_query = "SELECT prod_id FROM {}_wl".format(username)
		he_cursor.execute(sql_query)
		res = he_cursor.fetchall()
		if len(res) == 0:
			sql_query = "INSERT INTO {}_wl(prod_id) VALUES({})".format(username,prod_id)
			he_cursor.execute(sql_query)
			he_db.commit()
			messagebox.showinfo("Add to Wishlist Success!","Product has been added to Wishlist.")
		else:
			for i in res:
				if i[0] == prod_id:
					chk = True
					break
				else:
					chk = False
			if chk:
				messagebox.showerror("Add to Wishlist Failed!","Product already exists in Wishlist.")
			else:
				sql_query = "INSERT INTO {}_wl(prod_id) VALUES({})".format(username,prod_id)
				he_cursor.execute(sql_query)
				he_db.commit()
				messagebox.showinfo("Add to Wishlist Success!","Product has been added to Wishlist.")

def user_delwl(username,tree):
	try:
		prod_id = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Remove from Wishlist Failed!","Please select a product first.")
	else:
		sql_query = "DELETE FROM {}_wl WHERE prod_id = {}".format(username,prod_id)
		he_cursor.execute(sql_query)
		he_db.commit()
		messagebox.showinfo("Remove from Wishlist Success!","Product has been removed from  Wishlist.")
		user_wl(username)

def user_addcart(username,prod_qty,tree):
	try:
		prod_id = tree.item(tree.focus())['values'][0]
		prod_lim = tree.item(tree.focus())['values'][6]
	except:
		messagebox.showerror("Add to Cart Failed!","Please select a product first.")
	else:
		try:
			int(prod_qty)
		except:
			messagebox.showerror("Update Cart Failed!","Please enter a valid number.")
		else:
			if int(prod_qty) > 0:
				if int(prod_qty) > prod_lim:
					messagebox.showerror("Add to Cart Failed!","You cannot exceed Quantity above Availablity.")
				else:
					sql_query = "SELECT prod_id,prod_qty FROM {}_cart".format(username)
					he_cursor.execute(sql_query)
					result = he_cursor.fetchall()
					if len(result) == 0:
						sql_query = "INSERT INTO {}_cart(prod_id,prod_qty) VALUES({},{})".format(username,prod_id,prod_qty)
						he_cursor.execute(sql_query)
						he_db.commit()
						messagebox.showinfo("Add to Cart Success!","Product has been added to your Cart.")
					else:
						for i in result:
							if prod_id == i[0]:
								exists_prod = True
								exists_qty = i[1]
								break
							else:
								exists_prod = False
						if exists_prod:
							if int(exists_qty) + int(prod_qty) > prod_lim:
								messagebox.showerror("Add to Cart Failed!","You cannot exceed Quantity above Availablity.")
							else:
								sql_query = "UPDATE {}_cart SET prod_qty = {} WHERE prod_id = {}".format(username,int(exists_qty) + int(prod_qty),prod_id)
								he_cursor.execute(sql_query)
								he_db.commit()
								messagebox.showinfo("Update Cart Success!","Your cart has been updated.")
						else:
							sql_query = "INSERT INTO {}_cart(prod_id,prod_qty) VALUES({},{})".format(username,prod_id,prod_qty)
							he_cursor.execute(sql_query)
							he_db.commit()
							messagebox.showinfo("Add to Cart Success!","Product has been added to your Cart.")
			else:
				messagebox.showerror("Update Cart Failed!","Please enter a number greater than 0.")					

def user_wl(username):
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	mainscrn.configure(bg='#202020')
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
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),relief=FLAT,bg="#202020",fg="white").grid(row=13,column=0,padx=5,pady=0,sticky=W)
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

	sql_query = "SELECT * FROM {}_wl,he_products WHERE {}_wl.prod_id = he_products.prod_id".format(username,username)
	he_cursor.execute(sql_query)
	qur_list = he_cursor.fetchall()

	frm_tree = Frame(mainscrn,background="#909090")
	style = ttk.Style(frm_tree)
	style.theme_use("clam")
	style.configure("Treeview.Heading",background="#202020",foreground="white",borderwidth=0)
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
	frm_tree.pack(pady=32,anchor=E,side=BOTTOM)
	
	if len(qur_list) != 0:
		imgs_prod = []
		for app_res in qur_list:
			imgs_prod.append(ImageTk.PhotoImage(Image.open(app_res[9])))
		a=0
		for app_res in qur_list:
			price = '₹'+str(app_res[4])
			total = '₹'+str(round(app_res[4]*((100-app_res[5])/100)*((app_res[6]+100)/100),2))
			tree.insert('','end',image=imgs_prod[a],values=(app_res[1],app_res[2],price,str(app_res[5])+'%',str(app_res[6])+'%',total,app_res[7]))
			a+=1

	ad_crt = LabelFrame(mainscrn,background="#202020")
	ad_lb1 = Label(ad_crt,text="Select item, ",background="#202020",foreground="white").grid(row=0,column=0,padx=40)
	ad_des = Button(ad_crt,text="More Details",bg="#202020",fg="white",command=lambda:user_proddet(tree)).grid(row=0,column=1,padx=40,pady=2)
	ad_wli = Button(ad_crt,text="Delete",bg="#202020",fg="white",command=lambda:user_delwl(username,tree)).grid(row=0,column=2,padx=70)
	ad_lb2 = Label(ad_crt,text="         OR                              Specify Quantity:  ",bg="#202020",fg="white").grid(row=0,column=3)
	ad_spn = Spinbox(ad_crt,from_=1,to=999,width=3,bg="#202020",fg="white",buttonbackground="#202020")
	ad_crb = Button(ad_crt,text="Add to Cart",bg="#202020",fg="white",command=lambda:user_addcart(username,ad_spn.get(),tree))
	ad_spn.grid(row=0,column=4)
	ad_crb.grid(row=0,column=5,padx=80)

	shartlb.place(x=-4,y=-4)
	navfrm.place(x=-2,y=118)
	sh_but1.place(x=819,y=10)
	sh_but2.place(x=900,y=10)
	sh_but3.place(x=975,y=10)
	sh_but4.place(x=1060,y=10)
	ad_crt.place(x=158,y=648)
	mainscrn.mainloop()

def user_ord(username):
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	mainscrn.configure(bg='#202020')
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
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),relief=FLAT,bg="#202020",fg="white").grid(row=13,column=0,padx=5,pady=0,sticky=W)
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

	sql_query = "SELECT * FROM he_orders WHERE user_id = '{}' ORDER BY doa DESC".format(username)
	he_cursor.execute(sql_query)
	qur_list = he_cursor.fetchall()

	frm_tree = Frame(mainscrn,background="#909090")
	style = ttk.Style(frm_tree)
	style.theme_use("clam")
	style.configure("Treeview.Heading",background="#202020",foreground="white",borderwidth=0)
	style.configure("Treeview",borderwidth=0,rowheight=56)
	scrollbary = Scrollbar(frm_tree,orient = VERTICAL)
	tree = ttk.Treeview(frm_tree,columns = ("Order No.","Order Total","Payment Mode","Transaction ID","Status","Shipping Speed","Tracking ID","Date of Order"),height = 9,selectmode = "extended",yscrollcommand = scrollbary.set)
	scrollbary.config(command = tree.yview)
	scrollbary.pack(side = RIGHT,fill = Y)
	tree.heading('#0',text = "",anchor = W)
	tree.heading('Order No.',text = 'Order No.',anchor = W)
	tree.heading('Order Total',text = 'Order Total',anchor = W)
	tree.heading('Payment Mode',text = 'Payment Mode',anchor = W)
	tree.heading('Transaction ID',text = 'Transaction ID',anchor = W)
	tree.heading('Status',text = 'Status',anchor = W)
	tree.heading('Shipping Speed',text = 'Shipping Speed',anchor = W)
	tree.heading('Tracking ID',text = 'Tracking ID',anchor = W)
	tree.heading('Date of Order',text = 'Date of Order',anchor = W)
	tree.column('#0',stretch = NO,minwidth = 10,width = 10)
	tree.column('#1',stretch = NO,minwidth = 10,width = 110)
	tree.column('#2',stretch = NO,minwidth = 10,width = 110)
	tree.column('#3',stretch = NO,minwidth = 10,width = 100)
	tree.column('#4',stretch = NO,minwidth = 10,width = 130)
	tree.column('#5',stretch = NO,minwidth = 10,width = 130)
	tree.column('#6',stretch = NO,minwidth = 10,width = 110)
	tree.column('#7',stretch = NO,minwidth = 10,width = 120)
	tree.column('#8',stretch = NO,minwidth = 10,width = 120)
	tree.pack()
	frm_tree.pack(pady=30,anchor=E,side=BOTTOM)

	if len(qur_list) != 0:
		for app_res in qur_list:
			price = '₹'+str(app_res[2])
			tree.insert('','end',values=(app_res[0],price,app_res[3],app_res[4],app_res[5],app_res[6],app_res[7],app_res[8]))

	ad_crt = LabelFrame(mainscrn,background="#202020")
	adl1 = Label(ad_crt,text="Select order, ",background="#202020",foreground="white").grid(row=0,column=0,padx=51)
	but1 = Button(ad_crt,text="Show Order",bg="#202020",fg="white",command=lambda:user_oprod(tree,username)).grid(row=0,column=1,padx=51,pady=2)
	but2 = Button(ad_crt,text="Cancel Order",bg="#202020",fg="white",command=lambda:user_canord(tree,username)).grid(row=0,column=3,padx=51)
	but3 = Button(ad_crt,text="Change Transaction ID",bg="#202020",fg="white",command=lambda:user_chgtxn(tree,username)).grid(row=0,column=5,padx=51)
	but4 = Button(ad_crt,text="Generate Invoice",bg="#202020",fg="white",command=lambda:user_geninv(tree)).grid(row=0,column=7,padx=51)

	shartlb.place(x=-2,y=-2)
	navfrm.place(x=-2,y=119)
	sh_but1.place(x=819,y=10)
	sh_but2.place(x=900,y=10)
	sh_but3.place(x=975,y=10)
	sh_but4.place(x=1060,y=10)
	ad_crt.place(x=158,y=648)
	mainscrn.mainloop()

def user_oprod(tree,username):
	global mainscrn
	try:
		ord_id = tree.item(tree.focus())['values'][0]
		sql_query = "SELECT * FROM he_{},he_products WHERE he_{}.prod_id = he_products.prod_id".format(ord_id,ord_id)
		he_cursor.execute(sql_query)
		qur_list = he_cursor.fetchall()
	except:
		messagebox.showerror("Show Products Failed!","Please select a order first.")
	else:
		mainscrn.destroy()
		mainscrn = Tk()
		mainscrn.grab_set()
		mainscrn.focus_force()
		mainscrn.configure(bg='#202020')
		width = 960
		height = 570
		screen_width = mainscrn.winfo_screenwidth()
		screen_height = mainscrn.winfo_screenheight()
		x = (screen_width/2) - (width/2)
		y = (screen_height/2) - (height/2) - (height/12)
		mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
		mainscrn.resizable(0, 0)
		mainscrn.title("Hacking Electronics Shop")
		mainscrn.iconbitmap('images/icon.ico')

		frm1 = Frame(mainscrn)
		style = ttk.Style(frm1)
		style.theme_use("clam")
		style.configure("Treeview",borderwidth=0,rowheight=56)
		style.configure("Treeview.Heading",background="#202020",foreground="white",borderwidth=0)
		scrollbary = Scrollbar(frm1,orient = VERTICAL)
		tree = ttk.Treeview(frm1,columns = ("PID","Product Name","Price","Discount","GST","Quantity","Total"),height = 9,selectmode = "extended",yscrollcommand = scrollbary.set)
		scrollbary.config(command = tree.yview)
		scrollbary.pack(side = RIGHT,fill = Y)
		tree.heading('#0',text = "Image",anchor = W)
		tree.heading('PID',text = 'PID',anchor = W)
		tree.heading('Product Name',text = 'Product Name',anchor = W)
		tree.heading('Price',text = 'Price',anchor = W)
		tree.heading('Discount',text = 'Discount',anchor = W)
		tree.heading('GST',text = 'GST',anchor = W)
		tree.heading('Quantity',text = 'Quantity',anchor = W)
		tree.heading('Total',text = 'Total',anchor = W)
		tree.column('#0',stretch = NO,minwidth = 10,width = 116)
		tree.column('#1',stretch = NO,minwidth = 10,width = 94)
		tree.column('#2',stretch = NO,minwidth = 10,width = 250)
		tree.column('#3',stretch = NO,minwidth = 10,width = 95)
		tree.column('#4',stretch = NO,minwidth = 10,width = 95)
		tree.column('#5',stretch = NO,minwidth = 10,width = 95)
		tree.column('#6',stretch = NO,minwidth = 10,width = 95)
		tree.column('#7',stretch = NO,minwidth = 10,width = 100)
		tree.pack()
		frm1.pack()
		
		if len(qur_list) != 0:
			imgs_prod = []
			gtotal = 0
			for app_res in qur_list:
				imgs_prod.append(ImageTk.PhotoImage(Image.open(app_res[10])))
			a=0
			for app_res in qur_list:
				price = '₹'+str(app_res[5])
				total = '₹'+str(round(app_res[5]*((100-app_res[6])/100)*((app_res[7]+100)/100),2)*app_res[1])
				gtotal += float(round(app_res[5]*((100-app_res[6])/100)*((app_res[7]+100)/100),2)*app_res[1])
				tree.insert('','end',image=imgs_prod[a],values=(app_res[0],app_res[3],price,str(app_res[6])+'%',str(app_res[7])+'%',app_res[1],total))
				a+=1
		but1 = Button(mainscrn,text="Return",command=lambda:user_ord(username),bg="#202020",fg="white")
		frm1.pack()
		but1.pack(pady=5,ipadx=100)
		mainscrn.mainloop()

def user_canord(tree,username):
	try:
		ord_id = tree.item(tree.focus())['values'][0]
		status = tree.item(tree.focus())['values'][4]
	except:
		messagebox.showerror("Cancel Order Failed!","Please select a order first.")
	else:
		if status == "Order Shipped":
			messagebox.showerror("Cancel Order Failed!","Order has been shipped.")
		elif status == "Order Complete":
			messagebox.showerror("Cancel Order Failed!","Order has been completed.")
		elif status == "Order Cancelled":
			messagebox.showerror("Cancel Order Failed!","Order has alread been cancelled.")
		else:
			conf = messagebox.askokcancel("Cancel Order Confirmation","Are you sure you want to cancel the order?")
			if conf:
				sql_query = "UPDATE he_orders SET status = 'Order Cancelled' WHERE order_no = {}".format(ord_id)
				he_cursor.execute(sql_query)
				he_db.commit()
				messagebox.showinfo("Cancel Order Success!","Order has been cancelled.")
				user_ord(username)

def user_chgtxn(tree,username):
	global mainscrn
	try:
		ord_id = tree.item(tree.focus())['values'][0]
		status = tree.item(tree.focus())['values'][4]
	except:
		messagebox.showerror("Change Transaction ID Failed!","Please select a order first.")
	else:
		if status != "Payment Rejected":
			messagebox.showerror("Change Transaction ID Failed!","Status is not Payment Rejected.")
		else:
			mainscrn.destroy()
			mainscrn = Tk()
			mainscrn.grab_set()
			mainscrn.focus_force()
			mainscrn.title("Hacking Electronics Shop")
			mainscrn.iconbitmap('images/icon.ico')
			mainscrn.configure(bg='#202020')
			width = 350
			height = 115
			screen_width = mainscrn.winfo_screenwidth()
			screen_height = mainscrn.winfo_screenheight()
			x = (screen_width/2) - (width/2)
			y = (screen_height/2) - (height/2) - (height/18)
			mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
			mainscrn.resizable(0, 0)
			
			payvar = StringVar()
			payvar.set("Select Payment Mode")
			Label(mainscrn,text=" Please select payment mode: ",bg="#202020",fg="white").grid(row=1,column=0,sticky=W,pady=10)
			ddon = OptionMenu(mainscrn,payvar,"Paytm","Google Pay","IMPS")
			ddon.config(bg="#202020",fg="white")
			ddon["highlightthickness"]=0
			ddon["menu"].config(bg="#202020")
			ddon["menu"].config(fg="white")
			ddon.grid(row=1,column=1,sticky=W)
			Label(mainscrn,text=" Please enter Transaction Number: ",bg="#202020",fg="white").grid(row=2,column=0,sticky=W,pady=10)
			trne = Entry(mainscrn,width=18,bg="#202020",fg="white")
			trne.grid(row=2,column=1,sticky=W)
			Button(mainscrn,text="Return",command=lambda:user_ord(username),bg="#202020",fg="white").grid(row=3,column=1,ipadx=30,padx=35)
			Button(mainscrn,text="Continue",command=lambda:user_chgtxnn(username,ord_id,payvar.get(),trne.get()),bg="#202020",fg="white").grid(row=3,column=0,ipadx=30,padx=35)
			mainscrn.mainloop()

def user_chgtxnn(username,ord_id,payvar,trxnid):
	global mainscrn
	if payvar == "Select Payment Mode":
		messagebox.showerror("Change Transaction ID Failed!","Please select payment mode.")
	elif payvar == "Paytm" and len(trxnid) != 18:
		messagebox.showerror("Change Transaction ID Failed!","Invalid Transaction ID Length.")
	elif payvar == "Google Pay" and len(trxnid) != 12:
		messagebox.showerror("Change Transaction ID Failed!","Invalid Transaction ID Length.")
	elif payvar == "IMPS" and len(trxnid) != 12:
		messagebox.showerror("Change Transaction ID Failed!","Invalid Transaction ID Length.")
	else:
		sql_query = "UPDATE he_orders SET pay_mode = '{}',pay_id = '{}', status = 'Payment Processing' WHERE order_no = {}".format(payvar,trxnid,ord_id)
		he_cursor.execute(sql_query)
		he_db.commit()
		messagebox.showinfo("Change Transaction Number Success!","Order Transaction ID has been changed for Order number {}".format(ord_id))
		user_ord(username)

def user_geninv(tree):
	try:
		os.mkdir("C:\\InvoiceGenerator")
	except:
		pass
	try:
		ord_id = tree.item(tree.focus())['values'][0]
		status = tree.item(tree.focus())['values'][4]
		shipspd = tree.item(tree.focus())['values'][5]
	except:
		messagebox.showerror("Generate Invoice Failed!","Please select something first.")
	else:
		if status == "Payment Rejected":
			messagebox.showerror("Generate Invoice Failed!","You cannot generate invoice if your payment is rejected.")
		elif status == "Payment Processing":
			messagebox.showerror("Generate Invoice Failed!","You can generate invoice after payment approval.")
		elif status == "Order Cancelled":
			messagebox.showerror("Generate Invoice Failed!","You cannot generate invoice if order is cancelled.")
		else:
			Products = []
			sql_query = "SELECT user_id,g_total FROM he_orders WHERE order_no = {}".format(ord_id)
			he_cursor.execute(sql_query)
			ord_res = he_cursor.fetchall()
			uid = ord_res[0][0]
			if shipspd == "Low Priority":
				gtotal = float(ord_res[0][1])
				gtotal -= 100
			sql_query = "SELECT f_name,l_name,mob,email FROM he_users WHERE user_id = '{}'".format(uid)
			he_cursor.execute(sql_query)
			custlist = he_cursor.fetchall()
			CustomerName = str(custlist[0][0]) + str(custlist[0][1])		
			CustomerContact = str(custlist[0][2]) + "    Email: " + str(custlist[0][3])
			sql_query = "SELECT * FROM he_{},he_products WHERE he_{}.prod_id = he_products.prod_id".format(ord_id,ord_id)
			he_cursor.execute(sql_query)
			prod_res = he_cursor.fetchall()
			for i in prod_res:
				prod = str(i[0]) + ': ' + i[3]
				qty = i[1]
				rate = float(i[5])
				dis = float((qty*float(rate))*(float(i[6])/100))
				total = float(qty*rate-dis)
				tax = float(float(i[7])*0.01*total)
				Products.append((prod,qty,rate,dis,total,tax))
			if shipspd == "High Priority":
				Products.append(("High Priority Shipping Charges",1,423.73,0,500,76.27))
			else:
				if gtotal < 1000:
					Products.append(("Low Priority Shipping Charges",1,84.74,0.00,100.00,15.26))
				else:
					Products.append(("Low Priority Shipping Charges",1,84.74,84.74,0.00,0.00))
			head = header(CustomerName,CustomerContact)
			pdf = canvas.Canvas("C:\\InvoiceGenerator\\" + str(int(head.InvoiceNumber)) + ".pdf")
			pdf_gen.header(head,pdf)
			pdf_gen.middle(pdf)
			ycooridinate = 650
			x = 1
			for item in Products:
				currproduct = product(item[0],item[1],item[2],item[5],item[3])
				pdf.drawString(35,ycooridinate,str(x))
				x += 1
				pdf.setFont("Courier-Bold",9)
				ycooridinate = pdf_gen.additem(currproduct,pdf,ycooridinate)
			pdf.setFont("Courier-Bold",11)
			pdf_gen.footer(pdf,Products)
			pdf.save()
			webbrowser.open("C:\\InvoiceGenerator\\" + str(int(head.InvoiceNumber)) + ".pdf")

def user_acc(username):
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	mainscrn.configure(bg='#202020')
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
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),relief=FLAT,bg="#202020",fg="white").grid(row=13,column=0,padx=5,pady=0,sticky=W)
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

	Button(mainscrn,text="Logout",command=user_logout,bg="#202020",fg="white").place(x=990,y=150)

	shartlb.place(x=-2,y=-2)
	navfrm.place(x=-2,y=119)
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
	mainscrn.configure(bg='#202020')
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
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),relief=FLAT,bg="#202020",fg="white").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="white").grid(row=14,column=0,padx=5,pady=0,sticky=W)
	nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="white").grid(row=15,column=0,padx=5,pady=0,sticky=W)
	nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="white").grid(row=16,column=0,padx=5,pady=0,sticky=W)
	nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="white").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="white").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="white").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="white").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	sql_query = "SELECT * FROM {}_cart,he_products WHERE {}_cart.prod_id = he_products.prod_id".format(username,username)
	he_cursor.execute(sql_query)
	qur_list = he_cursor.fetchall()

	frm_tree = Frame(mainscrn,background="#909090")
	style = ttk.Style(frm_tree)
	style.theme_use("clam")
	style.configure("Treeview.Heading",background="#202020",foreground="white",borderwidth=0)
	style.configure("Treeview",borderwidth=0,rowheight=56)
	scrollbary = Scrollbar(frm_tree,orient = VERTICAL)
	tree = ttk.Treeview(frm_tree,columns = ("PID","Product Name","Price","Discount","GST","Quantity","Total"),height = 9,selectmode = "extended",yscrollcommand = scrollbary.set)
	scrollbary.config(command = tree.yview)
	scrollbary.pack(side = RIGHT,fill = Y)
	tree.heading('#0',text = "Image",anchor = W)
	tree.heading('PID',text = 'PID',anchor = W)
	tree.heading('Product Name',text = 'Product Name',anchor = W)
	tree.heading('Price',text = 'Price',anchor = W)
	tree.heading('Discount',text = 'Discount',anchor = W)
	tree.heading('GST',text = 'GST',anchor = W)
	tree.heading('Quantity',text = 'Quantity',anchor = W)
	tree.heading('Total',text = 'Total',anchor = W)
	tree.column('#0',stretch = NO,minwidth = 10,width = 114)
	tree.column('#1',stretch = NO,minwidth = 10,width = 96)
	tree.column('#2',stretch = NO,minwidth = 10,width = 250)
	tree.column('#3',stretch = NO,minwidth = 10,width = 95)
	tree.column('#4',stretch = NO,minwidth = 10,width = 95)
	tree.column('#5',stretch = NO,minwidth = 10,width = 95)
	tree.column('#6',stretch = NO,minwidth = 10,width = 95)
	tree.column('#7',stretch = NO,minwidth = 10,width = 100)
	tree.pack()
	frm_tree.pack(pady=30,anchor=E,side=BOTTOM)
	
	if len(qur_list) != 0:
		imgs_prod = []
		gtotal = 0
		for app_res in qur_list:
			imgs_prod.append(ImageTk.PhotoImage(Image.open(app_res[10])))
		a=0
		for app_res in qur_list:
			price = '₹'+str(app_res[5])
			total = '₹'+str(round(app_res[5]*((100-app_res[6])/100)*((app_res[7]+100)/100),2)*app_res[1])
			gtotal += float(round(app_res[5]*((100-app_res[6])/100)*((app_res[7]+100)/100),2)*app_res[1])
			tree.insert('','end',image=imgs_prod[a],values=(app_res[0],app_res[3],price,str(app_res[6])+'%',str(app_res[7])+'%',app_res[1],total))
			a+=1

	shopart = ImageTk.PhotoImage(Image.open("images/shop_art/my_cart.png"))
	shartlb = Label(mainscrn,image=shopart,background="#909090")
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),bg="#202020",fg="white")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),bg="#202020",fg="white")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),bg="#202020",fg="white")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),state=DISABLED,bg="#202020",fg="white")

	ad_crt = LabelFrame(mainscrn,background="#202020")
	ad_lb1 = Label(ad_crt,text="Select item, ",background="#202020",foreground="white").grid(row=0,column=0,padx=30)
	ad_des = Button(ad_crt,text="More Details",bg="#202020",fg="white",command=lambda:user_proddet(tree)).grid(row=0,column=1,padx=30,pady=2)
	ad_wli = Button(ad_crt,text="Delete",bg="#202020",fg="white",command=lambda:user_delcart(username,tree)).grid(row=0,column=2,padx=30)
	ad_lb2 = Label(ad_crt,text="             OR                  Change Quantity:  ",bg="#202020",fg="white").grid(row=0,column=3)
	ad_spn = Spinbox(ad_crt,from_=1,to=999,width=3,bg="#202020",fg="white",buttonbackground="#202020")
	ad_crb = Button(ad_crt,text="Update Cart",bg="#202020",fg="white",command=lambda:user_editcart(username,ad_spn.get(),tree))
	ad_chk = Button(ad_crt,text="Checkout",bg="#202020",fg="white",command=lambda:user_ship(username,gtotal,tree))
	ad_spn.grid(row=0,column=4)
	ad_crb.grid(row=0,column=5,padx=30)
	ad_lb3 = Label(ad_crt,text="OR",bg="#202020",fg="white").grid(row=0,column=6,padx=35)
	ad_chk.grid(row=0,column=7,padx=30)

	shartlb.place(x=-2,y=-2)
	navfrm.place(x=-2,y=118)
	sh_but1.place(x=819,y=10)
	sh_but2.place(x=900,y=10)
	sh_but3.place(x=975,y=10)
	sh_but4.place(x=1060,y=10)
	ad_crt.place(x=158,y=648)
	mainscrn.mainloop()

def user_delcart(username,tree):
	try:
		prod_id = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Delete Product Failed!","Please select a product first.")
	else:
		sql_query = "DELETE FROM {}_cart WHERE prod_id = {}".format(username,prod_id)
		he_cursor.execute(sql_query)
		he_db.commit()
		messagebox.showinfo("Remove from Cart Success!","Product has been removed from Cart.")
		user_cart(username)

def user_editcart(username,prod_qty,tree):
	try:
		prod_id = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Update Cart Failed!","Please select a product first.")
	else:
		try:
			int(prod_qty)
		except:
			messagebox.showerror("Update Cart Failed!","Please enter a valid number.")
		else:
			if int(prod_qty) > 0:
				sql_query = "SELECT prod_avail FROM he_products WHERE prod_id = {}".format(prod_id)
				he_cursor.execute(sql_query)
				result = he_cursor.fetchall()
				if result[0][0] < int(prod_qty):
					messagebox.showerror("Update Cart Failed!","You cannot exceed Quantity above Availablity.")
				else:
					sql_query = "UPDATE {}_cart SET prod_qty = {} WHERE prod_id = {}".format(username,prod_qty,prod_id)
					he_cursor.execute(sql_query)
					he_db.commit()
					messagebox.showinfo("Update Cart Success!","Quantity changed successfully.")
					user_cart(username)
			else:
				messagebox.showerror("Update Cart Failed!","Please enter a value greater than 0.")

def user_ship(username,gtotal,tree):
	conf = messagebox.askokcancel("Checkout","Are you sure you want to checkout?")
	if not conf:
		return
	else:
		conf = messagebox.askokcancel("Shipping Speed","Would you like express shipping(next day)(+500)? Normal shipping(less than 1000)(+100)")
		if conf:
			ntotal = int(gtotal) + 500
			shipspd = True
		elif not conf and gtotal < 1000:
			ntotal = int(gtotal) + 100
			shipspd = False
		else:
			ntotal = int(gtotal)
			shipspd = False
		user_checkout(username,ntotal,tree,shipspd)

def user_checkout(username,gtotal,tree,shipspd,item=""):
	tc = """First read the following Steps & T&C to purchase products from Hacking Electronics Shop (Updated T&C on 22/04/2020)

Bank Name: Any Bank Of India
Account Number: ############### (Hacking Electronics)
IFSC Code: ###########
Amount: ₹{}/-

1. Only IMPS, Google Pay & Paytm will be marked as valid transactions, any other payment methods will be invalid.
2. Please don't send payment in Bank Account number via Paytm or Google Pay.
3. Payment Time is 10AM to 8PM (GMT 5:30+) only. If you place order after 8PM (GMT 5:30+) then order
     will be approved/rejected by the next working day after 10AM (GMT 5:30+).
4. Enter your Transaction Number/Reference Number, Provided by Bank (RRN Number), Google Pay (UPI TrxID)
     or Paytm (Order ID) or your order will be rejected.
5. All items are covered with a standard warranty of 15 days from the time of delivery against manufacturing defects only.
     This warranty is given for the benefit of Hacking Electronics customers from any kind of manufacturing defects.
     Reimbursement or replacement will be done against manufacturing defects.
     If the product is subjected to misuse, tampering, static discharge, accident, water or fire damage,
     use of chemicals & soldered or altered in any way will void warranty.
6. Any query call our helpline (Between 10AM to 6PM Only) or email: alpro.sayandeep@gmail.com.
7. If you generate multiple fake requests your account will be permanently BANNED.
8. Check the checkbox to agree to the T&C and click Continue.""".format(gtotal)
	a = 0
	for i in tree.get_children(item):
		a += 1
	if a == 0:
		messagebox.showerror("Checkout Failed","Please checkout only with some items in cart.")
		return
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.configure(bg='#202020')
	mainscrn.title("Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	width = 654
	height = 380
	screen_width = mainscrn.winfo_screenwidth()
	screen_height = mainscrn.winfo_screenheight()
	x = (screen_width/2) - (width/2)
	y = (screen_height/2) - (height/2) - (height/18)
	mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
	mainscrn.resizable(0, 0)
	lbl = Label(mainscrn,text=tc,justify=LEFT,bg="#202020",fg="white")
	chkvar = IntVar()
	chkbx = Checkbutton(mainscrn,text="Yes, I agree to the Terms and Conditions and have made the Payment.",selectcolor="#202020",activebackground="#202020",activeforeground="white",bg="#202020",fg="white",variable=chkvar)
	okbut = Button(mainscrn,text="Continue",bg="#202020",fg="white",command=lambda:user_pay(username,gtotal,shipspd,chkvar.get()))
	cnbut = Button(mainscrn,text="Cancel",bg="#202020",fg="white",command=lambda:user_cart(username))
	lbl.grid(row=0,column=0,columnspan=2,padx=5)
	chkbx.grid(row=1,column=0,columnspan=2)
	okbut.grid(row=2,column=0,ipadx=30)
	cnbut.grid(row=2,column=1,ipadx=30)
	mainscrn.mainloop()

def user_pay(username,gtotal,shipspd,chkvar):
	global mainscrn
	if chkvar == 0:
		messagebox.showerror("Checkout Failed!","Please agree to the Terms and Conditions.")
		user_cart(username)
	else:
		mainscrn.destroy()
		mainscrn = Tk()
		mainscrn.grab_set()
		mainscrn.focus_force()
		mainscrn.title("Hacking Electronics Shop")
		mainscrn.iconbitmap('images/icon.ico')
		mainscrn.configure(bg='#202020')
		width = 390
		height = 170
		screen_width = mainscrn.winfo_screenwidth()
		screen_height = mainscrn.winfo_screenheight()
		x = (screen_width/2) - (width/2)
		y = (screen_height/2) - (height/2) - (height/18)
		mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
		mainscrn.resizable(0, 0)
		
		payvar = StringVar()
		payvar.set("Select Payment Mode")
		Label(mainscrn,text="Please make the payment with Paytm/Google Pay/IMPS\nwith details as on last page. And then enter the\nUPI Transaction ID/Paytm Order No. Below.",bg="#202020",fg="white",justify=LEFT).grid(row=0,column=0,columnspan=2,padx=40)
		Label(mainscrn,text=" Please select payment mode: ",bg="#202020",fg="white").grid(row=1,column=0,sticky=W,pady=10)
		ddon = OptionMenu(mainscrn,payvar,"Paytm","Google Pay","IMPS")
		ddon.grid(row=1,column=1,sticky=W)
		ddon.config(bg="#202020",fg="white")
		ddon["highlightthickness"]=0
		ddon["menu"].config(bg="#202020")
		ddon["menu"].config(fg="white")
		Label(mainscrn,text=" Please enter Transaction Number: ",bg="#202020",fg="white").grid(row=2,column=0,sticky=W,pady=10)
		trne = Entry(mainscrn,width=18,bg="#202020",fg="white")
		trne.grid(row=2,column=1,sticky=W)
		Button(mainscrn,text="Return",command=lambda:user_cart(username),bg="#202020",fg="white").grid(row=3,column=1,ipadx=30,padx=35)
		Button(mainscrn,text="Continue",command=lambda:user_paid(username,gtotal,shipspd,payvar.get(),trne.get()),bg="#202020",fg="white").grid(row=3,column=0,ipadx=30,padx=35)
		mainscrn.mainloop()

def user_paid(username,gtotal,shipspd,payvar,trxnid):
	if payvar == "Select Payment Mode":
		messagebox.showerror("Checkout Failed!","Please select payment mode.")
	elif payvar == "Paytm" and len(trxnid) != 18:
		messagebox.showerror("Checkout Failed!","Invalid Transaction ID Length.")
	elif payvar == "Google Pay" and len(trxnid) != 12:
		messagebox.showerror("Checkout Failed!","Invalid Transaction ID Length.")
	elif payvar == "IMPS" and len(trxnid) != 12:
		messagebox.showerror("Checkout Failed!","Invalid Transaction ID Length.")
	else:
		global mainscrn
		mainscrn.destroy()
		mainscrn = Tk()
		mainscrn.grab_set()
		mainscrn.focus_force()
		width = 420
		height = 60
		screen_width = mainscrn.winfo_screenwidth()
		screen_height = mainscrn.winfo_screenheight()
		x = (screen_width/2) - (width/2)
		y = (screen_height/2) - (height/2) - (height/12)
		mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
		mainscrn.resizable(0, 0)
		mainscrn.title("Hacking Electronics Shop")
		mainscrn.iconbitmap('images/icon.ico')
		lblprogress = Label(mainscrn,text="Placing Order... Please Wait.",bg='white')
		progress = ttk.Progressbar(mainscrn, orient = HORIZONTAL,length = 400, mode = 'determinate')
		lblprogress.pack(pady=5)
		progress.pack()
		progress['value'] = 0
		mainscrn.update_idletasks()
		sql_query = "SELECT COUNT(order_no) FROM he_orders"
		he_cursor.execute(sql_query)
		a = he_cursor.fetchall()
		autoinc = a[0][0] + 1000001
		if shipspd:
			sql_query = "INSERT INTO he_orders(user_id,g_total,pay_mode,pay_id,status,ship_spd,track_id,doa) VALUES('{}',{},'{}','{}','Payment Processing','High Priority','Not Shipped Yet',now())".format(username,gtotal,payvar,trxnid)
		else:
			sql_query = "INSERT INTO he_orders(user_id,g_total,pay_mode,pay_id,status,ship_spd,track_id,doa) VALUES('{}',{},'{}','{}','Payment Processing','Low Priority','Not Shipped Yet',now())".format(username,gtotal,payvar,trxnid)
		he_cursor.execute(sql_query)
		progress['value'] = 25
		mainscrn.update_idletasks()
		sql_query = "CREATE TABLE he_{}(prod_id int(10) PRIMARY KEY,prod_qty int(3) NOT NULL)".format(autoinc)
		he_cursor.execute(sql_query)
		progress['value'] = 50
		mainscrn.update_idletasks()
		sql_query = "SELECT * FROM {}_cart".format(username)
		he_cursor.execute(sql_query)
		qur_res = he_cursor.fetchall()
		for prod_qur in qur_res:
			sql_query = "INSERT INTO he_{} VALUES({},{})".format(autoinc,prod_qur[0],prod_qur[1])
			he_cursor.execute(sql_query)
		progress['value'] = 75
		mainscrn.update_idletasks()
		sql_query = "DELETE FROM {}_cart".format(username)
		he_cursor.execute(sql_query)
		he_db.commit()
		progress['value'] = 100
		mainscrn.update_idletasks()
		messagebox.showinfo("Order Success!","Order has been placed successfully. Order number {}".format(autoinc))
		user_ord(username)
	mainscrn.mainloop()

def user_logout():
	messagebox.showinfo("Logout successful!","You have been logged out. Thank you for shopping with us. Come back soon!")
	mainscrn.destroy()
	mainpage()

progress['value'] = 20
mainscrn.update_idletasks()

#Check if db and tables are present and continue
try:
	he_db = sql.connect(host="localhost",user="root",passwd=sql_pass,database="hack_ele")
	he_cursor = he_db.cursor(buffered=True)
except:
	messagebox.showerror("Application Failed!","Application failed to load. Error Code: no_db")
	mainscrn.destroy()
else:
	progress['value'] = 40
	mainscrn.update_idletasks()
	sql_query = "SHOW TABLES"
	he_cursor.execute(sql_query)
	query_result = he_cursor.fetchall()
	for qur in query_result:
		if qur[0] == "he_users":
			noprob1 = True
			break
		else:
			noprob1 = False
	progress['value'] = 60
	mainscrn.update_idletasks()
	for qur in query_result:
		if qur[0] == "he_products":
			noprob2 = True
			break
		else:
			noprob2 = False
	progress['value'] = 80
	mainscrn.update_idletasks()
	for qur in query_result:
		if qur[0] == "he_orders":
			noprob3 = True
			break
		else:
			noprob3 = False
	if noprob1 and noprob2 and noprob3:
		progress['value'] = 100
		mainscrn.update_idletasks()
		mainscrn.destroy()
		mainpage()
	else:
		messagebox.showerror("Application Failed","Application failed to load. Error Code: no_tbl")
		mainscrn.destroy()
		
atexit.register(onExit)
mainscrn.mainloop()

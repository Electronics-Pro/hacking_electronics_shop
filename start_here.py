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
lblprogress = Label(mainscrn,text="Loading Hacking Electronics Shop, Please Wait...",bg='#EEEEEE')
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
	mainscrn.configure(bg='#202020')

	frm1 = Frame(mainscrn,bg="#202020")
	lbl1 = Label(mainscrn,text="Welcome to Hacking Electronics Workshop",font=("Arial Bold",10),fg="#EEEEEE",bg="#202020")
	lbl2 = Label(frm1,text="Please login/register to continue:",fg="#EEEEEE",bg="#202020")
	lbl3 = Label(frm1,text="UserID/Email:",fg="#EEEEEE",bg="#202020")
	lbl4 = Label(frm1,text="Password:",fg="#EEEEEE",bg="#202020")
	but1 = Button(mainscrn,text="Login",fg="#EEEEEE",bg="#202020",command=lambda:login(usern.get(),passw.get()))
	but2 = Button(mainscrn,text="Register",fg="#EEEEEE",bg="#202020",command=lambda:register(False,""))
	but3 = Button(mainscrn,text="Forgot Password",fg="#EEEEEE",bg="#202020",command=lambda:pwdforgot(usern.get()))
	usern = Entry(frm1,width=35,fg="#EEEEEE",bg="#202020")
	passw = Entry(frm1,show='*',width=35,fg="#EEEEEE",bg="#202020")
	bg_topl = ImageTk.PhotoImage(Image.open("images/top_bg.jpg"))
	bg_botl = ImageTk.PhotoImage(Image.open("images/bottom_bg.jpg"))
	bg_leftl = ImageTk.PhotoImage(Image.open("images/left_bg.jpg"))
	bg_rightl = ImageTk.PhotoImage(Image.open("images/right_bg.jpg"))
	lbl5 = Label(image=bg_topl,fg="#EEEEEE",bg="#202020")
	lbl6 = Label(image=bg_botl,fg="#EEEEEE",bg="#202020")
	lbl7 = Label(image=bg_leftl,fg="#EEEEEE",bg="#202020")
	lbl8 = Label(image=bg_rightl,fg="#EEEEEE",bg="#202020")

	frm1.grid(row=2,column=1,columnspan=3)
	lbl1.grid(row=1,column=1,columnspan=3)
	lbl2.grid(row=0,column=0,columnspan=2,sticky=W)
	lbl3.grid(row=1,column=0,sticky=E)
	lbl4.grid(row=2,column=0,sticky=E)
	but1.grid(row=3,column=1)
	but2.grid(row=3,column=3)
	but3.grid(row=3,column=2)
	usern.grid(row=1,column=1)
	passw.grid(row=2,column=1)
	lbl5.grid(row=0,column=1,columnspan=3)
	lbl6.grid(row=4,column=1,columnspan=3)
	lbl7.grid(row=0,column=0,rowspan=5)
	lbl8.grid(row=0,column=4,rowspan=5)
	mainscrn.mainloop()

def pwdforgot(user):
	if len(user) == 0:
		messagebox.showerror("Password Request Failed!","Please enter username/email.")
	else:
		sql_query = "SELECT * FROM he_users WHERE user_id = '{}'".format(user)
		he_cursor.execute(sql_query)
		uinfo = he_cursor.fetchall()
		if len(uinfo) == 0:
			sql_query = "SELECT * FROM he_users WHERE email = '{}'".format(user)
			he_cursor.execute(sql_query)
			uinfo = he_cursor.fetchall()
			if len(uinfo) == 0:
				messagebox.showerror("Password Request Failed!","This account does not exist.")
			else:
				messagebox.showinfo("Password Request Success!","This feature is still under development.")
		else:
			messagebox.showinfo("Password Request Success!","This feature is still under development.")

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
	mainscrn.configure(bg='#202020')
	
	frm2 = Frame(mainscrn,bg="#202020")
	lbl7 = Label(mainscrn,text="Please enter your details",fg="#EEEEEE",bg="#202020",font=("Arial Bold",10))
	lbl8 = Label(frm2,text="User ID:",fg="#EEEEEE",bg="#202020")
	lbl9 = Label(frm2,text="Email Add.:",fg="#EEEEEE",bg="#202020")
	lbl10 = Label(frm2,text="Password:",fg="#EEEEEE",bg="#202020")
	lbl11 = Label(frm2,text="Retype:",fg="#EEEEEE",bg="#202020")
	lbl12 = Label(frm2,text="Firstname:",fg="#EEEEEE",bg="#202020")
	lbl13 = Label(frm2,text="Lastname:",fg="#EEEEEE",bg="#202020")
	lbl14 = Label(frm2,text="Mobile:",fg="#EEEEEE",bg="#202020")
	lbl15 = Label(frm2,text="Address:",fg="#EEEEEE",bg="#202020")
	lbl16 = Label(frm2,text="City:",fg="#EEEEEE",bg="#202020")
	lbl17 = Label(frm2,text="State:",fg="#EEEEEE",bg="#202020")
	lbl18 = Label(frm2,text="Pincode:",fg="#EEEEEE",bg="#202020")
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
	
	userr = Entry(frm2,width=50,fg="#EEEEEE",bg="#202020")
	emair = Entry(frm2,width=50,fg="#EEEEEE",bg="#202020")
	passr = Entry(frm2,show='*',width=50,fg="#EEEEEE",bg="#202020")
	agair = Entry(frm2,show='*',width=50,fg="#EEEEEE",bg="#202020")
	fnamr = Entry(frm2,width=50,fg="#EEEEEE",bg="#202020")
	lnamr = Entry(frm2,width=50,fg="#EEEEEE",bg="#202020")
	mobir = Entry(frm2,width=50,fg="#EEEEEE",bg="#202020")
	add1r = Entry(frm2,width=50,fg="#EEEEEE",bg="#202020")
	add2r = Entry(frm2,width=50,fg="#EEEEEE",bg="#202020")
	cityr = Entry(frm2,width=50,fg="#EEEEEE",bg="#202020")
	pincr = Entry(frm2,width=50,fg="#EEEEEE",bg="#202020")

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
	sttdw.config(bg="#202020",fg="#EEEEEE")
	sttdw["highlightthickness"]=0
	sttdw["menu"].config(bg="#202020")
	sttdw["menu"].config(fg="#EEEEEE")
	
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

	but5 = Button(mainscrn,text="Clear",fg="#EEEEEE",bg="#202020",command=reg_clr)
	but6 = Button(mainscrn,text="Cancel",fg="#EEEEEE",bg="#202020",command=reg_can)
	but7 = Button(mainscrn,text="Register",fg="#EEEEEE",bg="#202020",command=lambda:reg_add(reg_edit,username))
	but5.grid(row=2,column=0,pady=10)
	but6.grid(row=2,column=1,pady=10)
	but7.grid(row=2,column=2,pady=10)

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
	if len(userr.get()) == 0:
		messagebox.showerror("Registration Failed!","Username not entered.")
	elif len(userr.get()) > 255:
		messagebox.showerror("Registration Failed!","Username is longer than 255 characters.")
	elif len(emair.get()) == 0:
		messagebox.showerror("Registration Failed!","Email not entered.")
	elif len(emair.get()) > 255:
		messagebox.showerror("Registration Failed!","Email is longer than 255 characters.")
	elif len(passr.get()) == 0:
		messagebox.showerror("Registration Failed!","Password not entered.")
	elif len(passr.get()) > 255:
		messagebox.showerror("Registration Failed!","Password is longer than 255 characters.")
	elif len(fnamr.get()) == 0:
		messagebox.showerror("Registration Failed!","Firstname not entered.")
	elif len(fnamr.get()) > 255:
		messagebox.showerror("Registration Failed!","Firstname is longer than 255 characters.")
	elif len(lnamr.get()) == 0:
		messagebox.showerror("Registration Failed!","Lastname not entered.")
	elif len(lnamr.get()) > 255:
		messagebox.showerror("Registration Failed!","Lastname is longer than 255 characters.")
	elif len(mobir.get()) == 0:
		messagebox.showerror("Registration Failed!","Mobile Number not entered.")
	elif len(add1r.get()) == 0:
		messagebox.showerror("Registration Failed!","Address 1 not entered.")
	elif len(add1r.get()) > 255:
		messagebox.showerror("Registration Failed!","Address 1 is longer than 255 characters.")
	elif len(add2r.get()) == 0:
		messagebox.showerror("Registration Failed!","Address 2 not entered.")
	elif len(add2r.get()) > 255:
		messagebox.showerror("Registration Failed!","Address 2 is longer than 255 characters.")
	elif len(pincr.get()) == 0:
		messagebox.showerror("Registration Failed!","Pincode not entered.")
	elif len(cityr.get()) == 0:
		messagebox.showerror("Registration Failed!","City not entered.")
	elif len(cityr.get()) > 255:
		messagebox.showerror("Registration Failed!","City is longer than 255 characters.")
	elif state.get() == "Select State":
		messagebox.showerror("Registration Failed!","Please enter your State.")
	elif passr.get() != agair.get():
		messagebox.showerror("Registration Failed!","Passwords do not match.")
	elif len(pincr.get()) != 6:
		messagebox.showerror("Registration Failed!","Pincode is not of 6 digits.")
	elif len(mobir.get()) != 10:
		messagebox.showerror("Registration Failed!","Mobile number is not of 10 digits.")
	elif len(emair.get()) < 7:
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
		nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=1,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Top Deals",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/best_deals.png"))
	else:
		nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=1,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "New Arrivals":
		nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=2,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="New Arrivals",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/new_arr.png"))
	else:
		nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=2,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Learning and Robotics":
		nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=3,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Learning and Robotics",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/lar.png"))
	else:
		nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=3,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Drones and Parts":
		nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=4,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Drones and Parts",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/drone.png"))
	else:
		nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=4,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "E-Bikes and Parts":
		nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=5,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="E-Bikes and Parts",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/ebike.png"))
	else:
		nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=5,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "3D Printers and Parts":
		nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=6,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="3D Printers and Parts",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/3d.png"))
	else:
		nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=6,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Batteries":
		nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=7,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Batteries",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/bat.png"))
	else:
		nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=7,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Motors, Drivers, Actuators":
		nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=8,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Motors, Drivers, Act...",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/mot_act.png"))
	else:
		nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=8,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Development Boards":
		nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=9,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Development Boards",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/dev_board.png"))
	else:
		nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=9,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Arduino":
		nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=10,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Arduino",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/ard.png"))
	else:
		nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=10,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Raspberry Pi":
		nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=11,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Raspberry Pi",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/rpi.png"))
	else:
		nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=11,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Sensors":
		nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=12,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Sensors",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/sen.png"))
	else:
		nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=12,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "IoT and Wireless":
		nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=13,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="IoT and Wireless",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/iot.png"))
	else:
		nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Displays":
		nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=14,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Displays",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/dis.png"))
	else:
		nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=14,column=0,padx=5,pady=0,sticky=W)

	if cate_chk == "Power Supply":
		nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=15,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Power Supply",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/ps.png"))
	else:
		nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=15,column=0,padx=5,pady=0,sticky=W)

	if cate_chk == "Electronic Modules":
		nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=16,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Electronic Modules",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/e_mod.png"))
	else:
		nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=16,column=0,padx=5,pady=0,sticky=W)

	if cate_chk == "Electronic Components":
		nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=17,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Electronic Components",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/e_com.png"))
	else:
		nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Wires and Cables":
		nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=18,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Wires and Cables",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/wire.png"))
	else:
		nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Instruments and Tools":
		nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=19,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Instruments and Tools",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/tools.png"))
	else:
		nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	
	if cate_chk == "Mechanical Parts":
		nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),state=DISABLED,relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=20,column=0,padx=5,pady=0,sticky=W)
		nav_lbl = Label(navfrm,text="Mechanical Parts",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/mech.png"))
	else:
		nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	if cate_chk == "Search":
		shopart = ImageTk.PhotoImage(Image.open("images/shop_art/best_deals.png"))
		nav_lbl = Label(navfrm,text="Search Results",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)

	frm_tree = Frame(mainscrn,background="#909090")
	style = ttk.Style(frm_tree)
	style.theme_use("clam")
	style.configure("Treeview.Heading",background="#202020",foreground="#EEEEEE",borderwidth=0)
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
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),bg="#202020",fg="#EEEEEE")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),bg="#202020",fg="#EEEEEE")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),bg="#202020",fg="#EEEEEE")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),bg="#202020",fg="#EEEEEE")
	sh_ent = Entry(mainscrn,bg="#202020",fg="#EEEEEE",width=30)
	sort_opt = StringVar()
	sort_opt.set("Relevance")
	sh_ddon = OptionMenu(shartlb,sort_opt,"Relevance","Discount","Newest","Oldest","Price L to H","Price H to L","A to Z","Z to A")
	sh_ddon.config(bg="#202020",fg="#EEEEEE")
	sh_ddon["highlightthickness"]=0
	sh_ddon["menu"].config(bg="#202020")
	sh_ddon["menu"].config(fg="#EEEEEE")
	if cate_chk == "Top Deals" or cate_chk == "New Arrivals":
		stext = "Search the Store"
	else:
		stext = "Search " + cate_chk
	
	if cate_chk == "Search":
		sh_ser = Button(mainscrn,text=stext,bg="#202020",fg="#EEEEEE",command=lambda:user_search(username,cate_chk,sh_ent.get(),sort_opt.get()),state=DISABLED)
	else:
		sh_ser = Button(mainscrn,text=stext,bg="#202020",fg="#EEEEEE",command=lambda:user_search(username,cate_chk,sh_ent.get(),sort_opt.get()))

	ad_crt = LabelFrame(mainscrn,background="#202020")
	ad_lb1 = Label(ad_crt,text="Select item, ",background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=40)
	ad_des = Button(ad_crt,text="More Details",bg="#202020",fg="#EEEEEE",command=lambda:user_proddet(tree)).grid(row=0,column=1,padx=40,pady=2)
	ad_wli = Button(ad_crt,text="Add to Wishlist",bg="#202020",fg="#EEEEEE",command=lambda:user_addwl(username,tree)).grid(row=0,column=2,padx=50)
	ad_lb2 = Label(ad_crt,text="               OR                           Specify Quantity:  ",bg="#202020",fg="#EEEEEE").grid(row=0,column=3)
	ad_spn = Spinbox(ad_crt,from_=1,to=999,width=3,bg="#202020",fg="#EEEEEE",buttonbackground="#202020")
	ad_crb = Button(ad_crt,text="Add to Cart",bg="#202020",fg="#EEEEEE",command=lambda:user_addcart(username,ad_spn.get(),tree))
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
	user_shop("Search",username,qur_list)

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
		canvas = Canvas(frame,width=800,height=680,bg="#EEEEEE")
		canvas.config(scrollregion=(-400,300,2000,5000))
		vbar = Scrollbar(frame,orient=VERTICAL)
		vbar.pack(side=RIGHT,fill=Y)
		vbar.config(command=canvas.yview)
		hbar = Scrollbar(frame,orient=HORIZONTAL)
		hbar.pack(side=BOTTOM,fill=X)
		hbar.config(command=canvas.xview)
		canvas.config(yscrollcommand=vbar.set,xscrollcommand=hbar.set)
		canvas.pack()

		sql_query = "SELECT prod_img1,prod_img2,prod_img3,prod_desc FROM he_products WHERE prod_id = {}".format(prod_id)
		he_cursor.execute(sql_query)
		qur_res = he_cursor.fetchall()
		img1 = ImageTk.PhotoImage(Image.open(qur_res[0][0]))
		img2 = ImageTk.PhotoImage(Image.open(qur_res[0][1]))
		img3 = ImageTk.PhotoImage(Image.open(qur_res[0][2]))
		prd_des = Label(canvas,text=qur_res[0][3],justify=LEFT)
		canvas.create_image(400,600,image=img1)
		canvas.create_image(400,1200,image=img2)
		canvas.create_image(400,1800,image=img3)
		canvas.create_window((800,2400),window=prd_des)

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
	nav_lbl = Label(navfrm,text="My Wishlist",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
	nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=1,column=0,padx=5,pady=0,sticky=W)
	nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=2,column=0,padx=5,pady=0,sticky=W)
	nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=3,column=0,padx=5,pady=0,sticky=W)
	nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=4,column=0,padx=5,pady=0,sticky=W)
	nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=5,column=0,padx=5,pady=0,sticky=W)
	nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=6,column=0,padx=5,pady=0,sticky=W)
	nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=7,column=0,padx=5,pady=0,sticky=W)
	nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=8,column=0,padx=5,pady=0,sticky=W)
	nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=9,column=0,padx=5,pady=0,sticky=W)
	nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=10,column=0,padx=5,pady=0,sticky=W)
	nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=11,column=0,padx=5,pady=0,sticky=W)
	nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=12,column=0,padx=5,pady=0,sticky=W)
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=14,column=0,padx=5,pady=0,sticky=W)
	nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=15,column=0,padx=5,pady=0,sticky=W)
	nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=16,column=0,padx=5,pady=0,sticky=W)
	nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	shopart = ImageTk.PhotoImage(Image.open("images/shop_art/my_wl.png"))
	shartlb = Label(mainscrn,image=shopart,background="#909090")
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),state=DISABLED,bg="#202020",fg="#EEEEEE")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),bg="#202020",fg="#EEEEEE")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),bg="#202020",fg="#EEEEEE")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),bg="#202020",fg="#EEEEEE")

	sql_query = "SELECT * FROM {}_wl,he_products WHERE {}_wl.prod_id = he_products.prod_id".format(username,username)
	he_cursor.execute(sql_query)
	qur_list = he_cursor.fetchall()

	frm_tree = Frame(mainscrn,background="#909090")
	style = ttk.Style(frm_tree)
	style.theme_use("clam")
	style.configure("Treeview.Heading",background="#202020",foreground="#EEEEEE",borderwidth=0)
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
	ad_lb1 = Label(ad_crt,text="Select item, ",background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=40)
	ad_des = Button(ad_crt,text="More Details",bg="#202020",fg="#EEEEEE",command=lambda:user_proddet(tree)).grid(row=0,column=1,padx=40,pady=2)
	ad_wli = Button(ad_crt,text="Delete",bg="#202020",fg="#EEEEEE",command=lambda:user_delwl(username,tree)).grid(row=0,column=2,padx=70)
	ad_lb2 = Label(ad_crt,text="         OR                              Specify Quantity:  ",bg="#202020",fg="#EEEEEE").grid(row=0,column=3)
	ad_spn = Spinbox(ad_crt,from_=1,to=999,width=3,bg="#202020",fg="#EEEEEE",buttonbackground="#202020")
	ad_crb = Button(ad_crt,text="Add to Cart",bg="#202020",fg="#EEEEEE",command=lambda:user_addcart(username,ad_spn.get(),tree))
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
	nav_lbl = Label(navfrm,text="My Orders",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
	nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=1,column=0,padx=5,pady=0,sticky=W)
	nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=2,column=0,padx=5,pady=0,sticky=W)
	nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=3,column=0,padx=5,pady=0,sticky=W)
	nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=4,column=0,padx=5,pady=0,sticky=W)
	nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=5,column=0,padx=5,pady=0,sticky=W)
	nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=6,column=0,padx=5,pady=0,sticky=W)
	nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=7,column=0,padx=5,pady=0,sticky=W)
	nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=8,column=0,padx=5,pady=0,sticky=W)
	nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=9,column=0,padx=5,pady=0,sticky=W)
	nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=10,column=0,padx=5,pady=0,sticky=W)
	nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=11,column=0,padx=5,pady=0,sticky=W)
	nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=12,column=0,padx=5,pady=0,sticky=W)
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=14,column=0,padx=5,pady=0,sticky=W)
	nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=15,column=0,padx=5,pady=0,sticky=W)
	nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=16,column=0,padx=5,pady=0,sticky=W)
	nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	shopart = ImageTk.PhotoImage(Image.open("images/shop_art/my_ord.png"))
	shartlb = Label(mainscrn,image=shopart,background="#909090")
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),bg="#202020",fg="#EEEEEE")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),state=DISABLED,bg="#202020",fg="#EEEEEE")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),bg="#202020",fg="#EEEEEE")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),bg="#202020",fg="#EEEEEE")

	sql_query = "SELECT * FROM he_orders WHERE user_id = '{}' ORDER BY doa DESC".format(username)
	he_cursor.execute(sql_query)
	qur_list = he_cursor.fetchall()

	frm_tree = Frame(mainscrn,background="#909090")
	style = ttk.Style(frm_tree)
	style.theme_use("clam")
	style.configure("Treeview.Heading",background="#202020",foreground="#EEEEEE",borderwidth=0)
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
	adl1 = Label(ad_crt,text="Select order, ",background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=51)
	but1 = Button(ad_crt,text="Show Order",bg="#202020",fg="#EEEEEE",command=lambda:user_oprod(tree,username)).grid(row=0,column=1,padx=51,pady=2)
	but2 = Button(ad_crt,text="Cancel Order",bg="#202020",fg="#EEEEEE",command=lambda:user_canord(tree,username)).grid(row=0,column=3,padx=51)
	but3 = Button(ad_crt,text="Change Transaction ID",bg="#202020",fg="#EEEEEE",command=lambda:user_chgtxn(tree,username)).grid(row=0,column=5,padx=51)
	but4 = Button(ad_crt,text="Generate Invoice",bg="#202020",fg="#EEEEEE",command=lambda:user_geninv(tree,username)).grid(row=0,column=7,padx=51)

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
		style.configure("Treeview.Heading",background="#202020",foreground="#EEEEEE",borderwidth=0)
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
		but1 = Button(mainscrn,text="Return",command=lambda:user_ord(username),bg="#202020",fg="#EEEEEE")
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
			Label(mainscrn,text=" Please select payment mode: ",bg="#202020",fg="#EEEEEE").grid(row=1,column=0,sticky=W,pady=10)
			ddon = OptionMenu(mainscrn,payvar,"Paytm","Google Pay","IMPS")
			ddon.config(bg="#202020",fg="#EEEEEE")
			ddon["highlightthickness"]=0
			ddon["menu"].config(bg="#202020")
			ddon["menu"].config(fg="#EEEEEE")
			ddon.grid(row=1,column=1,sticky=W)
			Label(mainscrn,text=" Please enter Transaction Number: ",bg="#202020",fg="#EEEEEE").grid(row=2,column=0,sticky=W,pady=10)
			trne = Entry(mainscrn,width=18,bg="#202020",fg="#EEEEEE")
			trne.grid(row=2,column=1,sticky=W)
			Button(mainscrn,text="Return",command=lambda:user_ord(username),bg="#202020",fg="#EEEEEE").grid(row=3,column=1,ipadx=30,padx=35)
			Button(mainscrn,text="Continue",command=lambda:user_chgtxnn(username,ord_id,payvar.get(),trne.get()),bg="#202020",fg="#EEEEEE").grid(row=3,column=0,ipadx=30,padx=35)
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

def user_geninv(tree,username):
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
			lblprogress = Label(mainscrn,text="Generating Invoice... Please Wait.",bg='#EEEEEE')
			progress = ttk.Progressbar(mainscrn, orient = HORIZONTAL,length = 400, mode = 'determinate')
			lblprogress.pack(pady=5)
			progress.pack()
			progress['value'] = 0
			mainscrn.update_idletasks()
			Products = []
			sql_query = "SELECT user_id,g_total FROM he_orders WHERE order_no = {}".format(ord_id)
			he_cursor.execute(sql_query)
			ord_res = he_cursor.fetchall()
			uid = ord_res[0][0]
			progress['value'] = 14
			mainscrn.update_idletasks()
			if shipspd == "Low Priority":
				gtotal = float(ord_res[0][1])
				gtotal -= 100
			sql_query = "SELECT f_name,l_name,mob,email FROM he_users WHERE user_id = '{}'".format(uid)
			he_cursor.execute(sql_query)
			custlist = he_cursor.fetchall()
			CustomerName = str(custlist[0][0]) + str(custlist[0][1])		
			CustomerContact = str(custlist[0][2]) + "    Email: " + str(custlist[0][3])
			progress['value'] = 28
			mainscrn.update_idletasks()
			sql_query = "SELECT * FROM he_{},he_products WHERE he_{}.prod_id = he_products.prod_id".format(ord_id,ord_id)
			he_cursor.execute(sql_query)
			prod_res = he_cursor.fetchall()
			progress['value'] = 43
			mainscrn.update_idletasks()
			for i in prod_res:
				prod = str(i[0]) + ': ' + i[3]
				qty = i[1]
				rate = float(i[5])
				dis = float((qty*float(rate))*(float(i[6])/100))
				total = float(qty*rate-dis)
				tax = float(float(i[7])*0.01*total)
				Products.append((prod,qty,rate,dis,total,tax))
			progress['value'] = 57
			mainscrn.update_idletasks()
			if shipspd == "High Priority":
				Products.append(("High Priority Shipping Charges",1,423.73,0,500,76.27))
			else:
				if gtotal < 1000:
					Products.append(("Low Priority Shipping Charges",1,84.74,0.00,100.00,15.26))
				else:
					Products.append(("Low Priority Shipping Charges",1,84.74,84.74,0.00,0.00))
			progress['value'] = 71
			mainscrn.update_idletasks()
			head = header(CustomerName,CustomerContact)
			pdf = canvas.Canvas("C:\\InvoiceGenerator\\" + str(int(head.InvoiceNumber)) + ".pdf")
			pdf_gen.header(head,pdf)
			pdf_gen.middle(pdf)
			ycooridinate = 650
			progress['value'] = 85
			mainscrn.update_idletasks()
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
			progress['value'] = 100
			mainscrn.update_idletasks()
			webbrowser.open("C:\\InvoiceGenerator\\" + str(int(head.InvoiceNumber)) + ".pdf")
			user_ord(username)
			mainscrn.mainloop()

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
	nav_lbl = Label(navfrm,text="My Account",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
	nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=1,column=0,padx=5,pady=0,sticky=W)
	nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=2,column=0,padx=5,pady=0,sticky=W)
	nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=3,column=0,padx=5,pady=0,sticky=W)
	nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=4,column=0,padx=5,pady=0,sticky=W)
	nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=5,column=0,padx=5,pady=0,sticky=W)
	nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=6,column=0,padx=5,pady=0,sticky=W)
	nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=7,column=0,padx=5,pady=0,sticky=W)
	nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=8,column=0,padx=5,pady=0,sticky=W)
	nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=9,column=0,padx=5,pady=0,sticky=W)
	nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=10,column=0,padx=5,pady=0,sticky=W)
	nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=11,column=0,padx=5,pady=0,sticky=W)
	nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=12,column=0,padx=5,pady=0,sticky=W)
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=14,column=0,padx=5,pady=0,sticky=W)
	nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=15,column=0,padx=5,pady=0,sticky=W)
	nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=16,column=0,padx=5,pady=0,sticky=W)
	nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	shopart = ImageTk.PhotoImage(Image.open("images/shop_art/my_acc.png"))
	shartlb = Label(mainscrn,image=shopart,background="#909090")
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),bg="#202020",fg="#EEEEEE")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),bg="#202020",fg="#EEEEEE")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),state=DISABLED,bg="#202020",fg="#EEEEEE")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),bg="#202020",fg="#EEEEEE")

	sql_query = "SELECT f_name,l_name,add1,add2,city,state,pin,mob,pass FROM he_users where user_id ='{}'".format(username)
	he_cursor.execute(sql_query)
	qur_res = he_cursor.fetchall()[0]

	chg_acc = Frame(mainscrn,bg="#202020")
	Label(chg_acc,text="Manage Account Details",font=("Arial Bold",14),fg="#EEEEEE",bg="#202020").grid(row=0,column=0,columnspan=4,padx=10,pady=10)
	Label(chg_acc,text="First Name:",fg="#EEEEEE",bg="#202020").grid(row=1,column=0,padx=10,pady=10,sticky=E)
	fnamc = Entry(chg_acc,width=40,fg="#EEEEEE",bg="#202020")
	fnamc.grid(row=1,column=1,padx=10,pady=10)
	fnamc.insert(0,qur_res[0])
	Label(chg_acc,text="Last Name:",fg="#EEEEEE",bg="#202020").grid(row=1,column=2,padx=10,pady=10,sticky=E)
	lnamc = Entry(chg_acc,width=40,fg="#EEEEEE",bg="#202020")
	lnamc.grid(row=1,column=3,padx=10,pady=10)
	lnamc.insert(0,qur_res[1])
	Label(chg_acc,text="Address 1:",fg="#EEEEEE",bg="#202020").grid(row=2,column=0,padx=10,pady=10,sticky=E)
	add1c = Entry(chg_acc,width=40,fg="#EEEEEE",bg="#202020")
	add1c.grid(row=2,column=1,padx=10,pady=10)
	add1c.insert(0,qur_res[2])
	Label(chg_acc,text="Address 2:",fg="#EEEEEE",bg="#202020").grid(row=2,column=2,padx=10,pady=10,sticky=E)
	add2c = Entry(chg_acc,width=40,fg="#EEEEEE",bg="#202020")
	add2c.grid(row=2,column=3,padx=10,pady=10)
	add2c.insert(0,qur_res[3])
	Label(chg_acc,text="City:",fg="#EEEEEE",bg="#202020").grid(row=3,column=0,padx=10,pady=10,sticky=E)
	cityc = Entry(chg_acc,width=40,fg="#EEEEEE",bg="#202020")
	cityc.grid(row=3,column=1,padx=10,pady=10)
	cityc.insert(0,qur_res[4])
	Label(chg_acc,text="State:",fg="#EEEEEE",bg="#202020").grid(row=3,column=2,padx=10,pady=10,sticky=E)
	statc = StringVar()
	statc.set(qur_res[5])
	states = ["Andaman & Nicobar","Andhra Pradesh","Arunachal Pradesh",
	"Assam","Bihar","Chandigarh","Chhattisgarh","Dadra & Nagar Haveli",
	"Daman & Diu","Delhi","Goa","Gujarat","Haryana","Himachal Pradesh",
	"Jammu & Kashmir","Jharkhand","Karnataka","Kerala","Lakshadweep",
	"Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram",
	"Nagaland","Orissa","Pondicherry","Punjab","Rajasthan","Sikkim",
	"Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttaranchal","West Bengal"]
	st_ddon = OptionMenu(chg_acc,statc,*states)
	st_ddon.config(bg="#202020",fg="#EEEEEE")
	st_ddon["highlightthickness"]=0
	st_ddon["menu"].config(bg="#202020")
	st_ddon["menu"].config(fg="#EEEEEE")
	st_ddon.grid(row=3,column=3,padx=10,pady=10,sticky=W)
	Label(chg_acc,text="Pincode:",fg="#EEEEEE",bg="#202020").grid(row=4,column=0,padx=10,pady=10,sticky=E)
	pincc = Entry(chg_acc,width=40,fg="#EEEEEE",bg="#202020")
	pincc.grid(row=4,column=1,padx=10,pady=10)
	pincc.insert(0,qur_res[6])
	Label(chg_acc,text="Mobile:",fg="#EEEEEE",bg="#202020").grid(row=4,column=2,padx=10,pady=10,sticky=E)
	mobic = Entry(chg_acc,width=40,fg="#EEEEEE",bg="#202020")
	mobic.grid(row=4,column=3,padx=10,pady=10)
	mobic.insert(0,qur_res[7])
	Button(chg_acc,text="Save New Address",bg="#202020",fg="#EEEEEE",command=lambda:user_chadd(fnamc.get(),lnamc.get(),add1c.get(),add2c.get(),cityc.get(),statc.get(),pincc.get(),mobic.get())).grid(row=5,column=0,padx=10,pady=10,columnspan=4,ipadx=50)

	Label(chg_acc,text="Old Password:",fg="#EEEEEE",bg="#202020").grid(row=7,column=0,padx=10,pady=10,sticky=E)
	oldpc = Entry(chg_acc,width=40,fg="#EEEEEE",bg="#202020",show='*')
	oldpc.grid(row=7,column=1,padx=10,pady=10)
	Label(chg_acc,text="New Password:",fg="#EEEEEE",bg="#202020").grid(row=7,column=2,padx=10,pady=10,sticky=E)
	newpc = Entry(chg_acc,width=40,fg="#EEEEEE",bg="#202020",show='*')
	newpc.grid(row=7,column=3,padx=10,pady=10)
	Label(chg_acc,text="Retype Password:",fg="#EEEEEE",bg="#202020").grid(row=8,column=0,padx=10,pady=10,sticky=E)
	reepc = Entry(chg_acc,width=40,fg="#EEEEEE",bg="#202020",show='*')
	reepc.grid(row=8,column=1,padx=10,pady=10)
	Button(chg_acc,text="Change Password",bg="#202020",fg="#EEEEEE",command=lambda:user_chpass(oldpc.get(),newpc.get(),reepc.get(),qur_res[8],username)).grid(row=9,column=0,padx=10,pady=10,columnspan=4,ipadx=50)

	rgt_frm = Frame(chg_acc,bg="#202020")
	rgt_frm.grid(row=0,column=5,rowspan=9,padx=15)
	if len(username) > 10:
		eduser = "Hello There! " + username[0:6] + "... "
	else:
		eduser = "Hello There! " + username + " "
	Label(rgt_frm,text=eduser,fg="#EEEEEE",bg="#202020").grid(row=0,column=0)
	Button(rgt_frm,text="Logout",command=user_logout,bg="#202020",fg="#EEEEEE").grid(row=0,column=1,padx=10,pady=10)
	Label(rgt_frm,text="More Actions",fg="#EEEEEE",bg="#202020",font=("Arial Bold",12)).grid(row=1,column=0,padx=10,pady=10,columnspan=2)
	Button(rgt_frm,text="Ask a Question",command=user_askq,bg="#202020",fg="#EEEEEE").grid(row=2,column=0,padx=10,pady=20,columnspan=2)
	Button(rgt_frm,text="Answered Questions",command=user_readq,bg="#202020",fg="#EEEEEE").grid(row=3,column=0,padx=10,pady=20,columnspan=2)
	Button(rgt_frm,text="FAQs",command=user_faq,bg="#202020",fg="#EEEEEE").grid(row=4,column=0,padx=10,pady=20,columnspan=2)
	Button(rgt_frm,text="About Us",command=user_about,bg="#202020",fg="#EEEEEE").grid(row=5,column=0,padx=10,pady=20,columnspan=2)

	he_gurimg = ImageTk.PhotoImage(Image.open("images/he_guran.png"))
	Label(mainscrn,image=he_gurimg,background="#202020").place(x=160,y=538)

	shartlb.place(x=-2,y=-2)
	chg_acc.place(x=160,y=123)
	navfrm.place(x=-2,y=119)
	sh_but1.place(x=819,y=10)
	sh_but2.place(x=900,y=10)
	sh_but3.place(x=975,y=10)
	sh_but4.place(x=1060,y=10)
	mainscrn.mainloop()

def user_chadd(fname,lname,add1,add2,city,state,pin,mob):
	if len(fname) > 255:
		messagebox.showerror("Change Address Failed!","Length of Firstname is too long.")
	elif len(fname) == 0:
		messagebox.showerror("Change Address Failed!","Firstname not entered.")
	elif len(lname) > 255:
		messagebox.showerror("Change Address Failed!","Length of Lastname is too long.")
	elif len(lname) == 0:
		messagebox.showerror("Change Address Failed!","Lastname not entered.")
	elif len(add1) > 255:
		messagebox.showerror("Change Address Failed!","Length of Address 1 is too long.")
	elif len(add1) == 0:
		messagebox.showerror("Change Address Failed!","Address 1 not entered.")
	elif len(add2) > 255:
		messagebox.showerror("Change Address Failed!","Length of Address 2 is too long.")
	elif len(add2) == 0:
		messagebox.showerror("Change Address Failed!","Address 2 not entered.")
	elif len(city) > 50:
		messagebox.showerror("Change Address Failed!","Length of City is too long.")
	elif len(city) == 0:
		messagebox.showerror("Change Address Failed!","City not entered.")
	elif len(pin) == 0:
		messagebox.showerror("Change Address Failed!","Pincode not entered.")
	elif len(pin) != 6:
		messagebox.showerror("Change Address Failed!","Pincode is not of 6 digits.")
	elif len(mob) == 0:
		messagebox.showerror("Change Address Failed!","Mobile number not entered.")
	elif len(mob) != 10:
		messagebox.showerror("Change Address Failed!","Mobile number is not of 10 digits.")
	else:
		sql_query = "UPDATE he_users SET f_name = '{}',l_name = '{}',mob = '{}',add1 = '{}',add2 = '{}',city = '{}',state = '{}',pin = '{}'".format(fname,lname,mob,add1,add2,city,state,pin)
		he_cursor.execute(sql_query)
		he_db.commit()
		messagebox.showinfo("Address Changed Successfully!","Your new address has been saved.")

def user_chpass(opass,npass,rpass,cpass,username):
	if opass != cpass:
		messagebox.showerror("Password change Failed!","Old password is not correct.")
	elif npass != rpass:
		messagebox.showerror("Password change Failed!","Reentered password is not correct.")
	else:
		if len(npass) > 30:
			messagebox.showerror("Password change Failed!","Password is longer than 30 characters.")
		else:
			sql_query = "UPDATE he_users SET pass = '{}'".format(npass)
			he_cursor.execute(sql_query)
			he_db.commit()
			messagebox.showinfo("Password Changed Successfully!","Your new password has been saved.")
			user_acc(username)

def user_askq():
	messagebox.showinfo("Ask a Question","This part of shop is still under development.")

def user_readq():
	messagebox.showinfo("Answered Questions","This part of shop is still under development.")

def user_faq():
	messagebox.showinfo("FAQs","This part of shop is still under development.")

def user_about():
	try:
		webbrowser.open("images\\about.pdf")
	except:
		messagebox.showerror("About Us Failed!","About Us failed to load. Error Code: no_file")

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
	nav_lbl = Label(navfrm,text="Mechanical Parts",font=("Arial Bold",10),background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=4,pady=1,sticky=W)
	nav_but1 = Button(navfrm,text="Top Deals",command=lambda:user_qur("Top Deals",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=1,column=0,padx=5,pady=0,sticky=W)
	nav_but2 = Button(navfrm,text="New Arrivals",command=lambda:user_qur("New Arrivals",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=2,column=0,padx=5,pady=0,sticky=W)
	nav_but3 = Button(navfrm,text="Learning and Robotics",command=lambda:user_qur("Learning and Robotics",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=3,column=0,padx=5,pady=0,sticky=W)
	nav_but4 = Button(navfrm,text="Drones and Parts",command=lambda:user_qur("Drones and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=4,column=0,padx=5,pady=0,sticky=W)
	nav_but5 = Button(navfrm,text="E-Bikes and Parts",command=lambda:user_qur("E-Bikes and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=5,column=0,padx=5,pady=0,sticky=W)
	nav_but6 = Button(navfrm,text="3D Printers and Parts",command=lambda:user_qur("3D Printers and Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=6,column=0,padx=5,pady=0,sticky=W)
	nav_but7 = Button(navfrm,text="Batteries",command=lambda:user_qur("Batteries",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=7,column=0,padx=5,pady=0,sticky=W)
	nav_but8 = Button(navfrm,text="Motors, Drivers, Actuators",command=lambda:user_qur("Motors, Drivers, Actuators",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=8,column=0,padx=5,pady=0,sticky=W)
	nav_but9 = Button(navfrm,text="Development Boards",command=lambda:user_qur("Development Boards",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=9,column=0,padx=5,pady=0,sticky=W)
	nav_but10 = Button(navfrm,text="Arduino",command=lambda:user_qur("Arduino",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=10,column=0,padx=5,pady=0,sticky=W)
	nav_but11 = Button(navfrm,text="Raspberry Pi",command=lambda:user_qur("Raspberry Pi",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=11,column=0,padx=5,pady=0,sticky=W)
	nav_but12 = Button(navfrm,text="Sensors",command=lambda:user_qur("Sensors",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=12,column=0,padx=5,pady=0,sticky=W)
	nav_but13 = Button(navfrm,text="IoT and Wireless",command=lambda:user_qur("IoT and Wireless",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=13,column=0,padx=5,pady=0,sticky=W)
	nav_but14 = Button(navfrm,text="Displays",command=lambda:user_qur("Displays",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=14,column=0,padx=5,pady=0,sticky=W)
	nav_but15 = Button(navfrm,text="Power Supply",command=lambda:user_qur("Power Supply",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=15,column=0,padx=5,pady=0,sticky=W)
	nav_but16 = Button(navfrm,text="Electronic Modules",command=lambda:user_qur("Electronic Modules",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=16,column=0,padx=5,pady=0,sticky=W)
	nav_but17 = Button(navfrm,text="Electronic Components",command=lambda:user_qur("Electronic Components",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=17,column=0,padx=5,pady=0,sticky=W)
	nav_but18 = Button(navfrm,text="Wires and Cables",command=lambda:user_qur("Wires and Cables",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=18,column=0,padx=5,pady=0,sticky=W)
	nav_but19 = Button(navfrm,text="Instruments and Tools",command=lambda:user_qur("Instruments and Tools",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=19,column=0,padx=5,pady=0,sticky=W)
	nav_but20 = Button(navfrm,text="Mechanical Parts",command=lambda:user_qur("Mechanical Parts",username),relief=FLAT,bg="#202020",fg="#EEEEEE").grid(row=20,column=0,padx=5,pady=0,sticky=W)

	sql_query = "SELECT * FROM {}_cart,he_products WHERE {}_cart.prod_id = he_products.prod_id".format(username,username)
	he_cursor.execute(sql_query)
	qur_list = he_cursor.fetchall()

	frm_tree = Frame(mainscrn,background="#909090")
	style = ttk.Style(frm_tree)
	style.theme_use("clam")
	style.configure("Treeview.Heading",background="#202020",foreground="#EEEEEE",borderwidth=0)
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
	sh_but1 = Button(mainscrn,text="My Wishlist",command=lambda:user_wl(username),bg="#202020",fg="#EEEEEE")
	sh_but2 = Button(mainscrn,text="My Orders",command=lambda:user_ord(username),bg="#202020",fg="#EEEEEE")
	sh_but3 = Button(mainscrn,text="My Account",command=lambda:user_acc(username),bg="#202020",fg="#EEEEEE")
	sh_but4 = Button(mainscrn,text="My Cart",command=lambda:user_cart(username),state=DISABLED,bg="#202020",fg="#EEEEEE")

	ad_crt = LabelFrame(mainscrn,background="#202020")
	ad_lb1 = Label(ad_crt,text="Select item, ",background="#202020",foreground="#EEEEEE").grid(row=0,column=0,padx=30)
	ad_des = Button(ad_crt,text="More Details",bg="#202020",fg="#EEEEEE",command=lambda:user_proddet(tree)).grid(row=0,column=1,padx=30,pady=2)
	ad_wli = Button(ad_crt,text="Delete",bg="#202020",fg="#EEEEEE",command=lambda:user_delcart(username,tree)).grid(row=0,column=2,padx=30)
	ad_lb2 = Label(ad_crt,text="             OR                  Change Quantity:  ",bg="#202020",fg="#EEEEEE").grid(row=0,column=3)
	ad_spn = Spinbox(ad_crt,from_=1,to=999,width=3,bg="#202020",fg="#EEEEEE",buttonbackground="#202020")
	ad_crb = Button(ad_crt,text="Update Cart",bg="#202020",fg="#EEEEEE",command=lambda:user_editcart(username,ad_spn.get(),tree))
	ad_chk = Button(ad_crt,text="Checkout",bg="#202020",fg="#EEEEEE",command=lambda:user_ship(username,gtotal,tree))
	ad_spn.grid(row=0,column=4)
	ad_crb.grid(row=0,column=5,padx=30)
	ad_lb3 = Label(ad_crt,text="OR",bg="#202020",fg="#EEEEEE").grid(row=0,column=6,padx=35)
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
	lbl = Label(mainscrn,text=tc,justify=LEFT,bg="#202020",fg="#EEEEEE")
	chkvar = IntVar()
	chkbx = Checkbutton(mainscrn,text="Yes, I agree to the Terms and Conditions and have made the Payment.",selectcolor="#202020",activebackground="#202020",activeforeground="#EEEEEE",bg="#202020",fg="#EEEEEE",variable=chkvar)
	okbut = Button(mainscrn,text="Continue",bg="#202020",fg="#EEEEEE",command=lambda:user_pay(username,gtotal,shipspd,chkvar.get()))
	cnbut = Button(mainscrn,text="Cancel",bg="#202020",fg="#EEEEEE",command=lambda:user_cart(username))
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
		Label(mainscrn,text="Please make the payment with Paytm/Google Pay/IMPS\nwith details as on last page. And then enter the\nUPI Transaction ID/Paytm Order No. Below.",bg="#202020",fg="#EEEEEE",justify=LEFT).grid(row=0,column=0,columnspan=2,padx=40)
		Label(mainscrn,text=" Please select payment mode: ",bg="#202020",fg="#EEEEEE").grid(row=1,column=0,sticky=W,pady=10)
		ddon = OptionMenu(mainscrn,payvar,"Paytm","Google Pay","IMPS")
		ddon.grid(row=1,column=1,sticky=W)
		ddon.config(bg="#202020",fg="#EEEEEE")
		ddon["highlightthickness"]=0
		ddon["menu"].config(bg="#202020")
		ddon["menu"].config(fg="#EEEEEE")
		Label(mainscrn,text=" Please enter Transaction Number: ",bg="#202020",fg="#EEEEEE").grid(row=2,column=0,sticky=W,pady=10)
		trne = Entry(mainscrn,width=18,bg="#202020",fg="#EEEEEE")
		trne.grid(row=2,column=1,sticky=W)
		Button(mainscrn,text="Return",command=lambda:user_cart(username),bg="#202020",fg="#EEEEEE").grid(row=3,column=1,ipadx=30,padx=35)
		Button(mainscrn,text="Continue",command=lambda:user_paid(username,gtotal,shipspd,payvar.get(),trne.get()),bg="#202020",fg="#EEEEEE").grid(row=3,column=0,ipadx=30,padx=35)
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
		lblprogress = Label(mainscrn,text="Placing Order... Please Wait.",bg='#EEEEEE')
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

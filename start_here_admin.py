import tkinter.ttk as ttk
import mysql.connector as sql
import smtplib
import atexit
import os
from email.message import EmailMessage
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

#Environment variables
admin_user = os.environ.get('adminus')
admin_pass = os.environ.get('adminpa')
email_user = os.environ.get('mailus')
email_pass = os.environ.get('mailpa')
sql_pass = os.environ.get('mysqlpa')

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

	frm1 = LabelFrame(mainscrn,text="Please login to continue.")
	lbl1 = Label(mainscrn,text="Welcome to Hacking Electronics Workshop",font=("Arial Bold",10))
	lbl3 = Label(frm1,text="UserID:")
	lbl4 = Label(frm1,text="Password:")
	but1 = Button(mainscrn,text="Login",command=lambda:login(usern.get(),passw.get()))
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

	frm1.grid(row=2,column=1)
	lbl1.grid(row=1,column=1)
	lbl3.grid(row=0,column=0,sticky=E)
	lbl4.grid(row=1,column=0,sticky=E)
	but1.grid(row=3,column=1)
	usern.grid(row=0,column=1)
	passw.grid(row=1,column=1)
	lbl5.grid(row=0,column=1)
	lbl6.grid(row=4,column=1)
	lbl7.grid(row=0,column=0,rowspan=5)
	lbl8.grid(row=0,column=2,rowspan=5)
	mainscrn.mainloop()

def send_email(msg):
	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(email_user,email_pass)
		smtp.send_message(msg)

def login(username,password):
	if username == admin_user and password == admin_pass:
		master_login()
	else:
		messagebox.showerror("Login Failed","Login Failed. Please check User ID and Password")

def master_login():
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.title("Hacking Electronics Admin")
	mainscrn.iconbitmap('images/icon.ico')
	lbl1 = Label(mainscrn,text="Welcome Hacking Electronics Admin.",font=("Arial Bold",10))
	but1 = Button(mainscrn,text="Logout",command=master_logout)
	but2 = Button(mainscrn,text="Add Products",command=lambda:add_prod('',False))
	but3 = Button(mainscrn,text="Edit Products",command=edit_prod)
	but4 = Button(mainscrn,text="Approve/Reject Register Requests",command=approv_reg)
	but5 = Button(mainscrn,text="Manage Orders",command=mg_ord)
	lbl1.grid(row=0,column=0,pady=5)
	but1.grid(row=1,column=0,pady=5)
	but2.grid(row=2,column=0,pady=5)
	but3.grid(row=3,column=0,pady=5)
	but4.grid(row=4,column=0,pady=5)
	but5.grid(row=5,column=0,pady=5)
	mainscrn.mainloop()

def master_logout():
	global mainscrn
	mainscrn.destroy()
	mainpage()

def approv_reg():
	global mainscrn
	sql_query = "SELECT * FROM he_users WHERE approved = 'n'"
	he_cursor.execute(sql_query)
	app_result = he_cursor.fetchall()
	if len(app_result) == 0:
		messagebox.showinfo("No requests.","No requests yet.")
		master_login()
	else:
		mainscrn.destroy()
		mainscrn = Tk()
		mainscrn.grab_set()
		mainscrn.focus_force()
		width = 960
		height = 550
		screen_width = mainscrn.winfo_screenwidth()
		screen_height = mainscrn.winfo_screenheight()
		x = (screen_width/2) - (width/2)
		y = (screen_height/2) - (height/2) - (height/12)
		mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
		mainscrn.resizable(0, 0)
		mainscrn.title("Hacking Electronics Shop")
		mainscrn.iconbitmap('images/icon.ico')

		frm1 = Frame(mainscrn)
		frm2 = Frame(mainscrn)
		scrollbarx = Scrollbar(frm1,orient = HORIZONTAL)
		scrollbary = Scrollbar(frm1,orient = VERTICAL)
		tree = ttk.Treeview(frm1,columns = ("uid","email","fname","lname","mob","add1","add2","city","state","pin","doj"),height = 22,selectmode = "extended",yscrollcommand = scrollbary.set,xscrollcommand = scrollbarx.set)
		scrollbary.config(command = tree.yview)
		scrollbary.pack(side = RIGHT,fill = Y)
		scrollbarx.config(command = tree.xview)
		scrollbarx.pack(side = BOTTOM,fill = X)
		tree.heading("#0",text="Sr. No.",anchor = W)
		tree.heading("uid",text="User ID",anchor = W)
		tree.heading("email",text="Email",anchor = W)
		tree.heading("fname",text="First Name",anchor = W)
		tree.heading("lname",text="Last Name",anchor = W)
		tree.heading("mob",text="Mobile",anchor = W)
		tree.heading("add1",text="Address Line 1",anchor = W)
		tree.heading("add2",text="Address Line 2",anchor = W)
		tree.heading("city",text="City",anchor = W)
		tree.heading("state",text="State",anchor = W)
		tree.heading("pin",text="Pin",anchor = W)
		tree.heading("doj",text="Date of Registration",anchor = W)
		tree.column("#0",stretch = NO,minwidth = 10, width=50)
		tree.column("uid",stretch = NO,minwidth = 10, width=100)
		tree.column("email",stretch = NO,minwidth = 10, width=150)
		tree.column("fname",stretch = NO,minwidth = 10, width=100)
		tree.column("lname",stretch = NO,minwidth = 10, width=100)
		tree.column("mob",stretch = NO,minwidth = 10, width=80)
		tree.column("add1",stretch = NO,minwidth = 10, width=200)
		tree.column("add2",stretch = NO,minwidth = 10, width=200)
		tree.column("city",stretch = NO,minwidth = 10, width=100)
		tree.column("state",stretch = NO,minwidth = 10, width=100)
		tree.column("pin",stretch = NO,minwidth = 10, width=50)
		tree.column("doj",stretch = NO,minwidth = 10, width=125)
		tree.pack()

		for qur_res in app_result:
			tree.insert('','end',values=(qur_res[0],qur_res[1],qur_res[3],qur_res[4],qur_res[5],qur_res[6],qur_res[7],qur_res[8],qur_res[9],qur_res[10],qur_res[12]))

		lbl1 = Label(frm2,text="Select a user and then click approve/reject:")
		but1 = Button(frm2,text="Approve",command=lambda:approv_ok(tree))
		but2 = Button(frm2,text="Reject",command=lambda:approv_nok(tree))
		but3 = Button(frm2,text="Send Confirmation Email",command=lambda:conf_email(tree))
		but4 = Button(frm2,text="Return",command=master_login)
		lbl1.grid(row=0,column=1,pady=5)
		but1.grid(row=1,column=0,padx=20,ipadx=50)
		but2.grid(row=1,column=1,padx=20,ipadx=50)
		but3.grid(row=1,column=2,padx=20,ipadx=50)
		but4.grid(row=1,column=3,padx=20,ipadx=50)
		frm1.pack()
		frm2.pack()
		mainscrn.mainloop()

def conf_email(tree):
	try:
		tomsg = tree.item(tree.focus())['values'][1]
		fname = tree.item(tree.focus())['values'][2]
	except:
		messagebox.showerror("Send Email Failed!","Please select a user first.")
	else:
		msg = EmailMessage()
		msg['Subject'] = "Final Step: Reply to activate account."
		msg['From'] = email_user
		msg['To'] = tomsg
		msg.set_content("""
		Hi {}!
		You received this email because it was submitted for registration to Hacking Electronics Shop.

		If you would like to Register please reply:
			Yes, Please activate my account.

		Or else if you would like not to register please reply:
		    No, do not activate account.

		If already registered do not reply.
		""".format(fname))
		send_email(msg)

def send_email(msg):
	with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
		smtp.login(email_user,email_pass)
		smtp.send_message(msg)
	messagebox.showinfo("Send Email Success!","Email sent successfully.")

def approv_ok(tree):
	try:
		uid = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Approve user Failed!","Please select a user first.")
	else:
		sql_query = "UPDATE he_users SET approved = 'y' WHERE user_id = '{}'".format(uid)
		he_cursor.execute(sql_query)
		sql_query = "CREATE TABLE {}_wl(prod_id int(10) PRIMARY KEY)".format(uid)
		he_cursor.execute(sql_query)
		sql_query = "CREATE TABLE {}_cart(prod_id int(10) PRIMARY KEY,prod_qty int(3) NOT NULL)".format(uid)
		he_cursor.execute(sql_query)
		he_db.commit()
		messagebox.showinfo("Approval Success","User has been approved.")
		approv_reg()

def approv_nok(tree):
	try:
		uid = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Reject user Failed!","Please select a user first.")
	else:
		sql_query = "UPDATE he_users SET approved = 'r' WHERE user_id = '{}'".format(uid)
		he_cursor.execute(sql_query)
		he_db.commit()
		messagebox.showinfo("Approval Rejected","User has been rejected.")
		approv_reg()

def add_prod(tree,editing):
	if editing:
		try:
			edit_item = tree.item(tree.focus())['values'][0]
		except:
			messagebox.showerror("Edit Product Failed!","Please select a product first.")
			return
	global mainscrn
	mainscrn.destroy()
	mainscrn = Tk()
	mainscrn.grab_set()
	mainscrn.focus_force()
	mainscrn.resizable(0, 0)
	mainscrn.title("Register to Hacking Electronics Shop")
	mainscrn.iconbitmap('images/icon.ico')
	
	frm2 = LabelFrame(mainscrn)
	lbl7 = Label(mainscrn,text="Please enter your product details",font=("Arial Bold",10))
	lbl8 = Label(frm2,text="Name:")
	lbl9 = Label(frm2,text="Category:")
	lbl10 = Label(frm2,text="Price:")
	lbl11 = Label(frm2,text="Discount:")
	lbl12 = Label(frm2,text="GST rate:")
	lbl13 = Label(frm2,text="Availability:")
	lbl14 = Label(frm2,text="Description:")
	lbl15 = Label(frm2,text="Icon filename:")
	lbl16 = Label(frm2,text="Img1 filename:")
	lbl17 = Label(frm2,text="Img2 filename:")
	lbl18 = Label(frm2,text="Img3 filename:")
	frm2.grid(row=1,column=0,columnspan=3,padx=4)
	lbl7.grid(row=0,column=0,columnspan=3)
	lbl8.grid(row=0,column=0,sticky=E)
	lbl9.grid(row=1,column=0,sticky=E)
	lbl10.grid(row=2,column=0,sticky=E)
	lbl11.grid(row=3,column=0,sticky=E)
	lbl12.grid(row=4,column=0,sticky=E)
	lbl13.grid(row=5,column=0,sticky=E)
	lbl14.grid(row=10,column=0,sticky=NE)
	lbl15.grid(row=6,column=0,sticky=E)
	lbl16.grid(row=7,column=0,sticky=E)
	lbl17.grid(row=8,column=0,sticky=E)
	lbl18.grid(row=9,column=0,sticky=E)

	global namer
	global categ
	global pricr
	global gstrr
	global avair
	global descr
	global discr
	global iconr
	global img1r
	global img2r
	global img3r	
	
	namer = Entry(frm2,width=60)
	pricr = Entry(frm2,width=10)
	gstrr = Entry(frm2,width=10)
	avair = Entry(frm2,width=10)
	iconr = Entry(frm2,width=60)
	discr = Entry(frm2,width=10)
	img1r = Entry(frm2,width=60)
	img2r = Entry(frm2,width=60)
	img3r = Entry(frm2,width=60)
	descr = Text(frm2,height=10,width=45)

	categ = StringVar()

	if editing:
		sql_query = "SELECT * FROM he_products where prod_id = '{}'".format(edit_item)
		he_cursor.execute(sql_query)
		edit_result = he_cursor.fetchall()
		categ.set(edit_result[0][2])
		namer.insert(0,edit_result[0][1])
		pricr.insert(0,edit_result[0][3])
		discr.insert(0,edit_result[0][4])
		gstrr.insert(0,edit_result[0][5])
		avair.insert(0,edit_result[0][6])
		iconr.insert(0,edit_result[0][8])
		img1r.insert(0,edit_result[0][9])
		img2r.insert(0,edit_result[0][10])
		img3r.insert(0,edit_result[0][11])
		descr.insert('1.0',edit_result[0][7])
	else:
		categ.set("Select Category")
		iconr.insert(0,"images/product_images/img_unic.jpeg")
		img1r.insert(0,"images/product_images/img_unav.jpeg")
		img2r.insert(0,"images/product_images/img_unav.jpeg")
		img3r.insert(0,"images/product_images/img_unav.jpeg")
		descr.insert('1.0',"No description yet.")

	categs = ["Learning and Robotics","Drones and Parts","E-Bikes and Parts","3D Printers and Parts","Batteries","Motors, Drivers, Actuators",
	"Development Boards","Arduino","Raspberry Pi","Sensors","IoT and Wireless","Displays","Power Supply","Electronic Modules",
	"Electronic Components","Wires and Cables","Instruments and Tools","Mechanical Parts"]
	cater = OptionMenu(frm2,categ,*categs)
	
	namer.grid(row=0,column=1)
	cater.grid(row=1,column=1,sticky=W)
	pricr.grid(row=2,column=1,sticky=W)
	discr.grid(row=3,column=1,sticky=W)
	gstrr.grid(row=4,column=1,sticky=W)
	avair.grid(row=5,column=1,sticky=W)
	iconr.grid(row=6,column=1)
	img1r.grid(row=7,column=1)
	img2r.grid(row=8,column=1)
	img3r.grid(row=9,column=1)
	descr.grid(row=10,column=1,ipady=35)

	but5 = Button(mainscrn,text="Clear",command=prod_clr)
	but6 = Button(mainscrn,text="Cancel",command=edit_prod)
	but7 = Button(mainscrn,text="Add",command=lambda:prod_add(edit_item,editing))
	but5.grid(row=2,column=0,pady=5)
	but6.grid(row=2,column=1,pady=5)
	but7.grid(row=2,column=2,pady=5)

	mainscrn.mainloop()

def prod_clr():
	namer.delete(0,END)
	pricr.delete(0,END)
	gstrr.delete(0,END)
	discr.delete(0,END)
	avair.delete(0,END)
	descr.delete('1.0',END)
	img1r.delete(0,END)
	img2r.delete(0,END)
	img3r.delete(0,END)
	iconr.insert(0,"images/product_images/img_unic.jpeg")
	img1r.insert(0,"images/product_images/img_unav.jpeg")
	img2r.insert(0,"images/product_images/img_unav.jpeg")
	img3r.insert(0,"images/product_images/img_unav.jpeg")
	descr.insert('1.0',"No description yet.")
	categ.set("Select Category")

def prod_add(edit_item,editing):
	add_prob = False
	if len(namer.get()) == 0 or len(namer.get()) > 255:
		messagebox.showerror("Add product failed","Product name should have less than 255 characters OR No name entered.")
		add_prob = True
	if len(pricr.get()) == 0 or len(pricr.get()) > 10:
		messagebox.showerror("Add product failed","Price should be less than 10 characters OR No price entered.")
		add_prob = True
	if len(gstrr.get()) == 0 or len(gstrr.get()) > 5:
		messagebox.showerror("Add product failed","GST should be less than 5 characters OR No GST entered.")
		add_prob = True
	if len(discr.get()) == 0 or len(discr.get()) > 5:
		messagebox.showerror("Add product failed","Discount should be less than 5 characters OR No Discount entered.")
		add_prob = True
	if len(avair.get()) == 0 or len(avair.get()) > 9:
		messagebox.showerror("Add product failed","Availability should be less than 10 characters OR No availability of product entered.")
		add_prob = True
	if len(descr.get('1.0',END)) == 0 or len(descr.get('1.0',END)) > 65535:
		messagebox.showerror("Add product failed","Description should be less than 65536 characters OR No description of product entered.")
		add_prob = True
	if categ.get() == "Select Category":
		messagebox.showerror("Add product failed","Please specify category.")
		add_prob = True
	try:
		price = float(pricr.get())
		gst = float(gstrr.get())
		disc = float(discr.get())
		avail = int(avair.get())
	except:
		messagebox.showerror("Add product failed","Please check if price, GST, Discount are float, availability integer.")
	else:
		try:
			Image.open(iconr.get())
			Image.open(img1r.get())
			Image.open(img2r.get())
			Image.open(img3r.get())
		except:
			messagebox.showerror("Add product failed","Check location of image")
		else:
			if editing and not add_prob:
				sql_query = "UPDATE he_products SET prod_nm = '{}',prod_categ = '{}',prod_price = {},prod_gst = {},prod_dis = {},prod_avail = {},prod_desc = '{}',prod_icon = '{}',prod_img1 = '{}',prod_img2 = '{}',prod_img3 = '{}',doa = NOW() WHERE prod_id = {}".format(namer.get(),categ.get(),price,gst,disc,avail,descr.get('1.0',END),iconr.get(),img1r.get(),img2r.get(),img3r.get(),edit_item)
				try:
					he_cursor.execute(sql_query)
				except:
					messagebox.showerror("Edit product failed. Please give a unique name/same name as before.")
				else:
					he_db.commit()
					editing = False
					messagebox.showinfo("Success","Product edited successfully.")
					edit_prod()
			else:
				sql_query = "SELECT prod_nm FROM he_products"
				he_cursor.execute(sql_query)
				result = he_cursor.fetchall()
				for query_result in result:
					if namer.get() == query_result[0]:
						messagebox.showerror("Add product failed","Please give unique name to product.")
						add_prob = True
						break
				if not add_prob:
					sql_query = "INSERT INTO he_products(prod_nm,prod_categ,prod_price,prod_gst,prod_dis,prod_avail,prod_desc,prod_icon,prod_img1,prod_img2,prod_img3,doa) VALUES('{}','{}',{},{},{},{},'{}','{}','{}','{}','{}',NOW())".format(namer.get(),categ.get(),price,gst,disc,avail,descr.get('1.0',END),iconr.get(),img1r.get(),img2r.get(),img3r.get())
					he_cursor.execute(sql_query)
					he_db.commit()
					messagebox.showinfo("Success","Product added successfully.")
					edit_prod()

def edit_prod():
	global mainscrn
	sql_query = "SELECT * FROM he_products"
	he_cursor.execute(sql_query)
	edit_result = he_cursor.fetchall()
	if len(edit_result) == 0:
		messagebox.showinfo("No Products","No products added yet!")
		master_login()
	else:
		mainscrn.destroy()
		mainscrn = Tk()
		mainscrn.grab_set()
		mainscrn.focus_force()
		width = 960
		height = 550
		screen_width = mainscrn.winfo_screenwidth()
		screen_height = mainscrn.winfo_screenheight()
		x = (screen_width/2) - (width/2)
		y = (screen_height/2) - (height/2) - (height/12)
		mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
		mainscrn.resizable(0, 0)
		mainscrn.title("Hacking Electronics Shop")
		mainscrn.iconbitmap('images/icon.ico')

		frm1 = Frame(mainscrn)
		frm2 = Frame(mainscrn)
		style = ttk.Style(frm1)
		style.configure("Treeview",rowheight=56)
		scrollbarx = Scrollbar(frm1,orient = HORIZONTAL)
		scrollbary = Scrollbar(frm1,orient = VERTICAL)
		tree = ttk.Treeview(frm1,columns = ("prod_id","prod_nm","prod_categ","prod_price","prod_dis","prod_gst","prod_avail","prod_desc","prod_icon","prod_img1","prod_img2","prod_img3","doa"),height = 8,selectmode = "extended",yscrollcommand = scrollbary.set,xscrollcommand = scrollbarx.set)
		scrollbary.config(command = tree.yview)
		scrollbary.pack(side = RIGHT,fill = Y)
		scrollbarx.config(command = tree.xview)
		scrollbarx.pack(side = BOTTOM,fill = X)
		tree.heading("#0",text="Prod Img",anchor = W)
		tree.heading("prod_id",text="Prod ID",anchor = W)
		tree.heading("prod_nm",text="Prod Name",anchor = W)
		tree.heading("prod_categ",text="Category",anchor = W)
		tree.heading("prod_price",text="Price",anchor = W)
		tree.heading("prod_dis",text="Discount",anchor = W)
		tree.heading("prod_gst",text="GST",anchor = W)
		tree.heading("prod_avail",text="Availability",anchor = W)
		tree.heading("prod_dis",text="Discount",anchor = W)
		tree.heading("prod_desc",text="Description",anchor = W)
		tree.heading("prod_icon",text="Icon loc",anchor = W)
		tree.heading("prod_img1",text="Image loc 1",anchor = W)
		tree.heading("prod_img2",text="Image loc 2",anchor = W)
		tree.heading("prod_img3",text="Image loc 3",anchor = W)
		tree.heading("doa",text="Date of Addition",anchor = W)
		tree.column("#0",stretch = NO,minwidth = 10, width=115)
		tree.column("prod_id",stretch = NO,minwidth = 10, width=55)
		tree.column("prod_nm",stretch = NO,minwidth = 10, width=250)
		tree.column("prod_categ",stretch = NO,minwidth = 10, width=100)
		tree.column("prod_price",stretch = NO,minwidth = 10, width=70)
		tree.column("prod_dis",stretch = NO,minwidth = 10, width=50)
		tree.column("prod_gst",stretch = NO,minwidth = 10, width=50)
		tree.column("prod_avail",stretch = NO,minwidth = 10, width=50)
		tree.column("prod_dis",stretch = NO,minwidth = 10, width=50)
		tree.column("prod_desc",stretch = NO,minwidth = 10, width=200)
		tree.column("prod_icon",stretch = NO,minwidth = 10, width=150)
		tree.column("prod_img1",stretch = NO,minwidth = 10, width=150)
		tree.column("prod_img2",stretch = NO,minwidth = 10, width=150)
		tree.column("prod_img3",stretch = NO,minwidth = 10, width=150)
		tree.column("doa",stretch = NO,minwidth = 10, width=125)
		tree.pack()

		imgs_prod = []
		for qur_res in edit_result:
			imgs_prod.append(ImageTk.PhotoImage(Image.open(qur_res[8])))
		a=0
		for qur_res in edit_result:
			tree.insert('','end',image=imgs_prod[a],values=(qur_res[0],qur_res[1],qur_res[2],qur_res[3],qur_res[4],qur_res[5],qur_res[6],qur_res[7],qur_res[8],qur_res[9],qur_res[10],qur_res[11],qur_res[12]))
			a+=1

		lbl1 = Label(frm2,text="Select product to edit and click Edit:")
		but1 = Button(frm2,text="Edit",command=lambda:add_prod(tree,True))
		but2 = Button(frm2,text="Return",command=master_login)
		lbl1.grid(row=0,column=0,columnspan=2)
		but1.grid(row=1,column=0,padx=20,pady=5,ipadx=100)
		but2.grid(row=1,column=1,padx=20,pady=5,ipadx=100)
		frm1.pack()
		frm2.pack()
		mainscrn.mainloop()

def mg_ord():
	global mainscrn
	sql_query = "SELECT * FROM he_orders"
	he_cursor.execute(sql_query)
	edit_result = he_cursor.fetchall()
	if len(edit_result) == 0:
		messagebox.showinfo("No Orders","No orders yet!")
		master_login()
	else:
		mainscrn.destroy()
		mainscrn = Tk()
		mainscrn.grab_set()
		mainscrn.focus_force()
		width = 960
		height = 550
		screen_width = mainscrn.winfo_screenwidth()
		screen_height = mainscrn.winfo_screenheight()
		x = (screen_width/2) - (width/2)
		y = (screen_height/2) - (height/2) - (height/12)
		mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
		mainscrn.resizable(0, 0)
		mainscrn.title("Hacking Electronics Shop")
		mainscrn.iconbitmap('images/icon.ico')

		frm1 = Frame(mainscrn)
		frm2 = Frame(mainscrn)
		style = ttk.Style(frm1)
		style.configure("Treeview",rowheight=56)
		scrollbarx = Scrollbar(frm1,orient = HORIZONTAL)
		scrollbary = Scrollbar(frm1,orient = VERTICAL)
		tree = ttk.Treeview(frm1,columns = ("ord_id","ord_nm","ord_tot","ord_mod","ord_pid","ord_stat","ord_shp","ord_trk","doa"),height = 8,selectmode = "extended",yscrollcommand = scrollbary.set,xscrollcommand = scrollbarx.set)
		scrollbary.config(command = tree.yview)
		scrollbary.pack(side = RIGHT,fill = Y)
		scrollbarx.config(command = tree.xview)
		scrollbarx.pack(side = BOTTOM,fill = X)
		tree.heading("ord_id",text="Order ID",anchor = W)
		tree.heading("ord_nm",text="User Name",anchor = W)
		tree.heading("ord_tot",text="Order Total",anchor = W)
		tree.heading("ord_mod",text="Payment Mode",anchor = W)
		tree.heading("ord_pid",text="Transaction No.",anchor = W)
		tree.heading("ord_stat",text="Order Status",anchor = W)
		tree.heading("ord_shp",text="Shipping Speed",anchor = W)
		tree.heading("ord_trk",text="Tracking No.",anchor = W)
		tree.heading("doa",text="Date of Order",anchor = W)
		tree.column("#0",minwidth = 10, width=10)
		tree.column("ord_id",stretch = NO,minwidth = 10, width=150)
		tree.column("ord_nm",stretch = NO,minwidth = 10, width=200)
		tree.column("ord_tot",stretch = NO,minwidth = 10, width=150)
		tree.column("ord_mod",stretch = NO,minwidth = 10, width=150)
		tree.column("ord_pid",stretch = NO,minwidth = 10, width=150)
		tree.column("ord_stat",stretch = NO,minwidth = 10, width=150)
		tree.column("ord_shp",stretch = NO,minwidth = 10, width=150)
		tree.column("ord_trk",stretch = NO,minwidth = 10, width=150)
		tree.column("doa",stretch = NO,minwidth = 10, width=130)
		tree.pack()

		for qur_res in edit_result:
			tree.insert('','end',values=(qur_res[0],qur_res[1],qur_res[2],qur_res[3],qur_res[4],qur_res[5],qur_res[6],qur_res[7],qur_res[8]))

		lbl1 = Label(frm2,text="Select order to edit:")
		but1 = Button(frm2,text="See Products",command=lambda:mg_pro(tree))
		but2 = Button(frm2,text="Pay Approve",command=lambda:mg_app(tree))
		but3 = Button(frm2,text="Pay Reject",command=lambda:mg_rej(tree))
		but4 = Button(frm2,text="Order Shipped",command=lambda:mg_shp(tree))
		but5 = Button(frm2,text="Edit Track ID",command=lambda:mg_shp(tree))
		but6 = Button(frm2,text="Cancel Order",command=lambda:mg_can(tree))
		but7 = Button(frm2,text="Return",command=master_login)
		lbl1.grid(row=0,column=0,columnspan=2)
		but1.grid(row=1,column=0,padx=30,pady=5,ipadx=10)
		but2.grid(row=1,column=1,pady=5,ipadx=10)
		but3.grid(row=1,column=2,padx=30,pady=5,ipadx=10)
		but4.grid(row=1,column=3,pady=5,ipadx=10)
		but5.grid(row=1,column=4,padx=30,pady=5,ipadx=10)
		but6.grid(row=1,column=5,pady=5,ipadx=10)
		but7.grid(row=1,column=6,padx=30,pady=5,ipadx=10)
		frm1.pack()
		frm2.pack()
		mainscrn.mainloop()

def mg_app(tree):
	try:
		ord_id = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Pay Approve Failed!","Please select a order first.")
	else:
		if tree.item(tree.focus())['values'][5] != "Payment Processing" and tree.item(tree.focus())['values'][5] != "Payment Rejected":
			messagebox.showerror("Pay Approve Failed!","Please select a order with status Payment Processing/Rejected.")
		else:
			sql_query = "UPDATE he_orders SET status = 'Payment Approved' where order_no = {}".format(ord_id)
			he_cursor.execute(sql_query)
			he_db.commit()
			messagebox.showinfo("Pay Approve Success!","Order Payment has been Approved.")
			mg_ord()

def mg_rej(tree):
	try:
		ord_id = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Pay Reject Failed!","Please select a order first.")
	else:
		if tree.item(tree.focus())['values'][5] != "Payment Processing" and tree.item(tree.focus())['values'][5] != "Payment Approved":
			messagebox.showerror("Pay Approve Failed!","Please select a order with status Payment Processing/Approved.")
		else:
			sql_query = "UPDATE he_orders SET status = 'Payment Rejected' where order_no = {}".format(ord_id)
			he_cursor.execute(sql_query)
			he_db.commit()
			messagebox.showinfo("Pay Reject Success!","Order Payment has been Rejected.")
			mg_ord()

def mg_shp(tree):
	global mainscrn
	try:
		ord_id = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Order Ship Failed!","Please select a order first.")
	else:
		if tree.item(tree.focus())['values'][5] != "Payment Approved" and tree.item(tree.focus())['values'][5] != "Order Shipped":
			messagebox.showerror("Order Ship Failed!","Please select a order with status Payment Approved/Shipped.")
		else:
			conf = messagebox.askokcancel("Order Ship","Are you sure you want to continue?")
			if conf:
				mainscrn.destroy()
				mainscrn = Tk()
				mainscrn.grab_set()
				mainscrn.focus_force()
				width = 270
				height = 90
				screen_width = mainscrn.winfo_screenwidth()
				screen_height = mainscrn.winfo_screenheight()
				x = (screen_width/2) - (width/2)
				y = (screen_height/2) - (height/2) - (height/12)
				mainscrn.geometry("%dx%d+%d+%d" % (width, height,x,y))
				mainscrn.resizable(0, 0)
				mainscrn.title("Hacking Electronics Shop")
				mainscrn.iconbitmap('images/icon.ico')
				lbl = Label(mainscrn,text="Please enter Tracking Number:")
				ent = Entry(mainscrn,width = 30)
				but = Button(mainscrn,text="OK",command=lambda:track_ent(ent.get(),ord_id))
				lbl.pack(padx=5,pady=5)
				ent.pack(padx=5)
				but.pack(padx=5,pady=5)
				mainscrn.mainloop()

def track_ent(trackid,ord_id):
	global mainscrn
	if len(trackid) > 99:
		messagebox.showerror("Order Ship Failed!","Tracking Number is too long!")
	else:
		sql_query = "UPDATE he_orders SET status = 'Order Shipped', track_id = '{}' where order_no = {}".format(trackid,ord_id)
		he_cursor.execute(sql_query)
		he_db.commit()
		messagebox.showinfo("Order Ship Success!","Order has been Shipped.")
		mg_ord()

def mg_can(tree):
	try:
		ord_id = tree.item(tree.focus())['values'][0]
	except:
		messagebox.showerror("Order Cancel Failed!","Please select a order first.")
	else:
		conf = messagebox.askokcancel("Order Cancel","Are you sure you want to continue?")
		if conf:
			sql_query = "UPDATE he_orders SET status = 'Order Cancelled' where order_no = {}".format(ord_id)
			he_cursor.execute(sql_query)
			he_db.commit()
			messagebox.showinfo("Order Cancel Success!","Order has been Cancelled.")
			mg_ord()

def mg_pro(tree):
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
		style.configure("Treeview",rowheight=56)
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
		but1 = Button(mainscrn,text="Return",command=mg_ord)
		frm1.pack()
		but1.pack(pady=5,ipadx=100)
		mainscrn.mainloop()

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

atexit.register(onExit)

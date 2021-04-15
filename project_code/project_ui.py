##--gui module
import time
from tkinter import *
import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk
import sqlite3
from openpyxl import load_workbook

# make database and users (if not exists already) table at programme start up
with sqlite3.connect('quit1.db') as db:
	c = db.cursor()


#c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT PRIMARY KEY  NOT NULL,NAME   TEXT    NOT NULL,EMPID   INT   NOT NULL,PASSWORD  TEXT    NOT NULL,);')

c.execute('CREATE TABLE IF NOT EXISTS user (username TEXT NOT NULL PRIMARY KEY,'
		  'password TEXT NOT NULL,'
		  'NAME   TEXT    NOT NULL,'
		  'EMPID   INT   NOT NULL);')
db.commit()
db.close()

class rpi_UI:
	def __init__(self):
		if __name__ == '__main__':
			self.window = tk.Tk()
			self.window.overrideredirect(False)
			# ===============================================================
			##--background support for all UI
			self.window.title("Penguin Version")
			self.window.resizable(width=900, height=600)

			self.GUIFrame_default = tk.Frame(self.window, width=900, height=600)
			self.GUIFrame_default.pack(expand=False, anchor=CENTER)
			self.GUIFrame_default.pack()

			# ===============================================================
			##--Supporting IMAGES

			
			self.photo_user_icon = tk.PhotoImage(file="/home/ubuntu18/project2021/Images/icon/icons8-user.png")
			self.photo_user_pwd = tk.PhotoImage(file="/home/ubuntu18/project2021/Images/icon/icons8-password.png")
			self.photo_wrong = tk.PhotoImage(file="/home/ubuntu18/project2021/Images/icon/wrong-icon5.gif")
			self.photo_correct = tk.PhotoImage(file="/home/ubuntu18/project2021/Images/icon/correct.gif")


			self.photo_stockLogo = tk.PhotoImage(file="/home/ubuntu18/project2021/Images/banners/stock.png")
			self.photo_westtek = tk.PhotoImage(file="/home/ubuntu18/project2021/Images/banners/westtek.png")

			self.photo_asiLogo = tk.PhotoImage(file="/home/ubuntu18/project2021/Images/banners/asi_logo_1.png")
			self.photo_user_scn = tk.PhotoImage(file="/home/ubuntu18/project2021/Images/icon/icons8-barcode-scanner.png")

			self.update_log=tk.PhotoImage(file="/home/ubuntu18/project2021/Images/icon/update_icon1.png")

			self.wb = load_workbook("/home/ubuntu18/project2021/data_storage/store_details.xlsx")
			self.sheet = self.wb["Sheet1"]
			self.row_count = self.sheet.max_row
			self.column_count = self.sheet.max_column

			##--FONT TYPE
			self.helv36_login = font.Font(family='Helvetica', size=16, weight='bold')
			self.helv8_login = font.Font(family='Helvetica', size=8, weight='normal')
			self.times_16 = font.Font(family="Times", size=16, weight='normal')
			self.page_one()
			self.window.mainloop()


	def page_one(self):
		##--Login page
		self.GUIFrame_login = tk.Frame(self.GUIFrame_default, width=900, height=600)
		self.GUIFrame_login.pack(expand=False, anchor=CENTER)
		self.GUIFrame_login.place(x=0, y=0)

		##--Login widiget
		self.login_label = tk.Label(self.GUIFrame_login, font=self.helv36_login, text="Login ID", fg='blue',)
		self.login_label.place(x=500, y=350)

		self.loginid = StringVar()
		self.login_entry = tk.Entry(self.GUIFrame_login, font=self.helv36_login, textvariable=self.loginid, width=16)
		self.login_entry.place(x=650, y=350)
		self.login_entry.configure(bg='snow')


		self.ltext_usr = tk.Label(self.GUIFrame_login, image=self.photo_user_icon)
		self.ltext_usr.place(x=610, y=350)
		self.login_entry.bind("<Button-1>", self.login_entry_event)

		##--password widiget
		self.Password_label = tk.Label(self.GUIFrame_login, font=self.helv36_login, text="Password", fg='blue')
		self.Password_label.place(x=500, y=400)

		self.password = StringVar()
		self.password_entry = tk.Entry(self.GUIFrame_login, font=self.helv36_login, textvariable=self.password,
		                               width=16, show="*")
		self.password_entry.place(x=650, y=400)
		self.password_entry.configure(bg='snow')

		self.ltext_pwd = tk.Label(self.GUIFrame_login, image=self.photo_user_pwd)
		self.ltext_pwd.place(x=610, y=400)
		self.password_entry.bind("<Button-1>", self.password_entry_event)
#---check user image check

		self.usr_img_check = tk.Label(self.GUIFrame_login)
		self.usr_img_check.place(x=860, y=350)
		self.pwd_img_check = tk.Label(self.GUIFrame_login)
		self.pwd_img_check.place(x=860, y=400)


		self.ltext1 = tk.Label(self.GUIFrame_login, image=self.photo_stockLogo)
		self.ltext1.place(x=0, y=100)

		self.ltext2 = tk.Label(self.GUIFrame_login, image=self.photo_westtek)
		self.ltext2.place(x=10, y=10)

		self.ltext3 = tk.Label(self.GUIFrame_login, image=self.photo_asiLogo)
		self.ltext3.place(x=500, y=100)

		self.login_text = tk.Label(self.GUIFrame_login, font=self.helv36_login, text=" USER LOGIN ",borderwidth=1, relief="solid")
		self.login_text.place(x=650, y=480)
		self.login_text.bind("<Button-1>",self.pwd_enter)

		self.ltext_scn = tk.Label(self.GUIFrame_login, image=self.photo_user_scn)
		self.ltext_scn.place(x=550, y=460)

		##-Admin Register button to enter numbers
		self.Button_one = tk.Button(self.GUIFrame_login, font=self.helv8_login, bd=1, text='Admin Register',
		                            command=lambda: self.admin_Register(), width=14)
		self.Button_one.place(x=770, y=20)

	def login_entry_event(self, key):
		self.password_entry.configure(bg='snow')
		self.login_entry.configure(bg='SeaGreen1')

	def password_entry_event(self, key):
		self.password_entry.configure(bg='SeaGreen1')
		self.login_entry.configure(bg='snow')

	def pwd_enter(self,key):
		if (self.login_entry.get() == "" and self.password_entry.get() == ""):
			self.usr_img_check.configure(image=self.photo_correct)
			self.pwd_img_check.configure(image=self.photo_correct)
			self.GUIFrame_login.destroy()
			self.page_two()

		elif (self.login_entry.get() == "12345" and self.password_entry.get() != "12345"):
			self.usr_img_check.configure(image=self.photo_correct)
			self.pwd_img_check.configure(image=self.photo_wrong)

		elif (self.login_entry.get() != "12345" and self.password_entry.get() == "12345"):
			self.usr_img_check.configure(image=self.photo_wrong)
			self.pwd_img_check.configure(image=self.photo_correct)

		else:
			self.usr_img_check.configure(image=self.photo_wrong)
			self.pwd_img_check.configure(image=self.photo_wrong)

	def admin_Register(self):
		# --Login page
		self.register_page()

		pass

	def register_page(self):
		self.GUIFrame_login.destroy()
		self.GUIFrame_admin = tk.Frame(self.GUIFrame_default, width=900, height=600)
		self.GUIFrame_admin.pack(expand=False, anchor=CENTER)
		self.GUIFrame_admin.place(x=0, y=0)

		self.ltext2 = tk.Label(self.GUIFrame_admin, image=self.photo_westtek)
		self.ltext2.place(x=10, y=10)
###---------NAME
		self.reg_name_label = tk.Label(self.GUIFrame_admin, font=self.helv36_login, text="NAME:", fg='blue')
		self.reg_name_label.place(x=200, y=100)

		self.name_reg = StringVar()
		self.reg_name_entry = tk.Entry(self.GUIFrame_admin, font=self.helv36_login, textvariable=self.name_reg, width=20)
		self.reg_name_entry.place(x=300, y=100)

###---------Employee ID
		self.reg_emp_label = tk.Label(self.GUIFrame_admin, font=self.helv36_login, text="EMP ID:", fg='blue')
		self.reg_emp_label.place(x=200, y=150)

		self.emp_reg = StringVar()
		self.emp_id_entry = tk.Entry(self.GUIFrame_admin, font=self.helv36_login, textvariable=self.emp_reg,
		                               width=20)
		self.emp_id_entry.place(x=300, y=150)

###---------USER NAME
		self.reg_usr_label = tk.Label(self.GUIFrame_admin, font=self.helv36_login, text="USER NAME:", fg='blue')
		self.reg_usr_label.place(x=150, y=200)

		self.usr_reg = StringVar()
		self.usr_reg_entry = tk.Entry(self.GUIFrame_admin, font=self.helv36_login, textvariable=self.usr_reg,
		                             width=20)
		self.usr_reg_entry.place(x=300, y=200)

###---------USER password
		self.reg_pwd_label = tk.Label(self.GUIFrame_admin, font=self.helv36_login, text="PASSWORD:", fg='blue')
		self.reg_pwd_label.place(x=150, y=250)

		self.pwd_reg = StringVar()
		self.pwd_reg_entry = tk.Entry(self.GUIFrame_admin, font=self.helv36_login, textvariable=self.pwd_reg,show="*",width=20)
		self.pwd_reg_entry.place(x=300, y=250)
###---------save REGISTER BUTTON
		self.Button_reg = tk.Button(self.GUIFrame_admin, font=self.helv36_login, bd=1, text='SAVE ',
		                            command=lambda: self.save_admin_Register(), width=10)
		self.Button_reg.place(x=700, y=520)
###---------Back BUTTON
		self.Button_bck = tk.Button(self.GUIFrame_admin, font=self.helv36_login, bd=1, text='BACK ',
		                            command=lambda: self.back_admin_Register(), width=10)
		self.Button_bck.place(x=100, y=520)

	def save_admin_Register(self):
		print(self.usr_reg.get())
		print(self.pwd_reg.get())
		print(self.emp_reg.get())
		print(self.name_reg.get())
		pass

	def back_admin_Register(self):
		self.GUIFrame_admin.destroy()
		self.page_one()

	def page_two(self):
		self.GUIFrame_login.destroy()
		self.GUIFrame_page_two = tk.Frame(self.GUIFrame_default, width=900, height=600)
		self.GUIFrame_page_two.pack(expand=False, anchor=CENTER)
		self.GUIFrame_page_two.place(x=0, y=0)

		self.ltext1 = tk.Label(self.GUIFrame_page_two, image=self.photo_stockLogo)
		self.ltext1.place(x=0, y=100)

		self.ltext2 = tk.Label(self.GUIFrame_page_two, image=self.photo_westtek)
		self.ltext2.place(x=10, y=10)
###---------Dispense BUTTON
		self.Button_admin_up = tk.Button(self.GUIFrame_page_two, font=self.helv36_login, bd=2, text='ADMIN UPDATE',
		                            command=lambda: self.admin_update_btn(),width=20)
		self.Button_admin_up.place(x=600, y=120)

###---------Refill BUTTON
		self.Button_view = tk.Button(self.GUIFrame_page_two, font=self.helv36_login, bd=1, text='VIEW STOCK ',
		                             command=lambda: self.viewStock_btn(), width=20)
		self.Button_view.place(x=600, y=200)

###---------Refill BUTTON
		self.Button_ind = tk.Button(self.GUIFrame_page_two, font=self.helv36_login, bd=1, text='INDENT STOCK ',
		                             command=lambda: self.indentStock_btn(), width=20)
		self.Button_ind.place(x=600, y=280)

###---------History BUTTON
		self.Button_htry = tk.Button(self.GUIFrame_page_two, font=self.helv36_login, bd=1, text='HISTORY ',
		                             command=lambda: self.history_btn(), width=20)
		self.Button_htry.place(x=600, y=360)

		###---------Logout BUTTON
		self.Button_log_out = tk.Button(self.GUIFrame_page_two, font=self.helv36_login, bd=1, text='LOGOUT ',
									 command=lambda: self.logout_btn(), width=15)
		self.Button_log_out.place(x=100, y=500)

	def logout_btn(self):
		self.GUIFrame_page_two.destroy()
		self.page_one()

#####################################ADMIN BUTTON########################################################
	def admin_update_btn(self):
		print("admin button")
		self.GUIFrame_page_two.destroy()
		self.GUIFrame_admin_update = tk.Frame(self.GUIFrame_default, width=900, height=600)
		self.GUIFrame_admin_update.pack(expand=False, anchor=CENTER)
		self.GUIFrame_admin_update.place(x=0, y=0)

		self.ltext2 = tk.Label(self.GUIFrame_admin_update, image=self.photo_westtek)
		self.ltext2.place(x=10, y=10)

		###---------Admin Logout BUTTON
		self.Button_log_out = tk.Button(self.GUIFrame_admin_update, font=self.helv36_login, bd=1, text='LOGOUT ',
										command=lambda: self.logoutAdmin_btn(), width=10)
		self.Button_log_out.place(x=100, y=500)

		###---------Admin back BUTTON
		self.Button_backAdmin = tk.Button(self.GUIFrame_admin_update, font=self.helv36_login, bd=1, text='BACK ',
										command=lambda: self.adminBack_btn(), width=10)
		self.Button_backAdmin.place(x=600, y=500)

		###---------Admin  Material code
		self.adminMaterialCode_Label = tk.Label(self.GUIFrame_admin_update, font=self.helv36_login, text="Material Code")
		self.adminMaterialCode_Label.place(x=50, y=150)

		self.adminMaterialCode_Var = StringVar()
		self.adminMaterialCode_Entry = tk.Entry(self.GUIFrame_admin_update, font=self.helv36_login, textvariable=self.adminMaterialCode_Var,
									  width=15)
		self.adminMaterialCode_Entry.place(x=50, y=180)


		###---------Admin  Material Description
		self.adminMaterialDesc_Label = tk.Label(self.GUIFrame_admin_update, font=self.helv36_login, text="Material Description")
		self.adminMaterialDesc_Label.place(x=270, y=150)

		self.adminMaterialDesc_Var = StringVar()
		self.adminMaterialDesc_Entry = tk.Entry(self.GUIFrame_admin_update, font=self.helv36_login,
											textvariable=self.adminMaterialDesc_Var,width=25)
		self.adminMaterialDesc_Entry.place(x=270, y=180)


		###---------Admin  store location
		self.adminStoreLoc_Label = tk.Label(self.GUIFrame_admin_update, font=self.helv36_login, text="Location")
		self.adminStoreLoc_Label.place(x=600, y=150)

		self.adminStoreLoc_Var = StringVar()
		self.adminStoreLoc_Entry = tk.Entry(self.GUIFrame_admin_update, font=self.helv36_login,
											textvariable=self.adminStoreLoc_Var,width=10)
		self.adminStoreLoc_Entry.place(x=600, y=180)

		###---------Admin  Batch
		self.adminBatch_Label = tk.Label(self.GUIFrame_admin_update, font=self.helv36_login, text="Batch")
		self.adminBatch_Label.place(x=50, y=240)

		self.adminBatch_Var = StringVar()
		self.adminBatch_Entry = tk.Entry(self.GUIFrame_admin_update, font=self.helv36_login,
											textvariable=self.adminBatch_Var, width=10)
		self.adminBatch_Entry.place(x=50, y=280)

		###---------Admin  Unrestricted
		self.adminUnrestricted_Label = tk.Label(self.GUIFrame_admin_update, font=self.helv36_login, text="Unrestricted")
		self.adminUnrestricted_Label.place(x=250, y=240)

		self.adminUnrestricted_Var = StringVar()
		self.adminUnrestricted_Entry = tk.Entry(self.GUIFrame_admin_update, font=self.helv36_login,
											textvariable=self.adminUnrestricted_Var, width=10)
		self.adminUnrestricted_Entry.place(x=250, y=280)

		###---------Admin  Measure
		self.adminMeasure_Label = tk.Label(self.GUIFrame_admin_update, font=self.helv36_login, text="Measure")
		self.adminMeasure_Label.place(x=450, y=240)

		self.adminMeasure_Var = StringVar()
		self.adminMeasure_Entry = tk.Entry(self.GUIFrame_admin_update, font=self.helv36_login,
											textvariable=self.adminMeasure_Var, width=10)
		self.adminMeasure_Entry.place(x=450, y=280)

		##-Admin Update button
		self.adminUpdateBtn = tk.Button(self.GUIFrame_admin_update, font=self.helv36_login, bd=2, text=' UPDATE ',
									command=lambda: self.admin_update_value(),image=self.update_log,compound=LEFT)
		self.adminUpdateBtn.place(x=550, y=400)

	def adminBack_btn(self):
		self.GUIFrame_admin_update.destroy()
		self.page_two()

	def logoutAdmin_btn(self):
		self.GUIFrame_admin_update.destroy()
		self.page_one()

	def admin_update_value(self):
		pass
#########################################VIEW BUTTON#################################################
	def viewStock_btn(self):
		print("view stock")
		self.GUIFrame_page_two.destroy()
		self.GUIFrame_view_stock = tk.Frame(self.GUIFrame_default, width=900, height=600)
		self.GUIFrame_view_stock.pack(expand=False, anchor=CENTER)
		self.GUIFrame_view_stock.place(x=0, y=0)

		self.ltext2 = tk.Label(self.GUIFrame_view_stock, image=self.photo_westtek)
		self.ltext2.place(x=10, y=10)

		# ---scrollbar frame
		self.GUIFramescrollbar = tk.Frame(self.GUIFrame_view_stock, width=600, height=400)
		self.GUIFramescrollbar.place(x=20, y=100)

		# ---scrollbar initilization
		self.scrollbar_y = Scrollbar(self.GUIFramescrollbar, width=40)
		self.scrollbar_y.pack(side=RIGHT, fill=Y)

		self.scrollbar_x = Scrollbar(self.GUIFramescrollbar, width=32, orient=HORIZONTAL)
		self.scrollbar_x.pack(side=BOTTOM, fill=X)

		# ---textbox frame
		self.txt = tk.Text(self.GUIFramescrollbar, height=20, width=100, wrap=tk.NONE,
						   xscrollcommand=self.scrollbar_x.set,
						   yscrollcommand=self.scrollbar_y.set)
		self.txt.pack()

		# ---adding scrollbar to text
		self.scrollbar_y.config(command=self.txt.yview)
		self.scrollbar_x.config(command=self.txt.xview)

		self.txt.configure(state='normal')
		self.txt.delete(1.0, END)
		for i in range(1, self.row_count + 1):
			for j in range(1, self.column_count + 1):
				data = self.sheet.cell(row=i, column=j).value
				if (j == 1):
					self.txt.insert(tk.END, str(data).ljust(5)+' | ')
				elif (j == 2):
					self.txt.insert(tk.END, str(data).ljust(10)+' | ')
				elif(j == 3):
					self.txt.insert(tk.END, str(data).ljust(40)+' | ')
				elif(j == 4):
				 	self.txt.insert(tk.END, str(data).ljust(18)+' | ')
				elif (j == 5):
					self.txt.insert(tk.END, str(data).ljust(10)+' | ')
				elif (j == 6):
					self.txt.insert(tk.END, str(data).ljust(12)+' | ')
				elif (j == 7):
					self.txt.insert(tk.END, str(data).ljust(10)+' | ')
			self.txt.insert(tk.INSERT,'\n')
		self.txt.configure(state='disable')
		###--------- view Logout BUTTON
		self.Button_log_out = tk.Button(self.GUIFrame_view_stock, font=self.helv36_login, bd=1, text='LOGOUT ',
										command=lambda: self.logoutview_btn(), width=10)
		self.Button_log_out.place(x=50, y=500)

		###---------view back BUTTON
		self.Button_backAdmin = tk.Button(self.GUIFrame_view_stock, font=self.helv36_login, bd=1, text='BACK ',
										command=lambda: self.viewBack_btn(), width=10)
		self.Button_backAdmin.place(x=650, y=500)

	def viewBack_btn(self):
		self.GUIFrame_view_stock.destroy()
		self.page_two()

	def logoutview_btn(self):
		self.GUIFrame_view_stock.destroy()
		self.page_one()

	#########################################INDENT BUTTON#################################################
	def indentStock_btn(self):
		print("indent stock")
		self.GUIFrame_page_two.destroy()
		self.GUIFrame_indentStock = tk.Frame(self.GUIFrame_default, width=900, height=600)
		self.GUIFrame_indentStock.pack(expand=False, anchor=CENTER)
		self.GUIFrame_indentStock.place(x=0, y=0)

		self.ltext2 = tk.Label(self.GUIFrame_indentStock, image=self.photo_westtek)
		self.ltext2.place(x=10, y=10)

		###--------- indent Logout BUTTON
		self.Button_log_out = tk.Button(self.GUIFrame_indentStock, font=self.helv36_login, bd=1, text='LOGOUT ',
										command=lambda: self.logoutindent_btn(), width=10)
		self.Button_log_out.place(x=100, y=500)

		###---------indent back BUTTON
		self.Button_backAdmin = tk.Button(self.GUIFrame_indentStock, font=self.helv36_login, bd=1, text='BACK ',
										  command=lambda: self.indentBack_btn(), width=10)
		self.Button_backAdmin.place(x=600, y=500)
		self.options = [
			"User 1",
			"User 2",
			"User 3",
			"User 4",
			"User 5",
			"User 6",
			"User 7"
		]
		# datatype of menu text
		self.clicked = StringVar()

		# initial menu text
		self.clicked.set("User 1")

		# Create Dropdown menu
		self.drop = tk.OptionMenu(self.GUIFrame_indentStock, self.clicked, *self.options)
		self.drop.config(width=10, font=self.helv36_login)
		menu = self.GUIFrame_indentStock.nametowidget(self.drop.menuname)
		menu.config(font=self.helv36_login)  # Set the dropdown menu's font
		self.drop.place(x=700, y=100)


		# ---scrollbar frame
		self.GUIFramescrollbarIndent = tk.Frame(self.GUIFrame_indentStock, width=400, height=400)
		self.GUIFramescrollbarIndent.place(x=30, y=110)

		# ---scrollbar initilization
		self.scrollbar_yIndent = Scrollbar(self.GUIFramescrollbarIndent, width=40)
		self.scrollbar_yIndent.pack(side=RIGHT, fill=Y)

		self.scrollbar_xIndent = Scrollbar(self.GUIFramescrollbarIndent, width=32, orient=HORIZONTAL)
		self.scrollbar_xIndent.pack(side=BOTTOM, fill=X)

		# ---textbox frame
		self.txtIndent = tk.Text(self.GUIFramescrollbarIndent, height=20, width=50, wrap=tk.NONE,
						   xscrollcommand=self.scrollbar_xIndent.set,
						   yscrollcommand=self.scrollbar_yIndent.set)
		self.txtIndent.pack()

		# ---adding scrollbar to text
		self.scrollbar_yIndent.config(command=self.txtIndent.yview)
		self.scrollbar_xIndent.config(command=self.txtIndent.xview)

		self.txtIndent.configure(state='normal')
		self.txtIndent.delete(1.0, END)

		###---------Reject button
		self.Button_rejectIndent = tk.Button(self.GUIFrame_indentStock, font=self.helv36_login, bd=1, text='Reject ',
										  command=lambda: self.indentReject_btn(), width=10)
		self.Button_rejectIndent.place(x=500, y=180)

		###---------Accept button
		self.Button_acceptIndent = tk.Button(self.GUIFrame_indentStock, font=self.helv36_login, bd=1, text='Accept ',
											 command=lambda: self.indentAccept_btn(), width=10)
		self.Button_acceptIndent.place(x=500, y=230)

		###---------Update button
		self.Button_updateIndent = tk.Button(self.GUIFrame_indentStock, font=self.helv36_login, bd=1, text='Update ',
											 command=lambda: self.indentUpdate_btn(), width=10)
		self.Button_updateIndent.place(x=650, y=400)

	def indentBack_btn(self):
		self.Button_backAdmin.destroy()
		self.page_two()

	def logoutindent_btn(self):
		self.Button_backAdmin.destroy()
		self.page_one()

	def indentReject_btn(self):
		pass

	def indentAccept_btn(self):
		pass
#########################################HISTORY BUTTON#################################################
	def history_btn(self):
		print("history")
		self.GUIFrame_page_two.destroy()
		self.GUIFrame_history = tk.Frame(self.GUIFrame_default, width=900, height=600)
		self.GUIFrame_history.pack(expand=False, anchor=CENTER)
		self.GUIFrame_history.place(x=0, y=0)

		###---------Logout BUTTON
		self.Button_history_out = tk.Button(self.GUIFrame_history, font=self.helv36_login, bd=1, text='LOGOUT ',
										command=lambda: self.logouthistory_btn(), width=15)
		self.Button_history_out.place(x=100, y=500)

		###---------indent back BUTTON
		self.Button_backHistory = tk.Button(self.GUIFrame_history, font=self.helv36_login, bd=1, text='BACK ',
										  command=lambda: self.historyBack_btn(), width=10)
		self.Button_backHistory.place(x=600, y=500)

	def historyBack_btn(self):
		self.GUIFrame_history.destroy()
		self.page_two()

	def logouthistory_btn(self):
		self.GUIFrame_history.destroy()
		self.page_one()
rpi_UI()
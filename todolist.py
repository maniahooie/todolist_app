import sqlite3
from PyQt5 import QtCore
from PyQt5 import uic
import sys
from datetime import datetime
from PyQt5.Qt import *

class UI(QMainWindow):
	def __init__(self):
		super(UI, self).__init__()

		# load the ui file
		uic.loadUi("todo_cust.ui", self)

		# define our widgets
		self.listwidget1 = self.findChild(QListWidget, "listWidget_1")
		self.lineedit1 = self.findChild(QLineEdit, "lineEdit_1")
		self.button1 = self.findChild(QPushButton, "pushButton_1")

		self.listwidget2 = self.findChild(QListWidget, "listWidget_2")
		self.lineedit2 = self.findChild(QLineEdit, "lineEdit_2")
		self.button2 = self.findChild(QPushButton, "pushButton_2")

		self.listwidget3 = self.findChild(QListWidget, "listWidget_3")
		self.lineedit3 = self.findChild(QLineEdit, "lineEdit_3")
		self.button3 = self.findChild(QPushButton, "pushButton_3")

		self.listwidget4 = self.findChild(QListWidget, "listWidget_4")
		self.lineedit4 = self.findChild(QLineEdit, "lineEdit_4")
		self.button4 = self.findChild(QPushButton, "pushButton_4")

		self.listwidget5 = self.findChild(QListWidget, "listWidget_5")
		self.lineedit5 = self.findChild(QLineEdit, "lineEdit_5")
		self.button5 = self.findChild(QPushButton, "pushButton_5")

		self.calendar = self.findChild(QCalendarWidget, "calendarWidget")
		# self.label = self.findChild(QLabel, "label_7")

		self.lcd = self.findChild(QLCDNumber, "lcdNumber")

		# connect the calendar to the function
		self.calendar.selectionChanged.connect(self.grab_date)

		# create a timer
		self.timer = QTimer()
		self.timer.timeout.connect(self.lcd_number)

		# start the timer and update every second
		self.timer.start(1000)

		# call the lcd function
		self.lcd_number()

		# connect the button to the function
		self.button1.clicked.connect(self.add_it)
		self.button2.clicked.connect(self.add_it2)
		self.button3.clicked.connect(self.add_it3)
		self.button4.clicked.connect(self.add_it4)
		self.button5.clicked.connect(self.add_it5)

		self.grab_date()
		self.grab_date2()
		self.grab_date3()
		self.grab_date4()
		self.grab_date5()

		# show the app
		self.show()

	def grab_date(self):
		dateSelected = self.calendar.selectedDate().toPyDate()
		self.updatetasklist(dateSelected)

	def grab_date2(self):
		dateSelected = self.calendar.selectedDate().toPyDate()
		self.updatetasklist2(dateSelected)

	def grab_date3(self):
		dateSelected = self.calendar.selectedDate().toPyDate()
		self.updatetasklist3(dateSelected)

	def grab_date4(self):
		dateSelected = self.calendar.selectedDate().toPyDate()
		self.updatetasklist4(dateSelected)

	def grab_date5(self):
		dateSelected = self.calendar.selectedDate().toPyDate()
		self.updatetasklist5(dateSelected)


	def updatetasklist(self, date):
		self.listwidget1.clear()
		db = sqlite3.connect("data.db")
		cursor = db.cursor()

		query = "SELECT task, timeline FROM tasks WHERE date = ?"
		row = (date,)
		results = cursor.execute(query, row).fetchall()
		for result in results:
			item = QListWidgetItem(str(result[0]))
			item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)

			if result[1] == "Yes":
				item.setCheckState(QtCore.Qt.Checked)
			elif result[1] == "No":
				item.setCheckState(QtCore.Qt.Unchecked)
			self.listwidget1.addItem(item)

	def updatetasklist2(self, date):
		self.listwidget2.clear()
		db = sqlite3.connect("data.db")
		cursor = db.cursor()

		query = "SELECT task, timeline FROM doing WHERE date = ?"
		row = (date,)
		results = cursor.execute(query, row).fetchall()
		for result in results:
			item = QListWidgetItem(str(result[0]))
			item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)

			if result[1] == "Yes":
				item.setCheckState(QtCore.Qt.Checked)
			elif result[1] == "No":
				item.setCheckState(QtCore.Qt.Unchecked)
			self.listwidget2.addItem(item)

	def updatetasklist3(self, date):
		self.listwidget3.clear()
		db = sqlite3.connect("data.db")
		cursor = db.cursor()

		query = "SELECT task, timeline FROM done WHERE date = ?"
		row = (date,)
		results = cursor.execute(query, row).fetchall()
		for result in results:
			item = QListWidgetItem(str(result[0]))
			item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)

			if result[1] == "Yes":
				item.setCheckState(QtCore.Qt.Checked)
			elif result[1] == "No":
				item.setCheckState(QtCore.Qt.Unchecked)
			self.listwidget3.addItem(item)

	def updatetasklist4(self, date):
		self.listwidget4.clear()
		db = sqlite3.connect("data.db")
		cursor = db.cursor()

		query = "SELECT task, timeline FROM urgent WHERE date = ?"
		row = (date,)
		results = cursor.execute(query, row).fetchall()
		for result in results:
			item = QListWidgetItem(str(result[0]))
			item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)

			if result[1] == "Yes":
				item.setCheckState(QtCore.Qt.Checked)
			elif result[1] == "No":
				item.setCheckState(QtCore.Qt.Unchecked)
			self.listwidget4.addItem(item)

	def updatetasklist5(self, date):
		self.listwidget5.clear()
		db = sqlite3.connect("data.db")
		cursor = db.cursor()

		query = "SELECT task, timeline FROM nonsignificant WHERE date = ?"
		row = (date,)
		results = cursor.execute(query, row).fetchall()
		for result in results:
			item = QListWidgetItem(str(result[0]))
			item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)

			if result[1] == "Yes":
				item.setCheckState(QtCore.Qt.Checked)
			elif result[1] == "No":
				item.setCheckState(QtCore.Qt.Unchecked)
			self.listwidget5.addItem(item)

	def lcd_number(self):
		# get the time
		time = datetime.now()
		formatted_time = time.strftime("%I:%M:%S %p")

		# set number of LCD digits
		self.lcd.setDigitCount(12)
		# make text flat (no white outline)
		self.lcd.setSegmentStyle(QLCDNumber.Flat)

		# display the time
		self.lcd.display(formatted_time)


	def add_it(self):
		db = sqlite3.connect("data.db")
		cursor = db.cursor()

		newtask =  str(self.lineedit1.text())
		date = self.calendar.selectedDate().toPyDate()

		query = "INSERT INTO tasks(task, date, timeline) VALUES (?,?,?)"
		row = (newtask, date, "timeline")

		cursor.execute(query, row)
		db.commit()
		self.updatetasklist(date)
		self.lineedit1.clear()

	def add_it2(self):
		db = sqlite3.connect("data.db")
		cursor = db.cursor()

		newtask =  str(self.lineedit2.text())
		date = self.calendar.selectedDate().toPyDate()

		query = "INSERT INTO doing(task, date, timeline) VALUES (?,?,?)"
		row = (newtask, date, "timeline")

		cursor.execute(query, row)
		db.commit()
		self.updatetasklist2(date)
		self.lineedit2.clear()

	def add_it3(self):
		db = sqlite3.connect("data.db")
		cursor = db.cursor()

		newtask =  str(self.lineedit3.text())
		date = self.calendar.selectedDate().toPyDate()

		query = "INSERT INTO done(task, date, timeline) VALUES (?,?,?)"
		row = (newtask, date, "timeline")

		cursor.execute(query, row)
		db.commit()
		self.updatetasklist3(date)
		self.lineedit3.clear()

	def add_it4(self):
		db = sqlite3.connect("data.db")
		cursor = db.cursor()

		newtask =  str(self.lineedit4.text())
		date = self.calendar.selectedDate().toPyDate()

		query = "INSERT INTO urgent(task, date, timeline) VALUES (?,?,?)"
		row = (newtask, date, "timeline")

		cursor.execute(query, row)
		db.commit()
		self.updatetasklist4(date)
		self.lineedit4.clear()

	def add_it5(self):
		db = sqlite3.connect("data.db")
		cursor = db.cursor()

		newtask =  str(self.lineedit5.text())
		date = self.calendar.selectedDate().toPyDate()

		query = "INSERT INTO nonsignificant(task, date, timeline) VALUES (?,?,?)"
		row = (newtask, date, "timeline")

		cursor.execute(query, row)
		db.commit()
		self.updatetasklist5(date)
		self.lineedit5.clear()


# initialize the app
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
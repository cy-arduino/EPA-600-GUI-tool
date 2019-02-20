#Author: ChihYing_Lin

from tkinter import *
import epa600
				
class EPA600GUI(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)

		self.epa600 = epa600.EPA600CTL()
		
		self.grid()
		self.createWidgets()
	
	def cbConn(self):
		#print (self.comEntry.get())
		self.epa600.connect(com=self.comEntry.get())
		self.conStatusLabel["text"] = self.epa600.getStatus()
	
	def cbSetVal(self):
		val = int(self.valueEntry.get())
		self.epa600.setValue(val)
		self.valueShowLabel["text"] = self.epa600.getValue()
		
	def cbValInc1(self):
		val = self.epa600.getValue()
		print(val)
		val += 1
		self.epa600.setValue(val)
		self.valueShowLabel["text"] = self.epa600.getValue()
	
	def cbValDec1(self):
		val = self.epa600.getValue()
		val -= 1
		self.epa600.setValue(val)
		self.valueShowLabel["text"] = self.epa600.getValue()

	def createWidgets(self):
		self.mGridRow = 0

		self.mGridRow += 1
		self.cLabel = Label(self)
		self.cLabel["text"] = "Com:"
		self.cLabel.grid(row=self.mGridRow, column=0)
		
		self.comEntry = Entry(self)
		self.comEntry["width"] = 8
		self.comEntry.grid(row=self.mGridRow, column=1)
		self.comEntry.insert(0, "COM156")		
				
		self.mGridRow += 1
		self.connBtn = Button(self)
		self.connBtn["text"] = "CONNECT"
		self.connBtn.grid(row=self.mGridRow, column=0)
		self.connBtn["command"] = self.cbConn
		
		self.discBtn = Button(self)
		self.discBtn["text"] = "DISCONNECT"
		self.discBtn.grid(row=self.mGridRow, column=1)

		self.mGridRow += 1
		self.sLabel = Label(self)
		self.sLabel["text"] = "Status:"
		self.sLabel.grid(row=self.mGridRow, column=0)
		
		self.conStatusLabel = Label(self)
		self.conStatusLabel["text"] = ""
		self.conStatusLabel.grid(row=self.mGridRow, column=1)

		self.mGridRow += 1
		self.vsLabel = Label(self)
		self.vsLabel["text"] = "Value:"
		self.vsLabel.grid(row=self.mGridRow, column=0)
		
		self.valueShowLabel = Label(self)
		self.valueShowLabel["text"] = ""
		self.valueShowLabel.grid(row=self.mGridRow, column=1)
		
		self.mGridRow += 1
		self.svLabel = Label(self)
		self.svLabel["text"] = "Set:"
		self.svLabel.grid(row=self.mGridRow, column=0)
		
		self.valueEntry = Entry(self)
		self.valueEntry["width"] = 8
		self.valueEntry.grid(row=self.mGridRow, column=1)
		
		self.mGridRow += 1
		self.valueApplyBtn = Button(self)
		self.valueApplyBtn["text"] = "APPLY"
		self.valueApplyBtn.grid(row=self.mGridRow, column=1)
		self.valueApplyBtn["command"] = self.cbSetVal
		
		self.mGridRow += 1
		self.emptyLabel = Label(self)
		self.emptyLabel["text"] = " "
		self.emptyLabel.grid(row=self.mGridRow, column=0)
		
		self.mGridRow += 1
		self.inc1Btn = Button(self)
		self.inc1Btn["text"] = "+1"
		self.inc1Btn.grid(row=self.mGridRow, column=0)
		self.inc1Btn["command"] = self.cbValInc1
		
		self.dec1Btn = Button(self)
		self.dec1Btn["text"] = "-1"
		self.dec1Btn.grid(row=self.mGridRow, column=1)
		self.dec1Btn["command"] = self.cbValDec1

		
if __name__ == '__main__':
	root = Tk()
	app = EPA600GUI(master=root)
	app.mainloop()
	
	'''
	epa600 = EPA600CTL()
	epa600.connect("COM156")
	print("get status:" + repr(epa600.getStatus()))
	
	epa600.setValue(10)
	print("get value: " + repr(epa600.getValue()))
	'''
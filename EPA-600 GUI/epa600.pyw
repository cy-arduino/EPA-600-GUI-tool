#Author: ChihYing_Lin

from tkinter import *
import serial
import time

class EPA600CTL():
	def __init__(self):
		#pyserial
		self.ser = None
		
		#com port
		self.com = None
		
		#status
		self.connected = 0
		
	def getStatus(self):
		"""getStatus
			return
				1: connected
				0: not connected
		"""
		return self.connected

	def disconnect(self):
		"""disconnect EPA600
			return
				None
		"""
		if self.ser != None:
			self.ser.close()
		self.connected = 0
		self.ser = None
		 
	def connect(self, com):
		"""connect EPA600
			return
				-1: error
		"""
		self.com = com
		print("com port: ")
		print(self.com)
		if self.com == "" or self.com == None:
			print("error: com port is invalid, do nothing")
			self.connected = 0
			return -1
		
		if self.ser != None:
			self.ser.close()
			self.ser = None
			
		self.ser = serial.Serial(self.com, timeout=1)
		self.ser.close()
		try:
			self.ser.open()
		except:
			print("error: com port open failed")
			self.connected = 0
			return -1

		print("com port open success")
		self.connected = 1
			
	def getValue(self):
		"""get value
			return
				-1: error
		"""
		if self.connected != 1:
			print("error: cannot get value before connect")
			return -1
		
		cmd = str.encode("V?;")
		try:
			self.ser.write(cmd)
			#wait for response
			time.sleep(0.1)
			b = self.ser.inWaiting()
			ret = self.ser.read(b)
			ret = ret.decode('ASCII')
			print("return1: " + ret)
			ret=ret.replace(';','')
			ret=ret.replace('V','')
			#ret = ret[2:len(ret)-1]
			print("return2: " + ret)
			ret = float(ret)
			print("getValue: ")
			print(ret)
			return ret
		except:
			print("error: get value failed")
			return -1
		
			
	def setValue(self, val):
		"""set value
			input
				int, range 0-95
			return
				-1: error
		"""
		if self.connected != 1:
			print("error: cannot set value before connect")
			return -1
		
		if val < 0 or val > 95:
			print("error: cannot set value. not in range(0-95)")
			return -1
		
		cmd = str.encode("V" + str(val) + ";")
		try:
			self.ser.write(cmd)
		except:
			print("error: set value failed")
			return -1
			
		print("set value success")
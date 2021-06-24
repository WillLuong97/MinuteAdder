#Program to test the minute adder program 

import unittest
import minuteAdder

class TestMinutesAdder(unittest.TestCase):
	def test_add_1(self):
		minute = 1
		timestamp = "5:02 PM"
		desired = "5:03 PM"
		result = minuteAdder.addMinute(timestamp, minute)
		
		#assertion test to check the desired and computed values 
		self.assertEqual(desired, result)

	def test_add_2(self):
		minute = 60
		timestamp = "5:02 PM"
		desired = "6:02 PM"
		result = minuteAdder.addMinute(timestamp, minute)
		
		#assertion test to check the desired and computed values 
		self.assertEqual(desired, result)

	def test_add_3(self):
		minute = 200
		timestamp = "9:13 AM"
		desired = "12:33 PM"
		result = minuteAdder.addMinute(timestamp, minute)
		
		#assertion test to check the desired and computed values 
		self.assertEqual(desired, result)
	
	def test_add_4(self):
		minute = 60
		timestamp = "9:13 AM"
		desired = "10:13 AM"
		result = minuteAdder.addMinute(timestamp, minute)
		
		#assertion test to check the desired and computed values 
		self.assertEqual(desired, result)

	def test_add_5(self):
		minute = 2
		timestamp = "9:13 AM"
		desired = "9:15 AM"
		result = minuteAdder.addMinute(timestamp, minute)
		
		#assertion test to check the desired and computed values 
		self.assertEqual(desired, result)

	def test_add_6(self):
		minute = 200
		timestamp = ""
		desired = "Invalid Timestamp: Empty String..."
		result = minuteAdder.addMinute(timestamp, minute)
		
		#assertion test to check the desired and computed values 
		self.assertEqual(desired, result)

	def test_add_7(self):
		minute = -60
		timestamp = "12:57 PM"
		desired = "11:57 AM"
		result = minuteAdder.addMinute(timestamp, minute)
		
		#assertion test to check the desired and computed values 
		self.assertEqual(desired, result)


	def test_add_8(self):
		minute = -2
		timestamp = "11:45 PM"
		desired = "11:43 PM"
		result = minuteAdder.addMinute(timestamp, minute)
		
		#assertion test to check the desired and computed values 
		self.assertEqual(desired, result)

	def test_add_9(self):
		minute = 120
		timestamp = "11:45 PM"
		desired = "1:45 AM"
		result = minuteAdder.addMinute(timestamp, minute)
		
		#assertion test to check the desired and computed values 
		self.assertEqual(desired, result)

	def test_add_10(self):
		minute = -120
		timestamp = "11:45 PM"
		desired = "9:45 PM"
		result = minuteAdder.addMinute(timestamp, minute)
		
		#assertion test to check the desired and computed values 
		self.assertEqual(desired, result)

if __name__ == '__main__':
	unittest.main()

#Problem statement: 
'''
Without using any built-in date or time functions, write a function or method that accepts two
mandatory arguments: the first argument is a 12-hour time string with the format &quot;[H]H:MM
{AM|PM}&quot;, and the second argument is a (signed) integer. The second argument is the number
of minutes to add to the time of day represented by the first argument. The return value should
be a string of the same format as the first argument. For example, AddMinutes(&quot;9:13 AM&quot;, 200)
would return 12:33
'''

'''
Observation:

The total length of time would be 7 if the hour is between 0 and 9 and 
the length of time would 8 if the hour is 10 - 12

example: "5:03 PM" => len(time) = 7
example: "12:12 PM" => len(time) = 8

Approach: 

Convert the given timestamp into an integer that represent its minute, then add the given number of minutes to the
coverted timestamp, then convert that into a string and return that string

time complexity: O(n), the algorithm will have to run through the length of the string to see i 
space complexity: O(n), we are storing space for the final string to be returned to. 
'''
def addMinute(time, minutes):
	#base case: 
	if(len(time) == 0): 
		return "Invalid Timestamp: Empty String..."
	n = len(time)
	#Result timestamp after the conversion 
	result = ""

	#variable to hold the hours and minute in the string timestamp 
	str_hour = 0
	str_minute = 0
	#the full timestamp in minute after adding the input minute
	converted_minute = 0
	#status to determine if the final result string should be in AM or PM
	status = "AM" 

	#converting the hours and mintues mark in the string into an integer
	if n == 7:
		str_hour= int(time[0])
		str_minute = int(time[2:4])
	if n == 8:
		str_hour = int(time[0:2])
		str_minute = int(time[3:5])
	
	#check to see if the timestamp is currently is the PM or AM mode
	if  time[n-2:n] == "PM" and str_hour != 12:
		#if the hour is PM, add the current hour to 12
		str_hour += 12

	
	#Convert the hour into minute and add the given minute into it as well
	converted_minute = str_hour * 60 + str_minute + minutes
	#The hour and minute found from the computed minutes
	res_hour = converted_minute // 60
	res_minute = converted_minute % 60
	
	#Checking to see if the new timestamp is in AM or PM
	if(res_hour == 12):
		status = "PM"
	if(res_hour > 12 and res_hour < 24):
		res_hour -= 12
		status = "PM"

	#If the hour is greater than 24, then we will reset the time to 0
	if(res_hour >= 24):
		res_hour -= 24

	#build the result string
	result += str(res_hour)
	result += ":"
	#minute is a single digit: 
	if(res_minute < 10):
		result += '0' + str(res_minute)
	else: 
		result += str(res_minute)
	result += " "
	result += status

	return result
		

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
Approach: Convert the given timestamp into an integer that represent its minute, then add the given number of minutes to the
coverted timestamp, then convert that into a string and return that string

time complexity: O(n), the algorithm will have to run through the length of the string to see i 
space complexity: O(1), we are not storing any extra spcaes

Observation: the total length of time would be 7 if the hour is between 0 and 9 and 
the length of time would 8 if the hour is 10 - 12

example: "5:03 PM" => len(time) = 7
example: "12:12 PM" => len(time) = 8

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
	
	#debugging
	#print(hour, minute)
	#print(time[n-1])
	#determine to see if the timestamp is currently is the PM or AM mode
	if time[n-2] == 'P' and str_hour != 12:
		#if the hour is PM, add the current hour to 12
		str_hour += 12

	#Debuggin: PM conversion
	#return [hour, minute]
	
	#Convert the hour into minute and add the given minute into it as well
	converted_minute = str_hour * 60 + str_minute + minutes
	
	#Since we are looking for the return value to be in a string and it has to be in the timestamp format, we will now convert
	#the converted_minute into hours and set it to hh:mm format
	
	#The hour found from the computed minutes
	res_hour = converted_minute // 60
	res_minute = converted_minute % 60
	
	#Debugging
	#return [res_hour, res_minute]
	if(res_hour > 12 and res_hour < 24):
		res_hour -= 12

	if(res_hour >= 12 and res_hour < 24):
		status = "PM"

	if(res_hour == 24):
		res_hour = 0

	#build the result string
	result += str(res_hour)
	result += ":"
	result += str(res_minute)
	result += " "
	result += status

	return result
		
			
	
	
	
	





def main():

	print("TESTING MINUTE ADDER...")
	print(addMinute("9:13 AM", 200))
	print(addMinute("12:12 PM", -290))
	print(addMinute("2:12 PM", -290))
	print(addMinute("2:12 PM", 60))
	print(addMinute("11:12 PM", 60))

	print("END OF TESTING...")


main()


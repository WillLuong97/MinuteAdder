#Problem statement: 
'''
Without using any built-in date or time functions, write a function or method that accepts two
mandatory arguments: the first argument is a 12-hour time string with the format &quot;[H]H:MM
{AM|PM}&quot;, and the second argument is a (signed) integer. The second argument is the number
of minutes to add to the time of day represented by the first argument. The return value should
be a string of the same format as the first argument. For example, AddMinutes(&quot;9:13 AM&quot;, 200)
would return 12:33
'''

def addMinute(time, minutes):
	pass

def main():

	print("TESTING MINUTE ADDER...")
	print(addMinute("9:13 AM", 200))
	print("END OF TESTING...")

main()


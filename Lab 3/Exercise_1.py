#  a Python program to square and cube every number in a given list of integers using Lambda.


numbers = [2, 3, 4, 5]

square = list(map(lambda x: x ** 2, numbers))
cube = list(map(lambda x: x ** 3, numbers))

print("Squared:", square)
print("Cubed:", cube)



# a Python program to find if a given string starts with a given character using Lambda


starts_with = lambda s, c: s.startswith(c)

string = "Hello"
char = "H"

print(f"Does '{string}' start with '{char}'? {starts_with(string, char)}")




#  a Python program to extract year, month, date and time using Lambda


from datetime import datetime

# Get current datetime
now = datetime.now()

# Lambda functions to extract year, month, date, and time
get_year = lambda dt: dt.year
get_month = lambda dt: dt.month
get_date = lambda dt: dt.day
get_time = lambda dt: dt.strftime("%H:%M:%S")  # Extracts time in HH:MM:SS format

# Printing the extracted values
print("Year:", get_year(now))
print("Month:", get_month(now))
print("Date:", get_date(now))
print("Time:", get_time(now))

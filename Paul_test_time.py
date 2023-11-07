import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format the date and time as "mm-dd-yyyy"
formatted_date = current_datetime.strftime("%m-%d-%Y")

# Print the formatted date
print(formatted_date)
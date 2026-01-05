# Module 3 - Part 2 
# This program calculates what hour it will be when an alarm goes off after a certain number of hours.

# Get user input for the current hour and hours until the alarm
current_hour = int(input("Enter the current hour (0-23): "))

hours_until_alarm = int(input("Enter the number of hours until the alarm goes off: "))
# Calculate the hour when the alarm will go off using modulo to wrap around 24 hours

alarm_hour = (current_hour + hours_until_alarm) % 24
# Display the result
print(f"The alarm will go off at hour: {alarm_hour}")

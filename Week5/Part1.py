import calendar 

#Ask for the Number of years 
months = 0
total_inches = []
years = int(input("How many years are we calculating average rainfall for?: "))
#Interate once for each year 
for x in range(1, years + 1):
#Inner loop that itertates 12 times, once for each moth, each time asking the user for icnhes of rainfalll that month,
    for i in range(1,13):
        inches = float(input(f'How many inches of rainfall was in the month of {calendar.month_name[i]} in year {x}?:'))
        total_inches.append(inches)
        months += 1

average_inches = sum(total_inches) / len(total_inches)
#Display the total number of months, inches of rainfall, and average rainfall per month for the entire period,.. 2
print(f"Over the a total of {months} months, there was total of {sum(total_inches)} of rain with an average of {round(average_inches)} per month.")
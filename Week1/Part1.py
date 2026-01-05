#Gather inputs from user and converts to int. 
num1 = int(input("Please enter first number: "))
num2 = int(input("Please enter second number: "))

def calculations(num1,num2):
    #Perform calculations
    Sum = num1 + num2 
    Difference = num1 - num2 

    #Output to user
    result = (f'The Sum is {Sum}, and the difference is {Difference}!')
    return result

print(calculations(num1, num2))
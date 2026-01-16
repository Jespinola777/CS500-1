#Ask user how many books they purchased, store as int. 
books_purchased = int(input("How many books did you purchase?: "))
#initiate points var at 0 
points = 0

#Use and operator and if/elif statemtments to decide how many points they get, assuming points inbetween point struture will recived points equal to closest/lower tier.
if books_purchased >= 2 and books_purchased < 4:
    points += 5
elif books_purchased >= 4 and books_purchased < 6:
    points += 15
elif books_purchased >= 6 and books_purchased < 8:
    points += 30
elif books_purchased >= 8:
    points += 60
else:
    points = 0 

#Print points
print(f"You earned {points} points!")
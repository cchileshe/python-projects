#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
total = input("What is your total bill? ")
percentage = input("What percentage tip would you like to give? ")
people = input("How many people are splitting the bill? ")
tip =  (float(percentage)/100) * float(total)
each = (tip + float(total)) / int(people)
print(f"Each person should pay ${round(each,2 )}")

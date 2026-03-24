student_scores = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000 ]
#print(max(student_scores))
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")    

#range function
for number in range(1, 10, 3):
    print(number)
    
#range to add number 1 to 100
total = 0
for number in range(1, 101):
    total += number
print(total)    

#fuzzy game - print all the numbers from 1 to 100. If the number is a multiple of 3, print "fuzzy". If the number is a multiple of 5, print "buzz". If the number is a multiple of both 3 and 5, print "fuzzy buzz". Otherwise, print the number itself.
for number in range(1, 101):    
    if number % 3 == 0 and number % 5 == 0:
        print("fuzzy buzz")
    elif number % 3 == 0:
        print("fuzzy")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)       
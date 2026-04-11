def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_case_names = combined_names.lower()
    
    true_count = sum(lower_case_names.count(letter) for letter in "true")
    love_count = sum(lower_case_names.count(letter) for letter in "love")
    
    love_score = int(str(true_count) + str(love_count))
    
    if love_score < 10 or love_score > 90:
        return f"Your love score is {love_score}, you go together like coke and mentos."
    elif 40 <= love_score <= 50:
        return f"Your love score is {love_score}, you are alright together."
    else:
        return f"Your love score is {love_score}."  
    
name1 = input("What is your name? ")
name2 = input("What is their name? ")   
print(calculate_love_score(name1, name2))


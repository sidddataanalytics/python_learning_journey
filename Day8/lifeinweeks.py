def life_in_weeks(age):
    years_remaining = 90 - age
    days_remaining = years_remaining * 365
    weeks_remaining = years_remaining * 52
    months_remaining = years_remaining * 12

    print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")      
    
age = int(input("What is your current age? "))
life_in_weeks(age)


# Building a Tips Calculator

# Display welcome message
print("Welcome to the Tips Calculator")

# Get the total bill amount from user (convert to float for decimal values)
bill = float(input("What was the total bill ? $"))

# Get tip percentage from user (10, 12, or 15)
tip = int(input("How much tip would you like to give ? 10, 12, or 15 ? "))

# Get number of people to split the bill
people = int(input("How many people to split the bill ? ")) 

# Convert tip percentage to decimal (e.g., 15 becomes 0.15)
tip_as_percent = tip / 100

# Calculate the tip amount from the bill
total_tip_amount = bill * tip_as_percent

# Add tip amount to the original bill
total_bill = bill + total_tip_amount

# Divide total bill by number of people to get amount per person
bill_per_person = total_bill / people

# Round to 2 decimal places for accurate currency display
final_amount = round(bill_per_person, 2)

# Display the final amount each person should pay for the bill
print(f"Each person should pay : ${final_amount}")  


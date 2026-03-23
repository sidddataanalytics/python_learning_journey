def print_intro():
    print(r"""
       _____                    _____ _           _ _
      |_   _|_ _ _ __ ___  ___  |_   _| |__   ___ | | |
        | |/ _` | '__/ _ \/ __|   | | | '_ \ / _ \| | |
        | | (_| | | |  __/\__ \   | | | | | | (_) | | |
        |_|\__,_|_|  \___||___/   |_| |_| |_|\___/|_|_|

               _                         _
              | |_ ___  _ __ _ __   __ _| |__
              | __/ _ \| '__| '_ \ / _` | '_ \
              | || (_) | |  | | | | (_| | | | |
               \__\___/|_|  |_| |_|\__, |_| |_|
                                     |___/

    """)
    print("Welcome to Treasure Island!")
    print("Your mission is to find the treasure.")
    print()

def start_game():
    print_intro()
    
    print("You arrive at a fork in the road.")
    choice1 = input("Do you go left or right? (left/right): ").lower()
    
    if choice1 == "left":
        print("You fall into a pit. Game Over!")
        return
    elif choice1 == "right":
        print("You encounter a river.")
    else:
        print("Invalid choice. Game Over!")
        return
    
    print("You see a boat. Do you swim or take the boat?")
    choice2 = input("(swim/boat): ").lower()
    
    if choice2 == "swim":
        print("A crocodile attacks! Game Over!")
        return
    elif choice2 == "boat":
        print("You safely cross the river.")
    else:
        print("Invalid choice. Game Over!")
        return
    
    print("You reach an island with three doors: red, blue, yellow.")
    choice3 = input("Which door do you choose? (red/blue/yellow): ").lower()
    
    if choice3 == "red":
        print("A dragon appears! Game Over!")
    elif choice3 == "blue":
        print("You found the treasure! You Win! 🎉")
    elif choice3 == "yellow":
        print("You fall off a cliff. Game Over!")
    else:
        print("Invalid choice. Game Over!")

if __name__ == "__main__":
    start_game()
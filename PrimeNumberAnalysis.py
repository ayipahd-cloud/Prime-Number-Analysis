# Prime Number Analysis Program

import math # Importing the math module to use mathematical functions for the program
import time # Importing the time module to add delays for a better user experience

# ------------------- CHECKING PRIME -------------------------------

def checkingprime(): # This function checks if a number is prime or not. It requires user input to work
    numberc = int(input("Enter a number to check if it's prime: ")) # Asks for a number input and stores it as a variable
    is_prime = True # Immediately sets the variable "is_prime" to True, assuming the number is prime until proven otherwise

    if numberc <= 1:
        is_prime = False # If the number is less than or equal to 1, it is not prime, so "is_prime" is set to False
    elif numberc <= 3:
        is_prime = True # If the number is less than or equal to 3, it is prime, so "is_prime" is set to True
    elif numberc % 2 == 0 or numberc % 3 == 0:
        is_prime = False # If the number is divisible by 2 or 3, it is not prime, so "is_prime" is set to False
    elif numberc > 3: # If the number is greater than 3, the function below will occur
        limit = int(math.isqrt(numberc))
        for i in range(5, limit + 1, 6):
            if numberc % i == 0 or numberc % (i + 2) == 0:
                is_prime = False # If the number is divisible by the range it's not prime and is set to False
                break
            else:
                is_prime = True # If the number is not divisible by the range, it is prime and is set to True

    time.sleep(1.2) # Adds a delay of 1.2 seconds before outputting the result for better user experience
    if is_prime == True: # Checks if the variable is True, if it is, it will output the message below
        print(f"{numberc} is a prime number. ✅")
        time.sleep(0.2)
        print("Returning to the main menu...")
        time.sleep(0.8)
        mainmenu() # Calls the mainmenu function to return to the main menu after checking if the number is prime
    elif is_prime == False: # Checks if the variable is False if not True, and it will output the message below
        print(f"{numberc} is not a prime number. ❌")
        time.sleep(0.2)
        print("Returning to the main menu...")
        time.sleep(0.8)
        mainmenu() # Calls the mainmenu function to return to the main menu after checking if the number is not prime
    else: # However, if the variable is neither True nor False (likely due to an error), it will output the message below
        print("An error occurred while checking the number.")
        time.sleep(0.2)
        print("Returning to the main menu...")
        time.sleep(0.8)
        mainmenu() # Calls the mainmenu function to return to the main menu after an error occurred while checking the number


# ------------------- GENERATE PRIMES  -------------------------------


def generatesprimes(): # This function generates a list of prime numbers up to a certain number and provides statistics about them
    numstart = int(input("Enter a number to generate its prime statistics: ")) # Asks for a number input and stores it as a variable
    if numstart < 2: # Checks if the input number is less than 2, which is the smallest prime number
        print("Please enter a number greater than or equal to 2.")
        time.sleep(0.8)
        mainmenu()
        return
    prime_list = [] # Creates an empty list to store the prime numbers
    
    prime_list.append(2) # Adds to the prime list if the number is 2, which is prime
    prime_list.append(3) # Adds to the prime list if the number is 3, which is prime

    for num in range(2, numstart + 1): # Loops through the range of numbers from 2 to the input number
        is_prime = True # Assumes the number is prime until proven otherwise

        if num % 2 == 0 or num % 3 == 0:
            is_prime = False # If the number is divisible by 2 or 3, it is not prime, so "is_prime" is set to False

        limit2 = int(math.isqrt(num))
        for i in range(5, limit2 + 1, 6):
                if num % i == 0 or num % (i + 2) == 0:
                    is_prime = False # If the number is divisible by the range it's not prime and is set to False
                    break
        if is_prime:
            prime_list.append(num) # If the number is prime, it is added to the prime list

    list_length = len(prime_list) # Calculates the length of the prime list and stores it as a variable
    print("Here are a list of statistics for the prime numbers up to your inputted number:") # Outputs a message indicating that statistics will be displayed
    time.sleep(3.2) # Adds a delay of 1.2 seconds before outputting the statistics for better user experience
    print(f"#️⃣ There are {list_length} prime numbers up to {numstart}.") # Outputs the length of the prime list
    print(f"#️⃣ The largest prime number within the list is, {max(prime_list)}.") # Outputs the largest prime number in the list
    print(f"#️⃣ The smallest prime number within the list is, {min(prime_list)}.") # Outputs the smallest prime number in the list
    print(f"#️⃣ The prime numbers up to {numstart} are {prime_list}. ")
    time.sleep(6.8) # Adds a delay of 6.8 seconds before returning to the main menu for better user experience
    print("Returning to the main menu...") # Outputs a thank you message to the user
    time.sleep(0.8)
    mainmenu() # Calls the mainmenu function to return to the main menu


# ------------------- MAIN MENU-------------------------------


def mainmenu(): # Displays the main menu and handles user input for the prime number analysis program
    print("🔢 Welcome to the Prime Number Analysis Program! 🔢")
    time.sleep(1)
    print("Please select an option. (1 - 3)")
    time.sleep(1.2)
    print("1. Check if a number is a prime number.")
    print("2. Generate a list of prime numbers up to a certain number (w/ stats).")
    print("3. Exit") # The entire block of code above is the main menu for the prime number analysis program. It displays a welcome message, prompts the user to select an option, and provides three choices

    choice = input("Enter your choice: ") # Asks the user for an input choice and stores it as a variable called 'choice'
    if choice == "1":
        time.sleep(0.2)
        print("You have selected option 1: Check if a number is a prime number.")
        time.sleep(1.5)
        checkingprime() # If the choice is 1, it will call upon the "checkingprime" function

    elif choice == "2":
        time.sleep(0.2)
        print("You have selected option 2: Generate a list of prime numbers up to a certain number (w/ stats).")
        time.sleep(1.5)
        generatesprimes() # If the choice is 2, it will call upon the "generatesprimes" function

    elif choice == "3":
        time.sleep(0.7)
        print("Exiting the program... Goodbye! 👋") # If the choice is 3, it will exit the program and print a goodbye message
        exit()

    else:
        time.sleep(0.7)
        print("Invalid choice. Please wait until you can try again. ❌")
        time.sleep(3)
        mainmenu() # If the choice input is invalid, it will print out the message and call the mainmenu function to restart the program

mainmenu()

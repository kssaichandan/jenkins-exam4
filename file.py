import random
import time

def manual_approval():
    """Task 2 & 3: Simulates the Jenkins 'Proceed' input step."""
    print("--- SYSTEM INITIALIZED ---")
    
    while True:
        # Task 2: Add input step asking 'Proceed with Build?'
        user_input = input(">> Proceed with Game Launch? (yes/no): ").lower().strip()
        
        if user_input == 'yes':
            # Task 3: Print confirmation message after approval
            print("\n[SUCCESS] Approval received. Loading Number Ranger...\)
            time.sleep(1) # Adding a small delay for dramatic effect
            return True
        elif user_input == 'no':
            print("\n[ABORTED] Game launch cancelled by user.")
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def play_game():
    secret_number = random.randint(1, 100)
    print("\nGame is running! I'm thinking of a number between 1 and 100.")
    guess = int(input("Quick guess to test the build: "))
    
    if guess == secret_number:
        print("Legendary! You guessed it immediately.")
    else:
        print(f"Build test complete. The number was {secret_number}.")

if __name__ == "__main__":
    # Task 1: (Simulated) Checkout code logic
    print("Cloning repository: 'number-ranger-v5'...")
    
    # Run the Manual Approval function
    if manual_approval():
        play_game()
    else:
        print("Exiting...")

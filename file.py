import random
import time

def get_admin_details():
    """Captures deployment parameters."""
    print("\n--- CONFIGURATION SETTINGS ---")
    admin_name = input("Enter Admin Name: ").strip()
    env = input("Enter Environment (Dev/Prod): ").strip().upper()
    return admin_name, env

def manual_approval():
    """Simulates the Jenkins 'Proceed' input step."""
    print("\n--- SYSTEM INITIALIZED ---")
    while True:
        user_input = input(">> Proceed with Game Launch? (yes/no): ").lower().strip()
        if user_input == 'yes':
            return True
        elif user_input == 'no':
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def log_build_event(admin, env, result):
    """New Function: Records the build outcome to a text file."""
    with open("build_history.log", "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] User: {admin} | Env: {env} | Result: {result}\n"
        log_file.write(log_entry)
    print(f"Log updated: {log_entry.strip()}")

def show_history():
    """New Function: Reads and displays previous build logs."""
    print("\n--- RECENT BUILD HISTORY ---")
    try:
        with open("build_history.log", "r") as log_file:
            lines = log_file.readlines()
            for line in lines[-3:]: # Show only the last 3 entries
                print(line.strip())
    except FileNotFoundError:
        print("No history found yet.")

def play_game():
    secret_number = random.randint(1, 100)
    try:
        guess = int(input("\nGuess the secret number (1-100): "))
        if guess == secret_number:
            print("🎉 Success!")
            return "SUCCESS"
        else:
            print(f"❌ Failed. Number was {secret_number}")
            return "FAILURE"
    except ValueError:
        return "ERROR (Invalid Input)"

if __name__ == "__main__":
    print("Fetching repository...")
    
    if manual_approval():
        name, environment = get_admin_details()
        
        # Run game and capture outcome
        outcome = play_game()
        
        # Task: Record the event
        log_build_event(name, environment, outcome)
        
        # Task: Show history
        show_history()
    else:
        print("Build Aborted.")

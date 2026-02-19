import random
import time

# --- PREVIOUS FUNCTIONS (get_admin_details, manual_approval, etc.) REMAIN THE SAME ---

def apply_env_configs(env):
    """New Function: Changes game settings based on the environment."""
    print(f"\n[CONFIG] Applying settings for {env} environment...")
    if env == "PROD":
        # Production is harder!
        print("!! SECURITY MODE ENABLED: Single attempt only !!")
        return 1 
    else:
        # Dev gives you more slack
        print("DEBUG MODE ENABLED: You get 3 attempts.")
        return 3

def run_system_integrity_check():
    """New Function: Simulates a Jenkins test suite or linting check."""
    print("\n--- RUNNING SYSTEM INTEGRITY CHECKS ---")
    checks = ["Disk Space", "Memory Allocation", "Source Code Linting", "Dependency Audit"]
    
    for check in checks:
        print(f"Checking {check}...", end=" ", flush=True)
        time.sleep(0.5)
        print("[PASSED]")
    
    print("--- ALL CHECKS PASSED: BUILD STABLE ---")
    return True

def play_game_with_lives(max_attempts):
    """Updated Function: Now uses the environment-based lives."""
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} | Guess (1-100): "))
            if guess == secret_number:
                print("🎉 SUCCESS: Build Verified!")
                return "SUCCESS"
            elif guess < secret_number:
                print("Higher!")
            else:
                print("Lower!")
            attempts += 1
        except ValueError:
            print("Invalid input.")
            
    print(f"❌ FAILURE: Out of attempts. Number was {secret_number}")
    return "FAILURE"

# --- MAIN EXECUTION BLOCK ---
if __name__ == "__main__":
    print("Fetching repository...")
    
    if manual_approval():
        # Task 2: Parameter Input
        name, environment = get_admin_details()
        
        # New Task: Integrity Testing
        if run_system_integrity_check():
            
            # New Task: Dynamic Environment Config
            lives = apply_env_configs(environment)
            
            # Execute
            outcome = play_game_with_lives(lives)
            
            # Logging and History
            log_build_event(name, environment, outcome)
            show_history()
    else:
        print("Build Aborted by user.")

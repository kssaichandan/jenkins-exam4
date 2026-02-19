import random
import time
import os

# --- 1. CONFIGURATION & APPROVAL ---

def manual_approval():
    """Task: Simulates the Jenkins 'Proceed' input step."""
    print("\n" + "="*40)
    print("      JENKINS PIPELINE INITIALIZED")
    print("="*40)
    while True:
        user_input = input(">> Proceed with Game Launch? (yes/no): ").lower().strip()
        if user_input == 'yes':
            print("\n[SUCCESS] Approval received. Accessing Workspace...")
            return True
        elif user_input == 'no':
            print("\n[ABORTED] Pipeline stopped by user.")
            return False
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

def get_admin_details():
    """Task: Collects parameters like a Jenkins Input Step."""
    print("\n--- CONFIGURATION SETTINGS ---")
    admin_name = input("Enter Admin Name: ").strip() or "Anonymous"
    env = input("Enter Environment (Dev/Prod): ").strip().upper()
    if env not in ["DEV", "PROD"]:
        env = "DEV"  # Default to Dev
    return admin_name, env

# --- 2. PRE-BUILD CHECKS ---

def run_system_integrity_check():
    """Task: Simulates automated testing/linting."""
    print("\n--- RUNNING SYSTEM INTEGRITY CHECKS ---")
    checks = ["Disk Space", "Memory Allocation", "Linting", "Dependencies"]
    for check in checks:
        print(f"Checking {check}...", end=" ", flush=True)
        time.sleep(0.4)
        print("[PASSED]")
    return True

def apply_env_configs(env):
    """Task: Changes logic based on Target Environment."""
    print(f"\n[CONFIG] Applying settings for {env}...")
    if env == "PROD":
        print("!! PRODUCTION MODE: Single attempt security enabled !!")
        return 1
    else:
        print("DEBUG MODE: 3 attempts allowed for testing.")
        return 3

# --- 3. EXECUTION & LOGIC ---

def play_game_with_lives(max_attempts):
    """The main application logic (Number Ranger Game)."""
    secret_number = random.randint(1, 100)
    print(f"\n[EXECUTION] I'm thinking of a number (1-100).")
    
    for i in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {i}/{max_attempts} | Guess: "))
            if guess == secret_number:
                print("🎉 BOOM! Target achieved. Build Stable.")
                return "SUCCESS"
            elif guess < secret_number:
                print("Too Low!")
            else:
                print("Too High!")
        except ValueError:
            print("Invalid input! Please enter a number.")
            
    print(f"❌ FAILURE: Build crashed. Correct number was {secret_number}.")
    return "FAILURE"

# --- 4. ERROR HANDLING & POST-BUILD ---

def trigger_rollback(env):
    """Simulates a Jenkins failure/rollback stage."""
    print(f"\n[CRITICAL] Build failed in {env}!")
    print("Initiating Rollback to last stable commit...")
    time.sleep(1)
    print("Restore Complete. System back to Green state.")

def log_build_event(admin, env, result):
    """Task: Records the build results to a log file."""
    with open("build_history.log", "a") as log_file:
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] User: {admin} | Env: {env} | Result: {result}\n")

def package_and_cleanup():
    """Task: Simulates Artifact Archiving and Workspace Cleaning."""
    print("\n--- POST-BUILD ACTIONS ---")
    print("Archiving 'build_history.log' as an Artifact...")
    time.sleep(0.5)
    print("Cleaning temporary workspace files...")
    time.sleep(0.5)
    print("Workspace Clean. End of Pipeline.")

# --- MAIN CONTROLLER ---

if __name__ == "__main__":
    # Simulate Checkout
    print("Cloning repository: 'jenkins-exam-version-4'...")
    time.sleep(0.5)

    if manual_approval():
        admin, target_env = get_admin_details()
        
        if run_system_integrity_check():
            lives = apply_env_configs(target_env)
            
            # Start Execution
            outcome = play_game_with_lives(lives)
            
            # Error Handling
            if outcome == "FAILURE":
                trigger_rollback(target_env)
            
            # Record Keeping
            log_build_event(admin, target_env, outcome)
            package_and_cleanup()
            
            print(f"\n[FINISH] Pipeline ID {random.randint(1000,9999)} closed.")

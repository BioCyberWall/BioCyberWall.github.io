# BioCyberWall - Cybersecurity Project
# Purpose: Simulate a login protection system against Brute Force attacks

def login_attempt(username, password, attempts):
    MAX_ATTEMPTS = 3
    locked_out = False
    
    if attempts >= MAX_ATTEMPTS:
        locked_out = True
        print(f"[ALERT] Account {username} is LOCKED due to multiple failed attempts.")
    else:
        # Simplified logic
        if password == "secret123":
            print(f"Access Granted for {username}")
        else:
            print(f"Access Denied. Attempt {attempts + 1} of {MAX_ATTEMPTS}")

if __name__ == "__main__":
    user = "admin"
    # Simulating 4 failed attempts
    for i in range(4):
        login_attempt(user, "wrong_pass", i)

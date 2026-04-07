import string

def check_password_strength(password):
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("❌ Add at least one uppercase letter.")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character (e.g., !, @, #, $).")

    print("\n" + "="*40)
    print(f"{BOLD}🛡️  PASSWORD STRENGTH REPORT 🛡️{RESET}")
    print("="*40)

    if score >= 5:
        print(f"Overall Strength: {GREEN}STRONG 💪{RESET}")
    elif score >= 3:
        print(f"Overall Strength: {YELLOW}MODERATE ⚠️{RESET}")
    else:
        print(f"Overall Strength: {RED}WEAK ❌{RESET}")

    print("-" * 40)
    
    if feedback:
        print(f"{BOLD}Tips to improve:{RESET}")
        for item in feedback:
            print(item)
    else:
        print(f"{GREEN}Perfect! Your password is highly secure.{RESET}")
        
    print("="*40 + "\n")


if __name__ == "__main__":
    print("Welcome to the Smart Password Checker!")
    print("Press Ctrl+C to exit.\n")
    
    while True:
        try:
            user_password = input("Enter a password to test: ")
            
            if not user_password:
                print("Please type a password!\n")
                continue
                
            check_password_strength(user_password)
            
        except KeyboardInterrupt:
            print("\n\nExiting program. Stay secure! 🔒")
            break
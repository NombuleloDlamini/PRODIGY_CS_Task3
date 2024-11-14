import re

def assess_password_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Assess the strength
    strength_score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_criteria])

    # Feedback for the user
    print("Password Strength Assessment:")
    if length_criteria:
        print("✓ Length is sufficient (8 or more characters)")
    else:
        print("✗ Password should be at least 8 characters long")

    if uppercase_criteria:
        print("✓ Contains uppercase letters")
    else:
        print("✗ Add uppercase letters")

    if lowercase_criteria:
        print("✓ Contains lowercase letters")
    else:
        print("✗ Add lowercase letters")

    if number_criteria:
        print("✓ Contains numbers")
    else:
        print("✗ Add numbers")

    if special_criteria:
        print("✓ Contains special characters")
    else:
        print("✗ Add special characters (!@#$%^&*(),.?\":{}|<>)")

    # Determine strength level
    if strength_score == 5:
        print("\nPassword Strength: Very Strong")
    elif strength_score == 4:
        print("\nPassword Strength: Strong")
    elif strength_score == 3:
        print("\nPassword Strength: Moderate")
    elif strength_score == 2:
        print("\nPassword Strength: Weak")
    else:
        print("\nPassword Strength: Very Weak")

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    assess_password_strength(password)

if __name__ == "__main__":
    main()
